<div align="center">
    <img src="https://raw.githubusercontent.com/nicehero/DWPose/main/title.jpg"/>
</div>

<div align="center">
    
[![PyPI](https://img.shields.io/pypi/v/dwpose)](https://pypi.org/project/dwpose/)

</div>

# Easy DWPose Detector

Effective Whole-body Pose Estimation with Two-stages Distillation

[DWPose official](https://github.com/IDEA-Research/DWPose)



## Installation
```shell
#need install pytorch for your platform
#pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip3 install onnxruntime==1.13.1
pip3 onnxruntime_gpu==1.13.1
pip3 install matplotlib==3.6.2
pip3 install opencv_python==4.7.0.68
pip3 install scipy==1.11.4
pip3 install scikit_image==0.19.3
pip3 install huggingface_hub==0.20.1 
pip3 install dwpose
```
## Easy to use 
```python
import json
import os
from dwpose import DwposeDetector
from PIL import Image

#if u need proxy
#os.environ['http_proxy'] = "http://127.0.0.1:1080"
#os.environ['https_proxy'] = "http://127.0.0.1:1080"

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

```
## References
- [DWPose official](https://github.com/IDEA-Research/DWPose)
- [controlnet_aux](https://github.com/patrickvonplaten/controlnet_aux/)
- [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
