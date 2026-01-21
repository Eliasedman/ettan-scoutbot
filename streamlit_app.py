import streamlit as st
import pandas as pd
from data_adapter import DataAdapter
from scoring_engine import ScoringEngine


def main():
    """Streamlit UI for Ettan Scoutbot"""
    st.title("Ettan Scoutbot")
    st.write("Upload player CSV data to get started.")
    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success(f"Loaded {len(df)} players.")

        # Define role profile weights
        st.subheader("Define Role Profile")
        role_profile = {}
        if not df.empty:
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
            for col in numeric_cols:
                weight = st.number_input(f"Weight for {col}", value=0.0, step=0.1)
                if weight != 0.0:
                    role_profile[col] = weight

        if st.button("Compute Scores"):
            engine = ScoringEngine()
            scores = []
            for _, row in df.iterrows():
                score = engine.compute_fit_score(row, role_profile)
                scores.append(score)
            df["FitScore"] = scores
            top25 = df.sort_values("FitScore", ascending=False).head(25)
            st.subheader("Top 25 Players")
            st.dataframe(top25[[col for col in ["name", "age", "club", "FitScore"] if col in top25.columns]])


if __name__ == "__main__":
    main()
