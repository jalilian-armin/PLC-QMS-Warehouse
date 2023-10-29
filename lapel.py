import os
# from PIL import Image
import zpl
from zebra import Zebra


l = zpl.Label(25,60)
height = 0
l.origin(30,2)
l.write_text("Hyundai AC", char_height=3, char_width=3, line_width=30, justification='C')
l.endorigin()

l.origin(30,10)
l.write_text("1402/08/07 12:40", char_height=3, char_width=3, line_width=30, justification='C')
l.endorigin()

l.origin(30,20)
l.write_text("QC PASSED", char_height=3, char_width=3, line_width=30, justification='C')
l.endorigin()

# height += 13
# image_width = 5
# l.origin((l.width-image_width)/2, height)
# image_height = l.write_graphic(
#     Image.open(os.path.join(os.path.dirname(zpl.__file__), 'trollface-large.png')),
#     image_width)
# l.endorigin()
barcode= '14020807044822'
# height += image_height + 5
l.origin(5, 2)
l.barcode('2', str(barcode), height=150, check_digit='N')
l.endorigin()

# l.origin(32, height)
# l.barcode('Q', 'https://github.com/cod3monk/zpl/', magnification=10)
# l.endorigin()

# height += 20
# l.origin(0, height)
# l.write_text('Happy Troloween!', char_height=5, char_width=4, line_width=60,
#              justification='C')
# l.endorigin()

print(l.dumpZPL())
l.preview()
label = l.dumpZPL()


printer_name = "Adobe PDF"

# Create a Zebra object
z = Zebra(printer_name)
z.output(label)
print(z.getqueues())