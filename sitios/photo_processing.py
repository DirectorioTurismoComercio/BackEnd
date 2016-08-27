from PIL import Image
import os
import imghdr
from django.conf import settings

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
		foo.save(photo_path+"/"+photo_filename,'JPEG',optimize=True,quality=quality)

	return photo_filename


def reduce_site_photos(dir,site_photos):
	for photo in site_photos:
		old_name = photo.URLfoto.name
		if photo.URLfoto.size > settings.MAX_TAMANO_IMAGEN_SIN_REDUCCION:
			photo.URLfoto.name = reduce_photo_size(dir,photo.URLfoto.name)
			if old_name != photo.URLfoto.name:
				os.remove(dir+"/"+old_name)
		photo.URLfoto.name = os.path.splitext(photo.URLfoto.name)[0]+'.jpg'
		photo.save()
		os.rename(dir+"/"+old_name, dir+"/"+photo.URLfoto.name)
