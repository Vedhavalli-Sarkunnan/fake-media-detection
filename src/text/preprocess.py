
import pandas as pd
import re

LABEL_MAP = {
    "true": 1,
    "mostly-true": 1,
    "half-true": 0,
    "barely-true": 0,
    "false": 0,
    "pants-fire": 0
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

