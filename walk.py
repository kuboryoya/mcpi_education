from mcpi.minecraft import Minecraft
from time import sleep

# プレイヤーが歩いた場所に花を植える

mc = Minecraft.create()

# ブロックの種類
grass = 2
flower = 38

# 0.1秒ごとの処理
while True:
  x, y, z = mc.player.getPos()
  block_beneath = mc.getBlock(x, y-1, z)  # block ID

  if block_beneath == grass:
    mc.setBlock(x, y, z, flower)
  else:
    mc.setBlock(x, y-1, z, grass)
  sleep(0.1)