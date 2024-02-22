from PIL import Image
technique_name = 'walk'
resolution = 16
frame = 1
im = Image.open(f'../Media/Video-{technique_name}-{resolution}/Image-{frame}.jpg')
im.show()