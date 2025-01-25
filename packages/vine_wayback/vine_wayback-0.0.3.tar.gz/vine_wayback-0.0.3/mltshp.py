import time
import vine_wayback
import requests

from pathlib import Path

for line in open("mltshp-vine-ids.csv"):
    vine_id = line.strip()
    url = f"https://vine.co/v/{vine_id}"

    output_dir = Path("mltshp-vines") / vine_id
    if output_dir.is_dir():
        continue

    try:
        vine_wayback.download(url, output_dir=f"mltshp-vines/{vine_id}")
        time.sleep(20)
    except requests.exceptions.ConnectionError as e:
        print(e)
        time.sleep(20)
