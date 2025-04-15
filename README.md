# 🧾 Invoice Info Extractor

An AI-powered web app to automatically extract key information from invoice images using a multimodal model (image + text).

> Extract the **company name**, **subtotal (excl. VAT)**, and **total amount (incl. VAT)** from invoices — with just one click.

---

## 🔍 Features

- Upload invoice images (JPG, PNG)
- Visual preview of the uploaded invoice
- Extract structured data (JSON output)
- Download the extracted data
- Powered by a large multimodal model (Mistral)

---

## 🚀 Tech Stack

- **Backend**: Python, [Mistral API](https://mistral.ai/)
- **Frontend**: Streamlit
- **Image Handling**: Base64 encoding
- **File I/O**: Tempfile for safe file handling

---

## 📦 Installation

```bash
git clone https://github.com/your-username/invoice-extractor.git
cd invoice-extractor
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
