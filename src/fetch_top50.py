import time
import pandas as pd
import subprocess

CSV_PATH = "data/top_sp500.csv"   # <-- keep this

def main():
    # FORCE all columns to string so cik/company never become int
    df = pd.read_csv(CSV_PATH, dtype=str).fillna("")
    df.columns = [c.strip() for c in df.columns]

    # Quick sanity check
    print("✅ Columns:", df.columns.tolist())
    print("✅ First row:", df.iloc[0].to_dict())

    for i, row in df.iterrows():
        ticker = str(row["ticker"]).strip().upper()
        company = str(row["company_name"]).strip()
        cik = str(row["cik"]).strip().replace(".0", "").zfill(10)

        if not ticker or not cik:
            print(f"⚠️ Skipping row {i+1} (missing ticker/cik)")
            continue

        # f-string is safest (no string + int concat)
        print(f"\n[{i+1}/{len(df)}] Fetching {ticker} | {company} | CIK={cik}")

        result = subprocess.run([
            "python", "-m", "src.sec_edgar_pipeline",
            "fetch",
            "--cik", cik,
            "--ticker", ticker,
            "--company", company,
            "--forms", "10-K",
            "--max-filings", "5"
        ])

        if result.returncode != 0:
            print(f"⚠️ Fetch failed for {ticker}. Continuing...")

        time.sleep(0.5)

    print(f"\n[{i+1}/{len(df)}] Fetching {str(ticker)} | {str(company)} | CIK={str(cik)}")

if __name__ == "__main__":
    main()