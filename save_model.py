# -*- coding: utf-8 -*-
import subprocess


args = [
    "onmt-main",
    "--config", "./config.yaml",
    "--auto_config",
    "export",
    "--output_dir", "./save_models",
    "--format", "ctranslate2"
]

# 运行OpenNMT-tf
command = " ".join(args)
subprocess.run(command, shell=True)
