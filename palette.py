import pygame, json, pyautogui, PIL, os, cv2, math, sys
import numpy as np

pygame.init()

colors = []

with open('colors.json', 'r') as file:
   data = json.load(file)

   for color in data['colors']:
       for value in color['N10']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['04']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['M3']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['C2']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['B34']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['N01']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['N21']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['N19']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['017']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['C14']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['040']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['M20']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['C18']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['048']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['M49']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['C50']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['N11']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['022']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['M16']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['C15']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['042']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['M24']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['C32']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['044']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['M43']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['C41']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['N09']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['030']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['M29']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['C28']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['R26']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['N05']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['012']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['M8']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['C6']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['N07']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['E60']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['E80']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['E100']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)
       for value in color['L46']:
           if value['enable'] == True:
                c = ((value['r'], value['g'], value['b']))
                colors.append(c)


print(colors)

files = os.listdir('InputPallete')
f = files[0]

image = pygame.image.load('InputPallete/' + f)
im = PIL.Image.open('InputPallete/' + f)
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



