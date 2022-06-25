import warnings
import os
from argparse import ArgumentParser
<<<<<<< Updated upstream
from os import listdir
from os.path import isfile, join
from pathlib import Path
from typing import List, Union
from utils.config import path_config
from utils.files import load_sound_file
from utils.compute import load_audio, compute, compare, score, normalise_score
=======
from utils.config import path_config
from utils.files import load_sound_file
from utils.compute import score, normalise_score
from utils.predict import predict_audio_class
>>>>>>> Stashed changes




def main()->float:
    input_file_path = load_sound_file('input')
    input_file_path = input_file_path[0]
<<<<<<< Updated upstream
    raw_score = score(input_file_path, path_config['train'])
=======

    raw_score = score(input_file_path, path_config['benchmark'])
>>>>>>> Stashed changes
    final_score = normalise_score(raw_score)
    print(f'Your hamba match is {final_score:.2%}')
    return final_score

if __name__ == '__main__':
    main()
