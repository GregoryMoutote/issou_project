import pygame,threading,os,time

from Model.Stage.Coordinates import *

class Animation:
	def __init__(self, screen,coordonate,name=""):
		thread = AnimationThread(screen, coordonate,name)  # crée le thread
		thread.start()



class AnimationThread(pygame.sprite.Sprite,threading.Thread):
	def __init__(self, screen, coordonate, name=""):
		threading.Thread.__init__(self)
		super().__init__()
		self.screen=screen
		self.sprites = []
		self.coordonne=coordonate
		for path in os.listdir("Pictures/Animations/"+name):
				self.sprites.append(pygame.transform.scale(pygame.image.load("Pictures/Animations/"+name+"/"+path),(200,200)))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.coordonne.x, self.coordonne.y]


	def run(self):
		while self.current_sprite < len(self.sprites):
			image = self.sprites[int(self.current_sprite)]
			self.current_sprite += 1
			time.sleep(0.03)
			self.screen.blit(image, (self.rect.x, self.rect.y))
			pygame.display.update(pygame.Rect(self.coordonne.x,self.coordonne.y,200,200))