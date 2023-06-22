# -*- coding: utf-8 -*-
def split_dataset(input_file, train_file, eval_file, split_ratio=0.8):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    train_size = int(len(lines) * split_ratio)
    train_lines = lines[:train_size]
    eval_lines = lines[train_size:]

    with open(train_file, 'w', encoding='utf-8') as train:
        train.writelines(train_lines)

    with open(eval_file, 'w', encoding='utf-8') as eval:
        eval.writelines(eval_lines)

    print("划分结束！")


# 示例用法
input_file = './source.txt'
train_file = './data/source.txt'
eval_file = 'D:./data/source_eval.txt'

split_dataset(input_file, train_file, eval_file, split_ratio=0.8)

tgt_input_file = './target.txt'
tgt_train_file = './data/target.txt'
tgt_eval_file = './data/target_eval.txt'
split_dataset(tgt_input_file, tgt_train_file, tgt_eval_file, split_ratio=0.8)


