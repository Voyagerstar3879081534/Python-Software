import time
from mpython import *


oled.DispChar("        |\\         /|-------", 0, (1-1)*16, 1)
oled.DispChar("        |   \\   /   |          |", 0, (2-1)*16, 1)
oled.DispChar("        |     ||     |-------", 0, (3-1)*16, 1)
oled.DispChar("        |     ||     |", 0, (4-1)*16, 1)
oled.show()
time.sleep(1)
oled.fill(0)
oled.show()
oled.DispChar("         MicroPython", 0, (1-1)*16, 1)
oled.DispChar("      Operation System", 0, (2-1)*16, 1)
oled.DispChar("           Copyright", 0, (3-1)*16, 1)
oled.DispChar("    Danhuangsu Studio", 0, (4-1)*16, 1)
oled.show()
time.sleep(1)
oled.fill(0)
oled.show()
oled.DispChar("Choose Language:", 0, (1-1)*16, 1)
oled.DispChar("A:Chinese  B:English", 0, (1-1)*16, 1)
oled.show()
while not ((button_a.value() == 0 or button_b.value() == 0)):
  pass
if button_a.value() == 0:
  language = (str("cn"))
else:
  language = (str("en"))
oled.fill(0)
oled.show()
if (language == (str("en"))):
  oled.DispChar("Welcome", 0, 0, 1)
else:
  oled.DispChar("欢迎", 0, 0, 1)
oled.show()
oled.fill(0)
oled.show()
