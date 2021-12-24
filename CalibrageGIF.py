import pygame, sys

class loadGIF(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y,screen):
		super().__init__()
		self.screen=screen
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-01.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-02.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-03.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-04.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-05.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-06.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-07.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-08.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-09.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-10.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-11.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-12.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-13.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-14.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-15.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-16.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-17.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-18.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-19.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-20.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-21.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-22.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-23.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-24.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-25.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-26.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-27.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-28.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-29.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-30.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-31.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-32.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-33.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-34.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-35.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-36.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-37.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-38.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-39.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-40.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-41.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-42.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-43.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-44.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-45.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-46.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-47.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-48.gif'))
		self.sprites.append(pygame.image.load('picture/interface/gif/ISSOUCalibrage/frame-49.gif'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def update(self,speed):
		self.current_sprite += speed
		if int(self.current_sprite) >= len(self.sprites):
			self.current_sprite = 0
			self.attack_animation = False
		self.image = self.sprites[int(self.current_sprite)]