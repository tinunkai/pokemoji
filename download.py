from lxml import etree
import requests
import time


def main():
    for no in range(1, 387):
        for s in ("", "_s"):
            r = requests.get(
                f"https://bulbapedia.bulbagarden.net/wiki/File:Spr_3e_{no:03d}{s}.png"
            )
            tree = etree.fromstring(r.content, parser=etree.HTMLParser())
            for e in tree.iter():
                if "href" in e.attrib:
                    if (
                        e.attrib["href"].startswith("//archives")
                        and "media" in e.attrib["href"]
                    ):
                        img_url = e.attrib["href"]
                        print(img_url)
                        r = requests.get(f"https:{img_url}")
                        with open(
                            f"./origins/{no:03d}{'s' if s else ''}.png", "wb"
                        ) as f:
                            f.write(r.content)
                        break
            print(f"{no}{s}")


if __name__ == "__main__":
    main()
