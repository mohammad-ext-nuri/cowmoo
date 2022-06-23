
from pathlib import Path
from os import listdir
from os.path import isfile, join
from typing import List, Union

from config import path_config

def load_sound_file(file_type:str)->List[Union[str, Path]]:
    filelist = [join(path_config[file_type], f) for f in listdir(path_config[file_type]) if isfile(join(path_config[file_type], f))]
    return filelist



print('ok')
