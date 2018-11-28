import cocos
import pyglet
from cocos.actions import *
from cocos.director import director
from pyglet.gl import *
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from pyglet.window import key

# Scene Sequence so far:
#   Intro Scene
#   FloorPlan 
#   Room1       Living Room     (Red -> Dining Room,    Green -> BedRoom,       Blue-> itself)
#   Room2       Dining Room     (Red -> Living Room,    Green -> itself,        Blue-> Bedroom)
#   Room3       Bedroom         (Red-> itself,          Green -> Dining Room,   Blue-> Living Room)

class IntroSceneLayer(cocos.layer.Layer):
    
    is_event_handler = True
    space_counter = 1
    def __init__(self):
        
        super(IntroSceneLayer, self).__init__()

        spr = cocos.sprite.Sprite("logo.jpeg")

        spr.position = 640 , 400
        spr.scale = 1

        self.add(spr, z = 10)
                
        introtextLabel = cocos.text.Label(
                        "Press Space to start",  font_name= 'Times New Roman', font_size=32,
                        anchor_x = "center", anchor_y = "center")
        introtextLabel.position = 620, 60
        self.add(introtextLabel)
                
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            director.replace(Scene(FloorPlanLayer()))
                

class FloorPlanLayer(cocos.layer.Layer):
    is_event_handler = True
    
    def __init__(self):
        super(FloorPlanLayer, self).__init__()
        
        floorPlanSprite = cocos.sprite.Sprite("Rooms/FloorPlan.png")
        floorPlanSprite.scale = 1
        self.position = 640, 400
        self.add(floorPlanSprite)
        
        floorPlanTL = cocos.text.Label(
                        "There are 7 rooms in the House. Can you escape? Press Space to start",  font_name= 'Times New Roman', font_size=25,
                        anchor_x = "center", anchor_y = "bottom", color = (0,0,0,255))
        floorPlanTL.position = -100 , -305
        self.add(floorPlanTL, z = 2)
        
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            print("space was pressed in floor plan")
            director.replace(LivingRoomScene())
            
class LivingRoomScene(cocos.scene.Scene):
    def __init__(self, *args, **kwargs):
        super(LivingRoomScene, self).__init__()
        
        livingRoom_layer = LivingRoomLayer()
        redDoor_layer = RedDoorLR()
        greenDoor_layer = GreenDoorLR()
        blueDoor_layer = BlueDoorLR()

                        
        self.add(livingRoom_layer, z = 0)
        self.add(redDoor_layer, z = 2)
        self.add(greenDoor_layer, z = 2)
        self.add(blueDoor_layer, z = 2)
                
# Living room scene:
class LivingRoomLayer(cocos.layer.Layer):
    # is_event_handler = True
    
    def __init__(self):
        super(LivingRoomLayer, self).__init__()
        
        LRspr = cocos.sprite.Sprite("Rooms/LivingRoom.png")
        LRspr.scale = 1
        self.position = 640, 400
        self.add(LRspr, z = 0)
        
        
class RedDoorLR(cocos.layer.Layer):  # transitions to dining room
    is_event_handler = True
    
    def __init__(self):
        
            super(RedDoorLR, self).__init__()
            spr = cocos.sprite.Sprite("Doors/RedDoor.png")
            spr.position = 900 , 260
            spr.scale = 1
            self.add(spr, z = 10)
            
            self.spriteHeight = spr.height
            print("sprite height: ", self.spriteHeight) #356
            self.spriteWidth = spr.width
            print("sprite width: ", self.spriteWidth) #154
            
            
    def on_mouse_motion (self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed
         (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        print(x,y)
    def on_mouse_press(self, x, y, buttons, modifiers):
        
        # print("self.mouseX + self.spriteWidth: ", self.mouseX + self.spriteWidth)
        # print("self.mouseY + self.spriteHeight: ", self.mouseY + self.spriteHeight)
        self.mouseX,self.mouseY = director.get_virtual_coordinates(x, y)
        if(self.mouseX >= 400 and self.mouseX <= 490 
            and self.mouseY>=40 and self.mouseY <= 218):
            # director.replace(Scene(TransitionScene()))
            director.replace(DiningRoomScene())
            
# class TransitionScene(cocos.layer.Layer):
#     def __init__(self):
#         super(TransitionScene, self).__init__()
#         spr1 = cocos.sprite.Sprite("Rooms/Bedroom.png")
#         spr1.scale = 1
#         self.position = 640, 400
#         self.add(spr1)
        
class GreenDoorLR(cocos.layer.Layer): # transitions to bedroom 
    is_event_handler = True
    
    def __init__(self):
            super(GreenDoorLR, self).__init__()

            spr4 = cocos.sprite.Sprite("Doors/GreenDoor.png")

            spr4.position = 600 , 260
            spr4.scale = 1

            self.add(spr4, z = 10)
            
    def on_mouse_motion (self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed
         (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        print(x,y)
        
    def on_mouse_press(self, x, y, buttons, modifiers):
        # print("self.mouseX + self.spriteWidth: ", self.mouseX + self.spriteWidth)
        # print("self.mouseY + self.spriteHeight: ", self.mouseY + self.spriteHeight)
        self.mouseX,self.mouseY = director.get_virtual_coordinates(x, y)
        
        if(self.mouseX >= 260 and self.mouseX <= 340 
            and self.mouseY>=40 and self.mouseY <= 218):
            # director.replace(Scene(TransitionScene()))
            director.replace(BedRoomScene())


class BlueDoorLR(cocos.layer.Layer): # doesn't do anything. ie, transitions to the same room.
    def __init__(self):
            super(BlueDoorLR, self).__init__()

            spr8 = cocos.sprite.Sprite("Doors/BlueDoor.png")

            spr8.position = 300, 260

            spr8.scale = 1

            self.add(spr8, z = 10)
            
            
# Dining Room Scene
class DiningRoomScene(cocos.scene.Scene):
    def __init__(self, *args, **kwargs):
        super(DiningRoomScene, self).__init__()

        diningRoom_layer = DiningRoomLayer()
        redDoor_layer = RedDoorDR()
        greenDoor_layer = GreenDoorDR()
        blueDoor_layer = BlueDoorDR()


        self.add(diningRoom_layer, z = 0)
        self.add(redDoor_layer, z = 2)
        self.add(greenDoor_layer, z = 2)
        self.add(blueDoor_layer, z = 2)

class DiningRoomLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(DiningRoomLayer, self).__init__()

        spr = cocos.sprite.Sprite("Rooms/DiningRoom.png")
        spr.scale = 1
        self.position = 640, 400
        self.add(spr, z = 0)


class RedDoorDR(cocos.layer.Layer): #transitions back to living room
    is_event_handler = True

    def __init__(self):
            super(RedDoorDR, self).__init__()

            spr = cocos.sprite.Sprite("Doors/RedDoor.png")

            spr.position = 900 , 260
            spr.scale = 1

            self.add(spr, z = 10)

            self.spriteHeight = spr.height
            # print("sprite height: ", self.spriteHeight) #356
            self.spriteWidth = spr.width
            # print("sprite width: ", self.spriteWidth) #154

    def on_mouse_motion (self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed
        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        print(x,y)
        self.mouseX = x
        # print("mouseX: ", self.mouseX)
        self.mouseY = y
        # print("mouseY: ", self.mouseY)

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.position_x, self.position_y = director.get_virtual_coordinates(x, y)
        if(self.position_x >= 400 and self.position_x <= 490
            and self.position_y >= 40 and self.position_y <= 218):
           director.replace(LivingRoomScene()) 



class GreenDoorDR(cocos.layer.Layer): # transitions to itself. nothing happens on click
    def __init__(self):
            super(GreenDoorDR, self).__init__()

            spr4 = cocos.sprite.Sprite("Doors/GreenDoor.png")

            spr4.position = 600 , 260
            spr4.scale = 1

            self.add(spr4, z = 10)


class BlueDoorDR(cocos.layer.Layer): # transitions to bedroom
    is_event_handler = True
    def __init__(self):
            super(BlueDoorDR, self).__init__()

            spr8 = cocos.sprite.Sprite("Doors/BlueDoor.png")

            spr8.position = 300, 260

            spr8.scale = 1

            self.add(spr8, z = 10)
            
            
    def on_mouse_motion (self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed
        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        print(x,y)
        self.mouseX = x
        # print("mouseX: ", self.mouseX)
        self.mouseY = y
        # print("mouseY: ", self.mouseY)

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.position_x, self.position_y = director.get_virtual_coordinates(x, y)
        if(self.position_x >= 115 and self.position_x <= 185
            and self.position_y >= 45 and self.position_y <= 210):
           director.replace(BedRoomScene())
           
           
# Bedroom scene
class BedRoomScene(cocos.scene.Scene):
    def __init__(self, *args, **kwargs):
        super(BedRoomScene, self).__init__()

        bedRoom_layer = BedRoomLayer()
        redDoor_layer = RedDoorBR()
        greenDoor_layer = GreenDoorBR()
        blueDoor_layer = BlueDoorBR()


        self.add(bedRoom_layer, z = 0)
        self.add(redDoor_layer, z = 2)
        self.add(greenDoor_layer, z = 2)
        self.add(blueDoor_layer, z = 2)

class BedRoomLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(BedRoomLayer, self).__init__()

        spr = cocos.sprite.Sprite("Rooms/Bedroom.png")
        spr.scale = 1
        self.position = 640, 400
        self.add(spr, z = 0)


class RedDoorBR(cocos.layer.Layer): #transitions to itself. Nothing happens onClick
    def __init__(self):
            super(RedDoorBR, self).__init__()

            spr = cocos.sprite.Sprite("Doors/RedDoor.png")

            spr.position = 900 , 260
            spr.scale = 1

            self.add(spr, z = 10)

            self.spriteHeight = spr.height
            print("sprite height: ", self.spriteHeight) #356
            self.spriteWidth = spr.width
            print("sprite width: ", self.spriteWidth) #154



class GreenDoorBR(cocos.layer.Layer): # transitions to dining room
    is_event_handler = True
    def __init__(self):
            super(GreenDoorBR, self).__init__()

            spr4 = cocos.sprite.Sprite("Doors/GreenDoor.png")

            spr4.position = 600 , 260
            spr4.scale = 1

            self.add(spr4, z = 10)
            
    def on_mouse_motion (self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed
         (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        print(x,y)
        
    def on_mouse_press(self, x, y, buttons, modifiers):
        # print("self.mouseX + self.spriteWidth: ", self.mouseX + self.spriteWidth)
        # print("self.mouseY + self.spriteHeight: ", self.mouseY + self.spriteHeight)
        self.mouseX,self.mouseY = director.get_virtual_coordinates(x, y)
        
        if(self.mouseX >= 260 and self.mouseX <= 340 
            and self.mouseY>=40 and self.mouseY <= 218):
            # director.replace(Scene(TransitionScene()))
            director.replace(DiningRoomScene())


class BlueDoorBR(cocos.layer.Layer): #transitions to living room
    is_event_handler = True;
    def __init__(self):
            super(BlueDoorBR, self).__init__()

            spr8 = cocos.sprite.Sprite("Doors/BlueDoor.png")

            spr8.position = 300, 260

            spr8.scale = 1

            self.add(spr8, z = 10)
            
    def on_mouse_motion (self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed
        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        print(x,y)
        self.mouseX = x
        # print("mouseX: ", self.mouseX)
        self.mouseY = y
        # print("mouseY: ", self.mouseY)

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.position_x, self.position_y = director.get_virtual_coordinates(x, y)
        if(self.position_x >= 115 and self.position_x <= 185
            and self.position_y >= 45 and self.position_y <= 210):
           director.replace(LivingRoomScene())

 

if __name__ == "__main__":
                director.init(width=1280, height = 920, caption="my cocos window")
                director.window.pop_handlers()
                
                introSceneLayer = IntroSceneLayer()
                
                introScene = cocos.scene.Scene()
                introScene.add(introSceneLayer, z = 0)
                
                director.run(introScene)