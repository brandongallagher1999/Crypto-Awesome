import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("Shooter")

walkRight = [pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png'), pygame.image.load('rr.png')]
walkLeft = [pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png'), pygame.image.load('ll.png')]
walkUp = [pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png'), pygame.image.load('uu.png')]
walkDown = [pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png'), pygame.image.load('dd.png')]
bg = pygame.image.load('bg.jpg')
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


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



class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)



def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


#mainloop
man = player(200, 410, 64,64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        if man.right:
            facing = 1
        if man.up:
            facing = -1
        if man.down:
            facing =1

        if len(bullets) < 1000:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.down=False
        man.up= False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.up=False
        man.down=False
        man.standing = False
    if keys[pygame.K_UP] and man.y > man.vel:
            man.y-= man.vel
            man.left = False
            man.right = False
            man.down=False
            man.up=True
            man.standing = False
    elif keys[pygame.K_DOWN] and man.y < 500 - man.width - man.vel:
            man.y += man.vel
            man.right = False
            man.left = False
            man.down=True
            man.up=False
            man.standing = False


    redrawGameWindow()

pygame.quit()
