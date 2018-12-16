def pilot(w):
  moves = ""
  letters = []
  for l in w:
    letters.append(ord(l)-ord('a'))
  pos = [0,0]
  for el in letters:
    el_pos = [el%5,el//5]
    ver = el_pos[0] - pos[0]
    hor = el_pos[1] - pos[1]
    if ver > 0:
      moves+=ver*'R'
    elif ver < 0:
      moves += (-ver)*'L'
    if hor > 0:
      moves += hor*'D'
    elif hor < 0:
      moves += (-hor)*'U'
    moves += '!'
    pos = el_pos[:]

  return moves
