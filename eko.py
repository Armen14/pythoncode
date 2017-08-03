#-*- coding: utf-8 -*-
#!/usr/bin/python

import matplotlib.pyplot as plt

xPointsAndLine = [0, 1, 2, 3, 4, 5, 6, 7]
yPointsAndLine = [0, -76394.63, -35038.41, 5815, 46081.8, 162356.9, 276620.8, 388244.9]
plt.plot(xPointsAndLine, yPointsAndLine, 'ro') #рисуются точки
plt.axis([0, 8, 0, 40])
plt.plot(xPointsAndLine, yPointsAndLine) # рисуется линия
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]) #линия оси x
val = 0
for i in yPointsAndLine:
    plt.annotate(str(i), xy=(val+0.2, i), xytext=(val+0.2, i))
    val += 1

plt.ylabel("NPV")
plt.ylim(-150000,500000)
plt.show()
