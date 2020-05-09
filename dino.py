import pygame
import time
import random
pygame.init()

def edgeLim(x, y):
    if x > 960:
        x -= 10
    if y > 420:
        y -= 10
    if x < 0:
        x += 10
    if y < 0:
        y += 10
    return x, y

def fall(T):
    V0 = -35
    A = 3 
    S = V0*T+A*T**2/2
    print("falling")
    return S

class object():
    def __init__(self, x, y, dWidth, dHeight, dVel):
        self.x = x
        self.y = y
        self.dWidth = dWidth
        self.dHeight = dHeight
        self.dVel = dVel

if __name__ == '__main__':    
    window = pygame.display.set_mode((1000,500))
    pygame.display.set_caption("game")

    limx       = 1000
    limy       = 500
    cloudY     = random.randint(50,200)
    cloud_obj  = object(1000, cloudY, 90, 30, 7)
    dino_obj   = object(50, 420, 40, 80, 10)
    cactus_obj = object(1000, 450, 30, 100, 20)
    count      = 0
    score      = 0

    jumping = False
    run     = True
    running = True
    
    while running:
        while run:
            pygame.time.delay(10)

            score      += 0.1
            score_font =  pygame.font.Font(None,50)
            score_surf =  score_font.render("score : "+str(int(score)),1,(0,0,0))
            score_pos  =  [10,10]

            if cloud_obj.x <= -90:
                cloud_obj.y = random.randint(50,200)
                cloud_obj.x = 1000

            if cactus_obj.x <= 0:
                cactus_obj.y   = random.randint(420,450)
                cactus_obj.x   = 1000
                cactus_obj.dVel    = 15

            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                if jumping == False and dino_obj.y <= 420:
                    jumping = True
            if jumping == True :
                count = count + 1
                dino_obj.y = 420+fall(count)

            if dino_obj.y >= 420:
                jumping = False
                count = 0

            if keys[pygame.K_DOWN]:
                dino_obj.y += dino_obj.dVel

            cloud_obj.x -= cloud_obj.dVel
            cactus_obj.x -= cactus_obj.dVel

            dino_obj.x, dino_obj.y = edgeLim(dino_obj.x, dino_obj.y)
            print(count)

            
            
            dino_rect   = pygame.Rect(dino_obj.x, dino_obj.y, dino_obj.dWidth, dino_obj.dHeight)
            cactus_rect = pygame.Rect(cactus_obj.x, cactus_obj.y, cactus_obj.dWidth, cactus_obj.dHeight)
            bump        = pygame.Rect.colliderect(dino_rect , cactus_rect)
            window.blit(score_surf, score_pos)
            
            if (bump == True):
                bump = False
                run  = False 
                
            
            window.fill((255,255,255))
            pygame.draw.rect(window, (255,227,132),(0, 300, 1000, 200))
            pygame.draw.rect(window, (200,200,200),(cloud_obj.x, cloud_obj.y, cloud_obj.dWidth, cloud_obj.dHeight))#cloud
            pygame.draw.rect(window, (255,0,0),(dino_obj.x, dino_obj.y, dino_obj.dWidth, dino_obj.dHeight))#dino
            pygame.draw.rect(window, (10,255,10),(cactus_obj.x, cactus_obj.y, cactus_obj.dWidth, cactus_obj.dHeight))#cactus

            

            pygame.display.update()
        
        gover_font = pygame.font.Font(None,100)
        gover_surf = gover_font.render('GAME OVER',1,(255,0,0))
        gover_pos  = [100,100]
        window.blit(gover_surf, gover_pos)
        pygame.display.update()
        running = False
        
        
    pygame.quit()
    time.sleep(5)

