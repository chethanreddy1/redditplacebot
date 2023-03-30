import json
import os
import pandas as pd
from PIL import Image, UnidentifiedImageError


def get_json_data(self, config_path):
    configFilePath = os.path.join(os.getcwd(), config_path)

    if not os.path.exists(configFilePath):
        exit("No config.json file found. Read the README")

    # To not keep file open whole execution time
    f = open(configFilePath)
    json_data = json.load(f)
    f.close()
    workersdata=pd.read_csv('E:\\reddit-place-script-2022-main\\reddit-place-script-2022-main\\workers.csv')
    
    wdict={}
    for i in range(len(workersdata)):
        wdict[workersdata['username'][i]]={"password":workersdata['password'][i],"start_coords": [workersdata['start_cords_x'][i], workersdata['start_cords_y'][i]]}

    json_data['workers']=wdict
    
    return json_data

    # Read the input image.jpg file


def load_image(self):
    # Read and load the image to draw and get its dimensions
    try:
        im = Image.open(self.image_path)
    except FileNotFoundError:
        self.logger.exception("Failed to load image")
        exit()
    except UnidentifiedImageError:
        self.logger.exception("File found, but couldn't identify image format")

    # Convert all images to RGBA - Transparency should only be supported with PNG
    if im.mode != "RGBA":
        im = im.convert("RGBA")
        self.logger.info("Converted to rgba")
    self.pix = im.load()

    self.logger.info("Loaded image size: {}", im.size)

    self.image_size = im.size


