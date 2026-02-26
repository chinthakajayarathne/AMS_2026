# Antibiotic Prescribing Clustering Analysis
## Flat Jupyter Notebook — Complete Pipeline Reference

| | |
|---|---|
| **File** | `antibiotic_clustering_analysis.ipynb` |
| **Study** | Paediatric Outpatient Antibiotic Prescribing Archetypes |
| **Institution** | Lady Ridgeway Hospital for Children, Colombo |
| **Researcher** | Dr. Chinthaka Jayarathne, MD Health Informatics Batch 05, PGIM |
| **University** | University of Colombo |
| **Data** | January 2026, HHIMS pseudonymised dataset (17,345 encounters) |
| **Method** | K-medoids clustering with Gower distance |

---

## Table of Contents
1. [Quick Start](#1-quick-start)
2. [Project Structure](#2-project-structure)
3. [Prerequisites and Installation](#3-prerequisites-and-installation)
4. [Configuration](#4-configuration)
5. [How to Run](#5-how-to-run)
6. [Notebook Cell Map](#6-notebook-cell-map)
7. [Pipeline Steps Detail](#7-pipeline-steps-detail)
8. [Output Files Reference](#8-output-files-reference)
9. [Methodology](#9-methodology)
10. [Key Findings Summary](#10-key-findings-summary)
11. [Troubleshooting](#11-troubleshooting)

---

## 1. Quick Start

```bash
# Launch the notebook
jupyter notebook antibiotic_clustering_analysis.ipynb

# Inside Jupyter:
# 1. Run Cell 1 (Install Dependencies) — once only, restart kernel if prompted
# 2. Edit Cell 2 (Configuration) — set PATH_TO_DATA to your CSV path
# 3. Run Cell 3 (Imports)
# 4. Kernel -> Restart & Run All   (runs the complete pipeline)
```

---

## 2. Project Structure

```
extracted data/
|
|-- antibiotic_clustering_analysis.ipynb   <-- MAIN NOTEBOOK (entire pipeline)
|-- generate_notebook.py                   <-- Rebuilds the .ipynb from src/ files
|-- README_NOTEBOOK.md                     <-- This file
|
|-- src/                                   <-- Modular step scripts
|   |-- main.py                            <-- CLI runner (python src/main.py)
|   |-- config.py                          <-- Paths and parameters
|   |-- step1_data_preparation.py
|   |-- step2_prescriber_analysis.py
|   |-- step3_clustering.py
|   |-- step4_archetype_interpretation.py
|   |-- step5_validation.py
|   `-- step6_deliverables.py
|
|-- output/                                <-- Auto-created when pipeline runs
|   |-- data/
|   |   |-- encounter_level_clean.csv
|   |   |-- encounter_level_with_prescriber.csv
|   |   `-- encounter_level_clustered.csv
|   |-- figures/                           <-- 15 PNG charts
|   `-- reports/                           <-- Word, Excel, PowerPoint outputs
|
`-- raw data/   (separate folder)
    `-- 2026_januaryPrescriptions_pseudonymised.csv
```

The notebook is a **fully self-contained flat file** — all code from all six
`src/step*.py` files is inlined directly into the notebook cells. No external
module imports are required.

---

## 3. Prerequisites and Installation

### Python Version
Python 3.8 or newer. Tested on Python 3.9-3.14, Windows 10.

### Required Packages

| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation |
| `numpy` | Numerical computation |
| `matplotlib` | Charts |
| `seaborn` | Statistical visualisation |
| `scikit-learn` | PCA, silhouette score, adjusted rand index |
| `gower` | Gower distance matrix (mixed data types) |
| `kmedoids` | FasterPAM k-medoids algorithm |
| `scipy` | Kruskal-Wallis non-parametric test |
| `python-docx` | Microsoft Word report generation |
| `openpyxl` | Microsoft Excel workbook generation |
| `python-pptx` | Microsoft PowerPoint generation |

### Install via Notebook
Run **Cell 1** (Install Dependencies) in the notebook, then restart the kernel if prompted.

### Install via pip
```bash
pip install pandas numpy matplotlib seaborn scikit-learn gower kmedoids scipy python-docx openpyxl python-pptx
```

---

## 4. Configuration

The only mandatory change before running is the data file path.

**In Cell 2 of the notebook:**
```python
PATH_TO_DATA = "D:/Academic/MD Research 2025/raw data/2026_januaryPrescriptions_pseudonymised.csv"
```

Replace with the location of your CSV. Use forward slashes (/) on Windows.

### All Parameters (Cell 2)

| Parameter | Default | Description |
|-----------|---------|-------------|
| `PATH_TO_DATA` | _(set by user)_ | Absolute path to raw CSV |
| `K_RANGE` | range(3, 9) | k values tested in clustering (k=3 to k=8) |
| `BOOTSTRAP_ITERATIONS` | 20 | Bootstrap resampling runs for validation |
| `BOOTSTRAP_SAMPLE_FRACTION` | 0.80 | Fraction of dataset per bootstrap iteration |
| `BOOTSTRAP_MAX_SAMPLE` | 3000 | Hard cap on rows per bootstrap iteration |
| `POLYPHARMACY_THRESHOLD` | 3 | Min distinct drugs to flag polypharmacy |
| `MAX_AGE_MONTHS` | 216 | Encounters above 18 years are excluded |
| `MAX_WEIGHT_KG` | 150 | Weights above this are set to NaN |

---

## 5. How to Run

### Full Pipeline (Recommended)
```
1. Open:    jupyter notebook antibiotic_clustering_analysis.ipynb
2. Edit:    Cell 2 — set PATH_TO_DATA to your CSV file
3. Run all: Kernel -> Restart & Run All
4. Wait:    ~20-40 minutes total (Steps 3 and 5 are the slow steps)
5. Collect: outputs from output/ folder
```

### Step-by-Step (for inspection or re-running individual steps)
Each step has a **markdown cell** (description) followed by a **code cell**
(all functions + a `run()` call). Run cells in order. You can re-run any
step cell after previous steps have completed.

### Estimated Runtime

| Step | Description | Time (8 GB RAM laptop) |
|------|-------------|------------------------|
| 1 | Data loading, cleaning, EDA | ~30 seconds |
| 2 | Prescriber metrics | ~10 seconds |
| **3** | **Gower matrix + k-medoids** | **5-15 minutes** |
| 4 | Archetype profiling, Word report | ~30 seconds |
| **5** | **Bootstrap validation** | **10-20 minutes** |
| 6 | Excel + PowerPoint + Word | ~30 seconds |
| **Total** | | **~20-40 minutes** |

### Alternative: Run as Python Scripts
```bash
cd "D:\Academic\MD Research 2025\extracted data"

python src/main.py           # all 6 steps
python src/main.py 1 2 3     # steps 1, 2, 3 only
python src/main.py 4 5 6     # steps 4, 5, 6 only
```

---

## 6. Notebook Cell Map

| Cell ID | Type | Purpose |
|---------|------|---------|
| `md-00-title` | Markdown | Title, study metadata, pipeline overview |
| `md-01-install` | Markdown | Install instructions header |
| `cd-02-install` | **Code** | pip install all required packages |
| `md-03-config` | Markdown | Configuration instructions |
| `cd-04-config` | **Code** | Paths, parameters, directory creation |
| `md-05-imports` | Markdown | Imports header |
| `cd-06-imports` | **Code** | All library imports + plot style |
| `md-07-s1` | Markdown | Step 1 description and output |
| `cd-08-s1` | **Code** | Step 1: data prep functions + run() |
| `md-09-s2` | Markdown | Step 2 description and output |
| `cd-10-s2` | **Code** | Step 2: prescriber analysis + run() |
| `md-11-s3` | Markdown | Step 3 description and output |
| `cd-12-s3` | **Code** | Step 3: clustering functions + run() |
| `md-13-s4` | Markdown | Step 4 description and output |
| `cd-14-s4` | **Code** | Step 4: archetype interpretation + run() |
| `md-15-s5` | Markdown | Step 5 description and output |
| `cd-16-s5` | **Code** | Step 5: bootstrap validation + run() |
| `md-17-s6` | Markdown | Step 6 description and output |
| `cd-18-s6` | **Code** | Step 6: final deliverables + run() |
| `md-19-done` | Markdown | Completion summary, output file table |

**Total: 20 cells** (11 markdown + 9 code)

---

## 7. Pipeline Steps Detail

### Step 1: Data Preparation and Exploratory Analysis

Reads the raw HHIMS CSV and builds the clean encounter-level dataset.

**Processing:**
- Renames pseudonymised columns: `patient_pseudo_id` -> `patient_id`, `prescriber_pseudo_id` -> `prescriber_id`
- Derives binary flags:
  - `antibiotic_monotherapy` = 1 if num_antibiotics == 1
  - `antibiotic_combination` = 1 if num_antibiotics >= 2
  - `polypharmacy_flag` = 1 if num_distinct_drugs >= 3
- Data cleaning: removes age > 216 months; sets invalid weight to NaN
- **Complaint harmonisation** via rule-based regex:
  - Strips duration markers (1d, 2d, 1/52, today, x3d)
  - Detects compound abbreviations first: ccf (cough+cold+fever), ccw (cough+cold+wheeze), cf, fc, vf, fv, cc
  - Matches standalone single-letter tokens: c=cough, f=fever, v=vomiting
  - Detects longer patterns: cold, fever, cough, wheeze, diarrhoea, rash, UTI, etc.
  - Produces `complaint_harmonized` text column (semicolon-separated canonical tags)
  - Produces 15 binary `symp_*` columns:
    symp_cough, symp_cold, symp_fever, symp_wheeze_sob, symp_vomiting,
    symp_diarrhoea, symp_rash, symp_abdom_pain, symp_trauma, symp_scabies,
    symp_worms, symp_ear, symp_eye, symp_uti, symp_urti
- Prints EDA: encounter counts, antibiotic rate, age groups, drug distribution
- Saves 5 figures (01-05)

**Output:** `output/data/encounter_level_clean.csv`

---

### Step 2: Prescriber Behaviour Analysis

Computes per-prescriber metrics and merges them onto encounter rows.

**Metrics computed per prescriber:**
- `prescriber_antibiotic_rate` - proportion of their encounters with an antibiotic
- `prescriber_mean_num_antibiotics` - mean antibiotics per encounter
- `prescriber_polypharmacy_rate` - proportion of encounters with polypharmacy

These three columns are merged back as encounter-level features so that
prescriber behaviour is included in the clustering step.

**Output:** `output/data/encounter_level_with_prescriber.csv`

---

### Step 3: K-medoids Clustering

Clusters all 17,345 encounters using Gower distance + FasterPAM k-medoids.

**Feature matrix:**

| Component | Features | Transform |
|-----------|---------|-----------|
| Numerical (5) | age_months, PatientWeight, num_distinct_drugs, num_antibiotics, prescriber_antibiotic_rate | StandardScaler |
| Binary (3) | has_antibiotic, antibiotic_combination, polypharmacy_flag | None (0/1) |
| Categorical (3) | age_stratum, Gender, VisitType | One-hot encoding |

**Algorithm:**
1. Missing weight: filled with column median
2. Gower distance matrix: n x n matrix, each cell [0, 1]
3. FasterPAM: run for k = 3, 4, 5, 6, 7, 8
4. Silhouette score: computed on precomputed distance for each k
5. Best k: maximum silhouette
6. Cluster assignment saved as `cluster` column (0 to k-1)
7. Cluster profiles: mean features, AB rates, cross-tabs with age stratum

> Computing the Gower distance matrix takes 5-15 minutes on a standard laptop.
> The matrix requires approximately 2.4 GB of RAM for 17k rows.

**Output:** `output/data/encounter_level_clustered.csv`

---

### Step 4: Archetype Interpretation

Profiles each cluster and generates a formatted Word report.

**Per-cluster analysis:**
- Clinical profile: dominant age group, mean age/weight, gender distribution, visit types
- Prescribing: AB rate, monotherapy%, combination%, polypharmacy%, mean drugs, mean antibiotics
- Prescriber: mean and SD of prescriber_antibiotic_rate
- Top 10 complaints: from raw Complaint field (comma-split)
- Top 10 drugs: from drug_names pipe-delimited field (`|` separator)
- Archetype name: auto-generated from AB rate + polypharmacy + dominant age

**Archetype naming rules:**
- AB rate < 20%: "Low-Antibiotic" | 20-50%: "Moderate-Antibiotic" | >50%: "High-Antibiotic"
- Polypharmacy > 50%: + "High-Polypharmacy"
- Combination > 30%: + "Combination-Therapy" | < 10%: + "Monotherapy-Dominant"
- Age group: maps to Neonatal, Infant, Toddler, Preschool, School-Age, Adolescent, Mixed-Age

**Output:** `output/reports/cluster_analysis_report.docx`

---

### Step 5: Bootstrap Validation

Quantifies cluster stability and tests statistical significance.

**Bootstrap stability (20 iterations):**
- Per iteration: sample 80% of data (max 3,000 rows), compute Gower, run FasterPAM
- Adjusted Rand Index (ARI): agreement between bootstrap labels and original labels
  - ARI = 1.0: perfect agreement | ARI = 0.0: random chance
- Silhouette: computed on each bootstrap subsample
- Cluster stability = mean ARI (used as proxy for per-cluster stability)

**Statistical tests (Kruskal-Wallis H-test):**
- Tests each variable for significant differences across clusters
- Variables: age_months, PatientWeight, num_distinct_drugs, num_antibiotics,
  has_antibiotic, polypharmacy_flag, prescriber_antibiotic_rate
- p < 0.05 = statistically significant difference between clusters

**Output:** `output/reports/validation_results.xlsx` (3 sheets: Bootstrap Summary, Cluster Stability, Statistical Tests)

---

### Step 6: Final Deliverables

Assembles presentation-ready output files.

**Excel workbook** `final_deliverables.xlsx` - 5 sheets:
1. Cluster Summary: one row per cluster, all key metrics
2. Encounter Data: full dataset (all columns, up to 100,000 rows)
3. Prescriber Analysis: per-prescriber stats sorted by total encounters
4. Top Drugs by Cluster: top 15 drugs per cluster with counts
5. Validation: bootstrap summary from Step 5

**PowerPoint** `final_presentation.pptx`:
- Slide 1: Title and study context
- Slide 2: Data overview (encounters, patients, prescribers, AB rate)
- Slide 3: Methodology (Gower + k-medoids, features, optimal k)
- Slides 4+: One slide per cluster (N, age, AB rate, polypharmacy, drugs, combination%)
- Figure slides: PCA projection, cluster heatmap, comparison bars, silhouette scores

**Word report** `summary_report.docx`:
- Methods paragraph, descriptive statistics, per-cluster summaries, embedded figures

**Output:** `output/reports/` (3 files)

---

## 8. Output Files Reference

### Data Files (`output/data/`)

| File | Rows | New Columns Added |
|------|------|-------------------|
| `encounter_level_clean.csv` | 17,345 | antibiotic_monotherapy, antibiotic_combination, polypharmacy_flag, complaint_harmonized, symp_* (15 cols) |
| `encounter_level_with_prescriber.csv` | 17,345 | prescriber_antibiotic_rate, prescriber_mean_num_antibiotics, prescriber_polypharmacy_rate |
| `encounter_level_clustered.csv` | 17,345 | cluster (integer, 0 to k-1) |

### Figures (`output/figures/`) — 15 PNG files @ 150 DPI

| File | Step | Description |
|------|------|-------------|
| 01_encounters_by_age.png | 1 | Bar: encounter count by age stratum |
| 02_antibiotic_pie.png | 1 | Pie: AB vs non-AB encounters |
| 03_drugs_histogram.png | 1 | Histogram: drugs per encounter |
| 04_antibiotics_by_age_box.png | 1 | Box: antibiotics/encounter by age |
| 05_ab_rate_by_age.png | 1 | Bar: antibiotic rate % by age stratum |
| 06_prescriber_ab_rate_dist.png | 2 | Histogram: prescriber AB rates |
| 07_prescriber_volume_vs_ab.png | 2 | Scatter: volume vs AB rate |
| 08_prescriber_behaviour_box.png | 2 | Box: 3 prescriber behaviour metrics |
| 09_silhouette_scores.png | 3 | Line: silhouette score by k (3-8) |
| 10_pca_clusters.png | 3 | Scatter: PCA 2D cluster projection |
| 11_cluster_heatmap.png | 3 | Heatmap: mean features per cluster |
| 12_cluster_comparison_bars.png | 3 | Bar: AB/polypharmacy/combo % by cluster |
| 13_cluster_sizes.png | 3 | Bar: encounter count per cluster |
| 14_bootstrap_distributions.png | 5 | Histogram: ARI + silhouette across iterations |
| 15_cluster_stability.png | 5 | Bar: per-cluster stability (mean ARI) |

### Reports (`output/reports/`)

| File | Format | Description |
|------|--------|-------------|
| `cluster_analysis_report.docx` | Word | Detailed per-cluster clinical profiles |
| `validation_results.xlsx` | Excel | Bootstrap results + Kruskal-Wallis table |
| `final_deliverables.xlsx` | Excel | 5-sheet comprehensive workbook |
| `final_presentation.pptx` | PowerPoint | Slides with embedded figures |
| `summary_report.docx` | Word | Summary with methods + embedded figures |

---

## 9. Methodology

### Study Design
Cross-sectional analysis of all outpatient prescriptions from Lady Ridgeway Hospital
HHIMS for January 2026. Unit of analysis: encounter (OPD visit).

### Why Gower Distance?
Handles mixed data types (numerical + binary + categorical) in a single distance
matrix without ad-hoc engineering. Each variable type uses its own dissimilarity
measure (normalised range for continuous, simple match for binary/categorical),
and results are averaged to a single [0,1] distance.

### Why K-medoids over K-means?
- **Interpretability**: medoids are actual encounters in the dataset
- **Robustness**: less sensitive to outliers than means
- **FasterPAM**: O(n^2) algorithm, feasible for 17k rows

### AWaRe Framework (WHO)
- **Access**: amoxicillin, cefalexin, cloxacillin, metronidazole, co-trimoxazole, doxycycline
- **Watch**: co-amoxiclav, azithromycin, clarithromycin, ciprofloxacin, clindamycin, cefuroxime, ceftriaxone
- **Reserve**: carbapenems, glycopeptides, polymyxins

### Key Data Notes
- `drug_groups` column contains UNIQUE drug groups per encounter (NOT per-drug)
- `drug_names` is a pipe-delimited string aligned per drug prescribed
- Antibiotic identification uses drug name matching, NOT the drug_groups column
- Pseudonymised IDs: patient_pseudo_id and prescriber_pseudo_id

---

## 10. Key Findings Summary

### Overall (January 2026, n = 17,345)

| Metric | Value |
|--------|-------|
| Antibiotic prescribing rate | 42.6% |
| Access-group (of AB encounters) | 77.6% |
| WHO Access target (>=60%) | MET |
| Top antibiotic | Amoxicillin 47.1% |
| 2nd | Cefalexin 21.3% |
| 3rd | Co-amoxiclav 12.3% |

### Patient Trajectory Archetypes

| Archetype | Proportion |
|-----------|-----------|
| AB-Free | 28.4% |
| Cluster-Stable | 26.6% |
| Appropriate-Escalation | 24.4% |
| AB-Every-Time (intervention target) | 18.2% |
| Treatment-Failure | 2.4% |

### Prescriber Archetypes

| Archetype | Proportion |
|-----------|-----------|
| Stable-Conservative | 43.2% |
| Stable-Moderate | 31.8% |
| Stable-Aggressive | 9.1% |
| Variable | 9.1% |

### Significant Factors

| Factor | Effect | Significance |
|--------|--------|-------------|
| Time of day (AM vs PM) | +10.7 pp antibiotic rate | p < 0.001 |
| Decision fatigue (encounter position) | +7.0 pp | p < 0.001 |
| Prescriber identity | 42% feature importance for Watch prediction | Key predictor |
| Volume-pressure | Not significant | — |
| Monday effect | Not significant | — |
| Institutional time trend | Not significant | — |

---

## 11. Troubleshooting

### "ModuleNotFoundError: No module named gower" (or kmedoids, docx, pptx)
```bash
pip install gower kmedoids python-docx python-pptx openpyxl
```

### Step 3 is very slow (>30 minutes)
Expected on low-RAM machines. The Gower matrix for 17k rows requires ~2.4 GB RAM
and millions of distance calculations.

To develop with a smaller sample (edit at the start of Step 3's code cell):
```python
df = df.sample(5000, random_state=42).reset_index(drop=True)
```

Or run on Google Colab (free, 12 GB RAM).

### MemoryError
Close all other applications, or reduce dataset. Colab is a good alternative.

### UnicodeEncodeError on Windows console
```bash
set PYTHONIOENCODING=utf-8
jupyter notebook antibiotic_clustering_analysis.ipynb
```

### Steps must run in order
Steps 1 -> 2 -> 3 -> 4 -> 5 -> 6 are sequential. Each reads the CSV from the
previous step. Use Kernel -> Restart & Run All for correct execution order.

### Silhouette scores all negative
The dataset may lack clear cluster structure for the chosen k range. Check
the `09_silhouette_scores.png` figure. Consider a narrower k range.

### Word/Excel/PowerPoint files do not open
Use LibreOffice (free, compatible with .docx, .xlsx, .pptx) if Microsoft
Office is not available.

### Regenerating the notebook after modifying src/ files
```bash
cd "D:\Academic\MD Research 2025\extracted data"
python generate_notebook.py
```

---

*Phase 2a: Quantitative Clustering Analysis*
*PGIM MD Health Informatics, University of Colombo | February 2026*
