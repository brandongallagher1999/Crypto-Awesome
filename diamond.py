import pygame
import math

pygame.init() #initialize pygame library

windowy=1000
windowx=1920

win = pygame.display.set_mode((windowx, windowy)) #Window for game


pygame.display.set_caption("Shooter") #Title of the window

#Array of the main sprite looking in certain directions
walkRight = [pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png')]
walkLeft = [pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png')]
walkUp = [pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png')]
walkDown = [pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png')]

#Background pictures
bg = pygame.image.load('bg.png')
bg = pygame.image.load('bg.png')


clock = pygame.time.Clock() #Frame-Rate of the game


class player(object):
    def __init__(self,x,y,width,height):
        self.ammo = 100
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.leftUp = False
        self.leftDown = False
        self.rightDown = False
        self.rightUp = False
        self.right = False
        self.down=False
        self.up= False
        self.walkCount = 0
        self.standing = True

    def inBounds(self): #Returns if the player is on in the bounds of the window
        if self.x > 0 and self.x < windowx and self.y > 0 and self.y < windowy:
            return True
        else:
            return False

    def move(self, direction):
        if direction == "left":
            self.left = True
            self.right = False
            self.down = False
            self.up = False
            self.leftDown = False
            self.leftUp = False
            self.rightDown = False
            self.rightUp = False
            self.x -= self.vel
        if direction == "right":
            self.left = False
            self.right = True
            self.down = False
            self.up = False
            self.leftDown = False
            self.leftUp = False
            self.rightDown = False
            self.rightUp = False
            self.x += self.vel
        if direction == "down":
            self.left = False
            self.right = False
            self.down = True
            self.up = False
            self.leftDown = False
            self.leftUp = False
            self.rightDown = False
            self.rightUp = False
            self.y += self.vel
        if direction == "up":
            self.left = False
            self.right = False
            self.down = False
            self.up = True
            self.leftDown = False
            self.leftUp = False
            self.rightDown = False
            self.rightUp = False
            self.y =- self.vel
        if direction == "leftUp":
            self.left = False
            self.right = False
            self.down = False
            self.up = False
            self.leftDown = False
            self.leftUp = True
            self.rightDown = False
            self.rightUp = False
            self.x -= self.vel
            self.y -= self.vel
        if direction == "leftDown":
            self.left = False
            self.right = False
            self.down = False
            self.up = False
            self.leftDown = True
            self.leftUp = False
            self.rightDown = False
            self.rightUp = False
            self.x -= self.vel
            self.y += self.vel
        if direction == "rightUp":
            self.left = False
            self.right = False
            self.down = False
            self.up = False
            self.leftDown = False
            self.leftUp = False
            self.rightDown = False
            self.rightUp = True
            self.x += self.vel
            self.y -= self.vel
        if direction == "rightDown":
            self.left = False
            self.right = False
            self.down = False
            self.up = False
            self.leftDown = False
            self.leftUp = False
            self.rightDown = True
            self.rightUp = False
            self.x += self.vel
            self.y += self.vel


    def fixBounds(self): #Fixes the bounds if player goes outside of it.
        if self.x == 0:
            self.x += self.vel
        if self.x == windowx:
            self.x -= self.vel
        if self.y == 0:
            self.y += self.vel
        if self.y == windowy:
            self.y -= self.vel

    #This function takes reference to the bullet list then does the code below.
    def shoot(self, bulletList):
        for bullet in bulletList:
            if bullet.x < windowx and bullet.x > 0:
                if self.up == True and self.left == False and self.right == False and self.down == False and self.leftUp == False and self.leftDown == False and self.rightDown == False and self.rightUp == False:
                    #bullet.x += bullet.vel
                    bullet.y += bullet.vel
                if self.down == True:
                    bullet.y -= bullet.vel
            else:
                bulletList.pop(bulletList.index(bullet))



    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            if self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
            if self.up:
                win.blit(walkUp[self.walkCount//3],(self.x,self.y))
                self.walkCount +=1
            if self.down:
                win.blit(walkDown[self.walkCount//3],(self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            if self.down:
                win.blit(walkRight[0], (self.x, self.y))
            if self.up:
                win.blit(walkLeft[0], (self.x, self.y))


def calculate_new_xy(old_xy,speed,angle_in_radians):
    new_x = old_xy[0] + (speed*math.cos(angle_in_radians))
    new_y = old_xy[1] + (speed*math.sin(angle_in_radians))
    return new_x, new_y

#Remember that the origin is top left of screen
'''class projectile(object):
    def __init__(self,x,y,radius,color,direction):
        self.rect.center = (x,y)
        self.radius = radius
        self.color = color
        self.direction = math.radians(direction)
        self.vel = 10 * 1

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)'''


class projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,speed):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.Surface((5,5))
            self.image.fill((255,0,0))
            self.rect=self.image.get_rect()
            self.rect.center=(x,y)
            self.direction=math.radians(direction)
            self.speed=speed
    def update(self):
            self.rect.center=calculate_new_xy(self.rect.center,self.speed,self.direction)

spr = pygame.sprite.Group()

man = player(200, 410, 40,80) #main character sprite
bullets = [] #bullet projectile list

#spr.add(bullets)

#draws all bullets
def redrawGameWindow():
    spr.update()
    spr.draw(win)

    man.draw(win)
    pygame.display.update()




run = True
while run:
    clock.tick(144)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(bg, (0,0))
    keys = pygame.key.get_pressed() #Keypress listener

    if keys[pygame.K_r]:
        print("Man X: ", man.x, " Man Y: ", man.y, "inBounds: ", man.inBounds() , " Man Vel: ", man.vel)

    if keys[pygame.K_a] and man.inBounds(): #Left
        man.move("left")
    if keys[pygame.K_a] and keys[pygame.K_w] and man.inBounds(): #Left up
        man.move("leftUp")
    if keys[pygame.K_a] and keys[pygame.K_s] and man.inBounds(): #Left Down
        man.move("leftDown")
    if keys[pygame.K_d] and man.inBounds(): #Right
        man.move("right")
    if keys[pygame.K_d] and keys[pygame.K_w] and man.inBounds(): #Right-Up
        man.x += man.vel
        man.y -= man.vel
        man.right = True
        man.left = False
        man.up=True
        man.down=False
        man.standing = False
    if keys[pygame.K_d] and keys[pygame.K_s] and man.inBounds(): #Right-Down
        man.x += man.vel
        man.y += man.vel
        man.right = True
        man.left = False
        man.up=False
        man.down=True
        man.standing = False
    if keys[pygame.K_w] and man.inBounds(): #Up
        man.y-= man.vel
        man.left = False
        man.right = False
        man.down=False
        man.up=True
        man.standing = False
    if keys[pygame.K_s] and man.inBounds(): #Down
        man.y += man.vel
        man.right = False
        man.left = False
        man.down=True
        man.up=False
        man.standing = False

    man.fixBounds() #This is required for the man sprite to stay within game bounds and not break movement

    for bullet in bullets:
        spr.add(bullet)


    mouseX, mouseY = pygame.mouse.get_pos() #Mouse position
    rel_x, rel_y = mouseX - man.x, mouseY - man.y #relative position from the man sprite to our mouse.

    angle = (180 / math.pi) * -math.atan2(-1*(rel_y), rel_x) #calculates angle of bullet shooting

    if keys[pygame.K_SPACE]: #Shooting
        if len(bullets) < man.ammo:
            temp = projectile(round(man.x + man.width //9), round(man.y + man.height/3),angle, 20)
            spr.add(temp)
            bullets.append(temp)


    for bullet in bullets: #Checking to see if the bullet is out of bounds
        if bullet.rect.center[0] > windowx or bullet.rect.center[0] < 0 or bullet.rect.center[1] > windowy or bullet.rect.center[1] < 0:
            bullets.pop(bullets.index(bullet))
            spr.remove(bullet)




    redrawGameWindow() #Draws the sprites on screen

pygame.quit()
