import cssjson
from PIL import Image
import numpy as np

w, h = 68, 56


def main():
    css = cssjson.toJSON("./data.css", path=True)["rules"]
    im = Image.open("./msp.png")
    for name, attr in css.items():
        if not name.startswith(".sprite-icon"):
            continue
        attr = attr["attr"]
        if "background" in attr:
            continue
        no = name[13:16]
        if name[16:] or no == "Egg":
            continue
        x, y = map(int, attr["background-position"].replace("px", "").split(" "))
        cim = im.crop((-x, -y, -x + w, -y + h))
        cim = trim(cim).resize((128, 128), Image.NEAREST)
        cim.save(f"./emojis/{no}.png")
        print(no)


def trim(cim):
    nim = np.array(cim)
    x1 = w
    x2 = 0
    y1 = h
    y2 = 0
    for line in nim:
        ne = np.arange(w)[line[:, 3] != 0]
        if ne.size > 0:
            w1, w2 = ne[0], ne[-1]
            if w1 < x1:
                x1 = w1
            if w2 > x2:
                x2 = w2
    for j in range(w):
        line = nim[:, j, :]
        ne = np.arange(h)[line[:, 3] != 0]
        if ne.size > 0:
            h1, h2 = ne[0], ne[-1]
            if h1 < y1:
                y1 = h1
            if h2 > y2:
                y2 = h2
    wc = x2 - x1
    hc = y2 - y1
    cc = max(x2 - x1 + 1, y2 - y1 + 1)
    cim = cim.crop((x1, y1, x1 + cc, y1 + cc))
    return cim


if __name__ == "__main__":
    main()
