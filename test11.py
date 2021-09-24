from PIL import Image

img = Image.open('12.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img = Image.fromarray(newData.astype('uint8'), 'RGB')
img.save("img2.png", "PNG")
img.show()