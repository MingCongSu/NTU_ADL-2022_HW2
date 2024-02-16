import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--train_file", type=str, default="./data/train.json", help="A csv or a json file containing the training data."
    )
    parser.add_argument(
        "--validation_file", type=str, default="./data/valid.json", help="A csv or a json file containing the validation data."
    )
    args = parser.parse_args()
    return args
args = parse_args()

# modify the "start" to "answer_start"
with open(args.train_file, 'r', encoding="utf-8") as reader:
    data = json.load(reader)
    for i in range(len(data)):
        data[i]["answer"]["answer_start"] = data[i]["answer"]["start"]
        text = data[i]["answer"]["text"]
        data[i]["answer"].pop("start")
        data[i]["answer"].pop("text")
        data[i]["answer"]["text"] = text
    json.dump(data, open(args.train_file, "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)

with open(args.validation_file, 'r', encoding="utf-8") as reader:
    data = json.load(reader)
    for i in range(len(data)):
        data[i]["answer"]["answer_start"] = data[i]["answer"]["start"]
        text = data[i]["answer"]["text"]
        data[i]["answer"].pop("start")
        data[i]["answer"].pop("text")
        data[i]["answer"]["text"] = text
    json.dump(data, open(args.validation_file, "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
