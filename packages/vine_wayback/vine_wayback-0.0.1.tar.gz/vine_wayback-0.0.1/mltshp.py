import time
import vine_wayback

from pathlib import Path

for line in open('mltshp-vine-ids.csv'):
    vine_id = line.strip()
    url = f'https://vine.co/v/{vine_id}'

    output_dir = Path('mltshp-vines') / vine_id
    if output_dir.is_dir():
        continue

    vine_wayback.download(url, output_dir=f'mltshp-vines/{vine_id}')
    time.sleep(10)

