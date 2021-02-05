import time
import datetime


file1 = open('place_tiles', 'rb')
file2 = open('raw.dat', 'w')

file1.seek(-2, 2)

while 1:
    nextc = b''
    line = ""
    while nextc != b'\n':
        line = nextc.decode("utf-8") + line
        nextc = file1.read(1)
        file1.seek(-2, 1)
    spline = line.split()
    dtime = spline[0] + " " + spline[1]
    data = spline[2].split(',')
    if '.' in dtime:
        unixstamp = time.mktime(datetime.datetime.strptime(dtime, "%Y-%m-%d %H:%M:%S.%f").timetuple())
    else:
        unixstamp = time.mktime(datetime.datetime.strptime(dtime, "%Y-%m-%d %H:%M:%S").timetuple())
    formatted = str(int(unixstamp)) + " " + data[2] + " " + data[3] + " " + data[4] + "\n"
    file2.write(formatted)
    print(formatted)

file1.close()
file2.close()