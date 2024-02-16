# "${1}": path to the context file.
# "${2}": path to the testing file.
# "${3}": path to the output predictions.

# preprocess only modify train.json & valid.json one time
# python preprocess_data.py

python run_swag.py \
  --do_predict \
  --model_name_or_path ./ckpt/MC/bert_base/pytorch_model.bin \
  --config_name ./ckpt/MC/bert_base/config.json \
  --tokenizer_name bert-base-chinese \
  --output_dir ./predict/MC \
  --test_file "${2}" \
  --context_file "${1}"\
  --output_file relevant.json \
  --cache_dir ./cache/ \
  --pad_to_max_length \
  --max_seq_length 512

python run_qa.py \
  --do_predict \
  --model_name_or_path ./ckpt/QA/roberta/pytorch_model.bin \
  --config_name ./ckpt/QA/roberta/config.json \
  --tokenizer_name hfl/chinese-roberta-wwm-ext \
  --output_dir ./predict/QA/ \
  --test_file ./predict/MC/relevant.json \
  --context_file "${1}" \
  --pad_to_max_length \
  --max_seq_length 512 \
  --doc_stride 128 \
  --per_device_eval_batch_size 4

python toCSV.py --output_predictions "${3}"