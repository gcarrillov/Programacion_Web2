from interpreter import draw
from chessPictures import *
pic = square
pic = square.join(square.negative())
pic = pic.horizontalRepeat(4)
draw(pic)