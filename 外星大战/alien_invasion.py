import sys, pygame, time
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():

    #初始话游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("飞机大战")
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets =Group()
    aliens =Group()
    gf.create_fleet(ai_settings, screen,ship, aliens)
    #创建一个用于统计游戏状态的实例
    stats = GameStats(ai_settings)

    #开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings,stats,screen, ship, aliens, bullets)

         #让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        time.sleep(0.2)

run_game()
