import requests
import random
import time

import keys


def main():
    names = list()
    with open("./names.tsv", "r") as f:
        for line in f.readlines():
            _, ch, ja, en = line.strip().split("\t")
            names.append((en, ja, ch))
    for idx, (en, ja, ch) in enumerate(names[:252]):
        r = requests.post(
            keys.url + "/emoji.remove",
            data={
                "token": keys.token,
                "name": f"pm-{idx+1:03d}-{ch}-{en}",
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": keys.cookie,
            },
        )
        print(idx + 1, r.json())
        time.sleep(random.uniform(1, 2))


if __name__ == "__main__":
    main()
