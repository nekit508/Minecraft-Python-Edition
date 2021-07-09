import pyglet
from pyglet.gl import *


def getTex(file,p):
    tex = pyglet.image.load("assets/textures/blocks/{file}/{p}.png".format(file=file,p=p)).get_texture()
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    return pyglet.graphics.TextureGroup(tex)

def getTexGr(bl):
    side = getTex(bl,"side")
    bottom = getTex(bl, "bottom")
    top = getTex(bl, "top")
    gr = (side,bottom,top)
    return gr

def addBlock(x,y,z,batch,side,bottom,top):
    X, Y, Z = x+1, y+1, z+1

    tex_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))

    batch.add(4, GL_QUADS, side,   ('v3f', (X, y, z,  x, y, z,  x, Y, z,  X, Y, z)), tex_coords)
    batch.add(4, GL_QUADS, side,   ('v3f', (x, y, Z,  X, y, Z,  X, Y, Z,  x, Y, Z)), tex_coords)

    batch.add(4, GL_QUADS, side,   ('v3f', (x, y, z,  x, y, Z,  x, Y, Z,  x, Y, z)), tex_coords)
    batch.add(4, GL_QUADS, side,   ('v3f', (X, y, Z,  X, y, z,  X, Y, z,  X, Y, Z)), tex_coords)

    batch.add(4, GL_QUADS, bottom, ('v3f', (x, y, z,  X, y, z,  X, y, Z,  x, y, Z)), tex_coords)
    batch.add(4, GL_QUADS, top,    ('v3f', (x, Y, Z,  X, Y, Z,  X, Y, z,  x, Y, z)), tex_coords)
    return batch

def addBlocks(toDraw,batch,textures):
    for i in range(len(toDraw)):
        x,y,z,t = toDraw[i]
        side,bottom,top = textures[t]
        addBlock(x,y,z,batch,side,bottom,top)
    return batch