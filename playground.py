import pygame, math, time
screen=pygame.display.set_mode((320,240))
clock=pygame.time.Clock()
pygame.init()
def calculate_new_xy(old_xy,speed,angle_in_radians):
    new_x = old_xy[0] + (speed*math.cos(angle_in_radians))
    new_y = old_xy[1] + (speed*math.sin(angle_in_radians))
    return new_x, new_y
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,speed):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.Surface((16, 16))
            self.image.fill((255,0,0))
            self.rect=self.image.get_rect()
            self.rect.center=(x,y)
            self.direction=math.radians(direction)
            self.speed=speed
    def update(self):
            self.rect.center=calculate_new_xy(self.rect.center,self.speed,self.direction)
spr=pygame.sprite.Group()
bullet=Bullet(160,120,45,2)
spr.add(bullet)
play=True
while play:
    clock.tick(60)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            play=False
    screen.fill((0,0,0))
    spr.update()
    spr.draw(screen)
    pygame.display.flip()
pygame.quit()