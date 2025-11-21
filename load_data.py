"""load_data.py
Create a sample SQLite database (`sec_data.db`) with simplified financial statement data
for a few technology companies. This is a reproducible stand-in for SEC data for the
purposes of the portfolio project.
"""
import sqlite3
from datetime import date

DB_NAME = "sec_data.db"

sample_data = [
    # company, fiscal_year, revenue, net_income, total_assets, total_liabilities, current_assets, current_liabilities, shareholders_equity
    ("AAPL", 2024, 394_000_000_000, 94_000_000_000, 352_000_000_000, 287_000_000_000, 135_000_000_000, 108_000_000_000, 65_000_000_000),
    ("MSFT", 2024, 225_000_000_000, 72_000_000_000, 358_000_000_000, 178_000_000_000, 150_000_000_000, 47_000_000_000, 180_000_000_000),
    ("GOOGL", 2024, 283_000_000_000, 59_000_000_000, 359_000_000_000, 97_000_000_000, 170_000_000_000, 22_000_000_000, 262_000_000_000),
]

CREATE_SQL = """
CREATE TABLE IF NOT EXISTS financials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    fiscal_year INTEGER NOT NULL,
    revenue REAL,
    net_income REAL,
    total_assets REAL,
    total_liabilities REAL,
    current_assets REAL,
    current_liabilities REAL,
    shareholders_equity REAL,
    loaded_at TEXT
);
"""

INSERT_SQL = """
INSERT INTO financials (company, fiscal_year, revenue, net_income, total_assets, total_liabilities, current_assets, current_liabilities, shareholders_equity, loaded_at)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""


def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.executescript(CREATE_SQL)

    today = date.today().isoformat()
    for row in sample_data:
        cur.execute(INSERT_SQL, (*row, today))

    conn.commit()
    conn.close()
    print(f"Sample database created: {DB_NAME} (rows inserted: {len(sample_data)})")


if __name__ == "__main__":
    main()
