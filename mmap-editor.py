# -*- coding: utf-8 -*-
import os
import pygame
from pygame.constants import *
import time
import math


white = [255, 255, 255]
black = [0, 0, 0]


class QuadInt:
	pass
	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0

class TileMap:
	pass
	deltaX = 0
	deltaY = 0
	mapDict = {}
	textbox_array = []
	def add_to_tilemap(self, list): # пока не используется
		pass
		for index_pair in index_pair_list:
			row = index_pair[0]
			col = index_pair[1]
			if row not in self.tileMap.mapDict:
				self.tileMap.mapDict[row] = {}
			if col not in self.tileMap.mapDict[row]:
				self.tileMap.mapDict[row][col] = []
			if textbox_id not in self.tileMap.mapDict[row][col]:
				self.tileMap.mapDict[row][col].append(textbox_id)
		
	def del_from_tilemap(self, list):
		pass
		
	def  get_screen_list(self):
		pass
		col = - self.deltaX // 64
		row = - self.deltaY // 64
		self.screenList = []
		for cols in range(col, col + 6):# зависит от ширины и высоты экрана
			for rows in range (row, row + 7):
				cell_exists_bool = False
				if rows in self.mapDict:
					if cols in self.mapDict[rows]:
						cell_exists_bool = True
				if cell_exists_bool:
					Cell_textbox_list = []
					Cell_textbox_list = self.mapDict[rows][cols]
					if Cell_textbox_list != []:
						
						for id in Cell_textbox_list:
							if id not in self.screenList: # Дорогостоящая операция, кажется
								self.screenList.append(id)
	def is_tile_exsists(self, row, col ):
		pass
		
	def get_object_id_under_object(self, textbox):
		pass
		tb = textbox
		# перебираем tb.ConsistList, добавляем в список
		textboxes_under_list = []
		# нужно не забыть исключить себя при создании, список, возможно, ещё ничего не содержит...
		for i in tb.consistList:
			row = i[0]
			col = i[1]
			cell_exists_bool = False
			if self.mapDict.get(row) != None:
				if self.mapDict[row].get(col)!= None:
					cell_exists_bool = True
			if cell_exists_bool:
				Cell_textbox_list = []
				Cell_textbox_list = self.mapDict[row][col]
				if Cell_textbox_list != []:
					for id in Cell_textbox_list:
						if id not in textboxes_under_list:
							textboxes_under_list.append(id)
				# список готов
		AddTextBoxAllow  = True
		for id in textboxes_under_list:
			first_obj = textbox
			second_obj = self.textbox_array[id]# уточнить адресацию
			AddTextBoxAllow = not self.check_intersect(first_obj, second_obj)# возвращает Пересекается (Да) или Не пересекается (нет)
			if not AddTextBoxAllow:
				return AddTextBoxAllow  # Ищем первое же пересечение (ДА) и выходим, больше не надо, запрещаем добавлять.
			#  Если постоянно было (нет) Не пересекаются, то разрешение остаётся в силе, перебрали все объекты, можно добавлять
		return AddTextBoxAllow 
	def get_object_id_under_point(self, x, y ):
		pass
		ObjectId = -1
		real_x = x - self.deltaX
		real_y = y - self.deltaY
		col = x // 64
		row = y // 64
		cell_exists_bool = False
		if self.mapDict.get(row) != None:
			if self.mapDict[row].get(col)!= None:
				cell_exists_bool = True
		if cell_exists_bool:
			Cell_textbox_list = []
			Cell_textbox_list = self.mapDict[row][col]
			if Cell_textbox_list != []:        
				for id in Cell_textbox_list:
					textbox = self.textbox_array[id]# уточнить адресацию
					if real_x > textbox.x and real_x < textbox.x + textbox.width and real_y > textbox.y and real_y < textbox.y +textbox.height:
						ObjectId = id
						return ObjectId
		return ObjectId
		
	def check_intersect(self, first_obj, second_obj):
		pass
		obj_intersect_bool = False
		quad1 = first_obj.get_bounding_box();
		quad2 = second_obj.get_bounding_box();
		x_intersect = False
		y_intersect = False
		if quad1.x1 > quad2.x1:
			quad1, quad2 = quad2, quad1
		if quad1.x2 > quad2.x1:
			x_intersect = True
		if quad1.y1 > quad2.y1:
			quad1, quad2 = quad2, quad1
		if quad1.y2 > quad2.y1:
			y_intersect = True
		if x_intersect and y_intersect:
			obj_intersect_bool = True
		return obj_intersect_bool

class Scene:
	FOCUS = -1# -1 == Map в начале в фокусе только карта, нет объектов
	selectionList = [] # Список выделенных объектов
	LEFT = 1
	RIGHT = 3
	GrabMapBool = False # перетаскиваем карту или нет
	GrabObjectsBool = False # флаг для перетаскивания объектов
	# Временный список для ВСЕХ объектов, потом будет только список экранных объектов, видимых
	mapDict = {} # структура для хранения объектов в ячейках карты
	tileMap = TileMap()
	
	def append_to_map(self, index_pair_list, textbox_id):
		pass
		for index_pair in index_pair_list:
			row = index_pair[0]
			col = index_pair[1]
			if row not in self.tileMap.mapDict:
				self.tileMap.mapDict[row] = {}
			if col not in self.tileMap.mapDict[row]:
				self.tileMap.mapDict[row][col] = []
			if textbox_id not in self.tileMap.mapDict[row][col]:
				self.tileMap.mapDict[row][col].append(textbox_id)
	
	def redraw_text_box(self, tb):
		# Отрисовка отдельного объекта
		x = tb.x + self.tileMap.deltaX
		y = tb.y + self.tileMap.deltaY
		pygame.draw.circle(self.surface, white,(x, y), tb.rx, 0)
		pygame.draw.circle(self.surface, black,(x, y), tb.rx, 1)
		pygame.draw.rect(self.surface, white, (x, y, tb.width, tb.height), 0)
		pygame.draw.rect(self.surface, tb.color, (x, y, tb.width, tb.height), 1)
	
	def render(self):
		self.surface.fill(white)
		self.redraw_visible_objects()
		pygame.display.flip()
	
	
	
	def redraw_visible_objects(self):
		self.surface.fill(white)
		self.tileMap.get_screen_list()
		# Кусок для тестирования вывода текста
		# Font2 =  pygame.font.Font(None, 24)#Courier New
		# text = "новый текст"
		# text_surf = Font2.render(text, 1, black, white)
		# self.surface.blit(text_surf, (10, 10))
		if len(self.tileMap.screenList) > 0:
			for id in self.tileMap.screenList:
				textbox = self.tileMap.textbox_array[id]        
				self.redraw_text_box(textbox)
		pygame.display.flip()
		
		
		
	def __init__(self, width, height, caption):
		
		# Передавать сюда поверхность, а инициализацию pygame вынести в main?
		self.Map = {}
		pygame.init()
		pygame.font.init()
		self.surface = pygame.display.set_mode((width, height))
		self.surface.fill(white)
		pygame.display.set_caption(caption)
		
	def try_create_textbox(self, mouse_x, mouse_y):
		pass
		tb = TextBox()# Временный текстбокс
			
		tb.set(mouse_x - self.tileMap.deltaX, mouse_y - self.tileMap.deltaY)# Установка объекта, коррекция положения 
		# учёт смещения относительно начального положения вью
		
		
		tb.consistList = self.get_consist_list(tb); 
		AddTextBoxAllow = self.tileMap.get_object_id_under_object(tb) # Проверка, можно ли создать объект
		if AddTextBoxAllow :                                        
			self.create_textbox(tb)
	
	def get_consist_list(self, tb):
		pass
		quad = tb.get_bounding_box()
		first_col = (quad.x1) // 64
		first_row = (quad.y1) // 64
		first_col_offset = quad.x1 %64
		first_row_offset = quad.y1 % 64
		
		last_col = quad.x2 // 64
		last_row = quad.y2 // 64
		last_col_offset = quad.x2 % 64
		last_row_offset = quad.y2 % 64
		
		tb.consistList = []
		for row in range(first_row, last_row + 1):
			for col in range(first_col, last_col + 1):
				tb.consistList.append((row, col))
		return tb.consistList
	
	def create_textbox(self, tb):
		pass
		textbox_id = len(self.tileMap.textbox_array)
		self.tileMap.textbox_array.append(tb)
		self.append_to_map(tb.consistList, textbox_id)
	
	
	def events_handlers(self):
		running = True
		clock = pygame.time.Clock()
		while running:
			clock.tick(10)
			self.render()# разве здесь нужно рендерить? А не после изменений?
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == self.LEFT:
					self.left_mouse_down_event_handler()
				if event.type == pygame.QUIT:
					running = False
	def left_mouse_down_event_handler(self):
		pos = pygame.mouse.get_pos()
		mouse_x, mouse_y = pos[0], pos[1]
		
		# проверка, не нажали ли на существующий объект левой кнопкой мыши
		ObjectId = self.tileMap.get_object_id_under_point(mouse_x, mouse_y)# Возвращает -1 если нет объекта под курсором
		if self.FOCUS != -1:# Если нажали
			textbox = self.tileMap.textbox_array[self.FOCUS-1]
			textbox.color = pygame.Color(0,0,0)
		self.FOCUS = ObjectId # Установка фокуса на новый объект, если он под курсором или -1
		if self.FOCUS != -1:
			self.selectionList = []
			self.selectionList.append(ObjectId)# Надо как-то убирать элементы из списка
			pygame.time.set_timer(pygame.USEREVENT+1, 100)# Старт Анимации
		if ObjectId == -1:
			self.try_create_textbox(mouse_x, mouse_y)# Попытка создать новый объект
			
			
			
			
class TextBox:
	def set(self, x, y, width = 60, height = 20, rx = 10, ry = 10):
		
		self.x = x
		self.y = y
		self.rx = rx
		self.ry = ry
		self.width = width  
		self.height = height
		
	def __init__(self):
		
		self.color = pygame.Color(0, 0, 0)
		self.x = 0
		self.y = 0
		self.rx = 10
		self.ry = 10
		self.width = 60
		self.height = 20
		
	def get_bounding_box(self):
		
		quad_int = QuadInt()
		quad_int.x1 = self.x - self.rx
		quad_int.y1 = self.y - self.ry
		quad_int.x2 = self.x + self.width
		quad_int.y2 = self.y + self.height
		self.quad_int = quad_int#?
		return quad_int	
		
	def draw(self, surface):
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