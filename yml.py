import os

import yaml


def main():
    rst = {
        "title": "pokemoji",
        "emojis": list(),
    }
    names = list()
    with open("./names.tsv", "r") as f:
        for line in f.readlines():
            _, ch, ja, en = line.strip().split("\t")
            names.append((en, ja, ch))
    for name in sorted(os.listdir("./emojis")):
        no, _ = os.path.splitext(name)
        en, ja, ch = names[int(no) - 1]
        try:
            rst["emojis"].append(
                {
                    "name": f"pm{no}-{ch}-{ja}-{en}",
                    "src": f"https://raw.githubusercontent.com/tinunkai/pokemoji/main/emojis/{no}.png",
                }
            )
            print(no, ch, ja, en)
        except:
            print(f"error:{no}")
    with open("./pokemoji.yaml", "w") as f:
        yaml.dump(rst, f, allow_unicode=True)


if __name__ == "__main__":
    main()
