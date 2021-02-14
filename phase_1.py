#here we will try moving the car on a simple straight line path

import pygame
pygame.init()

#make a window to put your track on. Our track is of 1200*400 so the window
window = pygame.display.set_mode((1200,400))
track = pygame.image.load('track1.png')
car = pygame.image.load('tesla.png')
#by default the image of car is very big. so we shrink it
car = pygame.transform.scale(car, (30,60))

# to set position of car dynamically
car_x=150
car_y=300

#focal distance-> how far do you want camera to look. 
focal_dis = 15 + 10
#clock to control speed of clock
clock = pygame.time.Clock()
drive = True

while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
# a camera in the car which will detect hurdles
    cam_x = car_x + 15 
    cam_y = car_y + 15
# you want to know where the road ends, that is where white color changes.
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
# moving the car fwd till road ends
    if up_px==255:
        car_y=car_y-2
    
#blit stands for block image transfer, we transfer our track to the window.
#(0,0) defines the start position
    window.blit(track,(0,0))
    
#window.blit(car,(0,0)) this will put your car on the origin of image, but we don't want that
    window.blit(car, (car_x,car_y))
    
# draw the camera, tell its color, position and radius
    pygame.draw.circle(window,(0,255,0),(cam_x,cam_y), 5, 5)
    
#then we ask pygame to update the display
    pygame.display.update()
    