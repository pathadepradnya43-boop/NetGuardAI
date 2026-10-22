import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NetGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ NetGuard AI")
st.subheader("Network Traffic Analysis and Intrusion Detection")

st.write(
    "Upload a CSV traffic dataset to inspect records "
    "and identify traffic that needs further investigation."
)

# Demonstration dataset used when no file is uploaded
sample_data = {
    "Source IP": [
        "192.168.1.10",
        "192.168.1.15",
        "192.168.1.20",
        "192.168.1.25"
    ],
    "Protocol": ["TCP", "UDP", "TCP", "TCP"],
    "Destination Port": [443, 53, 22, 80],
    "Connection Count": [12, 8, 150, 10]
}

uploaded_file = st.file_uploader(
    "Upload network traffic CSV",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        if df.empty:
            st.error("The uploaded CSV contains no records.")
            st.stop()

        st.success("CSV uploaded successfully!")

    except Exception as error:
        st.error(f"Could not read the CSV: {error}")
        st.stop()

else:
    df = pd.DataFrame(sample_data)
    st.info(
        "Showing demonstration data. Upload your own CSV "
        "to analyse a dataset."
    )

# Clean column names to make matching easier
df.columns = [
    str(column).strip()
    for column in df.columns
]

st.markdown("### Dataset Overview")

col1, col2 = st.columns(2)
col1.metric("Total Records", len(df))
col2.metric("Total Columns", len(df.columns))

st.write("Available columns:")
st.write(", ".join(df.columns))

# Find a connection-count column, ignoring capitalization
column_lookup = {
    str(column).strip().lower(): column
    for column in df.columns
}

count_column = column_lookup.get("connection count")

if count_column is None:
    count_column = column_lookup.get("connection_count")

if count_column is None:
    st.warning(
        "No Connection Count column was found. "
        "Your records are displayed below, but the "
        "connection-count detection rule cannot run. "
        "We will add support for other dataset formats next."
    )

    st.markdown("### Uploaded Traffic Records")
    st.dataframe(df, width="stretch")

else:
    # Convert the chosen column to numbers
    df[count_column] = pd.to_numeric(
        df[count_column],
        errors="coerce"
    )

    # Explain missing values rather than silently treating them as normal
    df["Status"] = "Needs Review"
    df["Reason"] = "Connection count is missing or invalid"

    valid = df[count_column].notna()

    df.loc[valid, "Status"] = "Normal"
    df.loc[valid, "Reason"] = (
        "No alert triggered by the demonstration rule"
    )

    suspicious = valid & (df[count_column] > 100)

    df.loc[suspicious, "Status"] = "Suspicious - Review"
    df.loc[suspicious, "Reason"] = (
        "Connection count exceeds the demonstration threshold of 100"
    )

    normal_count = int((df["Status"] == "Normal").sum())
    flagged_count = int(
        (df["Status"] == "Suspicious - Review").sum()
    )
    review_count = int((df["Status"] == "Needs Review").sum())

    st.markdown("### Detection Summary")

    col1, col2, col3 = st.columns(3)
    col1.metric("Normal", normal_count)
    col2.metric("Flagged for Review", flagged_count)
    col3.metric("Needs Review", review_count)

    st.markdown("### Analysed Traffic")

    status_filter = st.selectbox(
        "Filter records",
        [
            "All Records",
            "Suspicious - Review",
            "Normal",
            "Needs Review"
        ]
    )

    if status_filter == "All Records":
        display_df = df
    else:
        display_df = df[df["Status"] == status_filter]

    st.dataframe(display_df, width="stretch")

    csv_output = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Analysed CSV",
        data=csv_output,
        file_name="netguard_analysis.csv",
        mime="text/csv"
    )

st.caption(
    "Important: The threshold of 100 is a demonstration rule, "
    "not a validated attack detector or trained AI model. "
    "A flagged record requires investigation and is not proof "
    "of malicious activity."
)