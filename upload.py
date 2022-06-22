import requests
import random
import time

import keys


def main():
    names = list()
    with open("./names.tsv", "r") as f:
        for line in f.readlines():
            no, ch, ja, en = line.strip().split("\t")
            names.append((no, en, ja, ch))
    start = 865
    for no, en, ja, ch in names[start - 1 :]:
        fail = True
        while fail:
            with open(f"./emojis/{no}.png", "rb") as f:
                r = requests.post(
                    keys.url + "/emoji.add",
                    data={
                        "token": keys.token,
                        "name": f"pm-{no}-{ch}-{en}",
                        "mode": "data",
                    },
                    files={
                        "image": f,
                    },
                    headers={
                        "Cookie": keys.cookie,
                    },
                )
                print(no, ch, r.json())
                if r.json()["ok"] or r.json()["error"] == "error_name_taken":
                    fail = False
                time.sleep(random.uniform(1, 2))


if __name__ == "__main__":
    main()
