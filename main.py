import pyglet
from pyglet.window import key, mouse
from game import tile_set_loader
from game.character import Character

window = pyglet.window.Window()

def init():
	global player
	player = Character(speed=100, image=tile_set_loader.image_part)
	window.push_handlers(player.key_handler)
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

if __name__ == "__main__":
	init()
	# Handle update at 60 fps
	pyglet.clock.schedule_interval(update, 1 / 60.0)
	pyglet.app.run()