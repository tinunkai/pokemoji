from pprint import pprint
import os

from PIL import Image
import numpy as np


def trim(cim):
    w, h = x1, y1 = cim.size
    x2, y2 = 0, 0
    nim = np.array(cim.copy().convert("RGBA"))
    for i in range(h):
        line = nim[i, :, :]
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
    return x1, y1, x2, y2


def main():
    for no in range(1, 387):
        no = f"{no:03d}"
        duration = list()
        for s in ("", "s"):
            gifs = list()
            ims = Image.open(f"./origins/{no}{s}.gif")
            x1, y1 = ims.size
            x2, y2 = 0, 0
            for idx in range(1, ims.n_frames):
                ims.seek(idx)
                cx1, cy1, cx2, cy2 = trim(ims)
                x1 = min(cx1, x1)
                y1 = min(cy1, y1)
                x2 = max(cx2, x2)
                y2 = max(cy2, y2)
            wc = x2 - x1
            hc = y2 - y1
            cc = max(x2 - x1 + 1, y2 - y1 + 1)
            x1 = (x1 + x2 + 1) // 2 - cc // 2
            y1 = (y1 + y2 + 1) // 2 - cc // 2
            for idx in range(1, ims.n_frames):
                if no == "249" and s and idx % 2 == 1:
                    continue
                ims.seek(idx)
                if ims.disposal_method == 1:
                    continue
                gifs.append(ims.crop((x1, y1, x1 + cc, y1 + cc)).resize((64, 64), 0))
                if s == "":
                    duration.append(ims.info["duration"] * 2)
            duration[-1] = 1000
            gifs[0].save(
                f"./gifs/{no}{s}.gif",
                save_all=True,
                append_images=gifs[1 : len(duration) - 1],
                loop=0,
                transparency=0,
                disposal=2,
                duration=duration,
                optimize=True,
            )
            print(f"{no+s:4s} {len(gifs)} {len(duration)}")


if __name__ == "__main__":
    main()
