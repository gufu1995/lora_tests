# -*- coding: utf-8 -*-
import replicate
# from replicate.client import Client
from PIL import Image
from matplotlib.pyplot import imshow
import numpy as np

MyReplicate = replicate.client.Client(api_token="r8_OpRPzGcQ1PyIrGdHFrLRIHtefVSt3ZG2kgqmC")

input = {
    "disable_safety_checker" : True,
    "prompt": "Kamala Harris and Donald Trump holding hands.",
    "output_format": "png",
    "height" : 1024,
    "width" : 1024,
}

output = MyReplicate.run(
    "black-forest-labs/flux-dev",
    input=input
)


import requests
r = requests.get( output[0] )
with open('pic.png','wb') as f:
  f.write(r.content)

# urlretrieve(output[0], "/tmp/out.png")
PILImage = Image.open("pic.png")

imshow( np.asarray( PILImage ) )

