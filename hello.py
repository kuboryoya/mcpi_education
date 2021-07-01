from mcpi import minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("localhost")
pos = mc.player.getPos()
basex = int(pos.x) + 0
basey = int(pos.y) + 6
basez = int(pos.z) + 0

data = [
  "#  # ### #   #    ##   #   #  ##  ###  #   ### ",
  "#  # #   #   #   #  #  # # # #  # #  # #   #  #",
  "#### ### #   #   #  #  # # # #  # ###  #   #  #",
  "#  # #   #   #   #  #  # # # #  # # #  #   #  #",
  "#  # ### ### ###  ##    # #   ##  #  # ### ### "
]

for y, line in enumerate(data):
  for x, c in enumerate(line):
    if c == "#":
      mc.setBlock(basex + x, basey - y, basez, block.AIR.id)