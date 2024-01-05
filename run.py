import json
import os
from dwpose import DwposeDetector
from PIL import Image

#if u need proxy
os.environ['http_proxy'] = "http://127.0.0.1:1080"
os.environ['https_proxy'] = "http://127.0.0.1:1080"

img = Image.open("test.jpg") #your image file

from dwpose import DwposeDetector
model = DwposeDetector.from_pretrained_default()
imgOut,j,source = model(img,
    include_hand=True,
    include_face=True,
    include_body=True,
    image_and_json=True,
    detect_resolution=512)

#openpose json
f = open("keypoints.json","w")
f.write(json.dumps(j))
f.close()

#openpose image
imgOut.save("openpose.jpg")

#detected resolution image
source.save("source.jpg")

del model
