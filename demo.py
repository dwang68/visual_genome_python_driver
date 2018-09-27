import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from visual_genome import api as vg
from PIL import Image as PIL_Image
import requests

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO, BytesIO

ids = vg.get_image_ids_in_range(start_index=0, end_index=10)
image_id = ids[8]
print("We got an image with id: {0}".format(image_id))

image = vg.get_image_data(id=image_id)
print("The url of the image is: {0}".format(image.url))


regions = vg.get_region_descriptions_of_image(id=image_id)
print("The first region descriptions is: %s" % regions[0].phrase)
print("It is located in a bounding box specified by x:%d, y:%d, width:%d, height:%d" % (regions[0].x, regions[0].y, regions[0].width, regions[0].height))


fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)



def visualize_regions(image, regions):
    response = requests.get(image.url)
    strio = BytesIO(response.content)
    img = PIL_Image.open(strio)
    plt.imshow(img)
    ax = plt.gca()
    for region in regions:
        ax.add_patch(Rectangle((region.x, region.y),
                               region.width,
                               region.height,
                               fill=False,
                               edgecolor='red',
                               linewidth=3))
        ax.text(region.x, region.y, region.phrase, style='italic', bbox={'facecolor':'white', 'alpha':0.7, 'pad':10})
    fig = plt.gcf()
    plt.tick_params(labelbottom='off', labelleft='off')
    plt.show()


visualize_regions(image, regions[:3])