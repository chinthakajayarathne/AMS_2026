# Lady Ridgeway Hospital for Children
## Outpatient Department Drug Formulary
### Antibiotic Classification Report
**WHO AWaRe Categories | Antibiotic Groups | Spectrum of Activity**

---

| | |
|---|---|
| **Prepared by** | Dr. M.B.R.M.C.L. Jayarathne (SLMC: 27381) |
| **Programme** | MD Health Informatics (Batch 05), PGIM, University of Colombo |
| **Supervisors** | Dr. Roshan Hewapathirana & Dr. Udith Perera |
| **Date** | February 2026 |

---

## 1. Overview

This report documents all 423 drugs identified in the HHIMS outpatient prescription data extracted from Lady Ridgeway Hospital for Children for January 2026. It provides a comprehensive classification of all antibiotics present in the OPD formulary according to antibiotic group, route of administration, WHO AWaRe category (2023), and spectrum of activity.

This classification underpins the AWaRe enrichment step of Phase 2 of the MD Health Informatics research project, which aims to develop an EMR-integrated framework for rational antibiotic prescribing in the paediatric outpatient setting.

---

## 2. Summary Statistics

| Metric | Count |
|---|---|
| Total drugs in OPD formulary | 423 |
| Total antibiotic formulations identified | 83 |
| 🟢 Access category formulations | 40 |
| 🟡 Watch category formulations | 33 |
| 🔴 Reserve category formulations | 0 |
| ⚪ Not classified in WHO AWaRe 2023 | 10 |

> **Note:** AWaRe categories follow WHO 2023 classification. Topical-only formulations of Watch agents are classified per the active ingredient's systemic AWaRe category. Some agents used only topically or for specific indications (mupirocin, framycetin, furazolidone, clofazimine) are not listed in the WHO AWaRe 2023 EML and are classified as *Not classified*.

---

## 3. Antibiotic Classification — Detailed Table

**Colour key:** 🟢 ACCESS &nbsp;|&nbsp; 🟡 WATCH &nbsp;|&nbsp; 🔴 RESERVE &nbsp;|&nbsp; ⚪ NOT CLASSIFIED

### 3.1 Penicillins

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Amoxicillin 125 mg Tabs | Amoxicillin | Aminopenicillin | Oral | 🟢 Access | Narrow-Moderate | First-line for common paediatric infections |
| Amoxicillin 125mg/5ml Syrup | Amoxicillin | Aminopenicillin | Oral | 🟢 Access | Narrow-Moderate | Paediatric syrup formulation |
| Amoxicillin 250 mg Caps | Amoxicillin | Aminopenicillin | Oral | 🟢 Access | Narrow-Moderate | Standard oral dose |
| Amoxicillin 500 mg | Amoxicillin | Aminopenicillin | Oral | 🟢 Access | Narrow-Moderate | Higher dose |
| Cloxacillin sy 62.5mg in 2.5ml | Cloxacillin | Penicillinase-resistant Penicillin | Oral | 🟢 Access | Narrow | Anti-staphylococcal |
| Flucloxacillin 500mg | Flucloxacillin | Penicillinase-resistant Penicillin | Oral | 🟢 Access | Narrow | Anti-staphylococcal |
| Flucloxacillin Syr. 125mg/5ml | Flucloxacillin | Penicillinase-resistant Penicillin | Oral | 🟢 Access | Narrow | Paediatric syrup |
| Flucloxacillin capsule 250mg | Flucloxacillin | Penicillinase-resistant Penicillin | Oral | 🟢 Access | Narrow | Anti-staphylococcal |
| Flucloxacillin injection 500mg | Flucloxacillin | Penicillinase-resistant Penicillin | Parenteral | 🟢 Access | Narrow | IV/IM for severe infections |
| Phenoxymethylpenicillin 125mg Tab | Phenoxymethylpenicillin | Natural Penicillin | Oral | 🟢 Access | Narrow | Penicillin V |
| Phenoxymethylpenicillin 250mg Tabs | Phenoxymethylpenicillin | Natural Penicillin | Oral | 🟢 Access | Narrow | Penicillin V |

### 3.2 Beta-lactam / Beta-lactamase Inhibitor Combinations

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Co-Amoxiclav (Augmentin) 125/31mg/5ml Sy. | Amoxicillin + Clavulanate | Aminopenicillin + BLI | Oral | 🟡 Watch | Broad | BLI combination — reserve for resistant organisms |
| Co-Amoxiclav (Augmentin) 625mg tab | Amoxicillin + Clavulanate | Aminopenicillin + BLI | Oral | 🟡 Watch | Broad | BLI combination — reserve for resistant organisms |
| Co-amoxiclav (Augmentin) Tab. 375mg | Amoxicillin + Clavulanate | Aminopenicillin + BLI | Oral | 🟡 Watch | Broad | BLI combination — reserve for resistant organisms |
| Co-amoxiclav Inj. 1000/200mg | Amoxicillin + Clavulanate | Aminopenicillin + BLI | Parenteral | 🟡 Watch | Broad | IV form for moderate-severe infections |
| Co-amoxiclav Inj. 500/100mg | Amoxicillin + Clavulanate | Aminopenicillin + BLI | Parenteral | 🟡 Watch | Broad | IV form for moderate-severe infections |

### 3.3 Cephalosporins

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Cephalexin 125mg Dispersible Tab | Cephalexin | 1st Gen. Cephalosporin | Oral | 🟢 Access | Narrow-Moderate | Skin/soft tissue, URTIs |
| Cephalexin 250 mg Caps | Cephalexin | 1st Gen. Cephalosporin | Oral | 🟢 Access | Narrow-Moderate | Skin/soft tissue, URTIs |
| Cephalexin Capsule 500mg | Cephalexin | 1st Gen. Cephalosporin | Oral | 🟢 Access | Narrow-Moderate | Skin/soft tissue, URTIs |
| Cephalexin Sy. 125mg/5ml 100ml | Cephalexin | 1st Gen. Cephalosporin | Oral | 🟢 Access | Narrow-Moderate | Paediatric syrup |
| Cefuroxime 250mg Tab | Cefuroxime | 2nd Gen. Cephalosporin | Oral | 🟡 Watch | Broad | Use restricted to guideline indications |
| Cefuroxime 500mg Tab | Cefuroxime | 2nd Gen. Cephalosporin | Oral | 🟡 Watch | Broad | Use restricted to guideline indications |
| Cefuroxime Axetil 125mg Tab | Cefuroxime | 2nd Gen. Cephalosporin | Oral | 🟡 Watch | Broad | Use restricted to guideline indications |
| Cefuroxime Syrup 125mg/5ml 100ml | Cefuroxime | 2nd Gen. Cephalosporin | Oral | 🟡 Watch | Broad | Paediatric syrup — Watch category |
| Cefixime Tablet 200mg | Cefixime | 3rd Gen. Cephalosporin | Oral | 🟡 Watch | Broad | Reserved for resistant/complicated infections |
| cefTAZidime Inj. 500mg | Ceftazidime | 3rd Gen. Cephalosporin | Parenteral | 🟡 Watch | Broad | For Gram-negative including Pseudomonas |

### 3.4 Macrolides

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Azithromycin 250mg Tab | Azithromycin | Macrolide | Oral | 🟡 Watch | Broad | Monitor for over-use; resistance concern |
| Azithromycin dihydrate syrup 200mg/5ml | Azithromycin | Macrolide | Oral | 🟡 Watch | Broad | Paediatric formulation; Watch category |
| Clarithromycin 250mg | Clarithromycin | Macrolide | Oral | 🟡 Watch | Broad | H. pylori eradication; atypicals |
| Clarithromycin 500mg Tab | Clarithromycin | Macrolide | Oral | 🟡 Watch | Broad | Higher dose formulation |
| Clarithromycin syrup 125mg/5ml 60ml | Clarithromycin | Macrolide | Oral | 🟡 Watch | Broad | Paediatric formulation |
| Erythromycin 250mg Tab | Erythromycin | Macrolide | Oral | 🟢 Access | Narrow-Moderate | Older macrolide; Access category |
| Erythromycin Syrup 125mg/5ml | Erythromycin | Macrolide | Oral | 🟢 Access | Narrow-Moderate | Paediatric formulation; Access category |

### 3.5 Fluoroquinolones

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Ciprofloxacin 250mg Tab | Ciprofloxacin | Fluoroquinolone | Oral | 🟡 Watch | Broad | Restricted in children — only when no alternative |
| Ciprofloxacin 500mg | Ciprofloxacin | Fluoroquinolone | Oral | 🟡 Watch | Broad | Restricted in children |
| Ciprofloxacin Ear drop 0.3% 5ml | Ciprofloxacin | Fluoroquinolone | Topical | 🟡 Watch | Broad | Topical — otitis externa |
| Ciprofloxacin Eye drops 0.3% 5ml | Ciprofloxacin | Fluoroquinolone | Topical | 🟡 Watch | Broad | Topical — bacterial conjunctivitis |
| Norfloxacin 400mg | Norfloxacin | Fluoroquinolone | Oral | 🟡 Watch | Narrow (urinary) | Urinary tract; avoid in children |
| Ofloxacin Ear drops 0.6% 5mL | Ofloxacin | Fluoroquinolone | Topical | 🟡 Watch | Broad | Topical otitis — Watch category |
| Moxifloxacin hydrochloride Ophthalmic solution 0.5% | Moxifloxacin | Fluoroquinolone | Topical | 🟡 Watch | Broad | Topical eye only; Watch category |

### 3.6 Tetracyclines

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Doxycycline 100mg Caps | Doxycycline | Tetracycline | Oral | 🟢 Access | Broad | Avoid in children <8 years |
| Tetracycline 250mg Caps | Tetracycline | Tetracycline | Oral | 🟢 Access | Broad | Avoid in children <8 years |
| Tetracycline Eye Ointment 1% | Tetracycline | Tetracycline | Topical | 🟢 Access | Broad | Topical; trachoma / neonatal conjunctivitis |

### 3.7 Aminoglycosides

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Gentamicin sulphate Ear drops 0.3% 5ml | Gentamicin | Aminoglycoside | Topical | 🟢 Access | Narrow (Gram-neg) | Topical ear; Access category |
| Gentamycin Eye drops 0.3% 5ml | Gentamicin | Aminoglycoside | Topical | 🟢 Access | Narrow (Gram-neg) | Topical eye; Access category |
| Gentamycin ear drops 0.3% 10ml | Gentamicin | Aminoglycoside | Topical | 🟢 Access | Narrow (Gram-neg) | Topical ear; Access category |
| gentamicin 0.3% with Hydrocortisone 1% Ear drops | Gentamicin + Hydrocortisone | Aminoglycoside | Topical | 🟢 Access | Narrow (Gram-neg) | Combined anti-infective + anti-inflammatory |
| Tobramycin 0.3%+Dexamethasone 0.1% eye drops | Tobramycin + Dexamethasone | Aminoglycoside | Topical | 🟡 Watch | Narrow (Gram-neg) | Combined ophthalmic; Watch category |
| Tobramycin ear drops 0.3% 5ml | Tobramycin | Aminoglycoside | Topical | 🟡 Watch | Narrow (Gram-neg) | Topical ear; Watch category |

### 3.8 Nitroimidazoles

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| metroNIDAZOLE 125mg/5ml Syrup | Metronidazole | Nitroimidazole | Oral | 🟢 Access | Narrow (anaerobes/protozoa) | Anaerobes and protozoa (Giardia, amoebiasis) |
| metroNIDAZOLE 200mg Tabs | Metronidazole | Nitroimidazole | Oral | 🟢 Access | Narrow (anaerobes/protozoa) | Anaerobes and protozoa |
| metroNIDAZOLE 400mg Tabs | Metronidazole | Nitroimidazole | Oral | 🟢 Access | Narrow (anaerobes/protozoa) | Standard adult/older child dose |
| metroNIDAZOLE Syr 200mg/5ml | Metronidazole | Nitroimidazole | Oral | 🟢 Access | Narrow (anaerobes/protozoa) | Paediatric syrup |
| metroNIDAZOLE gel 0.75-1% 30g | Metronidazole | Nitroimidazole | Topical | 🟢 Access | Narrow (anaerobes/protozoa) | Topical formulation |

### 3.9 Sulfonamides + Trimethoprim

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Co-trimoxazole 480mg Tabs | Sulfamethoxazole + Trimethoprim | Sulfonamide + Trimethoprim | Oral | 🟢 Access | Broad | PCP prophylaxis; UTI; Access category |
| Co-trimoxazole Cream 1% 15g | Sulfamethoxazole + Trimethoprim | Sulfonamide + Trimethoprim | Topical | 🟢 Access | Broad | Topical formulation |
| Co-trimoxazole Syr. 240mg/5ml 50ml | Sulfamethoxazole + Trimethoprim | Sulfonamide + Trimethoprim | Oral | 🟢 Access | Broad | Paediatric syrup |

### 3.10 Lincosamides

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Clindamycin gel 1% 30g | Clindamycin | Lincosamide | Topical | 🟡 Watch | Narrow (Gram-pos/anaerobes) | Topical acne treatment; Watch category |

### 3.11 Chloramphenicol

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Chloramphenicol Ear Drops 5% | Chloramphenicol | Chloramphenicol | Topical | 🟢 Access | Broad | Topical ear use only; Access category |
| Chloramphenicol Eye Drops 0.5% 5ml | Chloramphenicol | Chloramphenicol | Topical | 🟢 Access | Broad | Topical eye; Access category |

### 3.12 Fusidic Acid

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Fusidic Acid 250mg tablet | Fusidic Acid | Fusidic Acid | Oral | 🟡 Watch | Narrow (Staph.) | Narrow spectrum; used with another agent |
| Fusidic acid 2%+Betamethasone 0.1% Cream | Fusidic Acid + Betamethasone | Fusidic Acid | Topical | 🟡 Watch | Narrow (Staph.) | Combined topical; Watch category |
| Fusidic acid Eye Drop 1% | Fusidic Acid | Fusidic Acid | Topical | 🟡 Watch | Narrow (Staph.) | Topical ophthalmic |
| Fusidic acid cream 2% 5g | Fusidic Acid | Fusidic Acid | Topical | 🟡 Watch | Narrow (Staph.) | Skin infections; Watch category |

### 3.13 Nitrofurans

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Nitrofurantoin 25mg Tab | Nitrofurantoin | Nitrofuran | Oral | 🟢 Access | Narrow (urinary) | UTI prophylaxis/treatment; Access category |
| Nitrofurantoin 50mg Tab | Nitrofurantoin | Nitrofuran | Oral | 🟢 Access | Narrow (urinary) | UTI treatment; Access category |
| Furazolidone 100mg Tab | Furazolidone | Nitrofuran | Oral | ⚪ Not classified | Narrow (GI pathogens) | Enteric infections; not in WHO AWaRe 2023 |
| Furazolidone 25mg | Furazolidone | Nitrofuran | Oral | ⚪ Not classified | Narrow (GI pathogens) | Enteric infections |
| Furazolidone 50mg | Furazolidone | Nitrofuran | Oral | ⚪ Not classified | Narrow (GI pathogens) | Enteric infections |

### 3.14 Quinolones (1st Generation)

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Nalidixic Acid 500mg Tab | Nalidixic Acid | Quinolone (1st Gen.) | Oral | 🟡 Watch | Narrow (Gram-neg) | Older quinolone; urinary only; resistance concern |
| Nalidixic Acid Oral suspension 300mg | Nalidixic Acid | Quinolone (1st Gen.) | Oral | 🟡 Watch | Narrow (Gram-neg) | Paediatric suspension |
| Nalidixic acid 250mg Tab | Nalidixic Acid | Quinolone (1st Gen.) | Oral | 🟡 Watch | Narrow (Gram-neg) | Lower dose formulation |

### 3.15 Topical Antibacterials (Mupirocin)

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Mupirocin Cream 2% 5g | Mupirocin | Topical Antibacterial (Mupirocin) | Topical | ⚪ Not classified | Narrow (Staph./Strep.) | Impetigo; nasal decolonisation; topical only |
| Mupirocin Ointment 2% 5g | Mupirocin | Topical Antibacterial (Mupirocin) | Topical | ⚪ Not classified | Narrow (Staph./Strep.) | Impetigo; topical only |

### 3.16 Rifamycins

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| rifAMPicin 150mg | Rifampicin | Rifamycin | Oral | 🟡 Watch | Narrow (Mycobacteria/Staph.) | Anti-TB / anti-leprosy; Watch category |

### 3.17 Aminoglycosides — Framycetin (Soframycin)

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Framycetin Cream 1% 20g | Framycetin | Aminoglycoside (Framycetin) | Topical | ⚪ Not classified | Narrow (Gram-neg/Staph.) | Topical skin infections |
| Soframycin Cream | Framycetin | Aminoglycoside (Framycetin) | Topical | ⚪ Not classified | Narrow (Gram-neg/Staph.) | Topical skin infections |
| Soframycin Skin Cream 20g | Framycetin | Aminoglycoside (Framycetin) | Topical | ⚪ Not classified | Narrow (Gram-neg/Staph.) | Topical skin infections |
| Soframycin Skin Cream 5g | Framycetin | Aminoglycoside (Framycetin) | Topical | ⚪ Not classified | Narrow (Gram-neg/Staph.) | Topical skin infections |

### 3.18 Anti-leprosy

| Drug Name (as in HHIMS) | Compound | Antibiotic Group | Route | AWaRe | Spectrum | Notes |
|---|---|---|---|---|---|---|
| Clofazimine 100mg | Clofazimine | Riminophenazine (Anti-leprosy) | Oral | ⚪ Not classified | Narrow (Mycobacteria) | Anti-leprosy / anti-mycobacterial |

---

## 4. Summary by Antibiotic Group

| Antibiotic Group | Total Formulations | 🟢 Access | 🟡 Watch | 🔴 Reserve | ⚪ Not Classified |
|---|---|---|---|---|---|
| Aminopenicillin | 4 | 4 | — | — | — |
| Penicillinase-resistant Penicillin | 5 | 5 | — | — | — |
| Natural Penicillin | 2 | 2 | — | — | — |
| Aminopenicillin + Beta-lactamase inhibitor | 5 | — | 5 | — | — |
| 1st Gen. Cephalosporin | 4 | 4 | — | — | — |
| 2nd Gen. Cephalosporin | 4 | — | 4 | — | — |
| 3rd Gen. Cephalosporin | 2 | — | 2 | — | — |
| Macrolide | 7 | 2 | 5 | — | — |
| Fluoroquinolone | 7 | — | 7 | — | — |
| Tetracycline | 3 | 3 | — | — | — |
| Aminoglycoside | 6 | 4 | 2 | — | — |
| Nitroimidazole | 5 | 5 | — | — | — |
| Sulfonamide + Trimethoprim | 3 | 3 | — | — | — |
| Lincosamide | 1 | — | 1 | — | — |
| Chloramphenicol | 2 | 2 | — | — | — |
| Fusidic Acid | 4 | — | 4 | — | — |
| Nitrofuran | 5 | 2 | — | — | 3 |
| Quinolone (1st Gen.) | 3 | — | 3 | — | — |
| Topical Antibacterial (Mupirocin) | 2 | — | — | — | 2 |
| Rifamycin | 1 | — | 1 | — | — |
| Aminoglycoside (Framycetin) | 4 | — | — | — | 4 |
| Riminophenazine (Anti-leprosy) | 1 | — | — | — | 1 |
| **TOTAL** | **83** | **40** | **33** | **0** | **10** |

---

## 5. Complete OPD Drug Formulary — Alphabetical List

> Total: 423 drugs. Items marked with `*` are non-medicinal / consumable items.

| No. | Drug Name | No. | Drug Name |
|---|---|---|---|
| 1 | \*Balanced salt solution 500ml | 2 | \*Hydroxyethylcellulose 0.44% + Sodium Chloride 0.35% eye drop |
| 3 | 0.05% Fluoride Mouth Wash 60-100 ml | 4 | 0.2% Chlorhexidine Mouth Wash 100ml |
| 5 | Aciclovir Tab. 200mg | 6 | Aciclovir Tab. 800mg |
| 7 | Adapalene gel 0.1% 45g | 8 | Albendazole syrup 200mg/5ml 30ml |
| 9 | Alfa Calcidol 0.25mcg | 10 | Aluminium Hydroxide 500mg |
| 11 | Amitriptyline tab. 10mg | 12 | Amitriptyline tab. 25mg |
| 13 | Amorolfine Cream 1% 15g | 14 | Amoxicillin 125 mg Tabs |
| 15 | Amoxicillin 125mg/5ml Syrup | 16 | Amoxicillin 250 mg Caps |
| 17 | Amoxicillin 500 mg | 18 | Aqueous Cream |
| 19 | Aspirin Enteric-coated Tab 75mg | 20 | Atorvastatin 10mg Tab |
| 21 | Atorvastatin tab. 20mg | 22 | Atropine sulphate Eye Drops 1% 5ml |
| 23 | Azithromycin 250mg Tab | 24 | Azithromycin dihydrate syrup 200mg/5ml 15ml |
| 25 | Baby mask for spacer device | 26 | Baclofen tab. 10mg |
| 27 | Baclofen tablet 5mg | 28 | Beclometasone Nasal Spray 100mcg/MD 120D |
| 29 | Beclomethasone 0.025% and Miconazole 2% Lotion 30mL | 30 | Beclomethasone DP Caps 200mcg |
| 31 | Beclomethasone Dipropionate MDI 250mcg | 32 | Beclomethasone MDI 100mcg/MD 200D |
| 33 | Beclomethasone MDI 250mcg/MD 200D | 34 | Benzoyl Peroxide gel 5% 30g |
| 35 | Benzoyl peroxide gel 2.5% 20g | 36 | Benzyl Benzoate Application 25% 500ml |
| 37 | Betadine Cream (Povidone Iodine) 5% 20g | 38 | Betahistine 16mg |
| 39 | Betahistine tab. 8mg | 40 | Betamethasone Cream 0.1% 15g |
| 41 | Betamethasone Cream 0.1% 5g | 42 | Betamethasone Dipropionate Lotion 0.05% 30mL |
| 43 | Betamethasone Eye/Ear/Nasal drop 0.1% 5ml | 44 | Betamethasone Nasal/Ear/Eye Drops 0.1% 5ml |
| 45 | Betamethasone Ointment 0.1% 15g | 46 | Betamethasone Ointment 0.1% 5g |
| 47 | Betamethasone with Neomycin Ear/Nasal/Eye drop | 48 | Biphasic Isophane Insulin (human) inj. 30/70 |
| 49 | Bisacodyl suppository 10mg | 50 | Bisacodyl suppository 5mg |
| 51 | Bisacodyl tablet 10mg | 52 | Bisacodyl tablet 5mg |
| 53 | Budesonide+Formoterol MDI 200/6 120DOSE | 54 | Busulphan Tab 2mg |
| 55 | Calamine Powder | 56 | Calamine lotion |
| 57 | Calcipot 50mcg+Betamethasone oint. 15g | 58 | Calcitriol cap. 0.25mcg |
| 59 | Calcium 500mg+Vitamin D3 250IU Tab | 60 | Calcium Carbonate 1.25g Tab |
| 61 | Calcium Carbonate 500mg tab. | 62 | Calcium Carbonate Chewable Tab 1.25g |
| 63 | Calcium Lactate tab. 300mg | 64 | Calcium Polystyrene Sulphonate (RESONIUM) 15-17g sachet |
| 65 | Candid Ear Drops | 66 | Cefixime Tablet 200mg |
| 67 | Cefuroxime 250mg Tab | 68 | Cefuroxime 500mg Tab |
| 69 | Cefuroxime Axetil 125mg Tab | 70 | Cefuroxime Syrup 125mg/5ml 100ml |
| 71 | Celecoxib capsule 100mg | 72 | Cephalexin 125mg Dispersible Tab |
| 73 | Cephalexin 250 mg Caps | 74 | Cephalexin Capsule 500mg |
| 75 | Cephalexin Sy. 125mg/5ml 100ml | 76 | Cetirizine HCL syr. 5mg/5ml 60ml |
| 77 | Cetirizine Hydrochloride tab. 10mg | 78 | Cetrimide Cream 50g |
| 79 | Cetrimide Shampoo 1% | 80 | Cetrimide Shampoo 2% |
| 81 | Cetrimide Shampoo 3% | 82 | Cetrimide Shampoo 5% |
| 83 | Cetrimide Shampoo 10% | 84 | Chloral hydrate Oral Solution 500mg/5ml 200ml |
| 85 | Chlorambucil Tablet 2mg | 86 | Chloramphenicol Ear Drops 5% |
| 87 | Chloramphenicol Eye Drops 0.5% 5ml | 88 | Chlorhexidine solution 4% 500ml |
| 89 | Chlorpheniramine (Piriton) syr. 2mg/5ml 60ml | 90 | Chlorpheniramine (Piriton) tab. 4mg |
| 91 | Chlorpheniramine Maleate Inj. 10mg/1ml | 92 | Cholecalciferol (Cal D) tab 5000IU |
| 93 | Cholecalciferol cap/tab 1000IU | 94 | Cinnarizine Tab. 25mg |
| 95 | Ciprofloxacin 250mg Tab | 96 | Ciprofloxacin 500mg |
| 97 | Ciprofloxacin Ear drop 0.3% 5ml | 98 | Ciprofloxacin Eye drops 0.3% 5ml |
| 99 | Clarithromycin 250mg | 100 | Clarithromycin 500mg Tab |
| 101 | Clarithromycin syrup 125mg/5ml 60ml | 102 | Clindamycin gel 1% 30g |
| 103 | Clobetasol Cream 15g | 104 | Clobetasol Ointment 0.05% 15g |
| 105 | Clofazimine 100mg | 106 | Clotrimazole cream 1% 15g |
| 107 | Clotrimazole mouth paint 1% 15ml | 108 | Clotrimazole vaginal Tablets 100mg |
| 109 | Cloxacillin sy 62.5mg in 2.5ml | 110 | Co-Amoxiclav (Augmentin) 125/31mg/5ml Sy. |
| 111 | Co-Amoxiclav (Augmentin) 625mg tab | 112 | Co-amoxiclav (Augmentin) Tab. 375mg |
| 113 | Co-amoxiclav Inj. 1000/200mg | 114 | Co-amoxiclav Inj. 500/100mg |
| 115 | Co-careldopa (SINEMET) Modified release tab. 25/100mg | 116 | Co-careldopa (SINEMET) tab. 25/100mg |
| 117 | Co-careldopa (SINEMET) tab. 25/250mg | 118 | Co-trimoxazole 480mg Tabs |
| 119 | Co-trimoxazole Cream 1% 15g | 120 | Co-trimoxazole Syr. 240mg/5ml 50ml |
| 121 | Crepe Bandage | 122 | Crotamiton Cream 10% 20g |
| 123 | Cyclopentolate Eye Drops 1.0% 5ml | 124 | Desferrioxamine inj. 500mg |
| 125 | Desloratadine tablet 5mg | 126 | Desmopressin Tablet 100mcg |
| 127 | Desmopressin acetate Nasal spray 10mcg/metered spray | 128 | Dexamethasone 0.5mg Tabs |
| 129 | Diazoxide tablet 50mg | 130 | Diclofenac Sodium 25mg SR tablet |
| 131 | Diclofenac Sodium 50mg Tabs SR | 132 | Diclofenac Sodium Gel 1% 20g |
| 133 | Diclofenac Sodium Supp. 12.5mg | 134 | Diclofenac Sodium Tab. 50mg |
| 135 | Diclofenac sodium Tab. 25mg | 136 | Diethylcarbamazine Citrate 100mg tab. |
| 137 | Diethylcarbamazine Citrate 50mg | 138 | Domperidone 10mg Tabs |
| 139 | Domperidone Sy. 5mg/5ml 100ml | 140 | Domperidone syrup 5mg/5ml 60ml |
| 141 | Doxycycline 100mg Caps | 142 | Emulsifying Ointment |
| 143 | Enoxaparin Inj. 40mg/0.4ml | 144 | Epoetin Inj. 4000IU |
| 145 | Epoetin inj. 2000IU | 146 | Erythromycin 250mg Tab |
| 147 | Erythromycin Syrup 125mg/5ml | 148 | Esomeprazole Tab/Cap 20mg |
| 149 | Esomeprazole Tab/Cap 40mg | 150 | Famotidine 10mg |
| 151 | Famotidine 20mg Tab | 152 | Ferrous Fumarate chewable 100mg |
| 153 | Ferrous Sulphate 200mg Tab | 154 | Fexofenadine HCL 120mg tab |
| 155 | Fexofenadine HCL 30mg tab | 156 | Fexofenadine HCL 60mg tab |
| 157 | Flucloxacillin 500mg | 158 | Flucloxacillin Syr. 125mg/5ml 100ml |
| 159 | Flucloxacillin capsule 250mg | 160 | Flucloxacillin injection 500mg |
| 161 | Fluconazole 50mg | 162 | Fluconazole Inj. 200mg |
| 163 | Fludrocortisone acetate 0.1mg | 164 | Flunarizine HCL tab. 5mg |
| 165 | Fluorometholone Eye drops 0.1% 5ml | 166 | Fluticasone + Salmeterol MDI 125/25mcg 120D |
| 167 | Fluticasone + Salmeterol MDI 250/25mcg 120D | 168 | Fluticasone nasal spray 50mcg/MD 150 doses |
| 169 | Folic Acid tab 1mg | 170 | Framycetin Cream 1% 20g |
| 171 | Frusemide (Lasix) 40mg tab | 172 | Furazolidone 100mg Tab |
| 173 | Furazolidone 25mg | 174 | Furazolidone 50mg |
| 175 | Furosemide Tablet 10mg | 176 | Fusidic Acid 250mg tablet |
| 177 | Fusidic acid 2%+Betamethasone 0.1% Cream | 178 | Fusidic acid Eye Drop 1% |
| 179 | Fusidic acid cream 2% 5g | 180 | Gentamicin sulphate Ear drops 0.3% 5ml |
| 181 | Gentamycin Eye drops 0.3% 5ml | 182 | Gentamycin ear drops 0.3% 10ml |
| 183 | Gliclazide MR tablet 30mg | 184 | Glycerin |
| 185 | Glycerin Suppository 2g | 186 | Griseofulvin Tab. 500mg |
| 187 | Haloperidol Tab. 1.5mg | 188 | Heparin Inj. 25,000 IU/5ml |
| 189 | Hydrating wound gel | 190 | Hydrocortisone 0.5% + Clioquinol 3% cream 15g |
| 191 | Hydrocortisone 5mg | 192 | Hydrocortisone Injection |
| 193 | Hydrocortisone Skin Cream 1% 5g | 194 | Hydrocortisone Skin Cream 1% 15g |
| 195 | Hydrocortisone Skin Ointment 1% 15g | 196 | Hydrocortisone Skin Ointment 1% 5g |
| 197 | Hydrocortisone tablet 10mg | 198 | Hydroxocobalamin (Vitamin B12) inj. 1mg/1ml |
| 199 | Hydroxychloroquine sulph. Tab. 200mg | 200 | Hydroxyurea capsule 500mg |
| 201 | Hyoscine Butylbromide 10mg Tab | 202 | Ibuprofen Tabs 200mg |
| 203 | Ibuprofen syr. 100mg/5ml 60ml | 204 | Ibuprofen tab. 400mg |
| 205 | Imipramine tab. 25mg | 206 | Indomethacin cap. 25mg |
| 207 | Insulin Glargine 100IU/ml | 208 | Iron Drops 125mg/ml |
| 209 | Iron Drops 50mg/1ml | 210 | Iron Drops 50mg/ml 15ml |
| 211 | Iron syr. 50mg/5ml 100ml | 212 | Itraconazole Cap. 100mg |
| 213 | Itraconazole Syr. 10mg | 214 | Ketorolac Tromethamine Gel 2% 30g |
| 215 | Labetalol HCl Inj. 100mg/20ml | 216 | Lactulose Syrup 3-3.7g/5ml 120ml |
| 217 | Lactulose Syrup 3.35g/5ml 100ml | 218 | Levamisole hydrochloride 40mg tab |
| 219 | Lidocaine Tropical aerosol 10% 50ml | 220 | Lignocaine anhydrous gel 2% 30g |
| 221 | Loperamide HCl Tab/Cap 2mg | 222 | Losartan Potassium 50mg Tabs |
| 223 | Mebendazole 100mg | 224 | Mebendazole Tab. 500mg |
| 225 | Mebeverine hydrochloride tablet 135mg | 226 | Mefenamic Acid Tab. 500mg |
| 227 | Methotrexate 2.5mg Tabs | 228 | Methyl Salicylate |
| 229 | Methyl Salicylate ointment | 230 | Methylphenidate hydrochloride Tab. 10mg |
| 231 | Metoclopramide 10mg Tabs | 232 | Miconazole Cream 2% 15g |
| 233 | Miconazole Cream 2% 30g | 234 | Miconazole Oromucosal gel 40g |
| 235 | Montelukast Sodium chewable Tab. 5mg | 236 | Montelukast sodium tab. 10mg |
| 237 | Moxifloxacin hydrochloride Ophthalmic solution 0.5% | 238 | Multivitamin Drops 15ml |
| 239 | Multivitamin+ Zinc Syrup 200ml | 240 | Mupirocin Cream 2% 5g |
| 241 | Mupirocin Ointment 2% 5g | 242 | Mycophenolate Mofetil (MMF) Tab. 250mg |
| 243 | Mycophenolate Mofetil (MMF) Tab. 500mg | 244 | Nalidixic Acid 500mg Tab |
| 245 | Nalidixic Acid Oral suspension 300mg | 246 | Nalidixic acid 250mg Tab |
| 247 | Naproxen tablet 250mg | 248 | Nebulize with Normal Saline |
| 249 | NIFEdipine SR 20mg tab | 250 | Nitrofurantoin 25mg Tab |
| 251 | Nitrofurantoin 50mg Tab | 252 | Norethisterone 5mg Tabs |
| 253 | Norfloxacin 400mg | 254 | Normal Saline 500ml |
| 255 | Normal Saline Nasal Drops | 256 | Nystatin 500000 IU |
| 257 | Oestrogen Vaginal Cream 0.1% 15g | 258 | Ofloxacin Ear drops 0.6% 5mL |
| 259 | Omeprazole 20mg Caps | 260 | Omeprazole sodium Inj. 40mg |
| 261 | Omeprazole tablet 10mg | 262 | Ondansetron Oral Solution 4mg/5ml 50ml |
| 263 | Ondansetron tablet 4mg | 264 | Oral Rehydration Powder Sachet (Jeewani) 200ml |
| 265 | Oral Rehydration Solution (Jeewani) | 266 | Oral rehydration Powder sachets 1 Liter |
| 267 | Oseltamivir Syr. 30mg/5ml 65ml | 268 | Paracetamol 10mg/ml solution for infusion 100ml |
| 269 | Paracetamol Suppository 125mg | 270 | Paracetamol Suppository 250mg |
| 271 | Paracetamol Suppository 500mg | 272 | Paracetamol syr. 120mg/5ml 60ml |
| 273 | Paracetamol tab. 500mg | 274 | Paraffin Liquid |
| 275 | Permethrin cream 5% 15g | 276 | Permethrin lotion 5% 60ml |
| 277 | PHENobarbital 15mg Tab | 278 | Phenobarbitone tab. 30mg |
| 279 | Phenoxymethylpenicillin 125mg Tab | 280 | Phenoxymethylpenicillin 250mg Tabs |
| 281 | Phosphate Buffer (Joulies) solution | 282 | Potassium chloride (KCl) 600mg tab |
| 283 | Potassium permanganate Crystal | 284 | Povidone iodine cream 5% 15g |
| 285 | Povidone iodine solution 10% 500ml | 286 | Prochlorperazine 5mg Tab |
| 287 | Promethazine HCL syr. 5mg/5ml 60ml | 288 | Promethazine HCL tab. 10mg |
| 289 | Promethazine HCL tab. 25mg | 290 | Propantheline 15mg Tabs |
| 291 | Propranolol 10mg Tab | 292 | Propranolol 40mg tab |
| 293 | Pyrantel Pamoate oral suspension 50mg/ml | 294 | Pyrantel oral Suspension |
| 295 | Pyrantel pamoate 125mg | 296 | Pyridoxal phosphate tablet 50mg |
| 297 | Pyridoxine HCL tab. 25mg | 298 | Salbutamol 4mg |
| 299 | Salbutamol D.P Caps 200mcg | 300 | Salbutamol D.P Caps 400mcg |
| 301 | Salbutamol MDI 100mcg/MD 200 doses | 302 | Salbutamol syr. 2mg/5ml 60ml |
| 303 | Salbutamol tab. 2mg | 304 | Salicylic Acid powder |
| 305 | Sertraline tab. 50mg | 306 | Sertraline tablet 25mg |
| 307 | Silver sulphadiazine cream 1% 500g | 308 | Sodium Bicarbonate Ear drops |
| 309 | Sodium Valproate 100mg tab | 310 | Sodium Valproate 200mg tab |
| 311 | Sodium bicarbonate powder | 312 | Sodium bicarbonate tab. 600mg |
| 313 | Sodium chloride for Oral use 3% | 314 | Sodium valproate syr. 200mg/5ml 100ml |
| 315 | Soframycin Cream | 316 | Soframycin Skin Cream 20g |
| 317 | Soframycin Skin Cream 5g | 318 | Soluble Insulin (HumuLIN S) 100IU/ml |
| 319 | Somatropin Liquid for inj. 6mg/1.03mL | 320 | Spacer device |
| 321 | Spironolactone 25mg tab | 322 | Sulfur 10% Ointment |
| 323 | Sulfur 2.5% Ointment | 324 | Sulfur 5% Ointment |
| 325 | Sulphur ointment | 326 | Sulphur precipitated powder |
| 327 | Surgical Spirit | 328 | Tacrolimus Capsule 0.5mg |
| 329 | Tamoxifen tablet 20mg | 330 | Terbinafine Cream 1% 15g |
| 331 | Terbinafine Tablet 250mg | 332 | Terbutaline 1.5mg/5ml Syrup |
| 333 | Terbutaline 2.5mg Tab | 334 | Terbutaline 5mg Tab |
| 335 | Tetracycline 250mg Caps | 336 | Tetracycline Eye Ointment 1% 3.5g |
| 337 | Theophylline SR tabs 125mg | 338 | Theophylline syr. 25mg/5ml 60ml |
| 339 | Thymol 3% in Spirit | 340 | Thymol 4% in spirit |
| 341 | Thyroxine 100mcg Tabs | 342 | Thyroxine 50mcg Tabs |
| 343 | Tobramycin 0.3%+Dexamethasone 0.1% eye drops 10ml | 344 | Tobramycin ear drops 0.3% 5ml |
| 345 | Topiramate Tab. 25mg | 346 | Topiramate Tab. 50mg |
| 347 | Tranexamic acid 500mg cap | 348 | Tretinoin cream 0.025% 15g |
| 349 | Trihexyphenidyl HCl (ARTANE) 2mg Tab | 350 | Urea 10% in aqueous cream |
| 351 | Urea 2% | 352 | Urea 5% in aqueous cream |
| 353 | Ursodeoxycholic acid tablets 150mg | 354 | Valaciclovir Tab. 500mg |
| 355 | Vaseline Ointment | 356 | Vigabatrin Tab. 500mg |
| 357 | Vitamin A & D (4000IU/400IU) Caps | 358 | Vitamin B Complex tab. |
| 359 | Vitamin B1 10mg | 360 | Vitamin C 50mg |
| 361 | Vitamin C tab. 100mg | 362 | Vitamin K (Phytomenadione) Tablet 5mg |
| 363 | Whitfield Lotion | 364 | Whitfield Ointment |
| 365 | Whitfield Ointment (Benzoic acid + Salicylic acid) | 366 | Xylometazoline Nasal Drops 0.1% 10ml |
| 367 | Xylometazoline Nasal Drops 0.05% 10ml | 368 | Zinc Oxide Powder |
| 369 | Zinc sulfate effervescent Tab. 20mg | 370 | Zinc sulphate dispersible tab. 20mg |
| 371 | amLODIPine Besilate 5mg | 372 | azaTHIOprine tablet 50mg |
| 373 | carBAMazepine modified release Tablet 200mg | 374 | carBAMazepine tab. 100mg |
| 375 | carBAMazepine tab. 200mg | 376 | cefTAZidime Inj. 500mg |
| 377 | chlorproMAZINE HCl tab. 50mg | 378 | cloBAZam 10mg Tab |
| 379 | cloBAZam 5mg Tab | 380 | clonazePAM tab. 0.5mg |
| 381 | clonazePAM tab. 2mg | 382 | cycloSPORINE capsule 25mg |
| 383 | dexAMETHasone Tablet 4mg | 384 | dexAMETHasone Tablet 8mg |
| 385 | diazePAM tab. 5mg | 386 | gentamicin 0.3% with Hydrocortisone 1% Ear drops 10ml |
| 387 | hydroCHLOROthiazide (HCT) 25mg Tab | 388 | lamoTRIgine tablet 25mg |
| 389 | lamoTRIgine tablet 50mg | 390 | levETIRAcetam Tablet 250mg |
| 391 | levETIRAcetam Tablet 500mg | 392 | methylPREDNISolone 4mg Tab |
| 393 | metroNIDAZOLE 125mg/5ml Syrup | 394 | metroNIDAZOLE 200mg Tabs |
| 395 | metroNIDAZOLE 400mg Tabs | 396 | metroNIDAZOLE Syr 200mg/5ml 100ml |
| 397 | metroNIDAZOLE gel 0.75-1% 30g | 398 | oxyBUTYnine Hydrochloride Tablet 2.5mg |
| 399 | prednisoLONE 10mg | 400 | prednisoLONE 20mg Tab |
| 401 | prednisoLONE 5mg Tab | 402 | prednisoLONE Acetate Eye Drop 1% 5ml |
| 403 | prednisoLONE Syr. 5mg/5ml 60ml | 404 | pyRIDostigmine Bromide Tab. 60mg |
| 405 | rifAMPicin 150mg | 406 | risperiDONE tab. 1mg |
| 407 | tiZANidine 2mg Tab | | |

---

## 6. AWaRe Classification — Implications for Stewardship

### What is AWaRe?

The WHO AWaRe classification (2023) groups antibiotics into three categories to guide stewardship:

**🟢 ACCESS** — First and second choice antibiotics for common infections. Lower resistance potential. The WHO target is **≥60% of all antibiotic consumption from the Access group**.

**🟡 WATCH** — Higher resistance potential or last-resort options for some infections. Should be key targets for stewardship monitoring. Use only when first-line options fail or are contraindicated.

**🔴 RESERVE** — Last-resort antibiotics only. Must be used only when all other options are insufficient. *No Reserve antibiotics were identified in the current OPD formulary.*

### Key Observations for Lady Ridgeway Hospital OPD

- The formulary contains **predominantly Access-category antibiotics**, which is consistent with appropriate stewardship.
- **Watch-category agents requiring active monitoring:** Co-amoxiclav, Azithromycin, Clarithromycin, Cefuroxime, Cefixime, Ciprofloxacin, Fusidic acid, Rifampicin, Tobramycin, Nalidixic acid, Clindamycin.
- **No Reserve-category antibiotics** are present in the OPD formulary — a positive finding.
- Several agents (Mupirocin, Framycetin/Soframycin, Furazolidone, Clofazimine) are **not listed in WHO AWaRe 2023** as they are topical-only or used for specific indications outside the standard classification scope.

### Use in Research

This classification table is used to enrich the HHIMS clustering dataset, enabling per-cluster AWaRe profiling as part of the **Phase 2 quantitative analysis** of the MD Health Informatics research project at PGIM, University of Colombo.

---

*MD Health Informatics Research — PGIM, University of Colombo — 2026*
