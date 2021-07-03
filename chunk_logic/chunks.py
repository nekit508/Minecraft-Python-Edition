from chunk_logic.noise import NoiseGen
from chunk_logic.noise import generate as gen
import os

def init():
    print("[Initializing]")
    world = [[[[[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
    chunkData = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
    return world,chunkData

def giveChunk(x,y,z,world,data,curSaveName):
    print("[Giving chunk at x:{x} y:{y} z:{z}]".format(x=x,y=y,z=z),end="")
    if "{x}-{y}-{z}.mpes".format(x=x,y=y,z=z) in os.listdir("saves/{name}".format(name=curSaveName)):
        file = open("saves/{name}/{x}-{y}-{z}.mpes".format(x=x,y=y,z=z,name=curSaveName))
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

def changeShownToChunk(world,cx,cy,cz,data,name):
    mas = []
    if data[cx][cy][cz] == 0:
        world,data = giveChunk(cx,cy,cz,world,data,name)
    for x in range(16):
        for y in range(16):
            for z in range(16):
                if world[cx][cy][cz][x][y][z] != 0:
                    val = 0
                    for i in range(-1,2):
                        for v in range(-1,2):
                            for c in range(-1,2):
                                try:
                                    if world[cx][cy][cz][x+i][y+v][z+c] == 0:
                                        val += 1
                                except:
                                    pass
                    if val != 0:
                        mas.append((cx*16+x,cy*16+y,cz*16+z))
    return mas,world,data

def changeShown(world,data,name):
    mas = []
    for i in range(-1,2):
        for c in range(-1,2):
            for v in range(-1,2):
                m,world,data = changeShownToChunk(world,i,c,v,data,name)
                mas += m
    print(len(mas),16**3*3)
    return mas,world,data