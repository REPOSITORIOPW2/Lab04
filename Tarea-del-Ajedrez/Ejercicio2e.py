from interpreter import draw
from chessPictures import *

unido = black_square.join(square)

for i in range(1,7):
    if i % 2 == 0:
        unido = unido.join(square)
    else:
        unido = unido.join(black_square)

draw(unido)
