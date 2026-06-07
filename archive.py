import requests
import time
import os

URLS = [
    "https://coles.com.au",
    "https://payorpissoff.com",
    "https://vic.gov.au",
    "https://kmart.com.au",
    "https://woolworths.com.au",
    "https://jims.net",
    "https://aldi.com.au",
    "https://nine.com.au",
    "https://9news.com.au",
    "https://7news.com.au",
    "https://10.com.au",
    "https://abc.net.au",
    "https://sbs.com.au",
    "https://freeview.com.au",
    "https://skynews.com.au",
    "https://news.com.au",
    "https://amnesty.org.au",
    "https://library.gov.au",
    "https://nla.gov.au",
    "https://onenation.org.au",
    "https://viclabor.org.au",
    "https://alp.org.au",
    "https://abs.gov.au",
    "https://liberal.org.au",
    "https://greens.org.au",
    "https://nationals.org.au",
    "https://australiasvoice.com.au",
    "https://premier.gov.au",
    "https://theaustralian.com.au",
    "https://afr.com",
    "https://3aw.com.au",
    "https://jmail.world"
]

ACCESS_KEY = os.getenv("IA_ACCESS_KEY")
SECRET_KEY = os.getenv("IA_SECRET_KEY")

for url in URLS:
    try:
        response = requests.post(
            "https://web.archive.org/save",
            data={"url": url},
            auth=(ACCESS_KEY, SECRET_KEY),
            timeout=60,
        )

        print(f"{url}: {response.status_code}")

    except Exception as e:
        print(f"{url}: ERROR {e}")

    time.sleep(15)