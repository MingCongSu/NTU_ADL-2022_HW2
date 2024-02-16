# Homework 2 ADL NTU
> This is a homework for Applied Deep Learning

## ***Environments***
----------------------------------------------------------------------------------------
pip install -r requirements.in


## ***Preprocess Data Format***
----------------------------------------------------------------------------------------
python preprocess_data.py --train_file /path/to/data/train.json --validation_file /path/to/data/valid.json

## ***Context Selection***
----------------------------------------------------------------------------------------
Train & Valid multiple-choice with 'bert-base-chinese':
python run_swag.py \
  --do_train \
  --do_eval \
  --model_name_or_path bert-base-chinese \
  --overwrite_output_dir True \
  --output_dir ./ckpt/MC/bert-base \
  --train_file ./data/train.json \
  --validation_file ./data/valid.json \
  --cache_dir ./cache/ \
  --pad_to_max_length \
  --learning_rate 3e-5 \
  --num_train_epochs 1 \
  --warmup_ratio 0.1

Test multiple-choice with 'bert-base-chinese':
python run_swag.py \
  --do_predict \
  --model_name_or_path ./ckpt/MC/bert-base/pytorch_model.bin \
  --config_name ./ckpt/MC/bert-base/config.json \
  --tokenizer_name ./ckpt/MC/bert-base \
  --output_dir ./predict/MC/bert_base \
  --test_file ./data/test.json \
  --output_file relevant.json \
  --cache_dir ./cache/ \
  --pad_to_max_length \
  --max_seq_length 512

----------------------------------------------------------------------------------------

## ***Question Answering***
----------------------------------------------------------------------------------------

Train & Valid question_answering with 'hfl/chinese-roberta-wwm-ext':
python run_qa.py \
  --do_train_and_valid \
  --model_name_or_path hfl/chinese-roberta-wwm-ext \
  --output_dir ./ckpt/QA/roberta \
  --train_file ./data/train.json \
  --validation_file ./data/valid.json \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 2 \
  --per_device_eval_batch_size 2 \
  --learning_rate 3e-5 \
  --num_train_epochs 1 \
  --max_seq_length 512 \
  --pad_to_max_length \
  --doc_stride 128

Test question-answering with 'hfl/chinese-roberta-wwm-ext':
python run_qa.py \
  --do_predict \
  --model_name_or_path ./ckpt/QA/roberta/pytorch_model.bin \
  --config_name ./ckpt/QA/roberta/config.json \
  --tokenizer_name ./ckpt/QA/roberta \
  --output_dir ./predict/QA/ \
  --test_file ./predict/MC/relevant.json \
  --context_file ./data/context.json \
  --cache_dir ./cache/ \
  --pad_to_max_length \
  --max_seq_length 512 \
  --doc_stride 128 \
  --per_device_eval_batch_size 4

----------------------------------------------------------------------------------------
## ***Postprocess Prediction***
----------------------------------------------------------------------------------------
  python toCSV.py --input_predictions /path/to/predict/QA/eval_predictions.json --output_predictions /path/to/pred/prediction.csv