import cmu_graphics
from cmu_graphics import *
from random import randrange

# Variables
xPos = 160
yPos = 160
Index = 0
needleLength = 20
isFound = False

# Icons (80x80px)
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
sceneBackground = Image('imgAssets\1000x100Scene.png', 500, 500)

Image('imgAssets/treasureMenu.png', 0, 0)
compassNeedle = Line(36,33,55,33,arrowEnd = True, lineWidth = 0.5, fill='red')

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

def pointNeedle(treasureX, treasureY):
    angle = angleTo(36, 33, treasureX, treasureY)
    endX, endY = getPointInDir(36, 33, angle, needleLength)
    compassNeedle.x2 = endX
    compassNeedle.y2 = endY

# Game logic
pointNeedle(treasureChest.left, treasureChest.top)

def onStep():
    global xPos, yPos, isFound, treasureChest
    if isFound == True: #Need to spawn in treasure chest
        treasureChest.left = randrange(10, 390)
        treasureChest.top = randrange(10, 390)
        pointNeedle(treasureChest.left, treasureChest.top)
        isFound = False
    elif isFound == False:
        distanceToChest = distance(xPos+40, yPos+40, treasureChest.left+14.5, treasureChest.top+12) #29x24px
        if distanceToChest <= 75: #Found chest
            isFound = True

# Movement Logic
def onKeyHold(keys):
    global xPos, yPos, Index, leftFacing, rightFacing
    if ('w' in keys) or ('a' in keys) or ('s' in keys) or ('d' in keys):  
        pointNeedle(treasureChest.left, treasureChest.top)
        if 'w' in keys:
            if yPos > 0:
                yPos -= 10
                updateSprites(None)
            
        if 's' in keys:
            if yPos < 350:
                yPos += 10
                updateSprites(None)    
           
        if 'a' in keys:
            if xPos > 0:
                xPos -= 10     
                updateSprites(leftFacing)   
        
        if 'd' in keys:
            if xPos < 350:
                xPos += 10
                updateSprites(rightFacing)   

           
            
        Index = (Index + 1) % 4
        

def onKeyRelease(keys):
    global Index
    if ('w' in keys) or ('a' in keys) or ('s' in keys) or ('d' in keys): 
        Index = 0
        updateSprites(None)

cmu_graphics.run()
