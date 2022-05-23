import math



bullet={'x':40,'y':'70','timeleft':4,'angle':12}
bullets = []
bullets.append(bullet)
bullet={'x':30,'y':'20','timeleft':4,'angle':45}
bullets.append(bullet)

bullet_speed=20
for bullet in bullets:


    bullet_speed_x=math.sin(bullet['angle']*(math.pi/180))*bullet_speed
    bullet_speed_y=math.sin(bullet['angle']*(math.pi/180))*bullet_speed
    print(bullet_speed_x,bullet_speed_y)
    bullet['x'] += bullet_speed_x
    bullet['y'] += bullet_speed_y
    print(bullet['x'],bullet['y'])

