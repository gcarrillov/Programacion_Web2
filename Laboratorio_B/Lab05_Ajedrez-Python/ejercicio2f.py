from interpreter import draw
from chessPictures import *
pic = square.join(square.negative())
pic = pic.horizontalRepeat(4)
pic = pic.up(pic.negative())
pic = pic.verticalRepeat(2)
draw(pic)