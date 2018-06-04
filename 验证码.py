from PIL import Image

im = Image.open("wm.gif")
his = im.histogram()
values = {}
for i in range(256):
    values[i] = his[i]
for j, k in sorted(values.items(), key=lambda x: x[i], reverse=True)[:10]:
    print j, k
