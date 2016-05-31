# implementation of Spaceship - program template for RiceRocks
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

# globals for user interface
WIDTH = 1000
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
#debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
debris_image = simplegui._load_local_image("debris.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
#nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")
nebula_image = simplegui._load_local_image("nebula.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
#splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
splash_image = simplegui._load_local_image("splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
#ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
ship_image = simplegui._load_local_image("ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
#missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
missile_image = simplegui._load_local_image("shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
#asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
asteroid_image = simplegui._load_local_image("asteroid.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
#explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
explosion_image = simplegui._load_local_image("explosion.png")

# sound assets purchased from sounddogs.com, please do not redistribute
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
#missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound = simplegui.load_sound("")
missile_sound.set_volume(.5)
#ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
ship_thrust_sound = simplegui.load_sound("")
#explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
explosion_sound = simplegui.load_sound("")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# Ship class
class Ship:

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1
            
        self.vel[0] *= .99
        self.vel[1] *= .99

    def set_thrust(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
       
    def increment_angle_vel(self):
        self.angle_vel += .1
        
    def decrement_angle_vel(self):
        self.angle_vel -= .1
        
    def shoot(self):
        global group_missile
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        group_missile.update([a_missile])
    
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        global remove
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        self.lifespan-=1
        #update lifespan
        if(self.lifespan<0):
            remove.update([self])

class explosion:
    def __init__(self,pos):
        self.time=0
        self.image=explosion_image
        self.imageInfo=explosion_info
        self.pos=pos
        
    def draw(self,canvas):
        i=int(self.time)%24
        canvas.draw_image(self.image, [ self.imageInfo.get_center()[0]+i*self.imageInfo.get_size()[0], self.imageInfo.get_center()[1]], self.imageInfo.get_size(), self.pos, self.imageInfo.get_size())
        self.time+=1

            
def group_collide(group_obj, one_obj):
    for obj in group_obj:
        if dist(one_obj.pos, obj.pos)< one_obj.radius+obj.radius:
            remove.update([obj, one_obj])
            
def group_group_collide(group1_obj, group2_obj):
    for obj in group2_obj:
        group_collide(group1_obj, obj)

# key handlers to control ship   
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
        
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(False)
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True

pos=[]

def draw(canvas):
    global time, started, remove, score, lives, rock_count, group_rock, group_missile,i, pos, last_score
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw UI
    canvas.draw_text("Lives", [50, 50], 22, "White")
    canvas.draw_text("Score", [780, 50], 22, "White")
    canvas.draw_text("Last Score", [300, 50], 22, "White")
    canvas.draw_text(str(lives), [50, 80], 22, "White")
    canvas.draw_text(str(last_score), [300, 80], 22, "White")
    canvas.draw_text(str(score), [780, 80], 22, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    rocks=group_rock
    for a_rock in rocks:
        a_rock.draw(canvas)
    for a_missile in group_missile:
        a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    for a_rock in rocks:
        a_rock.update()

    for a_missile in group_missile:
        a_missile.update()

    group_group_collide(group_rock, group_missile)
    rocks_hit=remove.difference(group_missile)
    
    score+=len(rocks_hit)
    rock_count-=len(rocks_hit)
#    if len(rocks_hit)!=0:
#        explosion_sound.rewind()
#        explosion_sound.play()
    group_missile.difference_update(remove)
    
    group_rock.difference_update(rocks_hit)
    remove=set([])
        
    for rock in rocks_hit:
        pos.append(explosion(rock.pos))
        
    removerlist=[]
    for p in pos:
        p.draw(canvas)
        if p.time>24:
            removerlist.append(p)
    for e in removerlist:
        pos.remove(e)
    
    
    group_collide(group_rock, my_ship)
    if len(remove)!=0:
#        explosion_sound.rewind()
#        explosion_sound.play()
        group_rock.difference_update(remove)
        lives-=1
        score-=2	# to compensate for two points gained on adding length of remove to the score
        if lives==0:
	    if score<0:
		last_score=0
	    else:
		last_score=score
            started=False
    if i%10==0:
	if rock_count<15 and started:
		rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
		rock_vel = [random.random()*3 - .3, random.random()*3 - .3]
		rock_avel = random.random() * .2 - .1
		a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info)
		group_rock.update([a_rock])
		rock_count+=1
    i+=1
    # draw splash screen if not started
    if not started:
        group_rock=set([])
        lives=3
        score=0
        rock_count=0
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
    
last_score=0
remove=set([])
rock_count=0
i=0
# timer handler that spawns a rock    
#def rock_spawner():
#    global group_rock, rock_count
#    if rock_count<10 and started:
#        rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
#        rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
#        rock_avel = random.random() * .2 - .1
#        a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info)
#        group_rock.update([a_rock])
#        rock_count+=1
            
# initialize stuff
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
group_rock = set([])
group_missile=set([])

#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)


# register handlers
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

#timer = simplegui.create_timer(2000.0, rock_spawner)

# get things rolling
#timer.start()
frame.start()
