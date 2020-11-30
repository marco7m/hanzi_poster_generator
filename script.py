from PIL import Image, ImageDraw, ImageFont
import csv

with open('word_list.csv', newline='') as f:
    reader = csv.reader(f)
    word_list = list(reader)
for i in range(len(word_list)):
    word_list[i] = word_list[i][0]

H_SIZE = 9*210
V_SIZE = 9*297

fnt = ImageFont.truetype('Hanzi-Pinyin-Font.top.ttf', 96)

img = Image.new('RGB', (H_SIZE, V_SIZE), color = (255, 255, 255))
d = ImageDraw.Draw(img)

spc_h = -120
spc_v = 0
spc_page = 0
for i in range(len(word_list)):
    print(i)
    if (spc_h + 120 + 200)+50 > H_SIZE and (spc_v + 120 + 250)+50 > V_SIZE:
        img.save('img/img_' + str(spc_page) + '.jpeg',format="JPEG")
        img = Image.new('RGB', (H_SIZE, V_SIZE), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        print(" === page: ", spc_page)
        spc_page += 1
        spc_h = 0
        spc_v = 0

    elif (spc_h + 120 + 200)+50 > H_SIZE:
        spc_h = 0
        spc_v += 120
    else:
        spc_h += 120
    d.text((120+spc_h,120+spc_v), word_list[i], font=fnt, fill=(0, 0, 0))

print(" === page: ", spc_page)
img.save('img/img_' + str(spc_page) + '.jpeg',format="JPEG")
