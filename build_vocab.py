# -*- coding: utf-8 -*-
import subprocess

command = f"onmt-build-vocab --size 20000 --save_vocab D:/onmt/source_vocab.txt D:/onmt/source.txt"
subprocess.run(command, shell=True)
command = f"onmt-build-vocab --size 20000 --save_vocab D:/onmt/target_vocab.txt D:/onmt/target.txt"
subprocess.run(command, shell=True)


