import numpy as np
#import Image
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
import numpy as np

plt.title("Sheep Image")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")

img=Image.open("P1060598.jpg")
image_data=np.asarray(img)

#for i in range(len(image_data)):
#    for j in range(len(image_data[0])):
#        print(image_data[i][j])

#img.show()
plt.imshow(img)
plt.show()
