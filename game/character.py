import pyglet, math
from pyglet.window import key
from .physical_object import PhysicalObject

class Character(PhysicalObject):
	def __init__(self, *args, **kwargs):
		image = kwargs.pop("image")
		visible = kwargs.pop("visible", True)
		speed = int(kwargs.pop("speed", 2.0))
		super(Character, self).__init__(img=image, *args, **kwargs)
		self.engine_sprite = pyglet.sprite.Sprite(img=image, *args, **kwargs)
		self.engine_sprite.visible = visible

		self.sprite_speed = speed

		# Characters should not collide with own weapons
		self.reacts_to_own_bullets = False

		# Tell the game handler about any event handlers
		self.key_handler = key.KeyStateHandler()
		self.event_handlers = [self, self.key_handler]

	def update(self, dt):
		super(Character, self).update(dt)
		if self.key_handler[key.LEFT]:
			self.x -= self.sprite_speed * dt
		if self.key_handler[key.RIGHT]:
			self.x += self.sprite_speed * dt
		if self.key_handler[key.UP]:
			self.y += self.sprite_speed * dt
		if self.key_handler[key.DOWN]:
			self.y -= self.sprite_speed * dt

	def on_key_press(self, symbol, modifiers):
		if symbol == key.SPACE:
			print("Talk")

	def delete(self):
		self.engine_sprite.delete()
		super(Player, self).delete()