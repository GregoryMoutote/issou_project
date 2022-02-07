import pygame,threading,os,time


class Animation:
	def __init__(self, screen,x,y,name=""):
		thread = AnimationThread(screen, x, y,name)  # crée le thread
		thread.start()



class AnimationThread(pygame.sprite.Sprite,threading.Thread):
	def __init__(self, screen, x, y, name=""):
		threading.Thread.__init__(self)
		super().__init__()
		self.screen=screen
		self.sprites = []
		for path in os.listdir("Pictures/Animations/"+name):
				self.sprites.append(pygame.image.load("Pictures/Animations/"+name+"/"+path))

		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [x, y]

	def run(self):
		print("run")
		while self.current_sprite < len(self.sprites):
			image = self.sprites[int(self.current_sprite)]
			self.current_sprite += 1
			time.sleep(0.02)
			self.screen.blit(image, (self.rect.x, self.rect.y))
			pygame.display.update()

