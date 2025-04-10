import streamlit as st
import webbrowser
import threading

def open_deployed_link():
    webbrowser.open_new_tab("https://dark-web-threat-intel-fbn7lrtwgt4dcccypgbwa2.streamlit.app")

threading.Timer(1.0, open_deployed_link).start()
import streamlit as st
import json

# Load the extracted data
with open('output.json', 'r') as f:
    data = json.load(f)

st.set_page_config(page_title="Dark Web Threat Intel", layout="wide")

st.title("🕵️ Dark Web Threat Intelligence Dashboard")
st.markdown("See leaked emails, Bitcoin addresses, and text snippets from dark web sources.")

for item in data:
    with st.expander(f"📡 Source: {item['source']}"):
        st.subheader("📧 Leaked Emails")
        if item['emails']:
            for email in item['emails']:
                if email.endswith('.onion'):
                    st.markdown(f"- 🛑 **[Threat Actor]** `{email}`")
                else:
                    st.markdown(f"- 🕵️ **[Victim]** `{email}`")
        else:
            st.write("No emails found.")

        st.subheader("₿ Bitcoin Addresses")
        if item['btc_addresses']:
            for btc in item['btc_addresses']:
                st.markdown(f"- 🪙 `{btc}`")
        else:
            st.write("No BTC addresses found.")

        st.subheader("📝 Text Snippet")
        st.code(item['text_snippet'][:500], language='text')  # limit to 500 chars for clarity

st.markdown("---")
st.markdown("🔐 *Simulated dark web crawl for educational demonstration only. No real data is used.*")
