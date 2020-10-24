class Settings:
    """ A class to store all settings for ALien Invasion"""
    def __init__(self):
        #Screen setting
        self.width = 1200
        self.height = 800
        self.bg_color = (150,200,255)
        #ship setting
        self.ship_speed = 2.5
        #bullet setting
        self.bullet_speed = 1
        self.bullet_rect_hight = 15
        self.bullet_rect_width = 3
        self.bullet_color = (60,60,60)
