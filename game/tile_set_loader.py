import pyglet
import os

base_path = os.path.dirname(__file__)

TILE_SIZE = 16
# Contents of the tile set are 15 x 15
SPRITE_COUNT = 15

KEY_COLOR = 255, 0, 255, 255

def chunker(data, length):
	# The length of a format string always returns the number of bytes per pixel
	# eg. the minimum for pitch for a given image would be len(image.format) * image.width
    colors = [iter(data)] * length
    return zip(*colors)

def apply_color_key(image):

	image_data = image.get_image_data()
	raw_bytes = image_data.get_data()
	pixel_length = len(image_data.format)
	new_arr = []
	for i in chunker(raw_bytes, pixel_length):
		if i == KEY_COLOR:
			new_arr.extend((0, 0, 0, 0))
		else:
			new_arr.extend(i)

	image_data.set_data(image_data.format, 0, bytes(new_arr))
	image.blit_into(image_data, 0, 0, 0)
	return image

pyglet.resource.path = [os.path.join(base_path, "../resources")]
pyglet.resource.reindex()
tile_set_image = pyglet.resource.image("tile_set.png")

tile_set_image = apply_color_key(tile_set_image)

image_part = tile_set_image.get_region(16, 16*15, TILE_SIZE, TILE_SIZE)

# Batch the sprites
#background = pyglet.graphics.Batch()
