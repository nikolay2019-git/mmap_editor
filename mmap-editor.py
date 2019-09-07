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
	
	def __init__(self, width, height, caption):
		self.Map = {}
		pygame.init()
		pygame.font.init()
		self.surface = pygame.display.set_mode((width, height))
		self.surface.fill(white)
		pygame.display.set_caption(caption)
		
		pass


class Text_Box:
	pass
	



def main():
	# Создаём объект Сцена, задаём параметры
	# Инициализируем нужные объекты внутри, класс pygame и текстуру экрана
	scene = Scene(400, 500, 'caption')
	#scene.events_handlers()# тут вся логика


if __name__ == '__main__':
	main()