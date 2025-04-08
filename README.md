# 🕵️ Dark Web Threat Intelligence Dashboard

This project is a simple but powerful dark web crawler that gathers potentially sensitive threat intelligence data like **leaked emails**, **Bitcoin addresses**, and **text snippets** from `.onion` websites on the dark web.

---

## 🚀 Features
- Crawls dark web `.onion` links over the Tor network
- Extracts:
  - Leaked **email addresses**
  - Potential **Bitcoin addresses**
  - Relevant **text snippets** (e.g., data dumps, breach details)
- Presents results in a beautiful, interactive **Streamlit dashboard**

---

## 💡 Problem It Solves
Traditional search engines can't reach the dark web, and analyzing `.onion` sites is a manual, risky task. This project automates:

- **Crawling** .onion links
- **Scraping** useful threat data
- **Visualizing** the findings securely

This makes it useful for **cybersecurity teams, SOCs, threat analysts**, and **researchers**.

---

## 🚧 Tech Stack
- Python 3
- [Streamlit](https://streamlit.io/) - for dashboard UI
- BeautifulSoup - HTML parsing
- requests + Tor proxy - for anonymous `.onion` crawling

---

## 📊 How It Works
1. `tor_crawler.py` crawls dummy/dark web pages via Tor and extracts emails, BTC addresses, and text.
2. Stores the results in `output.json`
3. `app.py` reads the data and displays it in a rich Streamlit dashboard

---

## 💼 How to Run
### 1. Start Tor locally
Make sure you have **Tor** running on port `9050`. You can use Tor Browser or the Tor service.

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the crawler
```bash
python tor_crawler.py
```

### 4. Launch the dashboard
```bash
streamlit run app.py
```

---

## 🏑 Example Output
```json
[
  {
    "source": "http://testleak.onion",
    "emails": ["leakeduser1@example.com"],
    "btc_addresses": ["1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"],
    "text_snippet": "This dump contains emails and BTC addresses..."
  }
]
```

---

## 🌟 Author
**Parvez Ali**  
GitHub: [ParvezAli1](https://github.com/ParvezAli1)

---

## ✉️ Disclaimer
This tool is for **educational and ethical research** purposes only. Accessing the dark web must comply with local laws and regulations.

---

## 📁 License
[MIT License](LICENSE)

## 📁 Project Structure
## 📁 Project Structure

```
dark_web_project/
│
├── app.py               # Streamlit dashboard
├── tor_crawler.py       # Crawler logic to extract emails & BTC addresses
├── output.json          # Extracted data from crawler (optional or .gitignored)
├── requirements.txt     # Python dependencies (Streamlit, requests, etc.)
├── README.md            # Full project documentation
├── .gitignore           # Files/folders to exclude from Git
├── LICENSE              # Optional open-source license file
```




