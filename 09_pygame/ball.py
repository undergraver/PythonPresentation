import sys, pygame

pygame.init()

size = width, height = 1024, 768
xsign = 1
ysign = 1
speed = 5
black = 0, 0, 0

framerate = 60
fps_limiter = pygame.time.Clock()

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
background = pygame.image.load("background.jpg")
#ball = pygame.image.load("pp.jfif")
ballrect = ball.get_rect()

print(str(ballrect))

def increase_speed():
    global speed
    if speed < 20:
        speed += 1
    print("speed is:"+str(speed))

def decrease_speed():
    global speed
    if speed > 1:
        speed -= 1
    print("speed is:"+str(speed))

drawLine=False
done = False
paused = False
while not done:
    if pygame.key.get_pressed()[pygame.K_UP]:
        increase_speed()
        paused = False

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        decrease_speed()
        paused = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_f:
                framerate+=30
            if event.key == pygame.K_g:
                if framerate >= 60:
                    framerate-=30
            if event.key == pygame.K_SPACE:
                paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawLine = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawLine = False

    if paused == True:
        speed_sign = [ 0 , 0 ]
    else:
        speed_sign = [ speed * xsign, speed * ysign ]

    ballrect = ballrect.move(speed_sign)
    if ballrect.left < 0 or ballrect.right > width:
        xsign = -xsign
    if ballrect.top < 0 or ballrect.bottom > height:
        ysign = -ysign

    screen.fill(black)
    screen.blit(background,(0,0,width,height))
    if drawLine:
        middlex = (ballrect.left+ballrect.right)/2
        middley = (ballrect.top+ballrect.bottom)/2
        mousepos=pygame.mouse.get_pos()
        pygame.draw.line(screen,(255,0,0),(middlex,middley),mousepos)

    screen.blit(ball, ballrect)
    pygame.display.flip()
    fps_limiter.tick(framerate)

pygame.quit()
sys.exit()
