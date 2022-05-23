import math
WIDTH=500
HEIGHT=500

alien=Actor('chuck')
alien.pos= 100,56

alien.center=(WIDTH/2,HEIGHT/2)
global alien_x
global alien_y
global alien_speed_x
global alien_speed_y
global bullets

bullets=[]
alien_speed_x=0
alien_speed_y=0
alien_x = 0
alien_y = 0
#dt = 1



line_end=[100,50]


def draw():
    screen.clear()
    screen.draw.line((120,200),(300,120),'orange')
    #screen.draw.line((10,10),line_end,'orange')
    alien.draw()
def update():
  line_end[0]+=2
  #alien.left+=2
  if alien.left>WIDTH:
        alien.right=0


#def on_mouse_down(pos):
 #   if alien.collidepoint(pos):
  #      print("ooo0o0o0o0000oo0o0o0o0ooo0o0ooo0oof !")
   #     sounds.eep.play()
    #    alien.image="splat"
    #else:
    #    print('you missed me ')



def update(dt):
    global alien_x
    global alien_y
    global alien_speed_x
    global alien_speed_y
    global bullets

    bullet_speed=20
    if keyboard.left:
        alien.angle+=5
    elif keyboard.right:
        alien.angle-=5
    elif keyboard.up:
        alien_speed=10
        alien_speed_y += math.cos(alien.angle*(math.pi/180))*alien_speed*dt
        alien_speed_x += math.sin(alien.angle*(math.pi/180))*alien_speed*dt
    elif keyboard.s:
        bullets.append({'x':alien.pos[0],
        'y':alien.pos[1],
        'angle':alien.angle,
        'time_left':4})
        print(bullets)


    for bullet in bullets.copy():
        bullet['x'] += math.sin(bullet['angle']*(math.pi/180))*bullet_speed*dt
        bullet['y']+=math.cos(bullet['angle']*(math.pi/180))*bullet_speed*dt
        #print({alien.pos})
       # print('x',alien.pos[0],'y',alien.pos[1])
        print(bullet['x'],bullet['y']

    alien.top -= alien_speed_y
    alien.left -= alien_speed_x

   # actual_speed = math.sqrt(alien_speed_x**2 + alien_speed_y**2)
    #print(actual_speed)
   # print(alien.top)




    alien.top %=HEIGHT
    alien.left %=WIDTH



def bullet_hit_asteroid(b_x,b_y,b_radius,a_x,a_y,a_radius):
    return(b_x-a_x)**2 + (b_y - a_y) *








