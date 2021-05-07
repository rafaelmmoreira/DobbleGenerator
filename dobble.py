import os
import shutil
from PIL import Image, ImageDraw
import random
import math

def loadImages():
    images = []
    imageNames = os.listdir(os.path.abspath('img'))
    if len(imageNames) < 57:
        print('Error! Must have at least 57 images in img folder.')
        return None
    else:
        for i in imageNames:
            try:
                images.append(Image.open(os.path.join('img',i)))
            except: 
                print('Error! File', i, 'is not a valid image file.')
                return None
    return images

def getMaxDimensions(images):
    maxw = 0
    maxh = 0
    for i in images:
        if i.width > maxw:
            maxw = i.width
        if i.height > maxh:
            maxh = i.height
    return (maxw, maxh)

def drawCard(images, w, h):
    dim = int(math.sqrt(w**2+h**2))
    diameter = int(4.3*dim)
    # place images in 3 x 3 grid:
    card = Image.new('RGBA', (diameter, diameter))
    card.paste((255,255,255), (0,0, 3*dim, 3*dim))
    offset = (diameter-3*dim)//2
    # random rotations and offsets will make the cards look more dynamic and fun :)
    card.paste(images[0].rotate(random.randint(0, 360), expand=True), (offset, offset))
    card.paste(images[1].rotate(random.randint(0, 360), expand=True), (random.randint(5, offset+dim//4), offset+dim))
    card.paste(images[2].rotate(random.randint(0, 360), expand=True), (offset, offset+2*dim))
    card.paste(images[3].rotate(random.randint(0, 360), expand=True), (offset+dim, random.randint(5, offset)))
    card.paste(images[4].rotate(random.randint(0, 360), expand=True), (offset+dim, random.randint(offset+2*dim, diameter-dim-5)))
    card.paste(images[5].rotate(random.randint(0, 360), expand=True), (offset+2*dim, offset))
    card.paste(images[6].rotate(random.randint(0, 360), expand=True), (random.randint(offset+3*dim//2, diameter-dim-5), offset+dim))
    card.paste(images[7].rotate(random.randint(0, 360), expand=True), (offset+2*dim, offset+2*dim))
    # draw a circle
    draw = ImageDraw.Draw(card)
    draw.ellipse((0, 0, diameter, diameter), outline='black', width=5)
    # eliminating alpha channel problems
    result = Image.new('RGBA', (diameter,diameter), (255,255,255))
    result = Image.alpha_composite(result, card)
    return result


symbols = loadImages()
currentSymbol = 0
n = 7
maxw, maxh = getMaxDimensions(symbols)

grid = [[[] for y in range(n)] for x in range(n)]
convergences = [[] for x in range(n+1)]


# Horizontals
for i in range(n):
    for j in range(n):
        grid[i][j].append(symbols[currentSymbol])
    convergences[0].append(symbols[currentSymbol])
    currentSymbol += 1

# Verticals
for j in range(n):
    for i in range(n):
        grid[i][j].append(symbols[currentSymbol])
    convergences[1].append(symbols[currentSymbol])
    currentSymbol += 1

# diagonals
for step in range(1, n):
    for j in range(n):
        for i in range(n):
            grid[i][step*(i+j) % n].append(symbols[currentSymbol])
        convergences[step+1].append(symbols[currentSymbol])
        currentSymbol+=1

# final symbol linking "convergences":
for c in convergences:
    c.append(symbols[currentSymbol])

# draw and save every image:
try:
    path = 'cards'
    shutil.rmtree(path, ignore_errors=True)
    os.mkdir(path)
except OSError as e:
    path = os.getcwd()

idx = 1
for row in grid:
    for card in row:
        c = drawCard(card, maxw, maxh)
        c.save(os.path.join(path, 'card{:02d}.png'.format(idx)))
        idx+=1
for card in convergences:
    c = drawCard(card, maxw, maxh)
    c.save(os.path.join(path, 'card{:02d}.png'.format(idx)))
    idx+=1    

print('Cards generated sucessfully!')
