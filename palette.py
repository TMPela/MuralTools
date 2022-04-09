import pygame, json, pyautogui, PIL, os, cv2, math, sys
import numpy as np

pygame.init()

colors = []

with open('colors.json', 'r') as file:
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
       for value in color['040']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['M20']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['C18']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
       for value in color['048']:
           c = ((value['r'], value['g'], value['b']))
           colors.append(c)
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

with open('available.json', 'r') as file:
   available = json.load(file)

   for codes in available['colors']: 
       if codes['N10'] != True:
            colors[0] = (1000, 1000, 1000)
       if codes['04'] != True:
            colors[1] = (1000, 1000, 1000)
       if codes['M3'] != True:
            colors[2] = (1000, 1000, 1000)
       if codes['C2'] != True:
            colors[3] = (1000, 1000, 1000)
       if codes['B34'] != True:
            colors[4] = (1000, 1000, 1000)
       if codes['N01'] != True:
            colors[5] = (1000, 1000, 1000)
       if codes['N21'] != True:
            colors[6] = (1000, 1000, 1000)
       if codes['N19'] != True:
            colors[7] = (1000, 1000, 1000)
       if codes['017'] != True:
            colors[8] = (1000, 1000, 1000)
       if codes['C14'] != True:
            colors[9] = (1000, 1000, 1000)
       if codes['040'] != True:
            colors[10] = (1000, 1000, 1000)
       if codes['M20'] != True:
            colors[11] = (1000, 1000, 1000)
       if codes['C18'] != True:
            colors[12] = (1000, 1000, 1000)
       if codes['048'] != True:
            colors[13] = (1000, 1000, 1000)
       if codes['M49'] != True:
            colors[14] = (1000, 1000, 1000)
       if codes['C50'] != True:
            colors[15] = (1000, 1000, 1000)
       if codes['N11'] != True:
            colors[16] = (1000, 1000, 1000)
       if codes['022'] != True:
            colors[17] = (1000, 1000, 1000)
       if codes['M16'] != True:
            colors[18] = (1000, 1000, 1000)
       if codes['C15'] != True:
            colors[19] = (1000, 1000, 1000)
       if codes['042'] != True:
            colors[20] = (1000, 1000, 1000)
       if codes['M24'] != True:
            colors[21] = (1000, 1000, 1000)
       if codes['C32'] != True:
            colors[22] = (1000, 1000, 1000)
       if codes['044'] != True:
            colors[23] = (1000, 1000, 1000)
       if codes['M43'] != True:
            colors[24] = (1000, 1000, 1000)
       if codes['C41'] != True:
            colors[25] = (1000, 1000, 1000)
       if codes['N09'] != True:
            colors[26] = (1000, 1000, 1000)
       if codes['030'] != True:
            colors[27] = (1000, 1000, 1000)
       if codes['M29'] != True:
            colors[28] = (1000, 1000, 1000)
       if codes['C28'] != True:
            colors[29] = (1000, 1000, 1000)
       if codes['R26'] != True:
            colors[30] = (1000, 1000, 1000)
       if codes['N05'] != True:
            colors[31] = (1000, 1000, 1000)
       if codes['012'] != True:
            colors[32] = (1000, 1000, 1000)
       if codes['M8'] != True:
            colors[33] = (1000, 1000, 1000)
       if codes['C6'] != True:
            colors[34] = (1000, 1000, 1000)
       if codes['N07'] != True:
            colors[35] = (1000, 1000, 1000)
       if codes['E60'] != True:
            colors[36] = (1000, 1000, 1000)
       if codes['E80'] != True:
            colors[37] = (1000, 1000, 1000)
       if codes['E100'] != True:
            colors[38] = (1000, 1000, 1000)
       if codes['L46'] != True:
            colors[39] = (1000, 1000, 1000)

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



