from chunk_logic.noise import NoiseGen
from chunk_logic.noise import generate as gen
import os

def init():
    world = [[[[[[[0]*16]*16]*16]*16]*16]*16]
    chunkData = [[[[0]*16]*16]*16]
    return world,chunkData

def giveChunk(x,y,z,world,chunkData,curSaveName):
    if "{x}-{y}-{z}.mpes".format(x=x,y=y,z=z) in os.listdir("saves/{name}".format(name=curSaveName)):
        pass
    else:
        noise = NoiseGen(gen(10,12))
        world