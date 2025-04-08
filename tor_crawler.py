import requests
from bs4 import BeautifulSoup
import re
import json

TOR_PROXY = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Add test .onion links (use dummy ones for now)
urls = [
    "http://dummyonionlink.onion"
]

def fetch(url):
    try:
        res = requests.get(url, proxies=TOR_PROXY, timeout=10)
        return res.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    btc = re.findall(r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b', text)
    return {
        'emails': emails,
        'btc_addresses': btc,
        'text_snippet': text[:500]
    }

results = []
for url in urls:
    html = fetch(url)
    if html:
        data = extract_info(html)
        data['source'] = url
        results.append(data)

with open('output.json', 'w') as f:
    json.dump(results, f, indent=4)

print("Crawling complete. Results saved to output.json")
