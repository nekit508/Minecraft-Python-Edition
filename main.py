import pyglet
from pyglet.gl import*
from pyglet.window import key
from chunk_logic.chunks import *
from draw_logic.draw import *

class MainWindow(pyglet.window.Window):
    def getCurChunk(self):
        x,y,z = self.pos
        self.curChunk = (x//16,y//16,z/16)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.pos = (0,0,0)
        self.rot = (0,0)
        self.controlling = True
        self.pressedKeys = []
        self.world = pyglet.graphics.Batch()
        self.chunks,self.chunksData = init()
        self.curSave = "gg"
        self.textures = [[],getTexGr("hren")]
        self.changeBatch()
        self.setLoc()
        self.curChunk = (0,0,0)
        self.getCurChunk()
        glClearColor(0.7,0.7,1,1)
        pyglet.clock.schedule(self.update)

    def lockRotate(self,dx,dy):
        rot = list(self.rot)
        rot[0] += -dx
        rot[1] += dy
        if rot[1] > 90:rot[1] = 90
        if rot[1] < -90:rot[1] = -90
        self.rot = tuple(rot)

    def move(self):
        for symbol in self.pressedKeys:
            if symbol == key.SPACE:
                pos = list(self.pos)
                pos[1] += 1
                self.pos = tuple(pos)
            elif symbol == key.LSHIFT:
                pos = list(self.pos)
                pos[1] -= 1
                self.pos = tuple(pos)
        x,y,z = self.pos
        if (x//16,y//16,z//16) != self.curChunk:
            px,py,pz = self.curChunk
            dx = x - px
            dy = y - py
            dz = z - pz
            self.chunksData = self.chunksData
            self.changeBatch()

    def on_mouse_motion(self,x,y,dx,dy):
        if self.controlling == True:
            self.lockRotate(dx,dy)

    def on_key_press(self,symbol,modifiers):
        if symbol == key.E:
            self.controlling = not self.controlling
        elif self.controlling:
            self.pressedKeys.append(symbol)

    def on_key_release(self,symbol,modifiers):
        if self.controlling:
            if symbol in self.pressedKeys:self.pressedKeys.remove(symbol)

    def changeBatch(self):
        self.world = pyglet.graphics.Batch()
        toDraw,self.chunks,self.chunksData = changeShown(self.chunks,self.chunksData,self.curSave,self.pos)
        self.world = addBlocks(toDraw,self.world,self.textures)

    def setLoc(self):
        glPushMatrix()
        glRotatef(-self.rot[1],1,0,0)
        glRotatef(-self.rot[0],0,1,0)
        glTranslatef(-self.pos[0],-self.pos[1],-self.pos[2])

    def projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def set3d(self):
        self.projection()
        gluPerspective(70, self.width / self.height, 0.05, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def update(self,dt):
        self.getCurChunk()
        self.move()

    def on_draw(self):
        self.set_exclusive_mouse(self.controlling)
        self.clear()
        self.set3d()
        self.setLoc()
        self.world.draw()
        glPopMatrix()

win = MainWindow(width=800,height=500,caption="MineHren")
glEnable(GL_DEPTH_TEST)
pyglet.app.run()