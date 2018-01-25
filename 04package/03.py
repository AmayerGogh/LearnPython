# from random import randint
# from asciimatics.screen import Screen

# def demo(screen):
#     #while True:
#     screen.print_at('hellp world',
#                     randint(0, screen.width), randint(0, screen.height),
#                     colour=randint(0, screen.colours - 1),
#                     bg=randint(0, screen.colours - 1))
#     ev =screen.get_key()
#     if ev in (ord('Q'),ord('q')):
#         return 
#     #screen.refresh()
# Screen.wrapper(demo)


from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from time import sleep

# def demo(screen):
        # '''
        # 基本
        # '''
#     effects = [
#         Cycle(
#             screen,
#             FigletText("Amayer"),
#             int(screen.height / 2 - 8)),
#         Cycle(
#             screen,
#             FigletText("你好!@#$%^&*++(*",),
#             int(screen.height / 2 + 3)),
#         #Stars(screen, 200)
#     ]
#     screen.play([Scene(effects, 500)])
# Screen.wrapper(demo)

# #creating a screen
# def demo(screen):        
#     for item in range(4):
#         screen.clear()
#         screen.print_at('☎你好我的世界!!!',item,item,item,item)
#         screen.refresh() #刷新屏幕
#         sleep(1) #
#     sleep(3) #
# Screen.wrapper(demo)    
# #print_att()
# #参数3
# # COLOUR_BLACK = 0
# # COLOUR_RED = 1
# # COLOUR_GREEN = 2
# # COLOUR_YELLOW = 3
# # COLOUR_BLUE = 4
# # COLOUR_MAGENTA = 5
# # COLOUR_CYAN = 6
# # COLOUR_WHITE = 7
# # 参数4
# # A_BOLD = 1
# # A_NORMAL = 2
# # A_REVERSE = 3
# # A_UNDERLINE = 4
