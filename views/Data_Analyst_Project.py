import streamlit as st
import pandas as pd
import numpy as np

st.title("Peran Public Awareness terhadap Kapasitas Energi Terbarukan: Analisis Data 2023")
st.write("A/B Testing 🧪")


# ---------- Upload File ---------- #
file_path = "assets/df_2023_agg.csv" 

try:
    df = pd.read_csv(file_path)
    st.dataframe(df)
except FileNotFoundError:
    st.error(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")


# ---------- Selection ---------- #
st.subheader("Filter")
num_cols = sorted(df.select_dtypes("number").columns.tolist())


countries = sorted(df["Country"].unique()) if "Country" in df.columns else []
energies  = sorted(df["Energy Type"].unique()) if "Energy Type" in df.columns else []

c1, c2, c3, c4 = st.columns([1,1,1,1.2])
country_sel = c1.multiselect("Country", countries, default=countries[:5]) if countries else []
energy_sel  = c2.multiselect("Energy Type", energies) if energies else []
metric      = c3.selectbox("Metric (numeric)", num_cols, index=(num_cols.index("Installed Capacity") if "Installed Capacity" in num_cols else 0))
top_n       = c4.slider("Top N (bar)", 5, 30, 10)


q = df.copy()
if country_sel:
    q = q[q["Country"].isin(country_sel)]
if energy_sel:
    q = q[q["Energy Type"].isin(energy_sel)]

st.caption(f"Rows after filter: {len(q)}")


# -------- Visual -------- #
st.subheader("Ringkasan")
m1, m2, m3 = st.columns(3)
m1.metric("Mean", f"{q[metric].mean():,.2f}")
m2.metric("Median", f"{q[metric].median():,.2f}")
m3.metric("N", int(q[metric].count()))


if "Country" in q.columns:
    st.write(f"**Top {top_n} Country — {metric}**")
    agg = (q.groupby("Country", as_index=False)[metric]
             .mean().sort_values(metric, ascending=False).head(top_n))
    st.bar_chart(agg, x="Country", y=metric)


cand = [c for c in num_cols if c != metric]
if cand:
    x_col = st.selectbox("X axis (numeric)", cand, index=(cand.index("Public Awareness") if "Public Awareness" in cand else 0))
    st.scatter_chart(q[[x_col, metric]].dropna(), x=x_col, y=metric)