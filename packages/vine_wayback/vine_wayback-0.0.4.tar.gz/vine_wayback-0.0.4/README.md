# vine_wayback

[![Tests](https://github.com/edsu/vine_wayback/actions/workflows/test.yml/badge.svg)](https://github.com/edsu/vine_wayback/actions/workflows/test.yml)

*vine_wayback* tries to retrieve a Vine video and its metadata from the Wayback Machine. If the Vine can be found in the Wayback Machine it will be written to disk as an MP4, JSON and standalone HTML file which you can use to view the Vine.

## Install

```shell
pip install vine_wayback
```

## Run

When you install *vine_wayback* you should get the `vine_wayback` command line utility installed as well:

```
vine_wayback https://vine.co/v/iuKJ7JjF2Jt
💾 saved https://vine.co/v/iuKJ7JjF2Jt to /Users/edsu/Projects/vine-wayback/iuKJ7JjF2Jt
```

This will create a directory like:

```
iuKJ7JjF2Jt
├── index.html
├── iuKJ7JjF2Jt.json
└── iuKJ7JjF2Jt.mp4
```

## Import

Maybe you want to make this part of a script that downloads a bunch of vines. You can use the `download()` function to download the Vine where you want to:

```python
import vine_wayback

vine_wayback.download("https://vine.co/v/iuKJ7JjF2Jt", output_dir="my/dir", quiet=True)
```

Or you can work with the metadata and video directly:

```python
import vine_wayback

vine = vine_wayback.vine("https://vine.co/v/iuKJ7JjF2Jt")

# print some of the metadata
print(vine['twitter:title'])

# save the video
open('media.mp4', 'wb').write(vine['video_raw'])
```
