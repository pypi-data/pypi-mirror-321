use std::cmp::Ordering;
use std::io::{Cursor, Read, Write};
use std::mem::size_of;

use base64::Engine;
use blake3::Hash;
use cas_types::ChunkRange;
use utils::serialization_utils::{read_u32, read_u64, write_u32, write_u64};

use super::BASE64_ENGINE;
use crate::error::ChunkCacheError;

const CACHE_ITEM_FILE_NAME_BUF_SIZE: usize = size_of::<u32>() * 2 + size_of::<u64>() + blake3::OUT_LEN;

/// A CacheItem represents metadata for a single range in the cache
/// it contains the range of chunks the item is for
/// the length of the file on disk and the hash of the file contents
/// for validation.
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub(crate) struct CacheItem {
    pub(crate) range: ChunkRange,
    pub(crate) len: u64,
    pub(crate) hash: Hash,
}

impl std::fmt::Display for CacheItem {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "CacheItem {{ range: {:?}, len: {}, hash: {} }}", self.range, self.len, self.hash,)
    }
}

// impl PartialOrd & Ord to sort by the range to enable binary search over
// sorted CacheItems using the range field to match a range for search
impl Ord for CacheItem {
    fn cmp(&self, other: &Self) -> Ordering {
        self.range.cmp(&other.range)
    }
}

impl PartialOrd for CacheItem {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

/// CacheItem is represented on disk as the file name of a cache file
/// the file name is created by base64 encoding a buffer that concatenates
/// all attributes of the CacheItem, numbers being written in little endian order
impl CacheItem {
    pub(crate) fn file_name(&self) -> Result<String, ChunkCacheError> {
        let mut buf = [0u8; CACHE_ITEM_FILE_NAME_BUF_SIZE];
        let mut w = Cursor::new(&mut buf[..]);
        write_u32(&mut w, self.range.start)?;
        write_u32(&mut w, self.range.end)?;
        write_u64(&mut w, self.len)?;
        write_hash(&mut w, &self.hash)?;
        Ok(BASE64_ENGINE.encode(buf))
    }

    pub(crate) fn parse(file_name: &[u8]) -> Result<CacheItem, ChunkCacheError> {
        let buf = BASE64_ENGINE.decode(file_name)?;
        if buf.len() != CACHE_ITEM_FILE_NAME_BUF_SIZE {
            return Err(ChunkCacheError::parse("decoded buf is not the right size for a cache item file name"));
        }
        let mut r = Cursor::new(buf);
        let start = read_u32(&mut r)?;
        let end = read_u32(&mut r)?;
        let len = read_u64(&mut r)?;
        let hash = read_hash(&mut r)?;
        if start >= end {
            return Err(ChunkCacheError::BadRange);
        }

        Ok(Self {
            range: ChunkRange { start, end },
            len,
            hash,
        })
    }
}

pub fn write_hash(writer: &mut impl Write, hash: &blake3::Hash) -> Result<(), std::io::Error> {
    writer.write_all(hash.as_bytes())
}

pub fn read_hash(reader: &mut impl Read) -> Result<blake3::Hash, std::io::Error> {
    let mut m = [0u8; 32];
    reader.read_exact(&mut m)?;
    Ok(blake3::Hash::from_bytes(m))
}

#[cfg(test)]
mod tests {
    use base64::Engine;
    use blake3::OUT_LEN;
    use cas_types::ChunkRange;

    use crate::disk::cache_item::CACHE_ITEM_FILE_NAME_BUF_SIZE;
    use crate::disk::{CacheItem, BASE64_ENGINE};

    impl Default for CacheItem {
        fn default() -> Self {
            Self {
                range: Default::default(),
                len: Default::default(),
                hash: blake3::Hash::from_bytes([0u8; OUT_LEN]),
            }
        }
    }

    #[test]
    fn test_to_file_name_len() {
        let cache_item = CacheItem {
            range: ChunkRange { start: 0, end: 1024 },
            len: 16 << 20,
            hash: blake3::hash(&(1..100).collect::<Vec<u8>>()),
        };

        let file_name = cache_item.file_name().unwrap();
        let decoded = BASE64_ENGINE.decode(file_name).unwrap();
        assert_eq!(decoded.len(), CACHE_ITEM_FILE_NAME_BUF_SIZE);
    }
}
