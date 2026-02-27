# =============================================================================
# COMPLAINT CLEANING SCRIPT  v1.0
# Adds three new columns to your OPD encounters dataframe:
#
#   complaint_clean        - Human-readable expanded complaint text
#   complaint_category     - Clinical category for EDA and clustering
#   complaint_duration_days - Duration in days extracted from complaint text
#
# HOW TO USE IN YOUR NOTEBOOK:
#   import sys
#   sys.path.insert(0, r'C:\path\to\this\folder')
#   from complaint_cleaning import add_complaint_features
#   df = add_complaint_features(df)
# =============================================================================

import pandas as pd
import re


# =============================================================================
# SECTION 1 — ABBREVIATION EXPANSION MAP
# =============================================================================

ABBREV_MAP = {
    # Single letters
    'c':   'cough',
    'f':   'fever',
    'w':   'unspecified',      # wheeze OR wound — cannot decode
    'r':   'rash',
    's':   'skin',
    'v':   'vomiting',
    'n':   'nausea',
    'd':   'diarrhoea',
    'p':   'pain',
    'e':   'unspecified',      # unknown
    'a':   'unspecified',

    # Two letters
    'cc':  'cough cold',
    'fc':  'fever cough',
    'cf':  'cough fever',
    'vf':  'vomiting fever',
    'ba':  'bronchial asthma',
    'ln':  'lymph node enlargement',
    'st':  'sore throat',
    'sk':  'skin',
    'cd':  'cough diarrhoea',
    'co':  'cough cold',
    'cx':  'cough',
    'f1':  'fever', 'f2': 'fever', 'f3': 'fever', 'f4': 'fever', 'f5': 'fever',
    'fe':  'fever',
    'c1':  'cough', 'c2': 'cough', 'c3': 'cough', 'c4': 'cough', 'c5': 'cough',

    # Duration-embedded fever/cough patterns  (f1d, fe3d, c2d etc.)
    'f1d': 'fever',  'f2d': 'fever',  'f3d': 'fever',  'f4d': 'fever',
    'f5d': 'fever',  'f6d': 'fever',  'f7d': 'fever',
    'fe1d':'fever',  'fe2d':'fever',  'fe3d':'fever',  'fe4d':'fever',
    'fe1': 'fever',  'fe2': 'fever',  'fe3': 'fever',
    'fever1d':'fever', 'fever2d':'fever', 'fever3d':'fever',
    'fever1':'fever',  'fever2':'fever',  'fever3':'fever',
    'c1d': 'cough',  'c2d': 'cough',  'c3d': 'cough',  'c4d': 'cough',
    'c5d': 'cough',  'c6d': 'cough',  'c7d': 'cough',

    # Three letters
    'ccf': 'cough cold fever',
    'fcc': 'fever cough cold',
    'fcv': 'fever cough vomiting',
    'f1c': 'fever cough',
    'fc1': 'fever cough',
    'cf1': 'cough fever',
    'sob': 'shortness of breath',
    'rti': 'respiratory tract infection',
    'uti': 'urinary tract infection',
    'hfm': 'hand foot mouth disease',
    'rsh': 'rash',
    'fev': 'fever',
    'cou': 'cough',
    'ough':'cough',
    'ugh': 'cough',
    'abd': 'abdominal pain',
    'loa': 'loss of appetite',
    'age': 'acute gastroenteritis',
    'wax': 'ear wax',
    'vfc': 'vomiting fever cough',
    'fvc': 'fever vomiting cough',
    'puf': 'fever',
    'dc':  'diarrhoea cough',
    'sob': 'shortness of breath',

    # Four+ letters
    'urti':   'upper respiratory tract infection',
    'lrti':   'lower respiratory tract infection',
    'hfmd':   'hand foot mouth disease',
    'couggh': 'cough',
    'cogh':   'cough',
    'couigh': 'cough',

    # Multi-word shorthand
    'abd pain':             'abdominal pain',
    'ab pain':              'abdominal pain',
    'adb pain':             'abdominal pain',
    'abd.pain':             'abdominal pain',
    'ear ache':             'ear pain',
    'earache':              'ear pain',
    'loose motion':         'diarrhoea',
    'loose stool':          'diarrhoea',
    'loose stools':         'diarrhoea',
    'running nose':         'nasal congestion',
    'runny nose':           'nasal congestion',
    'h ache':               'headache',
    'head ache':            'headache',
    'vom':                  'vomiting',
    'cough and cold':       'cough cold',
    'cold and cough':       'cough cold',
    'cough ,cold':          'cough cold',
    'cough, cold':          'cough cold',
    'cough cold and fever': 'cough cold fever',
}


# =============================================================================
# SECTION 2 — CATEGORY KEYWORD SETS
# Respiratory is split into sub-types because antibiotic treatment differs
# =============================================================================

CATEGORY_KEYWORDS = {
    'Respiratory-Wheeze': [
        'wheez', 'bronchial asthma', 'asthma', 'shortness of breath',
        'sob', 'stridor', 'croup', 'breathing difficulty', 'chest tightness',
    ],
    'Respiratory-LRTI': [
        'pneumon', 'bronchopneumon', 'lrti', 'lower respiratory',
        'consolidat', 'bronchitis',
    ],
    'Respiratory-URTI': [
        'cough', 'cold', 'chest pain', 'nasal', 'congestion', 'rhinitis', 'nasopharyngitis',
        'common cold', 'urti', 'upper respiratory', 'respiratory tract infection',
        'rti', 'runny', 'phlegm', 'sputum', 'sinusitis',
    ],
    'Fever': [
        'fever', 'pyrex', 'febrile', 'high temperature',
    ],
    'Skin': [
        'rash', 'skin', 'scabies', 'itch', 'urticaria', 'derma',
        'eczema', 'fungal', 'tinea', 'impetigo', 'cellulitis',
        'abscess', 'wound', 'boil', 'blister', 'hive',
        'hand foot mouth', 'chickenpox', 'varicella', 'allerg',
        'papule', 'vesicle', 'erythema',
        'dandruff', 'pityriasis', 'taenia', 'pustule', 'chicken pox',
        'hair scalp',
    ],
    'GI': [
        'vomit', 'diarrh', 'diarr', 'loose', 'abdominal', 'nausea',
        'gastro', 'constip', 'stomach', 'bowel', 'gerd', 'reflux',
        'worm', 'parasite', 'loss of appetite', 'acute gastroenteritis',
        'gastritis', 'epigastric', 'food poison', 'dyspepsia',
        'abdominal pain',
    ],
    'ENT': [
        'ear pain', 'ear ache', 'earache', 'ear wax', 'ear discharge', 'ear',
        'otitis', 'toothache',
        'eye', 'conjunctiv', 'sore throat', 'tonsil', 'throat',
        'lymph node', 'lymph', 'nasal polyp', 'adenoid', 'hearing',
        'neck',
    ],
    'UTI': [
        'dysuria', 'urinary', 'urination', 'uti', 'enuresis',
        'haematuria', 'kidney', 'renal', 'painful urin', 'bedwetting',
    ],
    'Neuro': [
        'seizure', 'convuls', 'headache', 'head ache', 'migraine',
        'developmental', 'behavioural', 'unconscious',
    ],
    'Musculo': [
        'joint pain', 'bone', 'limb', 'leg pain', 'arm pain', 'limp',
        'fracture', 'muscle', 'back pain', 'hip pain', 'swollen joint',
    ],
}

RESPIRATORY_PRIORITY = ['Respiratory-LRTI', 'Respiratory-Wheeze', 'Respiratory-URTI']

BROAD_SYSTEM = {
    'Respiratory-Wheeze': 'Respiratory',
    'Respiratory-LRTI':   'Respiratory',
    'Respiratory-URTI':   'Respiratory',
    'Fever':      'Fever',
    'Skin':       'Skin',
    'GI':         'GI',
    'ENT':        'ENT',
    'UTI':        'UTI',
    'Neuro':      'Neuro',
    'Musculo':    'Musculo',
}


# =============================================================================
# SECTION 3 — CORE FUNCTIONS
# =============================================================================

def _clean_raw(text):
    """Lowercase, replace separators with space, strip punctuation, normalise spaces."""
    text = str(text).lower().strip()
    text = re.sub(r'[,;/|\\]+', ' ', text)
    text = re.sub(r'\(([^)]{0,40})\)', r' \1 ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def _strip_duration(text):
    """Remove duration tokens like 1d, 2d, 1w, fever3d from text."""
    # Handles both 'fever 1d' and 'f1d' style
    text = re.sub(r'\d+\s*(?:days?|d)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\d+\s*(?:weeks?|wks?|w)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\d+\s*(?:months?|m)\b', '', text, flags=re.IGNORECASE)
    return re.sub(r'\s+', ' ', text).strip()


def extract_duration(text):
    """
    Extract complaint duration in days. Returns int or None.
    Handles: 1d, 1 day, 1w, 1 week, f1d, fe3d, fever1d, cough 3 days
    """
    text = str(text).lower()

    # Pattern: optional letters, then digits, then d/day/days
    day_match = re.search(r'[a-z]*?(\d+)\s*(?:days?\b|d\b)', text)
    if day_match:
        val = int(day_match.group(1))
        return val if 1 <= val <= 365 else None

    week_match = re.search(r'(\d+)\s*(?:weeks?\b|wks?\b|w\b)', text)
    if week_match:
        val = int(week_match.group(1))
        return val * 7 if val <= 52 else None

    month_match = re.search(r'(\d+)\s*(?:months?\b|m\b)', text)
    if month_match:
        val = int(month_match.group(1))
        return val * 30 if val <= 24 else None

    return None


def expand_abbreviations(text):
    """
    Expand abbreviations to plain English and strip duration tokens.
    Returns clean, human-readable complaint text.
    """
    text = _clean_raw(text)

    # Check whole string as exact abbreviation before anything else
    if text in ABBREV_MAP:
        return ABBREV_MAP[text]

    # Strip duration tokens, then check again
    text_no_dur = _strip_duration(text)
    if text_no_dur in ABBREV_MAP:
        return ABBREV_MAP[text_no_dur]

    # Apply multi-word abbreviations (longest first)
    for abbr in sorted(ABBREV_MAP.keys(), key=len, reverse=True):
        if ' ' in abbr and abbr in text_no_dur:
            text_no_dur = text_no_dur.replace(abbr, ABBREV_MAP[abbr])

    # Token-by-token expansion
    tokens = text_no_dur.split()
    expanded = []
    for tok in tokens:
        tok_clean = tok.strip('.,;-')
        if tok_clean in ABBREV_MAP:
            expanded.append(ABBREV_MAP[tok_clean])
        elif tok_clean:
            expanded.append(tok_clean)

    result = ' '.join(expanded).strip()
    # Remove duplicate consecutive words ("cough cough" → "cough")
    result = re.sub(r'\b(\w+)( \1)+\b', r'\1', result)
    return result if result else 'unspecified'


def get_complaint_category(cleaned_text):
    """
    Assign clinical category.
    - Single system match → that category (respiratory sub-typed)
    - Multiple different systems → 'Multi-system'
    - No match → 'Unclassified'
    """
    matched = []
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in cleaned_text:
                matched.append(category)
                break

    if not matched:
        return 'Unclassified'

    broad_systems = set(BROAD_SYSTEM[m] for m in matched)

    if len(broad_systems) > 1:
        return 'Multi-system'

    if 'Respiratory' in broad_systems:
        for resp_cat in RESPIRATORY_PRIORITY:
            if resp_cat in matched:
                return resp_cat
        return 'Respiratory-URTI'

    return matched[0]


# =============================================================================
# SECTION 4 — MAIN FUNCTION
# =============================================================================

def add_complaint_features(df, complaint_col='Complaint'):
    """
    Adds three columns to your dataframe:
        complaint_clean         - Expanded readable complaint text
        complaint_category      - Clinical category
        complaint_duration_days - Duration in days (int or NaN)

    Usage:
        from complaint_cleaning import add_complaint_features
        df = add_complaint_features(df)
    """
    print("Adding complaint features...")
    print(f"  Total encounters : {len(df):,}")

    raw = df[complaint_col].fillna('').astype(str)

    df['complaint_clean']          = raw.apply(expand_abbreviations)
    df['complaint_category']       = df['complaint_clean'].apply(get_complaint_category)
    df['complaint_duration_days']  = raw.apply(extract_duration)

    print("\n  complaint_category distribution:")
    print(df['complaint_category'].value_counts().to_string())

    covered = (df['complaint_category'] != 'Unclassified').sum()
    pct = 100 * covered / len(df)
    print(f"\n  Classified    : {covered:,} ({pct:.1f}%)")
    print(f"  Unclassified  : {len(df) - covered:,} ({100-pct:.1f}%)")
    print(f"  With duration : {df['complaint_duration_days'].notna().sum():,} "
          f"({100*df['complaint_duration_days'].notna().sum()/len(df):.1f}%)")

    return df


# =============================================================================
# SECTION 5 — TEST SUITE
# =============================================================================

if __name__ == '__main__':
    tests = [
        # (raw_input, expected_in_clean, expected_category, expected_duration)
        ('c',                       'cough',                    'Respiratory-URTI',   None),
        ('f',                       'fever',                    'Fever',              None),
        ('cc',                      'cough cold',               'Respiratory-URTI',   None),
        ('f1d',                     'fever',                    'Fever',              1),
        ('fe1d cough',              'fever cough',              'Multi-system',       1),
        ('cough 3d',                'cough',                    'Respiratory-URTI',   3),
        ('f 1d',                    'fever',                    'Fever',              1),
        ('fever 1 day',             'fever',                    'Fever',              1),
        ('cough 1w',                'cough',                    'Respiratory-URTI',   7),
        ('ba',                      'bronchial asthma',         'Respiratory-Wheeze', None),
        ('vf',                      'vomiting fever',           'Multi-system',       None),
        ('loa',                     'loss of appetite',         'GI',                 None),
        ('age',                     'acute gastroenteritis',    'GI',                 None),
        ('ln',                      'lymph node enlargement',   'ENT',                None),
        ('wax',                     'ear wax',                  'ENT',                None),
        ('n',                       'nausea',                   'GI',                 None),
        ('hfm',                     'hand foot mouth disease',  'Skin',               None),
        ('sob',                     'shortness of breath',      'Respiratory-Wheeze', None),
        ('uti',                     'urinary tract infection',  'UTI',                None),
        ('rti',                     'respiratory tract infection','Respiratory-URTI',  None),
        ('w',                       'unspecified',              'Unclassified',       None),
        ('e',                       'unspecified',              'Unclassified',       None),
        ('fever, cough',            'fever cough',              'Multi-system',       None),
        ('cough and cold,fever 1d', 'cough cold fever',         'Multi-system',       1),
        ('fever,vomiting,',         'fever vomiting',           'Multi-system',       None),
        ('wheezing,',               'wheezing',                 'Respiratory-Wheeze', None),
        ('pneumonia',               'pneumonia',                'Respiratory-LRTI',   None),
        ('scabies',                 'scabies',                  'Skin',               None),
        ('rash localized,',         'rash',                     'Skin',               None),
        ('dysuria,',                'dysuria',                  'UTI',                None),
        ('ear pain',                'ear pain',                 'ENT',                None),
        ('abdominal pain',          'abdominal pain',           'GI',                 None),
        ('seizure',                 'seizure',                  'Neuro',              None),
        ('headache,',               'headache',                 'Neuro',              None),
        ('loose motion',            'diarrhoea',                'GI',                 None),
        ('vomiting,',               'vomiting',                 'GI',                 None),
        ('wound',                   'wound',                    'Skin',               None),
        ('fc',                      'fever cough',              'Multi-system',       None),
        ('ccf',                     'cough cold fever',         'Multi-system',       None),
        ('fever1d',                 'fever',                    'Fever',              1),
        ('c c',                     'cough',                    'Respiratory-URTI',   None),
        ('scabies/other acariasis,','scabies',                  'Skin',               None),
    ]

    print(f"{'Original':<35} {'Cleaned':<30} {'Category':<22} {'Dur':<5} {'OK?'}")
    print("-" * 105)
    passed = 0
    for raw, exp_clean, exp_cat, exp_dur in tests:
        cleaned  = expand_abbreviations(raw)
        category = get_complaint_category(cleaned)
        duration = extract_duration(raw)
        ok_c = exp_clean in cleaned
        ok_k = category == exp_cat
        ok_d = duration == exp_dur
        ok   = '✓' if ok_c and ok_k and ok_d else '✗'
        if ok == '✓':
            passed += 1
        notes = ''
        if not ok_c: notes += f' clean:got "{cleaned}"'
        if not ok_k: notes += f' cat:got "{category}"'
        if not ok_d: notes += f' dur:got {duration}'
        print(f"{raw:<35} {cleaned:<30} {category:<22} {str(duration):<5} {ok}{notes}")

    print(f"\n{passed}/{len(tests)} tests passed.")


# =============================================================================
# SECTION 6 — SYMPTOM TAGGING (drug-style pipe-separated columns)
# =============================================================================

# Map each detailed category to its broad display label for symptom_profile
SYMPTOM_DISPLAY = {
    'Respiratory-LRTI':   'Respiratory',
    'Respiratory-Wheeze': 'Respiratory',
    'Respiratory-URTI':   'Respiratory',
    'Fever':              'Fever',
    'Skin':               'Skin',
    'GI':                 'GI',
    'ENT':                'ENT',
    'UTI':                'UTI',
    'Neuro':              'Neuro',
    'Musculo':            'Musculo',
}

# Priority order when multiple Respiratory sub-types match — for symptom_tags
# we still want the most specific sub-type listed
SYMPTOM_TAG_RESP_PRIORITY = [
    'Respiratory-LRTI', 'Respiratory-Wheeze', 'Respiratory-URTI'
]


def get_symptom_tags(cleaned_text):
    """
    Returns all matched categories as a pipe-separated string.
    Like drug AWaRe categories — one tag per system detected.
    Within Respiratory, only the highest-priority sub-type is listed
    (avoids duplicating Respiratory-URTI and Respiratory-Wheeze for same text).

    Examples:
      'fever cough'      → 'Fever|Respiratory-URTI'
      'fever vomiting'   → 'Fever|GI'
      'cough'            → 'Respiratory-URTI'
      'fever'            → 'Fever'
    """
    if not cleaned_text or cleaned_text == 'unspecified':
        return ''

    matched = []
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in cleaned_text:
                matched.append(category)
                break

    if not matched:
        return ''

    # Resolve respiratory sub-types: keep only the highest-priority one
    resp_matched = [m for m in matched if m.startswith('Respiratory')]
    non_resp     = [m for m in matched if not m.startswith('Respiratory')]

    final = list(non_resp)
    if resp_matched:
        for resp_cat in SYMPTOM_TAG_RESP_PRIORITY:
            if resp_cat in resp_matched:
                final.append(resp_cat)
                break

    # Consistent ordering: Fever first, then Respiratory, then others alphabetically
    def sort_key(cat):
        if cat == 'Fever':            return '0'
        if cat.startswith('Resp'):    return '1' + cat
        return '2' + cat

    final.sort(key=sort_key)
    return '|'.join(final)


def get_symptom_profile(symptom_tags_str):
    """
    Human-readable summary of the symptom combination.
    Maps detailed tags to broad display names and joins with '+'.

    Examples:
      'Fever|Respiratory-URTI'  → 'Fever+Respiratory'
      'Fever|GI'                → 'Fever+GI'
      'Respiratory-URTI'        → 'Respiratory-URTI'   (single — keep sub-type)
      'Fever'                   → 'Fever'
      ''                        → 'Unclassified'
    """
    if not symptom_tags_str:
        return 'Unclassified'

    tags = symptom_tags_str.split('|')

    if len(tags) == 1:
        # Single system — keep the detailed sub-type label
        return tags[0]

    # Multiple systems — map to broad display names and deduplicate
    seen  = set()
    parts = []
    for tag in tags:
        display = SYMPTOM_DISPLAY.get(tag, tag)
        if display not in seen:
            seen.add(display)
            parts.append(display)

    return '+'.join(parts)


def add_symptom_features(df, clean_col='complaint_clean'):
    """
    Adds four symptom-level columns to the dataframe.
    Requires complaint_clean to already exist (run add_complaint_features first).

    Columns added:
        symptom_tags       - pipe-separated system tags  (like aware_categories)
        symptom_profile    - readable combination label  (like aware_profile)
        has_fever          - 1 if Fever detected, else 0
        has_respiratory    - 1 if any Respiratory sub-type detected, else 0

    Usage:
        df = add_complaint_features(df)   # run first
        df = add_symptom_features(df)     # then this
    """
    print("Adding symptom features...")

    df['symptom_tags']    = df[clean_col].apply(get_symptom_tags)
    df['symptom_profile'] = df['symptom_tags'].apply(get_symptom_profile)
    df['has_fever']       = df['symptom_tags'].str.contains('Fever',       na=False).astype(int)
    df['has_respiratory'] = df['symptom_tags'].str.contains('Respiratory', na=False).astype(int)

    print("\n  symptom_profile distribution:")
    print(df['symptom_profile'].value_counts().head(20).to_string())

    print(f"\n  has_fever        = 1 : {df['has_fever'].sum():,} ({100*df['has_fever'].mean():.1f}%)")
    print(f"  has_respiratory  = 1 : {df['has_respiratory'].sum():,} ({100*df['has_respiratory'].mean():.1f}%)")

    fever_resp = ((df['has_fever'] == 1) & (df['has_respiratory'] == 1)).sum()
    print(f"  Fever+Respiratory combined : {fever_resp:,} ({100*fever_resp/len(df):.1f}%)")

    return df
