from PIL import Image, ExifTags
import os
import imghdr
from django.conf import settings

def reduce_photo_size(photo_path, photo_filename,size):
	quality = settings.PORCENTAJE_CALIDAD_FOTOS
	max_width = settings.MAXIMO_ANCHO_FOTOS;
	max_height = settings.MAXIMO_ALTO_FOTOS;
	file = Image.open(photo_path+"/"+photo_filename)
	orientation = None

	if "exif" in photo_filename:
		string_array=photo_filename.split("_exif_orientation")
		orientation=int(string_array[1])
		photo_filename=string_array[0]

	file = rotate_image(file,orientation)
    
	file.save(photo_path+"/"+photo_filename,'JPEG',optimize=True,quality=100)
    
	if file.size[0]>max_width or file.size[1]>max_height:
		print("reducing max_width",file.size[0],file.size[1])
		print("settings max_width",max_width,max_height)
		if file.size[0]>file.size[1]:
			scale_factor = file.size[0]/max_width
		else: 
			scale_factor = file.size[1]/max_height

		new_width = int(round(file.size[0]/scale_factor))
		new_height = int(round(file.size[1]/scale_factor))
		file = file.resize((new_width,new_height),Image.ANTIALIAS)
		file.save(photo_path+"/"+photo_filename,'JPEG',optimize=True,quality=100)

	if os.path.getsize(photo_path+"/"+photo_filename) > settings.MAX_TAMANO_IMAGEN_SIN_REDUCCION:
		print "reducing size",os.path.getsize(photo_path+"/"+photo_filename)
		if imghdr.what(photo_path+"/"+photo_filename)=='png' or imghdr.what(photo_path+"/"+photo_filename).lower()=='gif':
			photo_filename = os.path.splitext(photo_filename)[0]+'.jpg'
			file.load() 
			background = Image.new("RGB", file.size, (255, 255, 255))
			background.paste(file, mask=file.split()[3]) 
			background.save(photo_path+"/"+photo_filename,'JPEG',optimize=True,quality=quality)

		if imghdr.what(photo_path+"/"+photo_filename).lower()=='jpg' or imghdr.what(photo_path+"/"+photo_filename).lower()=='jpeg':
			file.save(photo_path+"/"+photo_filename,'JPEG',optimize=True,quality=quality)
	

	return photo_filename


def reduce_site_photos(dir,site_photos):
	for photo in site_photos:
		print photo.URLfoto.name
		old_name = photo.URLfoto.name	
		photo.URLfoto.name = reduce_photo_size(dir,photo.URLfoto.name,photo.URLfoto.size)
		if old_name != photo.URLfoto.name:
			os.remove(dir+"/"+old_name)
		photo.URLfoto.name = os.path.splitext(photo.URLfoto.name)[0]+'.jpg'
		photo.save()
		if os.path.isfile(dir+"/"+old_name):
			os.rename(dir+"/"+old_name, dir+"/"+photo.URLfoto.name)


def rotate_image(image, orientation):

	try:
		if orientation is None:
		    for orientation in ExifTags.TAGS.keys():
		        if ExifTags.TAGS[orientation]=='Orientation':
		            break
		    exif=dict(image._getexif().items())
		    orientation=exif[orientation]

		if orientation == 3:
		    image=image.rotate(180, expand=True)
		elif orientation == 6:
		    image=image.rotate(270, expand=True)
		elif orientation == 8:
		    image=image.rotate(90, expand=True)

	except (AttributeError, KeyError, IndexError):
		print AttributeError, KeyError, IndexError
		pass
	return image


