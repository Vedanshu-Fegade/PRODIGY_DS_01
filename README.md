# PRODIGY_DS_01
# Project 1 — Population Data Visualization

A Python data visualization project that analyzes official population data and visualizes population distributions across countries.

## 📌 Project Overview

This project uses population data from **Our World in Data (OWID)** to:

* Identify the 15 most populous countries.
* Visualize the distribution of country populations.
* Analyze the overall shape of the population distribution.
* Generate reusable visualization outputs.
* Save key findings to a text file.

The data is sourced from the official Our World in Data population dataset.

## 📊 Visualizations

### 1. Top 15 Most Populous Countries

A horizontal bar chart showing the 15 countries with the largest populations for the latest available year in the dataset.

**Output:**
`outputs/top_country_populations.png`

### 2. Distribution of Country Populations

A histogram showing how population sizes are distributed across countries.

**Output:**
`outputs/population_distribution.png`

The distribution is strongly **right-skewed**, meaning that a small number of countries have significantly larger populations than most countries.

## 🔍 Key Findings

* **Data year:** 2023
* **Countries analyzed:** 256
* **Largest population in the dataset:** World — 8,091.7 million
* The population distribution is strongly right-skewed.
* A relatively small number of countries account for much larger populations compared with most countries.

## 🛠️ Technologies Used

* **Python**
* **Pandas** — Data loading and analysis
* **Matplotlib** — Data visualization
* **Seaborn** — Visualization styling

The project automatically downloads the population dataset when the local data file is missing.

## 📁 Project Structure

```text
Project-1/
│
├── task01.py
├── data/
│   └── population.csv
│
├── outputs/
│   ├── top_country_populations.png
│   ├── population_distribution.png
│   └── findings.txt
│
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Project-1
```

### 2. Install dependencies

```bash
pip install pandas matplotlib seaborn
```

### 3. Run the project

```bash
python task01.py
```

The script will generate the visualization files and `findings.txt` inside the `outputs` folder.

## 📚 Data Source

**Our World in Data — Population Dataset**

Source:
https://ourworldindata.org/grapher/population.csv

The script uses the dataset's country codes to exclude aggregate regions from the country-level analysis.

## 📈 Learning Outcomes

Through this project, I practiced:

* Working with real-world datasets
* Reading and cleaning CSV data using Pandas
* Filtering and sorting datasets
* Finding the largest population values
* Creating bar charts and histograms
* Interpreting distributions
* Saving visualizations programmatically
* Structuring a Python data analysis project

## 👨‍💻 Author

**Vedanshu Fegade**

This project is part of my journey in learning **Python, Data Science, and Data Visualization**.

