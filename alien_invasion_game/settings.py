# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:12:21 2024

@author: yiyao
"""

class Settings:
    """储存游戏【外星人入侵】中所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 1050
        self.bg_color = (230, 230, 230)
        
        #飞船设置
        self.ship_limit = 3
    
        #子弹设置
        self.bullet_width = 3#300
        self.bullet_height = 15 #20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        
        #外星人设置
        self.fleet_drop_speed = 50 #10
        
        #以什么速度加快游戏的节奏
        self.speedup_scale = 1.1
        #外星人分数的提高速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 3.0 #1.0
        
        #fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        
        #记分设置
        self.alien_points = 50
        
        
        
    def increase_speed(self):
        """提高速度设置的值和外星人分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        
        
        
        
        
    