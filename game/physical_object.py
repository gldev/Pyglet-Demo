import pyglet
import math


def calculate_distance(p1, p2):
	s = math.sqrt(math.pow(p2.x - p1.x)) + math.sqrt(math.pow(p2.y - p1.y))
	return s

class PhysicalObject(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)

		self.velocity_x, self.velocity_y = 0.0, 0.0

		self.react_to_talk = True
		self.is_projectile = False
		self.is_dead = False
		self.is_collidable = True
		self.new_objects = []
		self.event_handlers = []

	def update(self, dt):
		#self.x += self.velocity_x * dt
		#self.y += self.velocity_y * dt

		self.check_bounds()


	def check_bounds(self):
		min_x = -self.image.width / 2
		min_y = -self.image.height / 2
		max_x = 800 + self.image.width / 2
		max_y = 600 + self.image.height / 2
		print(f"min {min_x} x {self.x}")
		if self.x < min_x:
			self.x = max_x
		if self.y < min_y:
			self.y = max_y
		if self.x > max_x:
			self.x = min_x
		if self.y > max_y:
			self.y = min_y

	def collides_with(self, other_object):

		# Here we can ignore collitions before the conditions using "collidable"
		if not self.is_collidable:
			return False

		collision_distance = self.image.width * 0.5 * self.scale + other_object.image.width * 0.5 * other_object.scale

		actual_distance = calculate_distance(self.position, other_object.position)

		return collision_distance <= actual_distance


	def handle_collision(self):
		pass