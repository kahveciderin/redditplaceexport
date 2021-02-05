from PIL import Image
import cv2
import os
import numpy as np

video_name = 'video.mp4'
img = Image.new('RGB', (1000, 1000), color = 'white')

prefix = "frames/place_"
frcnt = 0

colors = [(0xff, 0xff, 0xff),
          (0xe4, 0xe4, 0xe4),
          (0x88, 0x88, 0x88),
          (0x22, 0x22, 0x22),
          (0xff, 0xa7, 0xd1),
          (0xe5, 0x00, 0x00),
          (0xe5, 0x95, 0x00),
          (0xa0, 0x6a, 0x42),
          (0xe5, 0xd9, 0x00),
          (0x94, 0xe0, 0x44),
          (0x02, 0xbe, 0x01),
          (0x00, 0xe5, 0xf0),
          (0x00, 0x83, 0xc7),
          (0x00, 0x00, 0xea),
          (0xe0, 0x4a, 0xff),
          (0x82, 0x00, 0x80)]

file = open('raw_sorted.dat', 'r')

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MP4V'), 60, (1000,1000))
while True:

    if frcnt % 1000 == 0:
        #img.save(prefix + str(frcnt).zfill(12) + ".png")
        video.write(np.array(img)[:, :, ::-1].copy())

    frcnt += 1

    line = file.readline()
 
    
    if not line:
        break
    line = line.strip()
    data = line.split()
    try:
        img.putpixel((int(data[1]) - 1, int(data[2]) - 1), colors[int(data[3])])
    except:
        pass
#img.save(prefix + str(frcnt).zfill(12) + ".png")
img.save(prefix + "final" + ".png")
video.write(np.array(img)[:, :, ::-1].copy())
file.close()