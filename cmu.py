import cmu_graphics
from cmu_graphics import *
from random import randrange

# Variables
xPos = 0
yPos = 0
Index = 0
isFound = False

# Icons
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

treasureChest = Image('imgAssets/treasureChest.png', randrange(10, 390), randrange(10, 390))
Image('imgAssets/treasureMenu.png', 0, 0)

plrGold = Label(0, 115, 16, size=18, fill='white', bold=True, align='left')


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
     
# Game logic
def onStep():
    global xPos, yPos, isFound, treasureChest

    if isFound == True: #Need to spawn in treasure chest
        treasureChest.left = randrange(10, 390)
        treasureChest.top = randrange(10, 390)
        isFound = False
    elif isFound == False:
        distanceToChest = distance(xPos+40, yPos+40, treasureChest.left+14.5, treasureChest.top+12) #29x24px
        if distanceToChest <= 75: #Found chest
            isFound = True

# Movement Logic
def onKeyHold(keys):
    global xPos, yPos, Index, leftFacing, rightFacing
    if ('w' in keys) or ('a' in keys) or ('s' in keys) or ('d' in keys):  
        if yPos >= 0 and yPos < 400:     
            if 'w' in keys:
                yPos -= 10
                updateSprites(None)
            if 's' in keys:
                yPos += 10
                updateSprites(None)
        
        if xPos >= 0 and xPos < 400:
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
