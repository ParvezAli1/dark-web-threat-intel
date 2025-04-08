import requests
from bs4 import BeautifulSoup
import re
import json

# Proxy for TOR
TOR_PROXY = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Dark web URLs to crawl
urls = [
    "http://msydqstlz2kzerdg.onion",  # Ahmia Search Engine
    "http://torlinks6nlzoo7w.onion",  # TorLinks
    "http://libraryfy7bfwhut.onion"   # Imperial Library
]

# Function to fetch a webpage
def fetch(url):
    try:
        print(f"Trying to fetch: {url}")
        res = requests.get(url, proxies=TOR_PROXY, timeout=10)
        return res.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# Function to extract emails, BTC addresses, and a text snippet
def extract_info(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Extract all visible text
    text = soup.get_text(separator='\n', strip=True)

    # Extract emails and Bitcoin addresses
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    btc = re.findall(r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b', text)

    # Build a structured snippet
    snippet_lines = []
    snippet_lines.append("🔍 **Threat Intelligence Summary**")
    snippet_lines.append("")

    # Threat Actor Contacts
    threat_contacts = [email for email in emails if email.endswith('.onion')]
    if threat_contacts:
        snippet_lines.append("Possible threat actor contact addresses found:")
        for email in threat_contacts:
            snippet_lines.append(f"- `{email}`")
        snippet_lines.append("")

    # BTC Addresses
    if btc:
        snippet_lines.append("Bitcoin addresses likely used for donations or payments:")
        for address in btc[:3]:  # Show first 3
            snippet_lines.append(f"- `{address}`")
        snippet_lines.append("")

    if not threat_contacts and not btc:
        snippet_lines.append("No threat intelligence indicators found in the current document.")

    snippet = '\n'.join(snippet_lines)

    return {
        'emails': emails,
        'btc_addresses': btc,
        'text_snippet': snippet
    }



# Result list
results = []
tor_available = False

# Crawl each URL
for url in urls:
    html = fetch(url)
    if html:
        tor_available = True
        data = extract_info(html)
        data['source'] = url
        results.append(data)

# Use dummy data if Tor is not available
if not tor_available:
    print("Tor not available. Using simulated data for demonstration.")
    dummy_html = """
<html>
    <body>
        <h3>Contact our team:</h3>
        <ul>
            <li>admin@deepmail.onion</li>
            <li>contact@onionmail.org</li>
            <li>support@proton.onion</li>
            <li>exploit@torbox3uiot6wchz.onion</li>
        </ul>

        <h3>Leaked Emails from Dump:</h3>
        <p>
            Email: user01@example.com<br>
            Email: department.hr@corp-mail.org<br>
            Email: access.control@university.edu<br>
            Email: info.team@securebox.net<br>
            Email: sys.alert@internal.io<br>
        </p>

        <h3>Donate BTC:</h3>
        <ul>
            <li>1BoatSLRHtKNngkdXEeobR76b53LETtpyT</li>
            <li>3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy</li>
            <li>1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ</li>
        </ul>

        <p>
            This breach includes internal credentials, emails, and cryptocurrency donation links exposed on dark web forums.
        </p>
    </body>
</html>
"""
    data = extract_info(dummy_html)
    data['source'] = 'SIMULATED_ONION_SITE'
    results.append(data)

# Save results to output file
with open('output.json', 'w') as f:
    json.dump(results, f, indent=4)

print("Crawling complete. Results saved to output.json")
print(json.dumps(results, indent=4))