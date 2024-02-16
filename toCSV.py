import pandas as pd
import numpy as np
import argparse
import json
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_predictions", type=str, default="./predict/QA/eval_predictions.json", help="path to the input of predictions"
    )
    parser.add_argument(
        "--output_predictions", type=str, default=None, help="path to the output of predictions"
    )
    args = parser.parse_args()
    return args
args = parse_args()

with open(args.input_predictions, 'r', encoding="utf-8") as f:
    data = json.load(f)
    id = ['id']
    answer = ['answer']
    for i in data:
        id.append(i)
        answer.append(data[i])
    pred_id_answer = [id, answer]
    pred_id_answer = np.transpose(np.array(pred_id_answer))
if not os.path.isdir(os.path.split(args.output_predictions)[0]):
    os.mkdir(os.path.split(args.output_predictions)[0])
path = os.path.join(args.output_predictions)
pd.DataFrame(pred_id_answer).to_csv(
    path, header=None, index=None)
