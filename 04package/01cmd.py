# import urwid
# txt = urwid.Text(u"Hello World")
# fill = urwid.Filler(txt, 'top')
# loop = urwid.MainLoop(fill)
# loop.run()
# def show_or_exit(key):
#     if key in ('q', 'Q'):
#         raise urwid.ExitMainLoop()
#     txt.set_text(repr(key))

# txt = urwid.Text(u"Hello World")
# fill = urwid.Filler(txt, 'top')
# loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
# loop.run()



#!/usr/bin/env python
# encoding: utf-8

# import npyscreen
# class TestApp(npyscreen.NPSApp):
#     def main(self):
#         # These lines create the form and populate it with widgets.
#         # A fairly complex screen in only 8 or so lines of code - a line for each control.
#         F  = npyscreen.Form(name = "Welcome to Npyscreen",)
#         t  = F.add(npyscreen.TitleText, name = "Text:",)
#         fn = F.add(npyscreen.TitleFilename, name = "Filename:")
#         fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
#         dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
#         s  = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
#         ml = F.add(npyscreen.MultiLineEdit,
#                value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
#                max_height=5, rely=9)
#         ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
#                 values = ["Option1","Option2","Option3"], scroll_exit=True)
#         ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
#                 values = ["Option1","Option2","Option3"], scroll_exit=True)

#         # This lets the user interact with the Form.
#         F.edit()

#         print(ms.get_selected_objects())

# if __name__ == "__main__":
#     App = TestApp()
#     App.run()


import curses
#安装包   http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses 
#需要安装
myscreen = curses.initscr()  
myscreen.border(0)  
myscreen.addstr(12, 25, "Python curses in action!")  
myscreen.refresh()  
myscreen.getch()  
   
curses.endwin()  