import os

# cwd = os.getcwd()

# if not os.path.exists('model'):
#     os.mkdir('model')

# if not os.path.exists(f'{cwd}/result'):
#     os.mkdir(f'{cwd}/result')

# TRAIN_DATASET_PATH = f'{cwd}/dataset/train'
# VALID_DATASET_PATH = f'{cwd}/dataset/valid'
# TEST_DATASET_PATH = f'{cwd}/dataset/test'
# MODEL_PATH = f'{cwd}/model'

TRAIN_DATASET_PATH = f'/content/gdrive/MyDrive/dataset/train'
VALID_DATASET_PATH =  f'/content/gdrive/MyDrive/dataset/valid'
TEST_DATASET_PATH =  f'/content/gdrive/MyDrive/dataset/test'
MODEL_PATH = f'/content/tf-detection-training/model'

MODEL = 'efficientdet_lite0'
MODEL_NAME = 'car.tflite'
CLASSES = [
    'Front-Windscreen-Damage',  
    'Headlight-Damage', 
    'Major-Rear-Bumper-Dent', 
    'Rear-windscreen-Damage', 
    'RunningBoard-Dent', 
    'Sidemirror-Damage', 
    'Signlight-Damage', 
    'Taillight-Damage', 
    'bonnet-dent', 
    'boot-dent', 
    'doorouter-dent', 
    'fender-dent',
    'front-bumper-dent', 
    'medium-Bodypanel-Dent', 
    'pillar-dent', 
    'quaterpanel-dent', 
    'rear-bumper-dent', 
    'roof-dent',
]
EPOCHS = 100
BATCH_SIZE = 8

"""
CLASSES = [
    'Front-Windscreen-Damage',  
    'Headlight-Damage', 
    'Major-Rear-Bumper-Dent', 
    'Rear-windscreen-Damage', 
    'RunningBoard-Dent', 
    'Sidemirror-Damage', 
    'Signlight-Damage', 
    'Taillight-Damage', 
    'bonnet-dent', 
    'boot-dent', 
    'doorouter-dent', 
    'fender-dent',
    'front-bumper-dent', 
    'medium-Bodypanel-Dent', 
    'pillar-dent', 
    'quaterpanel-dent', 
    'rear-bumper-dent', 
    'roof-dent',
]
"""