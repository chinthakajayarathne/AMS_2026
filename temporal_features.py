# =============================================================================
# TEMPORAL FEATURE ENGINEERING  v2.0
# Adds two raw temporal columns from DateTimeOfVisit:
#
#   visit_month  - Month number (1–12)
#   visit_hour   - Hour of day (0–23)
#
# After EDA, you can decide how to group these into categories
# (e.g. season, time_category) for clustering.
#
# HOW TO USE IN YOUR NOTEBOOK:
#   import sys
#   sys.path.insert(0, r'd:\Academic\MD Research 2025\AMS_2026')
#   from temporal_features import add_temporal_features
#   df = add_temporal_features(df)
# =============================================================================

import pandas as pd


def add_temporal_features(df, datetime_col='DateTimeOfVisit'):
    """
    Adds two raw temporal columns to your dataframe:
        visit_month  - Month number (1 = January, 12 = December)
        visit_hour   - Hour of day (0 = midnight, 23 = 11pm)

    Parameters:
        df           : your OPD encounters dataframe
        datetime_col : name of the datetime column (default 'DateTimeOfVisit')

    Returns:
        df with two new columns added
    """
    print("Adding temporal features...")
    print(f"  Total encounters : {len(df):,}")

    # Parse datetime if not already done
    if not pd.api.types.is_datetime64_any_dtype(df[datetime_col]):
        df[datetime_col] = pd.to_datetime(df[datetime_col], errors='coerce')

    n_parsed = df[datetime_col].notna().sum()
    n_failed = df[datetime_col].isna().sum()
    print(f"  Datetime parsed  : {n_parsed:,} ({100*n_parsed/len(df):.1f}%)")
    if n_failed > 0:
        print(f"  Failed to parse  : {n_failed:,} -- these will be NULL")

    df['visit_month'] = df[datetime_col].dt.month
    df['visit_hour']  = df[datetime_col].dt.hour

    print("\n  visit_month distribution:")
    print(df['visit_month'].value_counts(dropna=False).sort_index().to_string())

    print("\n  visit_hour distribution:")
    print(df['visit_hour'].value_counts(dropna=False).sort_index().to_string())

    return df


# =============================================================================
# STANDALONE TEST
# =============================================================================

if __name__ == '__main__':
    test_data = {
        'OPDID': range(1, 7),
        'DateTimeOfVisit': [
            '2026-01-15 07:30:00',
            '2026-05-20 14:00:00',
            '2026-09-01 00:00:00',
            '2026-12-25 23:59:00',
            '2026-03-10 12:00:00',
            None,
        ]
    }
    expected = [
        (1,  7),
        (5,  14),
        (9,  0),
        (12, 23),
        (3,  12),
        (None, None),
    ]

    df_test = pd.DataFrame(test_data)
    df_test = add_temporal_features(df_test)

    print(f"\n{'DateTimeOfVisit':<28} {'Month':<8} {'Hour':<8} {'OK?'}")
    print("-" * 55)
    all_pass = True
    for i, (exp_m, exp_h) in enumerate(expected):
        got_m = df_test.loc[i, 'visit_month']
        got_h = df_test.loc[i, 'visit_hour']
        if exp_m is None:
            ok = pd.isna(got_m) and pd.isna(got_h)
        else:
            ok = (int(got_m) == exp_m and int(got_h) == exp_h)
        if not ok:
            all_pass = False
        raw = str(test_data['DateTimeOfVisit'][i])
        print(f"{raw:<28} {str(got_m):<8} {str(got_h):<8} {'✓' if ok else '✗'}")

    print(f"\n{'All tests passed!' if all_pass else 'Some tests failed.'}")
