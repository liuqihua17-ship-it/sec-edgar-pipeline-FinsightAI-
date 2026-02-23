# EDGAR NLP Pipeline (BANA 275)

This repo downloads SEC EDGAR filings (e.g., 10-K/10-Q/8-K), converts them into clean text, and builds a structured dataset for downstream NLP tasks (topic modeling, embeddings/RAG, classification, etc.).

## Project Structure

edgar-nlp-pipeline/
data/
raw/ # downloaded raw HTML/TXT (ignored by git)
dataset/ # output datasets JSONL/Parquet (ignored by git)
docs/
DATA_SCHEMA.md
src/
config.py
sec_edgar_pipeline.py
tests/
requirements.txt
.gitignore
README.md

## Setup (VSCode)
1. Create and activate venv:
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     python -m pip install --upgrade pip
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     python -m pip install --upgrade pip
     ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run:
    ```bash
    pip install -r requirements.txt

## Notes on SEC Access

Requests must include a descriptive User-Agent with contact information.

Use rate limiting to avoid overloading SEC servers.

## Output

data/raw/: raw downloaded filings (HTML/TXT)

data/dataset/: dataset files (JSONL/Parquet)

## Dataset Schema

See docs/DATA_SCHEMA.md.