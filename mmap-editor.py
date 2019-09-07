# -*- coding: utf-8 -*-
import os
import pygame
from pygame.constants import *
import time
import math


white = [255, 255, 255]
black = [0, 0, 0]


class Quad_Int:
	pass


class TileMap:
	pass

class Scene:
	FOCUS = -1# -1 == Map в начале в фокусе только карта, нет объектов
	
	selectionList = []
	LEFT = 1
	RIGHT = 3
	GrabMapBool = False # перетаскиваем карту или нет
	GrabObjectsBool = False
	# Временный список для ВСЕХ объектов, потом будет только список экранных объектов, видимых
	mapDict = {} # структура для хранения объектов в ячейках карты
	tileMap = TileMap()
	
	
	
	def Render(self):
		pass
		self.surface.fill(white)
		self.RedrawVisibleObjects()
		pygame.display.flip()
	
	
	
	def RedrawVisibleObjects(self):
		self.surface.fill(white)
		#self.tileMap.GetScreenList()
		
		
		
		Font2 =  pygame.font.Font(None, 24)#Courier New
		text = "новый текст"
		text_surf = Font2.render(text, 1, black, white)
		self.surface.blit(text_surf, (10, 10))
	
	def __init__(self, width, height, caption):
		self.Map = {}
		pygame.init()
		pygame.font.init()
		self.surface = pygame.display.set_mode((width, height))
		self.surface.fill(white)
		pygame.display.set_caption(caption)
		
		pass
		
	def events_handlers(self):
		running = True
		clock = pygame.time.Clock()
		
		while running:
			clock.tick(10)
			self.Render()# разве здесь нужно рендерить? А не после изменений?
			for event in pygame.event.get():
				
				
				if event.type == pygame.QUIT:
					running = False

class Text_Box:
	def set(self, x, y, width = 60, height = 20, rx = 10, ry = 10):
		
		self.x = x
		self.y = y
		self.rx = rx # 
		self.ry = ry # 
		self.width = width  
		self.height = height
		
	def __init__(self):
		
		self.color = pygame.Color(0, 0, 0)
		self.x = 0
		self.y = 0
		self.rx = 10 # 
		self.ry = 10 # 
		self.width = 60  # 
		self.height = 20		
		
	def GetBoundingBox(self):
		
		quad_int = Quad_Int()
		quad_int.x1 = self.x - self.rx
		quad_int.y1 = self.y - self.ry
		quad_int.x2 = self.x + self.width
		quad_int.y2 = self.y + self.height
		self.quad_int = quad_int
		return quad_int		
		
	def Draw(self, surface):
		
		pygame.draw.circle(surface, white,(self.x, self.y), self.rx, 0)
		pygame.draw.circle(surface, black,(self.x, self.y), self.rx, 1)
		pygame.draw.rect(surface, white, (self.x, self.y, self.width, self.height), 0)
		pygame.draw.rect(surface, black, (self.x, self.y, self.width, self.height), 1)



def main():
	# Создаём объект Сцена, задаём параметры
	# Инициализируем нужные объекты внутри, класс pygame и текстуру экрана
	scene = Scene(400, 500, 'caption')
	
	scene.events_handlers()# тут вся логика


if __name__ == '__main__':
	main()