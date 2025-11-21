"""analysis_and_viz.py
Connects to `sec_data.db`, computes financial ratios for each company, writes
`financial_ratios_analysis.csv` and produces `financial_ratios_visualization.png`.
"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DB_NAME = "sec_data.db"
CSV_OUT = "financial_ratios_analysis.csv"
PNG_OUT = "financial_ratios_visualization.png"

RATIO_ORDER = ["Current Ratio", "Debt-to-Equity", "Profit Margin", "ROA", "ROE"]


def fetch_financials(db=DB_NAME):
    conn = sqlite3.connect(db)
    df = pd.read_sql_query("SELECT company, fiscal_year, revenue, net_income, total_assets, total_liabilities, current_assets, current_liabilities, shareholders_equity FROM financials", conn)
    conn.close()
    return df


def compute_ratios(df):
    df = df.copy()
    df["Current Ratio"] = df["current_assets"] / df["current_liabilities"]
    df["Debt-to-Equity"] = df["total_liabilities"] / df["shareholders_equity"]
    df["Profit Margin"] = df["net_income"] / df["revenue"]
    df["ROA"] = df["net_income"] / df["total_assets"]
    df["ROE"] = df["net_income"] / df["shareholders_equity"]
    return df


def save_csv(df, path=CSV_OUT):
    df_out = df[["company", "fiscal_year"] + RATIO_ORDER]
    df_out.to_csv(path, index=False)
    print(f"Wrote CSV: {path}")


def plot_ratios(df, path=PNG_OUT):
    # Use latest fiscal_year per company (if multiple rows exist)
    df_latest = df.sort_values("fiscal_year").groupby("company").tail(1)
    companies = df_latest["company"].tolist()
    data = df_latest[RATIO_ORDER].astype(float).values

    x = np.arange(len(companies))
    width = 0.13

    fig, ax = plt.subplots(figsize=(11, 6))

    for i, ratio in enumerate(RATIO_ORDER):
        ax.bar(x + (i - 2) * width, data[:, i], width, label=ratio)

    ax.set_xticks(x)
    ax.set_xticklabels(companies)
    ax.set_ylabel("Ratio / % (profitability expressed as decimal)")
    ax.set_title("Comparative Financial Ratios — Tech Sector Giants")
    ax.legend()
    fig.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Wrote plot: {path}")


def main():
    try:
        df = fetch_financials()
    except Exception as e:
        print("Error reading database. Run `load_data.py` first to create `sec_data.db`.")
        raise

    if df.empty:
        print("No financial data found in DB. Ensure `load_data.py` was run.")
        return

    df_ratios = compute_ratios(df)
    save_csv(df_ratios)
    plot_ratios(df_ratios)


if __name__ == "__main__":
    main()
