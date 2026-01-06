
import pandas as pd
import os
import csv

EXPECTED_COL_COUNT = 14
LIAR_COLUMNS = [
    "id",
    "label",
    "statement",
    "subjects",
    "speaker",
    "speaker_job",
    "state",
    "party",
    "barely_true",
    "false",
    "half_true",
    "mostly_true",
    "pants_on_fire",
    "context"
]

def load_data(path, sep=None):
  if not sep:
    ext = os.path.splitext(path)[1].lower()
    if ext == ".tsv":
      sep_to_use = "\t"
    elif ext == ".csv":
      sep_to_use = ","
    else:
      sep_to_use = "," #default separator in case of ambuiguity
  else:
    sep_to_use = sep
  data = pd.read_csv(path, sep=sep_to_use, header=None, engine='python', on_bad_lines='warn')
  return data

def load_liar_data(path):
  valid_records = []
  bad_records = []
  with open(path, encoding="utf-8", errors="replace") as file:
    reader = csv.reader(file, delimiter="\t")
    for idx, row in enumerate(reader):
      if len(row) == EXPECTED_COL_COUNT:
        valid_records.append(row)
      else:
        bad_records.append(row)
  data = pd.DataFrame(valid_records)
  return data, bad_records

