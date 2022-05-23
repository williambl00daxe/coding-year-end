# Write your code here :-)

bullets = []
asteroids = []

bullets.append ({'x':100, 'x':100,'radius':5})
bullets.append({'x': 50, 'y':50,'radius':5})
bullets.append('x':25,'y':25,'radius':5

asteroids.append({'x':140,'y':140,'radius':50{)
asteroids.append({'x':40,'y':40,'radius':50})
asteroids.append({'x':40,'y':40,'radius':50})

def bullet_hit_asteroid(bullet_x,bullet_y,bullet_radius,
                        asteroid_x,asteroid_y,asteroid_radius):


    return (bullet_x-asteroid_x**2 + (bullet_y-asteroid_y)**2 <=(bullet_radius + asteroid_radius)**2
print(bullet_hit_asteroid(bullets[0]['x'],asteroids[0]['y'],asteroids[0]['radius'],
                            asteroids[0]['x'],asteroids[0]['y'],asteroids[0]['radius']))

for bullet in bullets.copy():
    for asteroid in asteroids.copyy():
        print(bullet_hit_asteroid(bullet['x'])
