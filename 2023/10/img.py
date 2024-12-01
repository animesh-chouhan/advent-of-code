import numpy as np
from PIL import Image

# Creates a random image 100*100 pixels
# mat = np.random.random((100, 100))
# print(mat)

path = [[255 for _ in range(100)] for _ in range(100)]
mat = np.array(path)
# print(mat)

# Creates PIL image
img = Image.fromarray(np.uint8(mat), "L")
img.show()
img.save("out.bmp")
