import os, sys, huggingface_hub, datasets
print("python:", sys.executable)
print("HUGGINGFACE_HUB_DISABLE_SYMLINKS:", os.environ.get("HUGGINGFACE_HUB_DISABLE_SYMLINKS"))
print("HF_HUB_DISABLE_SYMLINKS:", os.environ.get("HF_HUB_DISABLE_SYMLINKS"))
print("HF_HOME:", os.environ.get("HF_HOME"))
print("huggingface_hub:", getattr(huggingface_hub, "__version__", "n/a"))
print("datasets:", getattr(datasets, "__version__", "n/a"))

from datasets import load_dataset
cuad = load_dataset("theatticusproject/cuad", split="train")
print(cuad)

