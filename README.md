# Comparative Financial Ratio Analysis: Tech Sector Giants

[![Regenerate outputs](https://github.com/HimanshuRag/Financial-analysis-portfolio/actions/workflows/regenerate.yml/badge.svg)](https://github.com/HimanshuRag/Financial-analysis-portfolio/actions/workflows/regenerate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

This repository contains a complete financial analysis and consulting project comparing key financial ratios for major technology companies. It demonstrates skills in Financial Analysis, Python, SQL (SQLite), and Data Visualization using real-world-style data.

Skills demonstrated:
- Financial ratio calculation and interpretation (liquidity, leverage, profitability, efficiency)
- Data extraction and processing with `sqlite3` and `pandas`
- Visualization using `matplotlib`
- Reproducible workflows and deliverables for consulting reports

Files in this repository:
- `README.md` — Project overview and instructions
- `analysis_report.md` — Consulting-style interpretation and recommendations
- `load_data.py` — Script to create/load sample SEC-style data into a local SQLite database
- `analysis_and_viz.py` — Script that queries the SQLite DB, computes ratios, writes `financial_ratios_analysis.csv`, and generates `financial_ratios_visualization.png`
- `financial_ratios_analysis.csv` — Final computed ratios (generated)
- `financial_ratios_visualization.png` — Comparative bar chart (generated)
- `requirements.txt` — Python dependencies

Quick start
1. Create a Python virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create the sample SQLite database and load data (optional — sample DB is already included):

```bash
python3 load_data.py
```

3. Run the analysis and generate outputs:

```bash
python3 analysis_and_viz.py
```

Outputs will appear in the repository root:
- `financial_ratios_analysis.csv`
- `financial_ratios_visualization.png`

If you want to publish this project to GitHub, initialize a git repo, commit the files, and push to a remote repository (see `PUSH INSTRUCTIONS` in the bottom of this file).

PUSH INSTRUCTIONS
1. Initialize git (if not already):

```bash
git init
git add .
git commit -m "Initial commit: comparative financial ratio analysis project"
```

2. Create a GitHub repository (locally you can use the `gh` CLI or create it on github.com). Example using `gh`:

```bash
gh repo create your-username/financial-analysis-portfolio --public --source=. --remote=origin --push
```

Replace `your-username` with your GitHub username. If you prefer to push manually, create an empty repo on GitHub, then add the remote and push.

Contributing
- Bug reports and pull requests are welcome. For significant changes, open an issue first to discuss the proposed change.

License
- This project is licensed under the MIT License — see `LICENSE` for details.
