import cocos
import pyglet
from cocos.scene import Scene
from cocos.actions import *
from cocos.director import director
from pyglet.gl import *
from cocos.layer import Layer,ColorLayer
from cocos.sprite import Sprite
from pyglet.window import key
from cocos.scenes import *
import cocos.euclid as eu
import cocos.collision_model as cm

class DiningRoomSprite(cocos.sprite.Sprite):
    def __init__(self):
        super(DiningRoomSprite, self).__init__("Rooms/DiningRoom.png")
        self.position = 640, 400

class RedDoorSprite(cocos.layer.Layer):
    is_event_handler = True
    
    def __init__(self):
        super(RedDoorSprite, self).__init__()

        spr = cocos.sprite.Sprite("Doors/RedDoor.png")

        spr.position = 1170, 300
        spr.scale = 1
        
        spr.cshape = cm.AARectShape(spr.position, spr.width *0.5, spr.height * 0.5)
        self.add(spr, z = 10)
        
        
class PurpleDoorSprite(cocos.layer.Layer):
    def __init__(self):
            super(PurpleDoorSprite, self).__init__()

            spr3 = cocos.sprite.Sprite("Doors/PurpleDoor.png")

            spr3.position = 130 , 300
            spr3.scale = 1

            self.add(spr3, z = 10)

if __name__ == "__main__":
                director.init(width=1280, height = 920, caption="GetOut")
                director.window.pop_handlers()
                
                spr1_layer = DiningRoomSprite()
                spr2_layer = RedDoorSprite()
                spr3_layer = PurpleDoorSprite()


                test_scene = cocos.scene.Scene();
                test_scene.add(spr1_layer, z = 0) # background sprite
                test_scene.add(spr2_layer, z = 2)
                test_scene.add(spr3_layer, z = 2)

                director.run(test_scene)