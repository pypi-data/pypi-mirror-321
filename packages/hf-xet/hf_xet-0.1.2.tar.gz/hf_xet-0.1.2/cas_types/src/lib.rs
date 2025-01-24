use core::fmt;
use std::collections::{HashMap, HashSet};

use merklehash::MerkleHash;
use serde::{Deserialize, Serialize};
use serde_repr::{Deserialize_repr, Serialize_repr};

mod error;
mod key;
pub use key::*;

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct UploadXorbResponse {
    pub was_inserted: bool,
}

/// Start and exclusive-end range for chunk content
pub type ChunkRange = Range<u32>;
/// Start and exclusive-end range for file content
pub type FileRange = Range<u64>;
/// Start and inclusive-end range for HTTP range content
pub type HttpRange = Range<u32>;

// note that the standard PartialOrd/Ord impls will first check `start` then `end`
#[derive(Debug, Serialize, Deserialize, Clone, Eq, PartialEq, PartialOrd, Ord, Default, Hash)]
pub struct Range<Idx> {
    pub start: Idx,
    pub end: Idx,
}

impl<Idx: fmt::Display> fmt::Display for Range<Idx> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let Range { start, end } = self;
        write!(f, "{start}-{end}")
    }
}

#[derive(Debug)]
pub enum RangeParseError<Idx: std::str::FromStr> {
    InvalidFormat,
    ParseError(Idx::Err),
}

impl<Idx: std::str::FromStr> TryFrom<&str> for Range<Idx> {
    type Error = RangeParseError<Idx>;

    fn try_from(value: &str) -> Result<Self, Self::Error> {
        let parts: Vec<&str> = value.splitn(2, '-').collect();

        if parts.len() != 2 {
            return Err(RangeParseError::InvalidFormat);
        }

        let start = parts[0].parse::<Idx>().map_err(RangeParseError::ParseError)?;
        let end = parts[1].parse::<Idx>().map_err(RangeParseError::ParseError)?;

        Ok(Range { start, end })
    }
}

/// Describes a portion of a reconstructed file, namely the xorb and
/// a range of chunks within that xorb that are needed.
///
/// unpacked_length is used for validation, the result data of this term
/// should have that field's value as its length
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct CASReconstructionTerm {
    pub hash: HexMerkleHash,
    // the resulting data from deserializing the range in this term
    // should have a length equal to `unpacked_length`
    pub unpacked_length: u32,
    // chunk index start and end in a xorb
    pub range: ChunkRange,
}

/// To use a CASReconstructionFetchInfo fetch info all that's needed
/// is an http get request on the url with the Range header directly
/// formed from the url_range values.
///
/// the `range` key describes the chunk range within the xorb that the
/// url is used to fetch
#[derive(Debug, Serialize, Deserialize, Clone, PartialEq, Eq, Hash)]
pub struct CASReconstructionFetchInfo {
    // chunk index start and end in a xorb
    pub range: ChunkRange,
    pub url: String,
    // byte index start and end in a xorb, used exclusively for Range header
    pub url_range: HttpRange,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct QueryReconstructionResponse {
    // For range query [a, b) into a file content, the location
    // of "a" into the first range.
    pub offset_into_first_range: u64,
    // Series of terms describing a xorb hash and chunk range to be retreived
    // to reconstruct the file
    pub terms: Vec<CASReconstructionTerm>,
    // information to fetch xorb ranges to reconstruct the file
    // each key is a hash that is present in the `terms` field reconstruction
    // terms, the values are information we will need to fetch ranges from
    // each xorb needed to reconstruct the file
    pub fetch_info: HashMap<HexMerkleHash, Vec<CASReconstructionFetchInfo>>,
}

// Request json body type representation for the POST /reconstructions endpoint
// to get the reconstruction for multiple files at a time.
// listing of non-duplicate (enforced by HashSet) keys (file ids) to get reconstructions for
pub type BatchQueryReconstructionRequest = HashSet<HexKey>;

// Response type for querying reconstruction for a batch of files
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct BatchQueryReconstructionResponse {
    // Map of FileID to series of terms describing a xorb hash and chunk range to be retreived
    // to reconstruct the file
    pub files: HashMap<HexMerkleHash, Vec<CASReconstructionTerm>>,
    // information to fetch xorb ranges to reconstruct the file
    // each key is a hash that is present in the `terms` field reconstruction
    // terms, the values are information we will need to fetch ranges from
    // each xorb needed to reconstruct the file
    pub fetch_info: HashMap<HexMerkleHash, Vec<CASReconstructionFetchInfo>>,
}

#[derive(Debug, Serialize_repr, Deserialize_repr, Clone, Copy)]
#[repr(u8)]
pub enum UploadShardResponseType {
    Exists = 0,
    SyncPerformed = 1,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct UploadShardResponse {
    pub result: UploadShardResponseType,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct QueryChunkResponse {
    pub shard: MerkleHash,
}
