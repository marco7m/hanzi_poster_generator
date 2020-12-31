from PIL import Image, ImageDraw, ImageFont
import csv

with open('word_lists/word_list_by_frequency.csv', newline='') as f:
    reader = csv.reader(f)
    word_list = list(reader)
for i in range(len(word_list)):
    word_list[i] = word_list[i][0]

# size of the image
H_SIZE = 9*210
V_SIZE = 9*297

fnt = ImageFont.truetype('fonts/Hanzi-Pinyin-Font.top.ttf', 60)

img = Image.new('RGB', (H_SIZE, V_SIZE), color=(255, 255, 255))
d = ImageDraw.Draw(img)

H_SPACING = 60
V_SPACING = 70

L_MARGIN = 72
T_MARGIN = 70
R_MARGIN = 170
B_MARGIN = 170

spc_h = -H_SPACING
spc_v = 0
spc_page = 0

for i in range(len(word_list)):
    print(f"hanzi: {i} | page: {spc_page}")

    # if end of line and column, get new page
    if (spc_h + H_SPACING + R_MARGIN) > H_SIZE and (spc_v + V_SPACING + B_MARGIN) > V_SIZE:
        img.save('img/img_' + str(spc_page) + '.jpeg', format="JPEG")
        img = Image.new('RGB', (H_SIZE, V_SIZE), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        spc_page += 1
        spc_h = 0
        spc_v = 0

    # check if needs new line
    elif (spc_h + H_SPACING + R_MARGIN) > H_SIZE:
        spc_h = 0
        spc_v += V_SPACING

    else:
        spc_h += H_SPACING
    d.text((L_MARGIN+spc_h, T_MARGIN+spc_v), word_list[i], font=fnt, fill=(0, 0, 0))

img.save('img/img_' + str(spc_page) + '.jpeg', format="JPEG")
