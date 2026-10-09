import json

file_path = "colab/Lab22_DPO_T4_Kaggle.ipynb"
with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

new_source = [
    "import zipfile\n",
    "import os\n",
    "import glob\n",
    "from IPython.display import FileLink, display\n",
    "\n",
    "zip_path = '/kaggle/working/submission.zip'\n",
    "dir_to_zip = '/kaggle/working/lab22'\n",
    "\n",
    "patterns_to_include = [\n",
    "    'submission/screenshots/*.png',\n",
    "    'data/eval/*',\n",
    "    'adapters/dpo/*.json',\n",
    "    'submission/REFLECTION.md'\n",
    "]\n",
    "\n",
    "print('Zipping necessary files into submission.zip...')\n",
    "with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:\n",
    "    for pattern in patterns_to_include:\n",
    "        full_pattern = os.path.join(dir_to_zip, pattern)\n",
    "        for file_path in glob.glob(full_pattern):\n",
    "            if os.path.isfile(file_path):\n",
    "                arcname = os.path.relpath(file_path, start=os.path.dirname(dir_to_zip))\n",
    "                zipf.write(file_path, arcname)\n",
    "                print(f'Added {arcname}')\n",
    "\n",
    "print('Zip complete. Starting download...')\n",
    "display(FileLink(zip_path))"
]

for cell in nb["cells"]:
    if "import zipfile\n" in cell.get("source", []):
        cell["source"] = new_source

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
