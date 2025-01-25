import vine_wayback
import hashlib


def test_vine():
    vine = vine_wayback.vine("https://vine.co/v/iuKJ7JjF2Jt")
    assert vine["twitter:title"] == "i'm a loser"
    assert (
        vine["twitter:player:stream"]
        == "https://mtc.cdn.vine.co/r/videos_h264high/B1804A5DF51278582807920832512_3e1d614c73a.0.1.15942997023875548236.mp4?versionId=lM.gFKaPRWorQa9dRZKX1oNhRqZOymhS"
    )
    assert (
        hashlib.md5(vine["video_raw"]).hexdigest() == "96be7068ce10dd0d8eb4e0ad13fd4631"
    )
