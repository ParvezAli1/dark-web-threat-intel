import streamlit as st
import webbrowser
import threading

def open_deployed_link():
    webbrowser.open_new_tab("https://dark-web-threat-intel-fbn7lrtwgt4dcccypgbwa2.streamlit.app")

threading.Timer(1.0, open_deployed_link).start()
import streamlit as st
import json
import pandas as pd


st.set_page_config(page_title="Dark Web Threat Dashboard", layout="wide")

# --- Load Data ---
with open("output.json") as f:
    data = json.load(f)

# --- Convert to DataFrame for filtering ---
df = pd.DataFrame(data)

# --- Title ---
st.title("🕷️ Dark Web Threat Intelligence Dashboard")
st.markdown("Simulated dark web crawler data with enhanced features for threat tracking.")

# --- Summary Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Emails", sum(len(i['emails']) for i in data))
col2.metric("Total BTC Addresses", sum(len(i['btc_addresses']) for i in data))
col3.metric("Sources", df['source'].nunique())


# --- Search filters ---
search = st.text_input("🔍 Search by email, BTC address, or source:")
if search:
    filtered_data = [item for item in data if search.lower() in json.dumps(item).lower()]
else:
    filtered_data = data

# --- Display Results ---
st.subheader("📁 Crawler Results")
for item in filtered_data:
    with st.expander(f"Source: {item['source']}"):
        st.markdown("**Emails Found:**")
        if item['emails']:
            for email in item['emails']:
                role = "🛑 [Threat Actor]" if "threat_actor" in email.lower() else "🧑‍💻 [Victim]"
                st.markdown(f"- {role} `{email}`")
        else:
            st.markdown("- None")

        st.markdown("**BTC Addresses:**")
        if item['btc_addresses']:
            for btc in item['btc_addresses']:
                st.markdown(f"- `{btc}`")
        else:
            st.markdown("- None")

        st.code(item['text_snippet'], language="text")

# --- Download JSON ---
from fpdf import FPDF

if st.button("📄 Download PDF Report"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_title("Dark Web Threat Report")

    for item in filtered_data:
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 10, f"Source: {item['source']}", ln=True)

        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, "Emails Found:", ln=True)
        if item['emails']:
            for email in item['emails']:
                pdf.cell(0, 8, f"  - {email}", ln=True)
        else:
            pdf.cell(0, 8, "  - None", ln=True)

        pdf.cell(0, 8, "BTC Addresses:", ln=True)
        if item['btc_addresses']:
            for btc in item['btc_addresses']:
                pdf.cell(0, 8, f"  - {btc}", ln=True)
        else:
            pdf.cell(0, 8, "  - None", ln=True)

        pdf.ln(5)

    pdf.output("darkweb_report.pdf")
    with open("darkweb_report.pdf", "rb") as file:
        st.download_button("📥 Download PDF", file.read(), file_name="darkweb_report.pdf", mime="application/pdf")
