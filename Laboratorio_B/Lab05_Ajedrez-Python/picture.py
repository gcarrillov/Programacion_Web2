from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = self.img[::-1]
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for value in self.img:
      #Aplicamos la función _invColor() en cada caracter de value
      aux = "".join(map(self._invColor, value))
      negative.append(aux)
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    join = list(map(lambda a, b: a + b, self.img, p.img))
    return Picture(join)

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p debajo de la figura actual """
    up = self.img + p.img
    return Picture(up)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobrepuesta
    a la figura actual"""
    under = []
    for i in range (len(self.img)):
      aux = list("".join(map(lambda a, b: a if a != ' ' else b, p.img[i], self.img[i])))
      under.append(aux)
    return Picture(under)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    hRepeat = []
    for value in self.img:
      aux = ""
      for i in range (n):
        aux += value
      hRepeat.append(aux)
    return Picture(hRepeat)

  def verticalRepeat(self, n):
    vRepeat = []
    for i in range (n):
      vRepeat += self.img
    return Picture(vRepeat)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotate = []
    for i in range (len(self.img)):
      aux = ""
      for j in range (len(self.img[i])):
        aux += self.img[-(j + 1)][i]
      rotate.append(aux)
    return Picture(rotate)

