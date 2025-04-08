import streamlit as st
import json

# Load the extracted data
with open('output.json', 'r') as f:
    data = json.load(f)

st.set_page_config(page_title="Dark Web Threat Intel", layout="wide")

st.title("🕵️ Dark Web Threat Intelligence Dashboard")
st.markdown("See leaked emails, Bitcoin addresses, and text snippets from dark web sources.")

for item in data:
    with st.expander(f"Source: {item['source']}"):
        st.subheader("📧 Leaked Emails")
        if item['emails']:
            for email in item['emails']:
                st.write(f"- {email}")
        else:
            st.write("No emails found.")

        st.subheader("₿ Bitcoin Addresses")
        if item['btc_addresses']:
            for btc in item['btc_addresses']:
                st.write(f"- {btc}")
        else:
            st.write("No BTC addresses found.")

        st.subheader("📝 Text Snippet")
        st.code(item['text_snippet'], language='text')
