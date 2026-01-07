
import pandas as pd
import re

LABEL_MAP = {
    "true": 0,
    "mostly-true": 0,
    "half-true": 1,
    "barely-true": 1,
    "false": 1,
    "pants-fire": 1
}

def clean_text(text):
  text = text.lower()
  text = re.sub(r"\s+", " ", text)
  return text.strip()

def preprocess_liar_data(data):
  data = data[["label", "statement"]].copy()
  data["statement"] = data["statement"].apply(clean_text)
  data = data[data["statement"]!=""]
  data["label"] = data["label"].map(LABEL_MAP)
  data = data.dropna(subset=["label", "statement"])
  data["label"] = data["label"].astype(int)
  return data

