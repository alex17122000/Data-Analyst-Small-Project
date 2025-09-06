import pandas as pd

df = pd.read_csv("top_entity_matches_scored.csv")
df = df[df["verdict"] == "MATCHED"]
df_full = pd.read_csv("presales_data_sample.csv")

merged = pd.merge(df, df_full, on="veridion_id", how="left")

def get_existing_col(df_, base):
    for variant in [base, f"{base}_x", f"{base}_y"]:
        if variant in df_.columns:
            return variant
    return None

campuri = {
    "website_url": "Website valid",
    "linkedin_url": "LinkedIn prezent",
    "year_founded": "An înființare",
    "revenue": "Venit raportat",
    "employee_count": "Număr angajați",
    "nace_rev2_codes": "Cod NACE",
    "sic_codes": "Cod SIC",
    "naics_2022_primary_code": "Cod NAICS"
}

rezultate = []
linii_total = len(merged)

# Partea de Quality Check
for field, descriere in campuri.items():
    col = get_existing_col(merged, field)
    if col:
        lipsa = merged[col].isna().sum()
        procente = round((lipsa / linii_total) * 100, 2)
        rezultate.append({
            "Camp": descriere,
            "Lipsesc (count)": lipsa,
            "Complet (%)": 100 - procente
        })
    else:
        rezultate.append({
            "Camp": descriere,
            "Lipsesc (count)": "NU EXISTA",
            "Complet (%)": "-"
        })

qc_df = pd.DataFrame(rezultate)


try:
    qc_df.to_csv("qc_summary_report.csv", index=False)
    print("Salvat in qc_summary_report.csv !")
except Exception as err:
    print("Nu s a putut salva.", err)

print(qc_df)
