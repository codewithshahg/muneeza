import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up the page configuration
st.set_page_config(page_title="Data Sweeper", layout='wide')

# Custom CSS for dark theme
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("Data Sweeper Sterling Integrator By Syeda Muneeza")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization. Creating the project for Q3!")

# File uploader
uploaded_files = st.file_uploader("📂 Upload your file (accepts CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Process file based on its extension
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            try:
                df = pd.read_excel(file)
            except ImportError as e:
                st.error(f"Error: {e}")
                st.error("You need to install the 'openpyxl' library to read Excel files.")
                continue
        else:
            st.error(f"❌ Unsupported file type: {file_ext}. Please upload either a CSV or Excel file.")
            continue

        # Display file preview
        st.write("👀 Preview the head of the DataFrame:")
        st.dataframe(df.head())

        # Data cleaning options
        st.subheader("🧹 Data Cleaning Options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from {file.name} 🗑️"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed!")

            with col2:
                if st.button(f"Fill missing values for {file.name} 🔄"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values filled!")

            # Select columns to keep
            st.subheader("🔧 Select columns to keep.")
            columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
            df = df[columns]

            # Data visualization
            st.subheader("📊 Data Visualization")
            if st.checkbox(f"Show visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

            # Conversion option
            st.subheader("🔄 Conversion Option")
            conversation_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

            if st.button(f"Convert {file.name}"):

                buffer = BytesIO()

                # If converting to CSV
                if conversation_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"  # Correct MIME type for CSV

                # If converting to Excel
                elif conversation_type == "Excel":
                    df.to_excel(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # Correct MIME type for Excel

                buffer.seek(0)

                # Provide the download button
                st.download_button(
                    label=f"Download {file.name} as {conversation_type} 📥",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type,
                )

                st.success("✅ File processed successfully! 🎉")

try:
    import openpyxl
    st.success("openpyxl is successfully imported!")
except ImportError as e:
    st.error(f"ImportError: {e}")
