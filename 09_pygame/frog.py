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

frog = pygame.image.load("cute-frog.png")
background = pygame.image.load("background.jpg")
fw,fh = frog.get_size()
frogrect = (width/2-fw/2,height-fh-10,fw,fh)

drawLine=False
done = False
while not done:
    if pygame.key.get_pressed()[pygame.K_UP]:
        pass

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        pass

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawLine = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawLine = False

    screen.fill(black)
    screen.blit(background,(0,0,width,height))
    if drawLine:
        middlex = frogrect[0]+frogrect[2]/2
        middley = frogrect[1]+frogrect[2]/2
        mousepos=pygame.mouse.get_pos()
        pygame.draw.line(screen,(255,0,0),(middlex,middley),mousepos,3  )
    screen.blit(frog, frogrect)
    pygame.display.flip()
    fps_limiter.tick(framerate)

pygame.quit()
sys.exit()
