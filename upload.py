import requests
import random
import time
import os

import keys


def main():
    names = list()
    with open("./names.tsv", "r") as f:
        for line in f.readlines():
            no, ch, ja, en = line.strip().split("\t")
            names.append((no, en, ja, ch))
    for name in sorted(os.listdir("./emojis")):
        no, _ = os.path.splitext(name)
        if no == "Egg":
            ja = ch = en = no
        else:
            _, en, ja, ch = names[int(no[:3]) - 1]
        fail = True
        while fail:
            r = requests.post(
                keys.url + "/emoji.remove",
                data={
                    "token": keys.token,
                    "name": f"pm-{no.lower()}-{ch}-{en}",
                },
                headers={
                    "Cookie": keys.cookie,
                },
            )
            if not (r.json()["ok"] or r.json()["error"] == "emoji_not_found"):
                print(f"retry rm {no} {ch}: {r.json()['error']}")
                continue
            with open(f"./emojis/{no}.png", "rb") as f:
                r = requests.post(
                    keys.url + "/emoji.add",
                    data={
                        "token": keys.token,
                        "name": f"pm-{no.lower()}-{ch}-{en}",
                        "mode": "data",
                    },
                    files={
                        "image": f,
                    },
                    headers={
                        "Cookie": keys.cookie,
                    },
                )
                print(no, f"pm-{no}-{ch}-{en}", r.json())
                if r.json()["ok"] or r.json()["error"] == "error_name_taken":
                    fail = False
                time.sleep(random.uniform(1, 2))


def gif():
    names = list()
    with open("./names.tsv", "r") as f:
        for line in f.readlines():
            no, ch, ja, en = line.strip().split("\t")
            names.append((no, en, ja, ch))
    for name in sorted(os.listdir("./gifs")):
        no, _ = os.path.splitext(name)
        _, en, ja, ch = names[int(no[:3]) - 1]
        if int(no[:3]) < 1:
            continue
        fail = True
        while fail:
            r = requests.post(
                keys.url + "/emoji.remove",
                data={
                    "token": keys.token,
                    "name": f"gif-{no.lower()}-{ch}",
                },
                headers={
                    "Cookie": keys.cookie,
                },
            )
            if not (r.json()["ok"] or r.json()["error"] == "emoji_not_found"):
                print(f"retry rm {no} {ch}: {r.json()['error']}")
                time.sleep(random.uniform(1, 2))
                continue
            with open(f"./gifs/{no}.gif", "rb") as f:
                r = requests.post(
                    keys.url + "/emoji.add",
                    data={
                        "token": keys.token,
                        "name": f"gif-{no.lower()}-{ch}",
                        "mode": "data",
                    },
                    files={
                        "image": f,
                    },
                    headers={
                        "Cookie": keys.cookie,
                    },
                )
                print(no, f"gif-{no}-{ch}", r.text)
                if r.json()["ok"] or r.json()["error"] == "error_name_taken":
                    fail = False
                elif r.json()["error"] == "resized_but_still_too_large":
                    raise Exception
                else:
                    time.sleep(random.uniform(1, 2))


def item():
    for file in sorted(os.listdir("./items")):
        name, _ = os.path.splitext(file)
        name = name.translate(
            str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)})
        ).lower().replace(" ", "")
        name = f"item-{name}"
        while True:
            r = requests.post(
                keys.url + "/emoji.remove",
                data={
                    "token": keys.token,
                    "name": name,
                },
                headers={
                    "Cookie": keys.cookie,
                },
            )
            if not (r.json()["ok"] or r.json()["error"] == "emoji_not_found"):
                print(f"retry {name}: {r.json()['error']}")
                time.sleep(random.uniform(1, 2))
                continue
            with open(f"./items/{file}", "rb") as f:
                r = requests.post(
                    keys.url + "/emoji.add",
                    data={
                        "token": keys.token,
                        "name": name,
                        "mode": "data",
                    },
                    files={
                        "image": f,
                    },
                    headers={
                        "Cookie": keys.cookie,
                    },
                )
                print(name)
                if r.json()["ok"] or r.json()["error"] == "error_name_taken":
                    break
                elif r.json()["error"] == "resized_but_still_too_large":
                    raise Exception
                else:
                    print(r.json()["error"])
                    time.sleep(random.uniform(1, 2))


if __name__ == "__main__":
    item()
