# =============================================================================
# AWaRe ENRICHMENT SCRIPT  v4.0
# Adds antibiotic classification features to the OPD encounters dataframe
# Source: WHO AWaRe 2023 (WHO-MHP-HPS-EML-2023.04-eng.xlsx)
#
# Columns added:
#   aware_categories     - AWaRe category per antibiotic (pipe-separated)
#   aware_profile        - Access-only / Watch-only / Mixed / No antibiotic
#   has_watch_antibiotic - 1 if any antibiotic is Watch, else 0
#   has_broad_spectrum   - 1 if any antibiotic is Broad spectrum, else 0
#   antibiotic_groups    - Drug class per antibiotic (pipe-separated)
#   class_profile        - Most common antibiotic class in encounter
#   antibiotic_routes    - Route per antibiotic (pipe-separated)
#   spectrum_profile     - Broadest spectrum level across all antibiotics
#   antibiotic_compounds - Active compound name per antibiotic (NEW v4.0)
#   route_profile        - Single dominant route for the encounter (NEW v4.0)
# =============================================================================

import pandas as pd
from collections import Counter


# =============================================================================
# LOOKUP TABLE
# Key   = exact drug name as stored in HHIMS drug_names column
# Value = dict: aware, group, route, spectrum, compound
# =============================================================================

ANTIBIOTIC_LOOKUP = {

    # -- Penicillins ----------------------------------------------------------
    "Amoxicillin 125 mg Tabs":                  {"aware": "Access", "group": "Aminopenicillin",                    "route": "Oral",       "spectrum": "Narrow-Moderate", "compound": "Amoxicillin"},
    "Amoxicillin 125mg/5ml Syrup":              {"aware": "Access", "group": "Aminopenicillin",                    "route": "Oral",       "spectrum": "Narrow-Moderate", "compound": "Amoxicillin"},
    "Amoxicillin 250 mg Caps":                  {"aware": "Access", "group": "Aminopenicillin",                    "route": "Oral",       "spectrum": "Narrow-Moderate", "compound": "Amoxicillin"},
    "Amoxicillin 500 mg":                       {"aware": "Access", "group": "Aminopenicillin",                    "route": "Oral",       "spectrum": "Narrow-Moderate", "compound": "Amoxicillin"},
    "Cloxacillin sy 62.5mg in 2.5ml":           {"aware": "Access", "group": "Penicillinase-resistant Penicillin", "route": "Oral",       "spectrum": "Narrow",          "compound": "Cloxacillin"},
    "Flucloxacillin 500mg":                     {"aware": "Access", "group": "Penicillinase-resistant Penicillin", "route": "Oral",       "spectrum": "Narrow",          "compound": "Flucloxacillin"},
    "Flucloxacillin Syr. 125mg/5ml":            {"aware": "Access", "group": "Penicillinase-resistant Penicillin", "route": "Oral",       "spectrum": "Narrow",          "compound": "Flucloxacillin"},
    "Flucloxacillin capsule 250mg":             {"aware": "Access", "group": "Penicillinase-resistant Penicillin", "route": "Oral",       "spectrum": "Narrow",          "compound": "Flucloxacillin"},
    "Flucloxacillin injection 500mg":           {"aware": "Access", "group": "Penicillinase-resistant Penicillin", "route": "Parenteral", "spectrum": "Narrow",          "compound": "Flucloxacillin"},
    "Phenoxymethylpenicillin 125mg Tab":        {"aware": "Access", "group": "Natural Penicillin",                 "route": "Oral",       "spectrum": "Narrow",          "compound": "Phenoxymethylpenicillin"},
    "Phenoxymethylpenicillin 250mg Tabs":       {"aware": "Access", "group": "Natural Penicillin",                 "route": "Oral",       "spectrum": "Narrow",          "compound": "Phenoxymethylpenicillin"},

    # -- Beta-lactam + BLI ---------------------------------------------------
    "Co-Amoxiclav (Augmentin) 125/31mg/5ml Sy.": {"aware": "Access", "group": "Aminopenicillin + BLI", "route": "Oral",       "spectrum": "Broad", "compound": "Amoxicillin + Clavulanate"},
    "Co-Amoxiclav (Augmentin) 625mg tab":         {"aware": "Access", "group": "Aminopenicillin + BLI", "route": "Oral",       "spectrum": "Broad", "compound": "Amoxicillin + Clavulanate"},
    "Co-amoxiclav (Augmentin) Tab. 375mg":        {"aware": "Access", "group": "Aminopenicillin + BLI", "route": "Oral",       "spectrum": "Broad", "compound": "Amoxicillin + Clavulanate"},
    "Co-amoxiclav Inj. 1000/200mg":               {"aware": "Access", "group": "Aminopenicillin + BLI", "route": "Parenteral", "spectrum": "Broad", "compound": "Amoxicillin + Clavulanate"},
    "Co-amoxiclav Inj. 500/100mg":                {"aware": "Access", "group": "Aminopenicillin + BLI", "route": "Parenteral", "spectrum": "Broad", "compound": "Amoxicillin + Clavulanate"},

    # -- Cephalosporins -------------------------------------------------------
    "Cephalexin 125mg Dispersible Tab":  {"aware": "Access", "group": "1st Gen. Cephalosporin", "route": "Oral",       "spectrum": "Narrow-Moderate", "compound": "Cephalexin"},
    "Cephalexin 250 mg Caps":            {"aware": "Access", "group": "1st Gen. Cephalosporin", "route": "Oral",       "spectrum": "Narrow-Moderate", "compound": "Cephalexin"},
    "Cephalexin Capsule 500mg":          {"aware": "Access", "group": "1st Gen. Cephalosporin", "route": "Oral",       "spectrum": "Narrow-Moderate", "compound": "Cephalexin"},
    "Cephalexin Sy. 125mg/5ml 100ml":   {"aware": "Access", "group": "1st Gen. Cephalosporin", "route": "Oral",       "spectrum": "Narrow-Moderate", "compound": "Cephalexin"},
    "Cefuroxime 250mg Tab":              {"aware": "Watch",  "group": "2nd Gen. Cephalosporin", "route": "Oral",       "spectrum": "Broad",           "compound": "Cefuroxime"},
    "Cefuroxime 500mg Tab":              {"aware": "Watch",  "group": "2nd Gen. Cephalosporin", "route": "Oral",       "spectrum": "Broad",           "compound": "Cefuroxime"},
    "Cefuroxime Axetil 125mg Tab":       {"aware": "Watch",  "group": "2nd Gen. Cephalosporin", "route": "Oral",       "spectrum": "Broad",           "compound": "Cefuroxime"},
    "Cefuroxime Syrup 125mg/5ml 100ml":  {"aware": "Watch",  "group": "2nd Gen. Cephalosporin", "route": "Oral",       "spectrum": "Broad",           "compound": "Cefuroxime"},
    "Cefixime Tablet 200mg":             {"aware": "Watch",  "group": "3rd Gen. Cephalosporin", "route": "Oral",       "spectrum": "Broad",           "compound": "Cefixime"},
    "cefTAZidime Inj. 500mg":            {"aware": "Watch",  "group": "3rd Gen. Cephalosporin", "route": "Parenteral", "spectrum": "Broad",           "compound": "Ceftazidime"},

    # -- Macrolides -----------------------------------------------------------
    "Azithromycin 250mg Tab":                 {"aware": "Watch", "group": "Macrolide", "route": "Oral", "spectrum": "Broad",    "compound": "Azithromycin"},
    "Azithromycin dihydrate syrup 200mg/5ml": {"aware": "Watch", "group": "Macrolide", "route": "Oral", "spectrum": "Broad",    "compound": "Azithromycin"},
    "Clarithromycin 250mg":                   {"aware": "Watch", "group": "Macrolide", "route": "Oral", "spectrum": "Broad",    "compound": "Clarithromycin"},
    "Clarithromycin 500mg Tab":               {"aware": "Watch", "group": "Macrolide", "route": "Oral", "spectrum": "Broad",    "compound": "Clarithromycin"},
    "Clarithromycin syrup 125mg/5ml 60ml":    {"aware": "Watch", "group": "Macrolide", "route": "Oral", "spectrum": "Broad",    "compound": "Clarithromycin"},
    "Erythromycin 250mg Tab":                 {"aware": "Watch", "group": "Macrolide", "route": "Oral", "spectrum": "Moderate", "compound": "Erythromycin"},
    "Erythromycin Syrup 125mg/5ml":           {"aware": "Watch", "group": "Macrolide", "route": "Oral", "spectrum": "Moderate", "compound": "Erythromycin"},

    # -- Fluoroquinolones -----------------------------------------------------
    "Ciprofloxacin 250mg Tab":                           {"aware": "Watch", "group": "Fluoroquinolone", "route": "Oral",    "spectrum": "Broad",  "compound": "Ciprofloxacin"},
    "Ciprofloxacin 500mg":                               {"aware": "Watch", "group": "Fluoroquinolone", "route": "Oral",    "spectrum": "Broad",  "compound": "Ciprofloxacin"},
    "Ciprofloxacin Ear drop 0.3% 5ml":                   {"aware": "Watch", "group": "Fluoroquinolone", "route": "Topical", "spectrum": "Broad",  "compound": "Ciprofloxacin"},
    "Ciprofloxacin Eye drops 0.3% 5ml":                  {"aware": "Watch", "group": "Fluoroquinolone", "route": "Topical", "spectrum": "Broad",  "compound": "Ciprofloxacin"},
    "Norfloxacin 400mg":                                 {"aware": "Watch", "group": "Fluoroquinolone", "route": "Oral",    "spectrum": "Narrow", "compound": "Norfloxacin"},
    "Ofloxacin Ear drops 0.6% 5mL":                      {"aware": "Watch", "group": "Fluoroquinolone", "route": "Topical", "spectrum": "Broad",  "compound": "Ofloxacin"},
    "Moxifloxacin hydrochloride Ophthalmic solution 0.5%":{"aware": "Watch", "group": "Fluoroquinolone", "route": "Topical", "spectrum": "Broad",  "compound": "Moxifloxacin"},

    # -- Tetracyclines --------------------------------------------------------
    "Doxycycline 100mg Caps":       {"aware": "Access", "group": "Tetracycline", "route": "Oral",    "spectrum": "Broad", "compound": "Doxycycline"},
    "Tetracycline 250mg Caps":      {"aware": "Access", "group": "Tetracycline", "route": "Oral",    "spectrum": "Broad", "compound": "Tetracycline"},
    "Tetracycline Eye Ointment 1%": {"aware": "Access", "group": "Tetracycline", "route": "Topical", "spectrum": "Broad", "compound": "Tetracycline"},

    # -- Aminoglycosides ------------------------------------------------------
    "Gentamicin sulphate Ear drops 0.3% 5ml":               {"aware": "Access",         "group": "Aminoglycoside", "route": "Topical", "spectrum": "Narrow", "compound": "Gentamicin"},
    "Gentamycin Eye drops 0.3% 5ml":                        {"aware": "Access",         "group": "Aminoglycoside", "route": "Topical", "spectrum": "Narrow", "compound": "Gentamicin"},
    "Gentamycin ear drops 0.3% 10ml":                       {"aware": "Access",         "group": "Aminoglycoside", "route": "Topical", "spectrum": "Narrow", "compound": "Gentamicin"},
    "gentamicin 0.3% with Hydrocortisone 1% Ear drops 10ml":{"aware": "Access",         "group": "Aminoglycoside", "route": "Topical", "spectrum": "Narrow", "compound": "Gentamicin + Hydrocortisone"},
    "Tobramycin 0.3%+Dexamethasone 0.1% eye drops 10ml":    {"aware": "Watch",          "group": "Aminoglycoside", "route": "Topical", "spectrum": "Narrow", "compound": "Tobramycin + Dexamethasone"},
    "Tobramycin ear drops 0.3% 5ml":                        {"aware": "Watch",          "group": "Aminoglycoside", "route": "Topical", "spectrum": "Narrow", "compound": "Tobramycin"},
    "Betamethasone with Neomycin Ear/Nasal/Eye drop":        {"aware": "Not classified", "group": "Aminoglycoside", "route": "Topical", "spectrum": "Narrow", "compound": "Neomycin + Betamethasone"},

    # -- Nitroimidazoles ------------------------------------------------------
    "metroNIDAZOLE 125mg/5ml Syrup":  {"aware": "Access", "group": "Nitroimidazole", "route": "Oral",    "spectrum": "Narrow", "compound": "Metronidazole"},
    "metroNIDAZOLE 200mg Tabs":       {"aware": "Access", "group": "Nitroimidazole", "route": "Oral",    "spectrum": "Narrow", "compound": "Metronidazole"},
    "metroNIDAZOLE 400mg Tabs":       {"aware": "Access", "group": "Nitroimidazole", "route": "Oral",    "spectrum": "Narrow", "compound": "Metronidazole"},
    "metroNIDAZOLE Syr 200mg/5ml 100ml": {"aware": "Access", "group": "Nitroimidazole", "route": "Oral", "spectrum": "Narrow", "compound": "Metronidazole"},
    "metroNIDAZOLE gel 0.75-1% 30g":  {"aware": "Access", "group": "Nitroimidazole", "route": "Topical", "spectrum": "Narrow", "compound": "Metronidazole"},

    # -- Sulfonamides + Trimethoprim ------------------------------------------
    "Co-trimoxazole 480mg Tabs":          {"aware": "Access", "group": "Sulfonamide + Trimethoprim", "route": "Oral",    "spectrum": "Broad", "compound": "Sulfamethoxazole + Trimethoprim"},
    "Co-trimoxazole Cream 1% 15g":        {"aware": "Access", "group": "Sulfonamide + Trimethoprim", "route": "Topical", "spectrum": "Broad", "compound": "Sulfamethoxazole + Trimethoprim"},
    "Co-trimoxazole Syr. 240mg/5ml 50ml": {"aware": "Access", "group": "Sulfonamide + Trimethoprim", "route": "Oral",    "spectrum": "Broad", "compound": "Sulfamethoxazole + Trimethoprim"},

    # -- Lincosamides ---------------------------------------------------------
    "Clindamycin gel 1% 30g": {"aware": "Access", "group": "Lincosamide", "route": "Topical", "spectrum": "Narrow", "compound": "Clindamycin"},

    # -- Chloramphenicol ------------------------------------------------------
    "Chloramphenicol Ear Drops 5%":       {"aware": "Access", "group": "Chloramphenicol", "route": "Topical", "spectrum": "Broad", "compound": "Chloramphenicol"},
    "Chloramphenicol Eye Drops 0.5% 5ml": {"aware": "Access", "group": "Chloramphenicol", "route": "Topical", "spectrum": "Broad", "compound": "Chloramphenicol"},

    # -- Fusidic Acid ---------------------------------------------------------
    "Fusidic Acid 250mg tablet":                {"aware": "Watch", "group": "Fusidic Acid", "route": "Oral",    "spectrum": "Narrow", "compound": "Fusidic Acid"},
    "Fusidic acid 2%+Betamethasone 0.1% Cream": {"aware": "Watch", "group": "Fusidic Acid", "route": "Topical", "spectrum": "Narrow", "compound": "Fusidic Acid + Betamethasone"},
    "Fusidic acid Eye Drop 1%":                 {"aware": "Watch", "group": "Fusidic Acid", "route": "Topical", "spectrum": "Narrow", "compound": "Fusidic Acid"},
    "Fusidic acid cream 2% 5g":                 {"aware": "Watch", "group": "Fusidic Acid", "route": "Topical", "spectrum": "Narrow", "compound": "Fusidic Acid"},

    # -- Nitrofurans ----------------------------------------------------------
    "Nitrofurantoin 25mg Tab":  {"aware": "Access",         "group": "Nitrofuran", "route": "Oral", "spectrum": "Narrow", "compound": "Nitrofurantoin"},
    "Nitrofurantoin 50mg Tab":  {"aware": "Access",         "group": "Nitrofuran", "route": "Oral", "spectrum": "Narrow", "compound": "Nitrofurantoin"},
    "Furazolidone 100mg Tab":   {"aware": "Not classified", "group": "Nitrofuran", "route": "Oral", "spectrum": "Narrow", "compound": "Furazolidone"},
    "Furazolidone 25mg":        {"aware": "Not classified", "group": "Nitrofuran", "route": "Oral", "spectrum": "Narrow", "compound": "Furazolidone"},
    "Furazolidone 50mg":        {"aware": "Not classified", "group": "Nitrofuran", "route": "Oral", "spectrum": "Narrow", "compound": "Furazolidone"},

    # -- Quinolones (1st Generation) ------------------------------------------
    "Nalidixic Acid 500mg Tab":             {"aware": "Not classified", "group": "Quinolone (1st Gen.)", "route": "Oral", "spectrum": "Narrow", "compound": "Nalidixic Acid"},
    "Nalidixic Acid Oral suspension 300mg": {"aware": "Not classified", "group": "Quinolone (1st Gen.)", "route": "Oral", "spectrum": "Narrow", "compound": "Nalidixic Acid"},
    "Nalidixic acid 250mg Tab":             {"aware": "Not classified", "group": "Quinolone (1st Gen.)", "route": "Oral", "spectrum": "Narrow", "compound": "Nalidixic Acid"},

    # -- Mupirocin ------------------------------------------------------------
    "Mupirocin Cream 2% 5g":    {"aware": "Not classified", "group": "Topical Antibacterial", "route": "Topical", "spectrum": "Narrow", "compound": "Mupirocin"},
    "Mupirocin Ointment 2% 5g": {"aware": "Not classified", "group": "Topical Antibacterial", "route": "Topical", "spectrum": "Narrow", "compound": "Mupirocin"},

    # -- Rifamycins -----------------------------------------------------------
    "rifAMPicin 150mg": {"aware": "Watch", "group": "Rifamycin", "route": "Oral", "spectrum": "Broad", "compound": "Rifampicin"},

    # -- Framycetin / Soframycin ----------------------------------------------
    "Framycetin Cream 1% 20g":   {"aware": "Not classified", "group": "Aminoglycoside (Framycetin)", "route": "Topical", "spectrum": "Narrow", "compound": "Framycetin"},
    "Soframycin Cream":          {"aware": "Not classified", "group": "Aminoglycoside (Framycetin)", "route": "Topical", "spectrum": "Narrow", "compound": "Framycetin"},
    "Soframycin Skin Cream 20g": {"aware": "Not classified", "group": "Aminoglycoside (Framycetin)", "route": "Topical", "spectrum": "Narrow", "compound": "Framycetin"},
    "Soframycin Skin Cream 5g":  {"aware": "Not classified", "group": "Aminoglycoside (Framycetin)", "route": "Topical", "spectrum": "Narrow", "compound": "Framycetin"},

    # -- Anti-leprosy ---------------------------------------------------------
    "Clofazimine 100mg": {"aware": "Not classified", "group": "Riminophenazine", "route": "Oral", "spectrum": "Narrow", "compound": "Clofazimine"},

    # =========================================================================
    # ANTIFUNGALS / ANTIVIRALS
    # HHIMS stores these under drug_groups="Antibiotics" but they are not
    # bacterial antibiotics. Added here so they are recognised and labelled
    # "Not classified" rather than silently missed.
    # =========================================================================
    "Aciclovir Tab. 200mg":                     {"aware": "Not classified", "group": "Antiviral",  "route": "Oral",    "spectrum": "N/A", "compound": "Aciclovir"},
    "Clotrimazole cream 1%,15g tube":           {"aware": "Not classified", "group": "Antifungal", "route": "Topical", "spectrum": "N/A", "compound": "Clotrimazole"},
    "Clotrimazole mouth paint1%,15ml":          {"aware": "Not classified", "group": "Antifungal", "route": "Topical", "spectrum": "N/A", "compound": "Clotrimazole"},
    "Fluconazole 50mg":                         {"aware": "Not classified", "group": "Antifungal", "route": "Oral",    "spectrum": "N/A", "compound": "Fluconazole"},
    "Itraconazole Cap. 100mg":                  {"aware": "Not classified", "group": "Antifungal", "route": "Oral",    "spectrum": "N/A", "compound": "Itraconazole"},
    "MIcanazole 2% 5g":                         {"aware": "Not classified", "group": "Antifungal", "route": "Topical", "spectrum": "N/A", "compound": "Miconazole"},
    "Miconazole Cream 2%, 15g":                 {"aware": "Not classified", "group": "Antifungal", "route": "Topical", "spectrum": "N/A", "compound": "Miconazole"},
    "Miconazole Cream 2%, 30g Tube (contains 20mg of Miconazole ni": {"aware": "Not classified", "group": "Antifungal", "route": "Topical", "spectrum": "N/A", "compound": "Miconazole"},
    "Griseofulvin Tab. 500mg":                  {"aware": "Not classified", "group": "Antifungal", "route": "Oral",    "spectrum": "N/A", "compound": "Griseofulvin"},

    # =========================================================================
    # HHIMS NAME ALIASES
    # Same drugs as above but stored with different spellings in HHIMS
    # (extra spaces, commas, bracket formats, size descriptions)
    # =========================================================================

    # Penicillins
    "Cloxacillin sy 62.5 mg in  2.5 ml":  {"aware": "Access", "group": "Penicillinase-resistant Penicillin", "route": "Oral", "spectrum": "Narrow", "compound": "Cloxacillin"},
    "Flucloxacillin Syr.125mg/5ml 100ml": {"aware": "Access", "group": "Penicillinase-resistant Penicillin", "route": "Oral", "spectrum": "Narrow", "compound": "Flucloxacillin"},
    "Phenoxymethylpenicillin 125 mg Tab":  {"aware": "Access", "group": "Natural Penicillin", "route": "Oral", "spectrum": "Narrow", "compound": "Phenoxymethylpenicillin"},
    "Phenoxymethylpenicillin 250 mg Tabs": {"aware": "Access", "group": "Natural Penicillin", "route": "Oral", "spectrum": "Narrow", "compound": "Phenoxymethylpenicillin"},

    # Co-trimoxazole
    "Co-trimoxazole (CoTrimoxazole) 480 mg Tabs":          {"aware": "Access", "group": "Sulfonamide + Trimethoprim", "route": "Oral",    "spectrum": "Broad", "compound": "Sulfamethoxazole + Trimethoprim"},
    "Co-trimoxazole (CoTrimoxazole) Cream 1% 15 g":        {"aware": "Access", "group": "Sulfonamide + Trimethoprim", "route": "Topical", "spectrum": "Broad", "compound": "Sulfamethoxazole + Trimethoprim"},
    "Co-trimoxazole (CoTrimoxazole) Syr. 240mg/5ml, 50ml": {"aware": "Access", "group": "Sulfonamide + Trimethoprim", "route": "Oral",    "spectrum": "Broad", "compound": "Sulfamethoxazole + Trimethoprim"},

    # Macrolides
    "Azithromycin dihydrate syrup 200mg/5ml 15ml": {"aware": "Watch", "group": "Macrolide", "route": "Oral", "spectrum": "Broad", "compound": "Azithromycin"},
    "Clarithromycin syrup125mg/5ml,60ml":          {"aware": "Watch", "group": "Macrolide", "route": "Oral", "spectrum": "Broad", "compound": "Clarithromycin"},

    # Fluoroquinolones
    "Ciprofloxacin Ear drop, 0.3% w/v, 5ml":             {"aware": "Watch", "group": "Fluoroquinolone", "route": "Topical", "spectrum": "Broad",  "compound": "Ciprofloxacin"},
    "Ciprofloxacin Eye drops0.3%, 5ml vial":              {"aware": "Watch", "group": "Fluoroquinolone", "route": "Topical", "spectrum": "Broad",  "compound": "Ciprofloxacin"},
    "Ofloxacin ear drops 0.6%, 5ml":                      {"aware": "Watch", "group": "Fluoroquinolone", "route": "Topical", "spectrum": "Broad",  "compound": "Ofloxacin"},
    "Ofloxacin Ear drops 0.6% in 5mL Dropper bottle":    {"aware": "Watch", "group": "Fluoroquinolone", "route": "Topical", "spectrum": "Broad",  "compound": "Ofloxacin"},
    "Norfloxacin 400 mg":                                 {"aware": "Watch", "group": "Fluoroquinolone", "route": "Oral",    "spectrum": "Narrow", "compound": "Norfloxacin"},

    # Aminoglycosides
    "Gentamicin sulphate Ear drops 0.3% in 5ml vial.": {"aware": "Access", "group": "Aminoglycoside", "route": "Topical", "spectrum": "Narrow", "compound": "Gentamicin"},

    # Tetracyclines
    "Tetracycline 250 mg Caps": {"aware": "Access", "group": "Tetracycline", "route": "Oral", "spectrum": "Broad", "compound": "Tetracycline"},

    # Nitroimidazoles
    "metroNIDAZOLE 200 mg Tabs":          {"aware": "Access", "group": "Nitroimidazole", "route": "Oral", "spectrum": "Narrow", "compound": "Metronidazole"},
    "metroNIDAZOLE 400 mg Tabs":          {"aware": "Access", "group": "Nitroimidazole", "route": "Oral", "spectrum": "Narrow", "compound": "Metronidazole"},
    "metroNIDAZOLE Syr 200mg/5ml ,100ml": {"aware": "Access", "group": "Nitroimidazole", "route": "Oral", "spectrum": "Narrow", "compound": "Metronidazole"},

    # Nalidixic Acid
    "Nalidixic Acid Oral suspension 300mg/5mL in 100mL Bottle": {"aware": "Not classified", "group": "Quinolone (1st Gen.)", "route": "Oral", "spectrum": "Narrow", "compound": "Nalidixic Acid"},

    # Fusidic Acid
    "Fusidic acid 2%+Betamethasone 0.1% Cream 10g-15g tube": {"aware": "Watch", "group": "Fusidic Acid", "route": "Topical", "spectrum": "Narrow", "compound": "Fusidic Acid + Betamethasone"},
    "Fusidic acid Eye Drop 1%(S.R.)":  {"aware": "Watch", "group": "Fusidic Acid", "route": "Topical", "spectrum": "Narrow", "compound": "Fusidic Acid"},
    "Fusidic acid cream 2% , 5g":      {"aware": "Watch", "group": "Fusidic Acid", "route": "Topical", "spectrum": "Narrow", "compound": "Fusidic Acid"},
    "Fusidic acid cream 2%, 5g":       {"aware": "Watch", "group": "Fusidic Acid", "route": "Topical", "spectrum": "Narrow", "compound": "Fusidic Acid"},
    "Fusidic acid cream 2%, 5g tube":  {"aware": "Watch", "group": "Fusidic Acid", "route": "Topical", "spectrum": "Narrow", "compound": "Fusidic Acid"},

    # Framycetin
    "Framycetin Cream 1%, 20g": {"aware": "Not classified", "group": "Aminoglycoside (Framycetin)", "route": "Topical", "spectrum": "Narrow", "compound": "Framycetin"},
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_antibiotic_drugs(drug_names_str):
    """
    Returns only the drugs from a pipe-separated drug_names string
    that exist in ANTIBIOTIC_LOOKUP. All other drugs are ignored.
    """
    if pd.isna(drug_names_str) or drug_names_str == "":
        return []
    return [d.strip() for d in drug_names_str.split("|")
            if d.strip() in ANTIBIOTIC_LOOKUP]


def lookup_field(antibiotic_drugs, field):
    """Returns a list of values for a given field across matched antibiotic drugs."""
    return [ANTIBIOTIC_LOOKUP[d][field] for d in antibiotic_drugs]


SPECTRUM_RANK = {"Narrow": 1, "Narrow-Moderate": 2, "Moderate": 3, "Broad": 4, "N/A": 0}

ROUTE_RANK = {"Parenteral": 3, "Oral": 2, "Topical": 1, "N/A": 0}


def get_spectrum_profile(antibiotic_drugs):
    if not antibiotic_drugs:
        return "No antibiotic"
    spectrums = [s for s in lookup_field(antibiotic_drugs, "spectrum") if s != "N/A"]
    if not spectrums:
        return "Not applicable"
    return max(spectrums, key=lambda s: SPECTRUM_RANK.get(s, 0))


def get_aware_profile(antibiotic_drugs):
    if not antibiotic_drugs:
        return "No antibiotic"
    aware_values = set(lookup_field(antibiotic_drugs, "aware"))
    if aware_values == {"Access"}:        return "Access-only"
    elif aware_values == {"Watch"}:       return "Watch-only"
    elif aware_values == {"Not classified"}: return "Not classified"
    else:                                 return "Mixed"


def get_class_profile(antibiotic_drugs):
    if not antibiotic_drugs:
        return "No antibiotic"
    counts  = Counter(lookup_field(antibiotic_drugs, "group"))
    max_cnt = max(counts.values())
    top     = sorted([g for g, c in counts.items() if c == max_cnt])
    return "/".join(top)


def get_route_profile(antibiotic_drugs):
    """
    Returns the single most clinically significant route in the encounter.
    Priority order: Parenteral > Oral > Topical
    This gives a clean single value for use in clustering.
    Returns "No antibiotic" if no drugs matched.
    """
    if not antibiotic_drugs:
        return "No antibiotic"
    routes = [r for r in lookup_field(antibiotic_drugs, "route") if r != "N/A"]
    if not routes:
        return "Not applicable"
    return max(routes, key=lambda r: ROUTE_RANK.get(r, 0))


# =============================================================================
# MAIN ENRICHMENT FUNCTION
# =============================================================================

def enrich_dataframe(df):
    """
    Adds 10 AWaRe enrichment columns to the dataframe.

    Usage:
        from aware_enrichment import enrich_dataframe
        df = enrich_dataframe(df)
    """
    print("Starting AWaRe enrichment...")
    print(f"  Total encounters : {len(df)}")

    antibiotic_lists = df["drug_names"].apply(get_antibiotic_drugs)

    df["aware_categories"]      = antibiotic_lists.apply(
        lambda d: "|".join(lookup_field(d, "aware"))     if d else "")

    df["aware_profile"]         = antibiotic_lists.apply(get_aware_profile)

    df["has_watch_antibiotic"]  = antibiotic_lists.apply(
        lambda d: 1 if "Watch" in lookup_field(d, "aware") else 0)

    df["has_broad_spectrum"]    = antibiotic_lists.apply(
        lambda d: 1 if "Broad" in lookup_field(d, "spectrum") else 0)

    df["antibiotic_groups"]     = antibiotic_lists.apply(
        lambda d: "|".join(lookup_field(d, "group"))     if d else "")

    df["class_profile"]         = antibiotic_lists.apply(get_class_profile)

    df["antibiotic_routes"]     = antibiotic_lists.apply(
        lambda d: "|".join(lookup_field(d, "route"))     if d else "")

    df["spectrum_profile"]      = antibiotic_lists.apply(get_spectrum_profile)

    # NEW in v4.0 ─────────────────────────────────────────────────────────────
    df["antibiotic_compounds"]  = antibiotic_lists.apply(
        lambda d: "|".join(lookup_field(d, "compound"))  if d else "")

    df["route_profile"]         = antibiotic_lists.apply(get_route_profile)
    # ─────────────────────────────────────────────────────────────────────────

    print("\n  Enrichment complete. Columns added:")
    for col in ["aware_categories", "aware_profile", "has_watch_antibiotic",
                "has_broad_spectrum", "antibiotic_groups", "class_profile",
                "antibiotic_routes", "spectrum_profile",
                "antibiotic_compounds", "route_profile"]:
        print(f"     - {col}")

    print("\n  aware_profile distribution:")
    print(df["aware_profile"].value_counts().to_string())

    print("\n  route_profile distribution (antibiotic encounters only):")
    print(df[df["has_antibiotic"] == 1]["route_profile"].value_counts().to_string())

    return df


# =============================================================================
# CHECKER FUNCTION
# =============================================================================

def check_unmatched_drugs(df):
    """
    Checks how well ANTIBIOTIC_LOOKUP covers the antibiotics in your data.
    Uses num_antibiotics to detect when an encounter is under-covered.

    Usage:
        from aware_enrichment import check_unmatched_drugs
        check_unmatched_drugs(df)
    """
    print("Checking lookup coverage against your data...\n")

    ab_df = df[df["has_antibiotic"] == 1].copy()
    total = len(ab_df)
    missed_drugs = {}
    n_missed_enc = 0

    for _, row in ab_df.iterrows():
        if pd.isna(row["drug_names"]):
            continue
        all_drugs    = [d.strip() for d in row["drug_names"].split("|")]
        matched      = [d for d in all_drugs if d in ANTIBIOTIC_LOOKUP]
        num_expected = int(row["num_antibiotics"])
        if len(matched) < num_expected:
            n_missed_enc += 1
            for drug in all_drugs:
                if drug not in ANTIBIOTIC_LOOKUP:
                    missed_drugs[drug] = missed_drugs.get(drug, 0) + 1

    pct = 100 * (1 - n_missed_enc / total) if total else 0

    print(f"  Encounters with antibiotics (has_antibiotic=1) : {total}")
    print(f"  Encounters fully covered by our lookup         : {total - n_missed_enc}")
    print(f"  Encounters with at least one missed antibiotic : {n_missed_enc}")
    print(f"  Coverage                                       : {pct:.1f}%")

    if not missed_drugs:
        print("\n  All antibiotic encounters are fully covered!")
        return missed_drugs

    # Filter: separate likely true antibiotics from companion non-antibiotics
    NON_AB_KEYWORDS = [
        "paracetamol", "ibuprofen", "diclofenac", "mefenamic", "aspirin",
        "chlorpheniramine", "cetirizine", "loratadine", "desloratadine",
        "fexofenadine", "promethazine", "hydroxyzine",
        "salbutamol", "theophylline", "beclometasone", "beclomethasone",
        "prednisolone", "prednisolone", "dexamethasone", "dexamethazone",
        "hydrocortisone", "methylprednisolone", "betamethasone",
        "domperidone", "ondansetron", "prochlorperazine", "metoclopramide",
        "omeprazole", "famotidine", "ranitidine",
        "vitamin", "iron", "calcium", "zinc", "folic", "multivitamin",
        "saline", "oral rehydration", "jeewani",
        "aqueous cream", "emulsifying", "paraffin", "calamine",
        "cetrimide", "betadine", "povidone", "benzyl benzoate",
        "permethrin", "crotamitone", "sulphur", "sulfur", "mebendazole",
        "pyrantel", "diethylcarbamazine", "lactulose", "bisacodyl",
        "hyoscine", "propantheline", "lignocaine", "methyl salicylate",
        "crepe bandage", "amitriptyline", "diazepam", "clobazam",
        "levetiracetam", "sodium valproate", "chlorpromazine",
        "flunarizine", "sodium bicarbonate", "balanced salt",
        "adapalene", "benzoyl peroxide", "alfa calcidol", "thymol",
        "fluoride mouth wash", "chlorhexidine",
    ]

    def is_non_ab(name):
        n = name.lower()
        return any(kw in n for kw in NON_AB_KEYWORDS)

    likely_ab  = {d: c for d, c in missed_drugs.items() if not is_non_ab(d)}
    likely_non = {d: c for d, c in missed_drugs.items() if is_non_ab(d)}

    if likely_ab:
        print(f"\n  Likely missed antibiotics (add to ANTIBIOTIC_LOOKUP to fix):")
        print(f"  {'Drug name':<65}  Encounters")
        print(f"  {'-'*65}  ----------")
        for drug, count in sorted(likely_ab.items(), key=lambda x: -x[1]):
            print(f"  {drug:<65}  {count}")
    else:
        print("\n  No obvious missed antibiotics in the unmatched list.")

    if likely_non:
        print(f"\n  Non-antibiotic companion drugs (do NOT add — these appear")
        print(f"  alongside truly missed antibiotics in the same encounter):")
        print(f"  {len(likely_non)} drugs filtered  "
              f"(total appearances: {sum(likely_non.values())})")
        examples = list(likely_non.keys())[:4]
        print(f"  Examples: {', '.join(examples)} ...")

    return missed_drugs
