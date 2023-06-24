
from pinpong.extension.unihiker import *
from pinpong.board import Board,Pin
from unihiker import GUI
import spotify_functions as sf
import time

# Event callback function
def button_click1():
    buzzer.pitch(131,1)
    sf.prev_song()
   
def button_click2():
    buzzer.pitch(147,1)
    sf.play_pause()
    
def button_click3():
    buzzer.pitch(165,1)
    sf.next_song()


u_gui=GUI()
Board().begin()
do=u_gui.draw_image(image="PREV.png",x=20,y=3)
do.config(h=100)
do.config(onclick=button_click1)
re=u_gui.draw_image(image="PLAY.png",x=20,y=110)
re.config(h=100)
re.config(onclick=button_click2)
mi=u_gui.draw_image(image="NEXT.png",x=20,y=215)
mi.config(h=100)
mi.config(onclick=button_click3)

while True:
    time.sleep(0.01)
