import pygame
class Settings():
    """存储外星人所有的参数"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230,230 ,230)
        self.background = pygame.image.load("images/map.bmp")


        #子弹设置
        self.bullet_speed_factor = 50
        self.bullet_width =10
        self.bullet_height = 30
        self.bullet_color = 244,44,18
        self.bullet_allowed =3

        #外星人设置
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 100
        #fleet_direction 为1 表示向右移， 为-1 表示向左移
        self.fleet_direction =1

        #飞船设置
        self.ship_speed_factor = 20
        self.ship_limit=3