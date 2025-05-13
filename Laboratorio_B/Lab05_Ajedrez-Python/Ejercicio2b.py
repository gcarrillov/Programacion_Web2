from interpreter import draw
from chessPictures import *
pic = knight
pic = pic.join(pic.negative())
pic = pic.up(pic.verticalMirror())
draw(pic)