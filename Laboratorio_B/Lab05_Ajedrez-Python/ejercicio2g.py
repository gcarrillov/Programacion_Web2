from interpreter import draw
from chessPictures import *

upper = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
lower = pawn.horizontalRepeat(8)

board = square.join(square.negative())
board = board.horizontalRepeat(4)
board = board.up(board.negative())

pic = board.under(upper.negative().up(lower.negative()))\
    .up(board.verticalRepeat(2))\
    .up(board.under(lower.up(upper)))

draw(pic)