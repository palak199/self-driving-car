# in phase 4 we'll rotate the car by 90 degrees down

# earlier we were detecting foward backward, backward and right turns , now we' ll detect left turns as well

#here we will try moving the car on a simple straight line path

import pygame
pygame.init()

#make a window to put your track on. Our track is of 1200*400 so the window
window = pygame.display.set_mode((1200,400))
track = pygame.image.load('track5.png')
car = pygame.image.load('tesla.png')

#by default the image of car is very big. so we shrink it
car = pygame.transform.scale(car, (30,60))

# to set position of car dynamically
car_x=155   #not 150 because we want to observe on right as well
car_y=300

#focal distance-> how far do you want camera to look. 
focal_dis = 15 + 10

#setting the direction
direction = 'up'

#clock to control speed of clock
clock = pygame.time.Clock()
drive = True

# camera offset initially to 0
cam_x_offset = 0
cam_y_offset = 0

while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    
# a camera in the car which will detect hurdles
    cam_x = car_x + cam_x_offset + 15 
    cam_y = car_y + cam_y_offset + 15
    
# you want to know where the road ends, that is where white color changes.
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    
# turning to right when front ends
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        # one thing you might miss out, that is -> camera's position. So we have an offset this offset will readjust it.
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)

# turing down when road ends
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)

# turning left when down road ends 
    elif direction=='down' and down_px != 255 and right_px == 255:
        direction ='right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)

# moving ahead to right
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
        
# moving the car fwd till road ends
    if direction == 'up' and up_px == 255:
        car_y = car_y - 2
    
# moving car down till road ends
    if direction == 'down' and down_px == 255:
        car_y = car_y + 2

        
#blit stands for block image transfer, we transfer our track to the window.
#(0,0) defines the start position
    window.blit(track,(0,0))
    
#window.blit(car,(0,0)) this will put your car on the origin of image, but we don't want that
    window.blit(car, (car_x,car_y))
    
# draw the camera, tell its color, position and radius
    pygame.draw.circle(window,(0,255,0),(cam_x,cam_y), 5, 5)
    
#then we ask pygame to update the display
    pygame.display.update()
    