import streamlit as st
import tempfile
import json
from tools import extract_infos_from_receipt  # Remplace par le nom de ton fichier backend sans `.py`

st.set_page_config(page_title="Invoice Extractor", page_icon="🧾")

st.title("🧾 Invoice Information Extractor")
st.markdown("Upload a receipt or invoice image to extract key details (company name, subtotal, total amount).")

# Upload image
uploaded_file = st.file_uploader("Upload your invoice image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display the image
    st.image(uploaded_file, caption="Uploaded Invoice", use_container_width =True)

    # Temporary save of the uploaded image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    if st.button("📤 Extract Information"):
        with st.spinner("Extracting data..."):
            try:
                extracted_data = extract_infos_from_receipt(temp_path)
                parsed_data = json.loads(extracted_data)
                st.success("✅ Extraction completed!")
                st.json(parsed_data)

                # Enable download
                json_str = json.dumps(parsed_data, indent=4)
                st.download_button(
                    label="📥 Download JSON",
                    data=json_str,
                    file_name="invoice_data.json",
                    mime="application/json"
                )
            except Exception as e:
                st.error(f"❌ An error occurred during extraction: {e}")
