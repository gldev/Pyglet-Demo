import pyglet
from pyglet.window import key, mouse
from game import tile_set_loader
from game.character import Character
import math

window = pyglet.window.Window(width=800, height=600)
stage_batch = pyglet.graphics.Batch()

def init():
	global player, world, stage_sprites
	stage = [
		"LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
		"LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXL",
		"LXOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXLLLXXL",
		"LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXLELXXL",
		"LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXLDLXXL",
		"LXLLLLLLLLLLXXXXXXXXXXXXXXXXXXXXLDLXXL",
		"LXXXXXXXXXXLXXXXXXXXXXXXXXXXXXXXXXXXXL",
		"LXXXXXXXKXXLXXXXXXXXXXXXXXXXXXXXXXXXXL",
		"LXXXXXXXXXXLXXXXXXXXXXXXXXXXXXXXXXXXXL",
		"LXXXXXXXXXXLXXXXXXXXXXXXXXXXXXXXXXXXXL",
		"LXXXXXXXXXXXXXXXXXXXXXXXXXXLLLLLLLXXXL",
		"LXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXXXXXXL",
		"LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
	]
	world = {}
	stage_sprites = []
	for i in range(0, 13):
		for j in range(0, len(stage[i])):
			if stage[i][j] == "L":
				print(f" arr {stage[i][j]} i {i} j {j}")
				world[i,j] = Character(speed=0, x=j*21, y=i*48, image=tile_set_loader.horizontal_wall, batch=stage_batch)
				stage_sprites.append(world[i,j])

	player = Character(speed=100, x=16, y=16,image=tile_set_loader.image_part)
	window.push_handlers(player.key_handler)
	x_cells, y_cells = math.floor(800 / 20), math.floor(600 / 20)
	# pyglet.sprite.Sprite(img=tile_set_loader.image_part, x=0, y=0)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')

def update(dt):
	player.update(dt)
	pass


@window.event
def on_draw():
    window.clear()
    player.draw()
    stage_batch.draw()

if __name__ == "__main__":
	init()
	# Handle update at 60 fps
	pyglet.clock.schedule_interval(update, 1 / 60.0)
	pyglet.app.run()