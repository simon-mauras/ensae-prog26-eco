import random
random.seed(42)

def fill(s):
  def rd(): return chr(ord("0") + random.randrange(10))
  return "".join(rd() if c == " " else c for c in s)

with open("small.txt", "w") as f:
  f.write(fill("""\
#####
#S G#
#####
"""))

with open("impossible.txt", "w") as f:
  f.write(fill("""\
#######
#S  # #
# ### #
# #  G#
#######
"""))

with open("medium.txt", "w") as f:
  f.write(fill("""\
###########
#S    #   #
### ##### #
#     #   #
# ### # ###
# #      G#
###########
"""))


with open("circles.txt", "w") as f:
  f.write(fill("""\
#####################
#        S          #
# ###################
# #               # #
# # ## ########## # #
# # #           # # #
# # # ######### # # #
# # # #       # # # #
# # # # # ### # # # #
# # # # #   # # # # #
# # # # # G # # # # #
# # # # #   # # # # #
# # # # ##### # # # #
# # # #       # # # #
# # # ####### # # # #
# # #           # # #
# # ############# # #
# #               # #
# ##### ########### #
#                   #
#####################
"""))

with open("empty.txt", "w") as f:
  f.write(fill("""\
#################################################
#                                               #
#                                               #
#     S                                         #
#                                               #
#                                               #
#                                               #
#                                               #
#                                               #
#                                               #
#                                               #
#                                               #
#                                               #
#                                               #
#                                      G        #
#                                               #
#                                               #
#                                               #
#################################################
"""))


def gen(R, C):
  group = dict()
  grid = [["#" for _ in range(C)] for _ in range(R)]
  for r in range(1, R-1, 2):
    for c in range(1, C-1, 2):
      grid[r][c] = " "
      group[(r,c)] = (r,c)
  grid[1][1] = "S"
  grid[R-2][C-2] = "G"
  
  edges = []
  for r in range(1, R-1, 2):
    for c in range(2, C-2, 2):
      edges.append((r,c))
  for r in range(2, R-2, 2):
    for c in range(1, C-1, 2):
      edges.append((r,c))
  random.shuffle(edges)
  
  def unionfind(x):
    if group[x] != x:
      group[x] = unionfind(group[x])
    return group[x]
    
  for (r,c) in edges:
    if r%2:
      a, b = (r,c-1), (r, c+1)
    else:
      a, b = (r-1,c), (r+1, c)
    a, b = unionfind(a), unionfind(b)
    if a != b:
      group[a] = b
      grid[r][c] = " "
  
  return "\n".join("".join(l) for l in grid)

with open("large.txt", "w") as f:
  f.write(fill(gen(19, 49)))
