import pygame
pygame.init()

windowy=1080
windowx=1920

win = pygame.display.set_mode((windowx, windowy)) #Window for game 


pygame.display.set_caption("Shooter") #Title of the window

#Array of the main sprite looking in certain directions
walkRight = [pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png')]
walkLeft = [pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png')]
walkUp = [pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png')]
walkDown = [pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png')]

#Background pictures
bg = pygame.image.load('bg.jpg')
bg = pygame.image.load('bg.jpg')


clock = pygame.time.Clock() #Frame-Rate of the game


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5        
        self.isJump = False
        self.left = False
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

    def fixBounds(self): #Fixes the bounds if player goes outside of it.
        if self.x == 0:
            self.x += self.vel
        if self.x == windowx:
            self.x -= self.vel
        if self.y == 0:
            self.y += self.vel
        if self.y == windowy:
            self.y -= self.vel
        
    

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


#Remember that the origin is top left of screen
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

man = player(200, 410, 64,64) #main character sprite
bullets = [] #bullet projectile list

def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()




run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() #Keypress listener

    if keys[pygame.K_r]:
        print("Man X: ", man.x, " Man Y: ", man.y, "inBounds: ", man.inBounds())

    if keys[pygame.K_LEFT] and man.inBounds(): #Left
        man.x -= man.vel
        man.left = True
        man.right = False
        man.down=False
        man.up= False
        man.standing = False
    if keys[pygame.K_LEFT] and keys[pygame.K_UP] and man.inBounds(): #Left up      
        man.x -= man.vel
        man.y -= man.vel
        man.left = True
        man.up = True
        man.down = False 
        man.right = False
    if keys[pygame.K_LEFT] and keys[pygame.K_UP] and man.inBounds(): #Left Down  
        man.x -= man.vel
        man.y += man.vel
        man.left = True
        man.up = False 
        man.down = True
        man.right = False
    if keys[pygame.K_RIGHT] and man.inBounds(): #Right
        man.x += man.vel
        man.right = True
        man.left = False
        man.up=False
        man.down=False
        man.standing = False
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP] and man.inBounds(): #Right-Up
        man.x += man.vel
        man.y -= man.vel
        man.right = True
        man.left = False
        man.up=True
        man.down=False
        man.standing = False
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and man.inBounds(): #Right-Down
        man.x += man.vel
        man.y += man.vel
        man.right = True
        man.left = False
        man.up=False
        man.down=True
        man.standing = False
    if keys[pygame.K_UP] and man.inBounds(): #Up
        man.y-= man.vel
        man.left = False
        man.right = False
        man.down=False
        man.up=True
        man.standing = False
    if keys[pygame.K_DOWN] and man.inBounds(): #Down
        man.y += man.vel
        man.right = False
        man.left = False
        man.down=True
        man.up=False
        man.standing = False
    
    man.fixBounds() #This is required for the man sprite to stay within game bounds and not break movement

    for bullet in bullets:
        if bullet.x < windowx and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    

    if keys[pygame.K_SPACE]:
        if man.left == True:
            facing = -1
        if man.right == True:
            facing = 1
        if man.up == True:
            facing = -1
        if man.down == True:
            facing =1
        bulletAmount = 1000
        if len(bullets) < bulletAmount: #amount of bullets on screen
            bullets.append(projectile(round(man.x + man.width //9), round(man.y + man.height/3), 6, (0,0,0), facing))

    


    redrawGameWindow()

pygame.quit()
