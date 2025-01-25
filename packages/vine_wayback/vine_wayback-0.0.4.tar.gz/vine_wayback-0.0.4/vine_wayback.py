import argparse
import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from wayback import WaybackClient

wayback = WaybackClient()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "vine_url", help="A Vine URL, e.g. https://vine.co/v/iuKJ7JjF2Jt"
    )
    parser.add_argument("-q", "--quiet", help="Suppress output")
    parser.add_argument("-o", "--output", help="A directory to write the output files")
    args = parser.parse_args()

    download(args.vine_url, quiet=args.quiet, output_dir=args.output)


def download(vine_url: str, metadata=False, quiet=False, output_dir=None):
    m = re.match(r"https://vine.co/v/(.+)", vine_url)
    if not m:
        print(f"{vine_url} doesn't look like a Vine URL")
        return
    vine_id = m.group(1)

    v = vine(vine_url)
    if v is None and not quiet:
        print(f"The video for {vine_url} wasn't found in the Wayback Machine :(")
        return

    output_dir = Path(output_dir or vine_id)
    output_dir.mkdir(parents=True, exist_ok=True)

    v["id"] = vine_id

    video = v.pop("video_raw")
    video_path = output_dir / f"{vine_id}.mp4"
    open(video_path, "wb").write(video)

    json_path = output_dir / f"{vine_id}.json"
    json.dump(v, open(json_path, "w"), indent=2)

    html_path = output_dir / "index.html"
    write_html(html_path, v)

    if not quiet:
        print(f"💾 saved {vine_url} to {output_dir.absolute()}")


def vine(vine_url) -> dict:
    # go through each snapshot of the vine in the Wayback machine
    for vine_page in wayback.search(vine_url):
        resp = requests.get(vine_page.raw_url)
        if resp.status_code != 200:
            continue

        # extract the page metadata
        vine = get_metadata(resp.text)
        if vine is None:
            continue

        # look for the video url
        video_url = vine.get("twitter:player:stream")
        if not video_url:
            continue

        # look for a snapshot of the video in the Wayback Machine
        for video in wayback.search(video_url):
            resp = requests.get(video.raw_url)
            if resp.status_code == 200:
                vine["video_raw"] = resp.content
                break

        if "video_raw" in vine:
            vine["archive_url"] = vine_page.view_url
            return vine

    # if we made it here we weren't able to find the Vine :(
    return None


def get_metadata(html) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    metadata = {}
    for el in soup.select("head meta"):
        prop = el.attrs.get("property")
        content = el.attrs.get("content")
        if prop:
            metadata[prop] = content
    return metadata


def write_html(path, vine):
    html = f"""\
<!DOCTYPE html>
<html>
<head>
  <title>{vine["twitter:title"]}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    .vine {{
      max-width: 500;
      margin: 30 auto 30 auto;
      text-align: center;
    }}

    video {{
        width: 500px;
        height: 500px;
    }}

    .title {{
      font-size: larger;
      font-weight: bold;
    }}

    .provenance {{
      margin-top: 30px;
      font-style: italic;
      font-size: smaller;
    }}
  </style>
</head>
<body>
  <main class="vine">
    <video
      controls
      src="{vine['id']}.mp4" type="video/mp4"
      poster="{vine['id']}.jpg">
    </video>
    <p class="title">{vine['twitter:title']}</p>
    <p class="description">{vine['twitter:description']}</p>
    <p class="provenance">
        Originally published at:<br>
        <a href="https://vine.co/v/{vine['id']}">https://vine.co/v/{vine['id']}</a><br>
        <br>
        Archived at:<br>
        <a href="{vine['archive_url']}">{vine['archive_url']}</a>
    </p>
  </main>
</body>
</html>
"""
    open(path, "w").write(html)
