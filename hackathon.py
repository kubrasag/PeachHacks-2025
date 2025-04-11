import pygame
import sys
pygame.init()

font = pygame.font.SysFont(None, 36)
level_start_time = pygame.time.get_ticks()
score = 1000
game_finished = False
final_message = ""
lives = 5
finish_time = Nonefont = pygame.font.SysFont(None, 36)
pygame.display.set_caption('Worlds Hardest Game')
pygame.mixer.init()
clock=pygame.time.Clock()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


reset_x=30
reset_y=30
yellow=(247,203,38)
black=(0,0,0)
green=(155,242,154)
background=(168,166,254)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
speed=4
enemySpeed=5

screen=pygame.display.set_mode((1200,800))   #screen
surface=pygame.Surface((1000,600))           #white surface
surface.fill(white)
screen.blit(surface,(100,100))
player=pygame.Rect(30,30,20,20)               #player
startZone=pygame.Rect(0,0,75,75)
checkPoint=pygame.Rect(455,260,75,75)
endZone=pygame.Rect(925,525,75,75)

enemy=True
endZoneTest=True
horEnemy=True
startEnemy=True
startEnemyTest=True
endEnemy=True
checkPoint_check=True
checkPoint_check2=True
winnerMusic=True
#start enemies
startEnemy1=pygame.Rect(30,75,20,20)
startEnemy2=pygame.Rect(30,600,20,20)
#end enemies
endEnemy1=pygame.Rect(960,0,20,20)
endEnemy2=pygame.Rect(960,500,20,20)
#vertical enemies
enemy1=pygame.Rect(100,100,20,20)
enemy2=pygame.Rect(300,100,20,20)
enemy3=pygame.Rect(200,475,20,20)
enemy4=pygame.Rect(100,475,20,20)
enemy5=pygame.Rect(300,475,20,20)
enemy6=pygame.Rect(200,100,20,20)
enemy7=pygame.Rect(400,100,20,20)
enemy8=pygame.Rect(400,475,20,20)
enemy9=pygame.Rect(500,100,20,20)
enemy10=pygame.Rect(500,475,20,20)
enemy11=pygame.Rect(600,100,20,20)
enemy12=pygame.Rect(600,475,20,20)
enemy13=pygame.Rect(700,100,20,20)
enemy14=pygame.Rect(700,475,20,20)
enemy15=pygame.Rect(800,100,20,20)
enemy16=pygame.Rect(800,475,20,20)
enemy17=pygame.Rect(900,100,20,20)
enemy18=pygame.Rect(900,475,20,20)
#horizontal enemies
enemy19=pygame.Rect(0,100,20,20)
enemy20=pygame.Rect(980,100,20,20)
enemy21=pygame.Rect(0,200,20,20)
enemy22=pygame.Rect(980,200,20,20)
enemy23=pygame.Rect(0,300,20,20)
enemy24=pygame.Rect(980,300,20,20)
enemy25=pygame.Rect(0,400,20,20)
enemy26=pygame.Rect(980,400,20,20)
enemy27=pygame.Rect(0,500,20,20)
enemy28=pygame.Rect(980,500,20,20)
enemy29=pygame.Rect(62,19,20,20)
enemy30=pygame.Rect(980,19,20,20)
enemy31=pygame.Rect(0,560,20,20)
enemy32=pygame.Rect(918,560,20,20)

enemyList=[enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8,enemy9,enemy10,enemy11,enemy12,enemy13,enemy14,enemy15,enemy16,enemy17,enemy18, startEnemy1,startEnemy2,endEnemy1,endEnemy2,enemy19,enemy20,enemy21,enemy22,enemy23,enemy24,enemy25,enemy26,enemy27,enemy28,enemy29,enemy30,enemy31,enemy32]

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
    keys = pygame.key.get_pressed()
    if player.left>0:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= speed
    if player.right<1000:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += speed
    if player.top>0:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= speed
    if player.bottom<600:
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += speed
    if keys[pygame.K_m] and keys[pygame.K_o] and keys[pygame.K_e]:
        player.x = 930
        player.y = 530
    if keys[pygame.K_k] and keys[pygame.K_e] and keys[pygame.K_y]:
        player.x=475
        player.y=285

    if endZoneTest:
        enemy31.x+=enemySpeed
        enemy32.x-=enemySpeed
        if enemy31.colliderect(enemy32):
            endZoneTest=False
    else:
        enemy31.x-=enemySpeed
        enemy32.x+=enemySpeed
        if enemy32.colliderect(endZone):
            endZoneTest=True


    if startEnemyTest:
        enemy29.x+=enemySpeed
        enemy30.x-=enemySpeed
        if enemy29.x>=enemy30.x:
            startEnemyTest=False
    else:
        enemy29.x-=enemySpeed
        enemy30.x+=enemySpeed
        if enemy29.colliderect(startZone):
            startEnemyTest=True

    if checkPoint_check2:
        enemy9.y+=enemySpeed
        enemy10.y-=enemySpeed
        if enemy9.colliderect(checkPoint):
            checkPoint_check2=False
    else:
        enemy9.y-=enemySpeed
        enemy10.y+=enemySpeed
        if enemy9.y<=0:
            checkPoint_check2=True

    if checkPoint_check:
        enemy23.x+=enemySpeed
        enemy24.x-=enemySpeed
        if enemy23.colliderect(checkPoint):
            checkPoint_check=False
    else:
        enemy23.x-=enemySpeed
        enemy24.x+=enemySpeed
        if enemy23.left<=0:
            checkPoint_check=True

    if startEnemy:
        startEnemy1.y+=enemySpeed
        startEnemy2.y-=enemySpeed
        if startEnemy1.bottom>=600:
            startEnemy=False
    else:
        startEnemy1.y-=enemySpeed
        startEnemy2.y+=enemySpeed
        if startEnemy1.top<=75:
            startEnemy=True

    if endEnemy:
        endEnemy1.y+=enemySpeed
        endEnemy2.y-=enemySpeed
        if endEnemy1.bottom>=520:
            endEnemy=False
    else:
        endEnemy1.y-=enemySpeed
        endEnemy2.y+=enemySpeed
        if endEnemy1.top<=0:
            endEnemy=True

    if horEnemy:
        enemy19.x+=enemySpeed
        enemy20.x-=enemySpeed
        enemy21.x += enemySpeed
        enemy22.x -= enemySpeed
        enemy25.x += enemySpeed
        enemy26.x -= enemySpeed
        enemy27.x += enemySpeed
        enemy28.x -= enemySpeed
        if enemy19.right>=1000:
            horEnemy=False
    else:
        enemy19.x-=enemySpeed
        enemy20.x+=enemySpeed
        enemy21.x -= enemySpeed
        enemy22.x += enemySpeed
        enemy25.x -= enemySpeed
        enemy26.x += enemySpeed
        enemy27.x -= enemySpeed
        enemy28.x += enemySpeed
        if enemy19.left<=0:
            horEnemy=True
    if enemy:
        enemy1.y+=enemySpeed
        enemy2.y+=enemySpeed
        enemy3.y-=enemySpeed
        enemy4.y-=enemySpeed
        enemy5.y-=enemySpeed
        enemy6.y+=enemySpeed
        enemy7.y += enemySpeed
        enemy8.y -= enemySpeed
        enemy11.y += enemySpeed
        enemy12.y -= enemySpeed
        enemy13.y += enemySpeed
        enemy14.y -= enemySpeed
        enemy15.y += enemySpeed
        enemy16.y -= enemySpeed
        enemy17.y += enemySpeed
        enemy18.y -= enemySpeed
        if enemy1.bottom>=600:
            enemy=False
    else:
        enemy1.y-=enemySpeed
        enemy2.y-=enemySpeed
        enemy3.y+=enemySpeed
        enemy4.y+=enemySpeed
        enemy5.y+=enemySpeed
        enemy6.y-=enemySpeed
        enemy7.y -= enemySpeed
        enemy8.y += enemySpeed
        enemy11.y -= enemySpeed
        enemy12.y += enemySpeed
        enemy13.y -= enemySpeed
        enemy14.y += enemySpeed
        enemy15.y -= enemySpeed
        enemy16.y += enemySpeed
        enemy17.y -= enemySpeed
        enemy18.y += enemySpeed
        if enemy1.top<=0:
            enemy=True

    if player.collidelistall(enemyList) or keys[pygame.K_r]:
        lives -= 1
        if lives > 0:
            player.x = reset_x
            player.y = reset_y
        else:
            game_finished = True
            finish_time = (pygame.time.get_ticks() - level_start_time) // 1000
            score = 0  # max(0, 1000 - finish_time * 10)
            final_message = "Game Over - Try Again!"

    if player.colliderect(checkPoint):
        reset_x=475
        reset_y=300
        blue=(0,150,255)
        green=(0,255,150)
        enemySpeed=2
    else:
        blue=(0,0,255)
        green = (155, 242, 154)
        enemySpeed=5

    screen.fill(background)

    # Create and draw on surface
    surface = pygame.Surface((1000, 600))
    surface.fill(white)
    pygame.draw.rect(surface,green,startZone)
    pygame.draw.rect(surface,green,checkPoint)
    pygame.draw.rect(surface,green,endZone)
    pygame.draw.rect(surface, red, player)
    #pygame.draw.circle(surface, yellow,(coin1.x+10,coin1.y+40),12)
    pygame.draw.circle(surface, blue, (enemy1.x + 10, enemy1.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy2.x + 10, enemy2.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy3.x + 10, enemy3.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy4.x + 10, enemy4.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy5.x + 10, enemy5.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy6.x + 10, enemy6.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy7.x + 10, enemy7.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy8.x + 10, enemy8.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy9.x + 10, enemy9.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy10.x + 10, enemy10.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy11.x + 10, enemy11.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy12.x + 10, enemy12.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy13.x + 10, enemy13.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy14.x + 10, enemy14.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy15.x + 10, enemy15.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy16.x + 10, enemy16.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy17.x + 10, enemy17.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy18.x + 10, enemy18.y + 10), 12)
    pygame.draw.circle(surface, blue, (startEnemy1.x + 10, startEnemy1.y + 10), 12)
    pygame.draw.circle(surface, blue, (startEnemy2.x + 10, startEnemy2.y + 10), 12)
    pygame.draw.circle(surface, blue, (endEnemy1.x + 10, endEnemy1.y + 10), 12)
    pygame.draw.circle(surface, blue, (endEnemy2.x + 10, endEnemy2.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy19.x + 10, enemy19.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy20.x + 10, enemy20.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy21.x + 10, enemy21.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy22.x + 10, enemy22.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy23.x + 10, enemy23.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy24.x + 10, enemy24.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy25.x + 10, enemy25.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy26.x + 10, enemy26.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy27.x + 10, enemy27.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy28.x + 10, enemy28.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy29.x + 10, enemy29.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy30.x + 10, enemy30.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy31.x + 10, enemy31.y + 10), 12)
    pygame.draw.circle(surface, blue, (enemy32.x + 10, enemy32.y + 10), 12)
    screen.blit(surface, (100, 100))

    # Check win condition
    if player.colliderect(endZone) and not game_finished:
        if winnerMusic:
            pygame.mixer.music.load('Despicable Me 2  Happy Lyric Video by Pharrell Williams  Illumination.mp3')
            pygame.mixer.music.play(-1)
            winnerMusic=False
        game_finished = True
        finish_time = (pygame.time.get_ticks() - level_start_time) // 1000
        score = max(0, 1000 - finish_time * 10)
        if finish_time < 60:
            final_message = "Legendary!"
        elif finish_time < 120:
            final_message = "Great!"
        else:
            final_message = "Good Try!"

    lives_text = font.render(f"Lives: {lives}", True, black)
    text_rect = lives_text.get_rect(topright=(1180, 20))  # Adjust 1180 to fit your screen width
    screen.blit(lives_text, text_rect)

    # Timer and Score Display
    if not game_finished:
        current_time = pygame.time.get_ticks() - level_start_time
        time_seconds = current_time // 1000
        score = max(0, 1000 - time_seconds * 10)
        timer_text = font.render(f"Time: {time_seconds}s", True, black)
    else:
        time_seconds = finish_time
        timer_text = font.render(f"Time: {finish_time}s", True, black)

    timer_text = font.render(f"Time: {time_seconds}s", True, black)
    score_text = font.render(f"Score: {score}", True, black)

    screen.blit(timer_text, (20, 20))
    screen.blit(score_text, (20, 60))
    # Draw Lives Bar on the right side
    bar_x = 1120  # Adjust to screen width
    bar_y_start = 150
    bar_spacing = 40
    bar_width = 30
    bar_height = 30

    for i in range(lives):
        pygame.draw.rect(screen, red, (bar_x, bar_y_start + i * (bar_height + 10), bar_width, bar_height),
                         border_radius=6)

    if game_finished:
        while True:
            # Create final screen
            screen.fill(background)  # Clear the screen

            big_font = pygame.font.SysFont(None, 72)  # Big font for message
            middle_font = pygame.font.SysFont(None, 48)  # Middle font for score/time
            small_font = pygame.font.SysFont(None, 32)  # Smaller font for restart / quit

            # Create texts
            message_text = big_font.render(final_message, True, black)
            score_text = middle_font.render(f"Score: {score}", True, black)
            timer_text = middle_font.render(f"Time: {time_seconds}s", True, black)
            retry_text = small_font.render("Press R to Try Again or ESC to Quit", True, black)

            # Get screen center positions
            screen_width, screen_height = screen.get_size()
            msg_rect = message_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
            score_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 2 - 30))
            timer_rect = timer_text.get_rect(center=(screen_width // 2, screen_height // 2 + 30))
            retry_rect = retry_text.get_rect(center=(screen_width // 2, screen_height // 2 + 100))

            # Blit texts
            screen.blit(message_text, msg_rect)
            screen.blit(score_text, score_rect)
            screen.blit(timer_text, timer_rect)
            screen.blit(retry_text, retry_rect)

            pygame.display.flip()

            # R to restart, Q to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_r:
                        # Restart the game by re-running the script
                        import os

                        os.execl(sys.executable, sys.executable, *sys.argv)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()