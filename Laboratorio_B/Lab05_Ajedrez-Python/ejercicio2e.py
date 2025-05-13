from interpreter import draw
from chessPictures import *
pic = square.negative()
pic = pic.join(square)
pic = pic.horizontalRepeat(4)
draw(pic)