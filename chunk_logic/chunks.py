from chunk_logic.noise import NoiseGen
from chunk_logic.noise import generate as gen
import os,pickle,math

def init():
    print("[Initializing]")
    world = [[[[[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
    chunkData = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
    return world,chunkData

def giveChunk(x,y,z,world,data,curSaveName):
    print("[Giving chunk at x:{x} y:{y} z:{z}]".format(x=x,y=y,z=z),end="")
    if "{x}-{y}-{z}.mpes".format(x=x,y=y,z=z) in os.listdir("saves/{name}".format(name=curSaveName)):
        file = open("saves/{name}/{x}-{y}-{z}.mpes".format(x=x,y=y,z=z,name=curSaveName),"rb")
        toLoad = file.read()
        world[x][y][z] = pickle.loads(toLoad)
    else:
        print(" generating")
        noise = NoiseGen(gen(16,16,"{x}-{z}".format(x=x,z=z)))
        for xx in range(16):
            for zz in range(16):
                h = noise.getHeight(xx,zz)
                if h <= y*16+16:
                    for yy in range(16-h,16):
                        world[x][y][z][xx][yy][zz] = 1
    data[x][y][z] = 1
    return world,data

def saveChunk(world,data,x,y,z,curSave):
    chunk = world[x][y][z]
    world[x][y][z] = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
    toSave = pickle.dumps(chunk)
    file = open("saves/{save}/{x}-{y}-{z}.mpes".format(save=curSave,x=x,y=y,z=z),"ab")
    file.write(toSave)
    file.close()

def changeShown(pos,world,data):
    for xz in range(-70,70):
        for xy in range(-70,70):
            for i in range(48):
                x = math.cos(xz)
                z = math.sin(xz)
                y = math.sin(xy)