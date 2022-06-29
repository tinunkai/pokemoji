from lxml import etree
import requests


def main():
    for no in range(1, 387):
        for s in ("", "_s"):
            r = requests.get(
                f"https://wiki.52poke.com/wiki/File:Spr_3e_{no:03d}{s}.gif"
            )
            tree = etree.fromstring(r.content, parser=etree.HTMLParser())
            for e in tree.iter():
                if "href" in e.attrib:
                    if "//media" in e.attrib["href"]:
                        gif_url = e.attrib["href"]
                        r = requests.get(f"https:{gif_url}")
                        with open(f"./gifs/{no:03d}{'s' if s else ''}.gif", "wb") as f:
                            f.write(r.content)
                        break
            print(f"{no}{s}")


if __name__ == "__main__":
    main()
