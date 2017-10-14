import ui
import io
from PIL import Image
import Image as img
import numpy as np
		
		
# pil <=> ui
def pil2ui(imgIn):
	with io.BytesIO() as bIO:
		imgIn.save(bIO, 'PNG')
		imgOut = ui.Image.from_data(bIO.getvalue())
	del bIO
	return imgOut
	

def plt2data(plt):
	plt.canvas.draw()
	w, h = plt.canvas.get_width_height()
	buf = np.fromstring(plt.canvas.tostring_argb(), dtype = np.uint8)
	buf.shape = (w, h, 4)
	buf = np.roll(buf, 3, axis = 2)
	return buf

def plt2img(plt):
	buf = plt2data(plt)
	w, h, d = buf.shape
	return img.frombytes('RGBA', (w,h), buf.tostring())
