import requests
from pathlib import Path

pages = {
    "homepage": "https://sophilabs.com/",
    "services": "https://sophilabs.com/services",
    "case_studies": "https://sophilabs.com/work"
}

output_dir = Path("data/html")
output_dir.mkdir(parents=True, exist_ok=True)

for name, url in pages.items():
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()  # lanza error si no es 200
        (output_dir / f"{name}.html").write_text(resp.text, encoding="utf-8")
        print(f"Saved {name}.html")
    except Exception as e:
        print(f"Failed to fetch {url} -> {e}")
