# Ore Detector with LEDBorg has been created by user astrotutor on http://www.minecraftforum.net/
# http://www.minecraftforum.net/forums/other-platforms/minecraft-pi-edition/1959958-ore-detector-with-ledborg
# i take no credit for creating this


import minecraft as minecraft
import block as block
import time as time
mc = minecraft.Minecraft.create()
time.sleep(5)
while True:
depth = 1
#Find block type below player
while depth < 100:
  # Find player position
  playerPos = mc.player.getPos()
 
  # Get block info at increasing levels below player
  block = mc.getBlock(playerPos.x, playerPos.y - depth, playerPos.z)
 
  if block == 16: #Coal
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('202') #Magenta
   del LedBorg
   time.sleep(2)
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('000')
   del LedBorg
  
  if block == 15: #Iron
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('020') #Green
   del LedBorg
   time.sleep(2)
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('000')
   del LedBorg
  if block == 14: #Gold
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('220') #Yellow
   del LedBorg
   time.sleep(2)
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('000')
   del LedBorg
  
  if block == 73: #Redstone
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('200') #Red
   del LedBorg
   time.sleep(2)
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('000')
   del LedBorg
  
  if block == 56: #Diamond
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('222') # White
   del LedBorg
   time.sleep(2)
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('000')
   del LedBorg
  
  if block == 21: #Lapis Lazuli
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('002') # Blue
   del LedBorg
   time.sleep(2)
   LedBorg = open('/dev/ledborg', 'w')
   LedBorg.write('000')
   del LedBorg
  
  depth += 1
