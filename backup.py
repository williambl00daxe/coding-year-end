#
def update(dt):
    global alien_x
    global alien_y
    global alien_speed_x
    global alien_speed_y
    global bullets
    global bullet_time_between_shots
    global bullet_timer
    asteroidspeed = 100

    bullet_speed = 500
    bullet_timer += dt

    if keyboard.left:
        alien.angle +=5
    elif keyboard.right:
        alien.angle -=5
    elif keyboard.up:
        alien_speed = 10
        alien_speed_y += math.cos(alien.angle*(math.pi/180))*alien_speed*dt
        alien_speed_x += math.sin(alien.angle*(math.pi/180))*alien_speed*dt
    elif keyboard.s:
        if bullet_timer >= bullet_time_between_shots:
            bullet_timer = 0
            bullets.append({'x':alien.pos[0],
                           'y':alien.pos[1],
                           'angle':alien.angle,
                           'time_left':4})


    for asteroid in asteroids.copy():
        asteroid['asteroid_x'] -= math.sin(asteroid['asteroid_angle']*(math.pi/180))*asteroidspeed*dt
        asteroid['asteroid_y'] -= math.cos(asteroid['asteroid_angle']*(math.pi/180))*asteroidspeed*dt
        asteroid['asteroid_x'] %= WIDTH
        asteroid['asteroid_y'] %= HEIGHT




    for bullet in bullets.copy():
        bullet['x']-= math.sin(bullet['angle']*(math.pi/180))*bullet_speed*dt
        bullet['y'] -= math.cos(bullet['angle']*(math.pi/180))*bullet_speed*dt
        bullet['x'] %= WIDTH
        bullet['y'] %= HEIGHT
        bullet['time_left']-=dt

        for asteroid in asteroids.copy():
            if bullet_hit_asteroid(bullet['x'], bullet['y'], 5,
                                   asteroid['asteroid_x'],
                                   asteroid['asteroid_y'],
                                   asteroid['asteroid_radius']):
                bullets.remove(bullet)
                asteroid['asteroid_radius'] = int(asteroid['asteroid_radius']*.5)
                if asteroid['asteroid_radius']<= asteroid_radius/8:
                    asteroids.remove(asteroid)


    alien.top -= alien_speed_y
    alien.left -= alien_speed_x

    actual_speed = math.sqrt(alien_speed_x**2 + alien_speed_y**2)
    #print(actual_speed)
    #print(alien.bottom)

    alien.top %= HEIGHT
    alien.left %= WIDTH



    if alien.left > WIDTH:
        alien.right = 0



def bullet_hit_asteroid(b_x,b_y,b_radius,a_x,a_y,a_radius):
    return (b_x - a_x)**2 + (b_y - a_y)**2 <= (b_radius + a_radius)**2









