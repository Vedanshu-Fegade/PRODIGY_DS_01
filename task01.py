"""Task 01 — visualize population distributions with official population data.

Source: https://ourworldindata.org/grapher/population.csv
"""
from pathlib import Path
from urllib.request import Request, urlopen

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "population.csv"
OUT = ROOT / "outputs"
SOURCE = "https://ourworldindata.org/grapher/population.csv"


def load_data() -> pd.DataFrame:
    DATA.parent.mkdir(exist_ok=True)
    if not DATA.exists() or DATA.stat().st_size == 0:
        print("Downloading population data…")
        # OWID rejects Python's default anonymous user agent.
        request = Request(SOURCE, headers={"User-Agent": "Mozilla/5.0 (compatible; ProdigyDSProject/1.0)"})
        with urlopen(request) as response, DATA.open("wb") as destination:
            destination.write(response.read())
    frame = pd.read_csv(DATA)
    value_column = next(c for c in frame.columns if c not in {"Entity", "Code", "Year"})
    frame = frame.rename(columns={value_column: "Population"})
    # Keep countries; OWID aggregate regions have no ISO country code.
    return frame.dropna(subset=["Code", "Population"])


def main() -> None:
    sns.set_theme(style="whitegrid")
    OUT.mkdir(exist_ok=True)
    df = load_data()
    latest_year = int(df["Year"].max())
    latest = df[df["Year"] == latest_year].copy()
    top = latest.nlargest(15, "Population").sort_values("Population")

    plt.figure(figsize=(10, 7))
    plt.barh(top["Entity"], top["Population"] / 1e6, color="#4C78A8")
    plt.title(f"15 Most Populous Countries ({latest_year})")
    plt.xlabel("Population (millions)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(OUT / "top_country_populations.png", dpi=180)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.hist(latest["Population"] / 1e6, bins=30, color="#72B7B2", edgecolor="white")
    plt.title(f"Distribution of Country Populations ({latest_year})")
    plt.xlabel("Population (millions)")
    plt.ylabel("Number of countries")
    plt.tight_layout()
    plt.savefig(OUT / "population_distribution.png", dpi=180)
    plt.close()

    (OUT / "findings.txt").write_text(
        f"Data year: {latest_year}\nCountries analysed: {len(latest)}\n"
        f"Largest population: {top.iloc[-1]['Entity']} "
        f"({top.iloc[-1]['Population'] / 1e6:,.1f} million).\n"
        "The histogram is strongly right-skewed: a small number of countries "
        "contain much larger populations than most countries.\n",
        encoding="utf-8",
    )
    print(f"Task 01 complete — figures saved in {OUT}")


if __name__ == "__main__":
    main()
