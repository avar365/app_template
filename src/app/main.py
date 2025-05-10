import streamlit as st
from app.file_handler import handle_upload, list_uploaded_files

st.title("File Upload Tracker")

uploaded_file = st.file_uploader("Upload a file", type=None)

if uploaded_file:
    file_path = handle_upload(uploaded_file)
    st.success(f"Uploaded: {file_path}")

st.subheader("Uploaded Files")
for f in list_uploaded_files():
    st.write(f)
