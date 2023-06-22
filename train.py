import subprocess

args = [
    "onmt-main",
    "--config", "./config.yaml",
    "--auto_config",
    "--model_type", "Transformer",
    "train",
    "--with_eval"
]

# 运行OpenNMT-tf
command = " ".join(args)
subprocess.run(command, shell=True)
