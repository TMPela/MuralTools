import pygame, json, pyautogui, PIL, os, cv2, math, sys
import numpy as np

pygame.init()

colors = []

with open('Palette/colors.json', 'r') as file:
   data = json.load(file)

   for color in data['colors']:
       for value in color['N10']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['04']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['M3']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C2']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['B34']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['N01']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['N21']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['N19']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['017']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C14']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       #for value in color['040']:
           #c = ((value['r'], value['g'], value['b']))
           #colors.append(c)
       for value in color['M20']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C18']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       #for value in color['048']:
           #c = ((value['r'], value['g'], value['b']))
           #colors.append(c)
       for value in color['M49']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C50']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['N11']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['022']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['M16']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C15']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['042']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['M24']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C32']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['044']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['M43']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C41']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['N09']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['030']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['M29']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C28']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['R26']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['N05']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['012']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['M8']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C6']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['N07']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['E60']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['E80']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['E100']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['L46']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)

files = os.listdir('Palette/Input')
f = files[0]

image = pygame.image.load('Palette/Input/' + f)
im = PIL.Image.open('Palette/Input/' + f)
colorList = []
    
for y in range(image.get_height()):
    l = []
    for x in range(image.get_width()): 
        l.append(im.getpixel((x, y)))
    colorList.append(l)

img = np.zeros((image.get_height(), image.get_width(), 3), np.uint8)
newColorList = []

yCount = 0
for y in colorList:
    for color in colorList[yCount]:
        res = []
        for c in colors: 
            r = ((color[0] - c[0], color[1] - c[1], color[2] - c[2])) 
            r = (math.sqrt(r[0]**2), math.sqrt(r[1]**2), math.sqrt(r[2]**2)) 
            r = r[0] + r[1] + r[2]
            r = int(r)
            res.append(r)

        correct = min(res)
        index = res.index(correct)
        newColorList.append(colors[index])
    yCount += 1

count = 0
for x in range(image.get_height()):
    for y in range(image.get_width()):
        img[x,y] = (newColorList[count][2], newColorList[count][1], newColorList[count][0])
        count += 1

cv2.imshow('Img1', img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 



