import orjson, pandas as pd
from datasets import Dataset

# Read as raw bytes
with open("data/CUADv1.json", "rb") as f:
    text = f.read()

# Parse safely
raw = orjson.loads(text)

# Access the main dataset
data = raw["data"]

records = []
for doc in data:
    title = doc["title"]
    for para in doc["paragraphs"]:
        context = para["context"]
        for qa in para["qas"]:
            records.append({
                "title": title,
                "context": context,
                "question": qa["question"],
                "answers": qa["answers"]
            })

df = pd.DataFrame(records)
cuad = Dataset.from_pandas(df)

print("Loaded successfully!")
print("Rows:", len(df))
print("Columns:", df.columns.tolist())
print(df.head(2))