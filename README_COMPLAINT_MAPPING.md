# Complaint Field Cleaning — README

**Script:** `complaint_cleaning.py`  
**Study:** Developing a Framework for Rational Prescription of Antibiotics in EMR — Lady Ridgeway Hospital OPD  
**Author:** Dr M.B.R.M.C.L. Jayarathne | MD Health Informatics | PGIM, University of Colombo

---

## What this script does

The raw `Complaint` field in HHIMS is free text typed by medical officers. It contains single-letter abbreviations, multi-letter codes, embedded duration information, spelling variants, and occasional ICD-style labels. This script standardises that field and adds three new columns to your dataframe:

| New column | Type | Description |
|---|---|---|
| `complaint_clean` | String | Plain English expanded version of the complaint |
| `complaint_category` | String | Clinical category for EDA and clustering (12 values) |
| `complaint_duration_days` | Integer / NULL | Duration in days extracted from the complaint text |

**Coverage on full dataset (653,926 records):**
- Classified: **622,529 (95.2%)**
- Unclassified: 31,397 (4.8%)
- With duration: 123,622 (18.9%)

---

## How to use

```python
import sys
sys.path.insert(0, r'C:\path\to\your\folder')   # adjust to where you saved the script

from complaint_cleaning import add_complaint_features

df = add_complaint_features(df)
# Three new columns are now in df
```

The function expects your dataframe to have a column called `Complaint`.  
If your column has a different name, pass it: `add_complaint_features(df, complaint_col='YourColName')`

---

## Cleaning steps (in order)

### Step 1 — Standardise raw text
- Convert to lowercase
- Replace commas, semicolons, slashes, pipes with spaces
- Expand bracket contents (e.g. `"common cold (acute)"` → `"common cold acute"`)
- Normalise multiple spaces to single space

### Step 2 — Expand abbreviations
- Strip duration tokens first (`1d`, `2d`, `1w` etc.) so they don't interfere with matching
- Check if entire entry matches an abbreviation → replace whole string
- Apply multi-word abbreviations (longest match first)
- Expand remaining single tokens one by one
- Remove duplicate consecutive words (e.g. `"cough cough"` → `"cough"`)

### Step 3 — Assign category
- Match cleaned text against keyword lists for each of the 12 categories
- If keywords from **one category** match → assign that category
- If keywords from **two or more different body systems** match → `Multi-system`
- If **nothing matches** → `Unclassified`
- Within Respiratory: apply priority rule (see below)

---

## Abbreviation reference

### Single-letter codes
| Code | Meaning |
|---|---|
| c | cough |
| f | fever |
| r | rash |
| s | skin |
| v | vomiting |
| n | nausea |
| d | diarrhoea |
| p | pain |
| w | **unspecified** — ambiguous (wheeze or wound, cannot decode) |
| e | **unspecified** — meaning unknown |

### Two-letter codes
| Code | Meaning |
|---|---|
| cc | cough cold |
| fc / cf | fever cough |
| vf | vomiting fever |
| ba | bronchial asthma |
| ln | lymph node enlargement |
| st | sore throat |
| sk | skin |
| cd | cough diarrhoea |
| co / cx | cough cold / cough |
| fe, f1–f5 | fever |
| c1–c5 | cough |

### Three-letter and longer codes
| Code | Meaning |
|---|---|
| ccf / fcc | cough cold fever |
| sob | shortness of breath |
| rti / urti / lrti | respiratory tract infection (upper / lower) |
| uti | urinary tract infection |
| hfm / hfmd | hand foot mouth disease |
| abd / loa | abdominal pain / loss of appetite |
| age | acute gastroenteritis |
| wax | ear wax |
| rsh / fev / cou | rash / fever / cough (truncated) |
| ough / ugh / couggh | cough (typo variants) |
| puf | fever |

### Duration-embedded patterns
Entries like `f1d`, `fe3d`, `fever1d`, `c2d` are handled by:
1. Extracting the number as `complaint_duration_days`
2. Expanding the letter prefix as a normal abbreviation

Examples: `f1d` → clean=`fever`, duration=`1` | `cough 3d` → clean=`cough`, duration=`3`

### Multi-word shorthand
| Input | Expanded to |
|---|---|
| abd pain / ab pain | abdominal pain |
| ear ache / earache | ear pain |
| loose motion / loose stool | diarrhoea |
| running nose / runny nose | nasal congestion |
| h ache / head ache | headache |
| cough and cold | cough cold |

### Typo corrections
| Typo | Corrected to |
|---|---|
| couggh, cogh, copugh, ough, ugh | cough |
| feveer | fever |
| dysurea | dysuria |

---

## Category reference

| Category | What it captures | Count | % |
|---|---|---|---|
| `Respiratory-URTI` | Cough, cold, common cold, RTI, URTI, sinusitis | 295,535 | 45.2% |
| `Multi-system` | Two or more body systems in one complaint | 126,147 | 19.3% |
| `Fever` | Fever without localising features | 84,962 | 13.0% |
| `Skin` | Rash, scabies, eczema, wound, chickenpox, tinea | 51,137 | 7.8% |
| `GI` | Vomiting, diarrhoea, abdominal pain, worms, gastroenteritis | 33,667 | 5.1% |
| `Unclassified` | Vague, surgical, or truly ambiguous entries | 31,397 | 4.8% |
| `ENT` | Ear pain, eye, sore throat, lymph node, toothache | 12,846 | 2.0% |
| `Respiratory-Wheeze` | Wheeze, asthma, bronchial asthma, SOB, stridor | 11,794 | 1.8% |
| `Neuro` | Seizure, headache, convulsions, migraine | 3,521 | 0.5% |
| `UTI` | Dysuria, urinary symptoms, haematuria | 1,628 | 0.2% |
| `Musculo` | Joint pain, limp, back pain, fracture | 1,163 | 0.2% |
| `Respiratory-LRTI` | Pneumonia, bronchitis, LRTI, consolidation | 129 | 0.0% |

### Why Respiratory is split into three sub-types

Treatment implications differ significantly:

- **Respiratory-LRTI** — most likely bacterial (pneumonia, bronchitis); antibiotics clearly indicated
- **Respiratory-Wheeze** — asthma, wheezing; primary treatment is bronchodilators, not antibiotics
- **Respiratory-URTI** — cough, cold, common cold; mostly viral, antibiotics often not indicated

**Priority rule (when multiple Respiratory sub-types match):**  
`Respiratory-LRTI` > `Respiratory-Wheeze` > `Respiratory-URTI`

This priority is applied **only within the Respiratory system**.  
If a Respiratory keyword AND a keyword from another system (e.g. GI, Skin) both match → `Multi-system`.

---

## Duration extraction rules

| Pattern | Result |
|---|---|
| `3d`, `3 d`, `3 days`, `3 day` | 3 |
| `1w`, `1 wk`, `1 week`, `2 weeks` | 7, 14 |
| `1m`, `1 month` | 30 |
| `f1d`, `fe3d`, `fever2d` | digit extracted before abbreviation expansion |
| No duration pattern | NULL |

Valid range: 1–365 days. Values outside this range are set to NULL.

---

## What stays Unclassified (and why)

These entries are left as `Unclassified` deliberately:

- **`w`** (1,642 records) — could be wheeze or wound. Dr Jayarathne confirmed this cannot be decoded with certainty.
- **`e`** (479 records) — unknown meaning.
- **`pain`** — no anatomical location, cannot determine body system.
- **Surgical items** (phymosis etc.) — not relevant to antibiotic prescribing categories.
- **`age`** (313 records) — appears to be a data entry error (age number entered in the complaint field).

`Unclassified` is retained as a valid category. It should not be dropped during EDA or clustering.

---

## Files in this folder

| File | Purpose |
|---|---|
| `complaint_cleaning.py` | Main script — import and use `add_complaint_features(df)` |
| `Complaint_Mapping_Reference.docx` | Detailed reference document with all mapping tables |
| `README.md` | This file |

---

## Running the built-in test suite

```bash
python complaint_cleaning.py
```

This runs 42 test cases covering all abbreviation types, category assignments, and duration extractions. All 42 should pass.

---

*Last updated: February 2026*  
*Study: MD Health Informatics Thesis — PGIM, University of Colombo*
