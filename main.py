from chunk_logic.chunks import *
from ursina import EditorCamera,Ursina,Entity

app = Ursina()

shown = []
world,chunkData = init()

shown,world,chunkData = changeShown(world,chunkData,"gg")

ents = []
for i in shown:
    x,y,z = i
    #print(world[0][0][0][i][z][c])
    ents.append(Entity(model="cube",position=(x/10,-y/10,z/10),scale=(0.1,0.1,0.1),texture="brick"))

ec = EditorCamera()
app.run()