import warnings
import os
from argparse import ArgumentParser
from os import listdir
from os.path import isfile, join
from pathlib import Path
from typing import List, Union
from utils.config import path_config
from utils.files import load_sound_file
from utils.compute import load_audio, compute, compare, score, normalise_score




def main()->float:
    input_file_path = load_sound_file('input')
    input_file_path = input_file_path[0]
    raw_score = score(input_file_path, path_config['train_file_paths'])
    final_score = normalise_score(raw_score)
    print(f'Your hamba match is {final_score:.2%}')
    return final_score

if __name__ == '__main__':
    main()
