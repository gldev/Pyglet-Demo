import pyglet
from pyglet.window import key
from pyglet.window import mouse
from game import tile_set_loader

window = pyglet.window.Window()

sprite = pyglet.sprite.Sprite(img=tile_set_loader.image_part, x=400, y=300)

@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.LEFT:
		print('The left arrow key was pressed.')
		sprite.x-=1*5
	elif symbol == key.RIGHT:
		print('The right arrow key was pressed.')
		sprite.x+=1*2
	elif symbol == key.UP:
		print('The up arrow key was pressed.')
		sprite.y+=1*2
	elif symbol == key.DOWN:
		print('The down arrow key was pressed.')
		sprite.y-=1*2
	elif symbol == key.A:
		print('The "A" key was pressed.')


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')


@window.event
def on_draw():
    window.clear()
    sprite.draw()

if __name__ == "__main__":
	# Handle update at 60 fps
	#pyglet.clock.schedule_interval(update, 1 / 60.0)
	pyglet.app.run()