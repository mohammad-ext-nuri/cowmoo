import os
from pathlib import Path

# sys.path.append(os.path.dirname(__file__))

def get_project_root() -> Path:
    return Path(__file__).parent.parent

ROOT_DIR = get_project_root()

TRAIN_DIR = os.path.join(ROOT_DIR, 'data/train')
TEST_DIR = os.path.join(ROOT_DIR, 'data/test')
INPUT_DIR = os.path.join(ROOT_DIR, 'data/input')
LOG_DIR = os.path.join(ROOT_DIR, 'logs')
MODEL_DIR = os.path.join(ROOT_DIR, 'model')
OUT_DIR = os.path.join(ROOT_DIR, 'output')
IMAGE_DIR = os.path.join(OUT_DIR, 'images')

path_config = {'train':TRAIN_DIR,
                'test':TEST_DIR,
                'input':INPUT_DIR,
                'log':LOG_DIR,
                'model':MODEL_DIR,
                'out':OUT_DIR,
                'image':IMAGE_DIR
                }

# LOG_CONFIG = os.path.join(ROOT_DIR, 'logging.yml')
# print(LOG_CONFIG)

# DATA_DIR = os.path.join(ROOT_DIR, 'data')
# DATA_DIR_AUDIO = os.path.join(DATA_DIR, 'audio')
# DATA_DIR_GUITAR = os.path.join(DATA_DIR_AUDIO, 'Guitar_Only/')
# DATA_DIR_AUGMENTED = os.path.join(DATA_DIR_AUDIO, 'augmented')

# METADATA_DIR = os.path.join(DATA_DIR, 'metadata')
# METADATA_DIR_RAW = os.path.join(METADATA_DIR, 'raw')
# METADATA_DIR_PROCESSED = os.path.join(METADATA_DIR, 'processed')

# METADATA_DIR_AUGMENTED = os.path.join(METADATA_DIR, 'augmented')
# METADATA_DIR_AUGMENTED_RAW = os.path.join(METADATA_DIR_AUGMENTED, 'raw')
# METADATA_DIR_AUGMENTED_PROCESSED = os.path.join(METADATA_DIR_AUGMENTED, 'processed')

# LOG_DIR = os.path.join(ROOT_DIR, 'logs')
# LOG_DIR_TRAINING = os.path.join(LOG_DIR, 'training')



# WAVE_OUTPUT_FILE = os.path.join(RECORDING_DIR, "recorded.wav")
# SPECTROGRAM_FILE = os.path.join(RECORDING_DIR, "spectrogram.png")

# # Features


# # Audio configurations
# INPUT_DEVICE = 0
# MAX_INPUT_CHANNELS = 1  # Max input channels
# DEFAULT_SAMPLE_RATE = 44100   # Default sample rate of microphone or recording device
# DURATION = 3   # 3 seconds
# CHUNK_SIZE = 1024