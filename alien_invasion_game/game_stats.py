# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:56:58 2024

@author: yiyao
"""

class GameStats:
    """跟踪游戏的统计信息"""
    
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        #在任何情况下都不应重置最高分
       # self.high_score = 0
        
        #历史最高得分
        self.highest_score = self.check_highest_score()
        
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
    def check_highest_score(self):
        with open('highest_score.txt', 'r') as f:
            highest_score = int(f.read())
        return highest_score