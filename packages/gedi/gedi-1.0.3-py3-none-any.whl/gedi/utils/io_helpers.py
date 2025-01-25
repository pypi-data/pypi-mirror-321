import glob
import json
import os
import pandas as pd
import re
import shutil
import numpy as np
from collections import defaultdict
from pathlib import PurePath
from scipy.spatial.distance import euclidean

def select_instance(source_dir, log_path, destination=os.path.join("output","generated","instance_selection")):
    os.makedirs(destination, exist_ok=True)
    try:
        source_path=glob.glob(os.path.join(source_dir, log_path))[0]
        destination_path = os.path.join(destination, "_".join(source_path.rsplit("/")[-2:]))
        shutil.copyfile(source_path, destination_path)
    except IndexError:
        print(f"ERROR: No files found for {source_dir}{log_path}. Continuing.")
    return destination, len(os.listdir(destination))

def read_csvs(input_path, ref_feature):
    f_dict = defaultdict(pd.DataFrame)
    ref_short_name = get_keys_abbreviation([ref_feature])
    for file in glob.glob(f'{input_path}*.csv'):
        if ref_short_name in file[:-4].split(os.sep)[-1].split("_"):
            c_file = pd.read_csv(file, delimiter=",")
            if c_file.columns[0] == 'task':
                c_file = c_file.reindex(columns=[c_file.columns[1], c_file.columns[2], c_file.columns[0]])
                c_file.rename(columns={"task":"log"}, inplace=True)
            f_dict[c_file.columns[0] if c_file.columns[0]!=ref_feature else c_file.columns[1]] = c_file
    return f_dict


def sort_files(data):
    """
    Returns a alphanumeric sortered list
    """
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
    return sorted(data, key=alphanum_key)

def get_keys_abbreviation(obj_keys):
    abbreviated_keys = []
    for obj_key in obj_keys:
        key_slices = obj_key.split("_")
        chars = []
        for key_slice in key_slices:
            for idx, single_char in enumerate(key_slice):
                if idx == 0 or single_char.isdigit():
                    chars.append(single_char)
        abbreviated_key = ''.join(chars)
        abbreviated_keys.append(abbreviated_key)
    return '_'.join(abbreviated_keys)

def get_output_key_value_location(obj, output_path, identifier, obj_keys=None):
    obj_sorted = dict(sorted(obj.items()))
    if obj_keys is None:
        obj_keys = [*obj_sorted.keys()]

    obj_values = [round(x, 4) for x in [*obj_sorted.values()]]

    if len(obj_keys) > 10:
        folder_path = os.path.join(output_path, f"{len(obj_keys)}_features")
        generated_file_name = f"{identifier}"
    else:
        folder_path = os.path.join(output_path, f"{len(obj_keys)}_{get_keys_abbreviation(obj_keys)}")
        obj_values_joined = '_'.join(map(str, obj_values)).replace('.', '')
        generated_file_name = f"{identifier}_{obj_values_joined}"


    os.makedirs(folder_path, exist_ok=True)
    save_path = os.path.join(folder_path, generated_file_name)
    return save_path

def dump_features_json(features: dict, output_path, content_type="features"):
    output_parts = PurePath(output_path.split(".xes")[0]).parts
    features_path = os.path.join(output_parts[0], content_type,
                                   *output_parts[1:])
    json_path = features_path+'.json'

    os.makedirs(os.path.split(json_path)[0], exist_ok=True)
    with open(json_path, 'w') as fp:
        json.dump(features, fp, default=int)
        print(f"SUCCESS: Saved {len(features)-1} {content_type} in {json_path}")#-1 because 'log' is not a feature

def compute_similarity(v1, v2):

    # Convert all values to float except for the value for the key "Log"
    v1 = {k: (float(v) if k != "log" else v) for k, v in v1.items()}
    v2 = {k: (float(v) if k != "log" else v) for k, v in v2.items()}

    # Filter out non-numeric values and ensure the same keys exist in both dictionaries
    common_keys = set(v1.keys()).intersection(set(v2.keys()))
    numeric_keys = [k for k in common_keys if isinstance(v1[k], (int, float)) and isinstance(v2[k], (int, float))]

    # Create vectors from the filtered keys
    vec1 = np.array([v1[k] for k in numeric_keys])
    vec2 = np.array([v2[k] for k in numeric_keys])

    if len(vec1) == 0 or len(vec2) == 0:
        print("[ERROR]: No common numeric keys found for (Edit) Distance calculation.")
        return None

    else:
        # Calculate Euclidean Similarity
        target_similarity = 1 / (1 + euclidean(vec1, vec2))
        # print("VECTORS: ", vec1, vec2, target_similarity)

        return target_similarity
