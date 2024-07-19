import cmu_graphics
from cmu_graphics import *

# Variables
xPos = 0
yPos = 0
Index = 0

# Loading sprites
rightFacing = [
    Image('imgAssets/cycle1.png', xPos, yPos),
    Image('imgAssets/cycle2.png', xPos, yPos),
    Image('imgAssets/cycle3.png', xPos, yPos),
    Image('imgAssets/cycle4.png', xPos, yPos)
]
leftFacing = [
    Image('imgAssets/cycle1L.png', xPos, yPos),
    Image('imgAssets/cycle2L.png', xPos, yPos),
    Image('imgAssets/cycle3L.png', xPos, yPos),
    Image('imgAssets/cycle4L.png', xPos, yPos)
]

# Initialize visibility
for sprite in rightFacing[1:] + leftFacing:
    sprite.visible = False

selectedSprite = rightFacing
def updateSprites(sprite: list):
    global Index, selectedSprite    

    if sprite != None:
        if selectedSprite != sprite:
            for spriteElement in selectedSprite:
                spriteElement.visible = False

        selectedSprite = sprite

    for i, spriteElement in enumerate(selectedSprite):
        spriteElement.left = xPos
        spriteElement.top = yPos
        spriteElement.visible = (i == Index)
     
            
    

# Movement Logic
def onKeyHold(keys):
    global xPos, yPos, Index, leftFacing, rightFacing
    if ('w' in keys) or ('a' in keys) or ('s' in keys) or ('d' in keys): 
        if 'w' in keys:
            yPos -= 10
            updateSprites(None)
        if 's' in keys:
            yPos += 10
            updateSprites(None)
        if 'a' in keys:
            xPos -= 10     
            updateSprites(leftFacing)   
        if 'd' in keys:
            xPos += 10
            updateSprites(rightFacing)   

        Index = (Index + 1) % 4
        

def onKeyRelease(keys):
    global Index
    if ('w' in keys) or ('a' in keys) or ('s' in keys) or ('d' in keys): 
        Index = 0
        updateSprites(None)

cmu_graphics.run()
