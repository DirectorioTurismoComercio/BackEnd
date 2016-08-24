from PIL import Image
import os
import imghdr

def reduce_photo_size(photo_path, photo_filename):
	quality = 90
	file = Image.open(photo_path+"/"+photo_filename)
	if imghdr.what(photo_path+"/"+photo_filename)=='png' or imghdr.what(photo_path+"/"+photo_filename)=='gif':
		photo_filename = os.path.splitext(photo_filename)[0]+'.jpg'
		file.load() 
		background = Image.new("RGB", file.size, (255, 255, 255))
		background.paste(file, mask=file.split()[3]) 
		background.save(photo_path+"/"+photo_filename,'JPEG',optimize=True,quality=quality)

	if imghdr.what(photo_path+"/"+photo_filename)=='jpg':
		foo.save(file,'JPEG',optimize=True,quality=quality)

	return photo_filename

