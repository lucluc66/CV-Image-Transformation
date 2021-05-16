import sys
import numpy as np
from PIL import Image


if len(sys.argv) == 4:
    print(sys.argv[1] + int(sys.argv[2]) + sys.argv[3])

image = np.asarray(Image.open(sys.argv[1]).convert('L'))


draw.polygon([20, 20, 20, 140, 60, 60], None, 'white')

p = np.array([[20, 20, 1], [20, 140, 1], [60, 60, 1]])
b = np.array([[230, 130, 1], [350, 190, 1], [290, 110, 1]])
x = np.linalg.solve(p, b).transpose()

t = np.linalg.inv(x)

triangle = triangle.transform(triangle.size, Image.AFFINE, (t[0, 0], t[0, 1], t[0, 2],
                                                            t[1, 0], t[1, 1], t[1, 2]))
triangle.save('triangle2.png')
