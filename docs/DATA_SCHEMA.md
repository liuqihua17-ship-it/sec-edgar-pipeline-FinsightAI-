# Dataset Schema (Doc-level)

Each record represents one filing document.

## Required fields
- company: str
- ticker: str
- cik: str
- form: str (e.g., 10-K, 10-Q, 8-K)
- filing_date: str (YYYY-MM-DD)
- report_date: str (YYYY-MM-DD or null)
- accession_number: str
- primary_document: str
- source_url: str
- local_path: str
- text: str

## Optional fields
- primary_doc_description: str
- hash_md5: str
- ingested_at: str (ISO timestamp)

# Dataset Schema (Chunk-level)

Each record represents one chunk of a filing.

## Required fields
- doc_id: str (use accession_number)
- chunk_id: str (stable id, e.g., "{doc_id}_c000123")
- company: str
- ticker: str
- cik: str
- form: str
- filing_date: str
- source_url: str
- local_path: str
- char_start: int
- char_end: int
- text: str

## Optional fields
- section_hint: str (best-effort)