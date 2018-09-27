import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from visual_genome import api as vg
from PIL import Image as PIL_Image
import requests

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

ids = vg.get_image_ids_in_range(start_index=0, end_index=10)
image_id = ids[8]
print("We got an image with id: {0}".format(image_id))