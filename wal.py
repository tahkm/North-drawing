import pygame
import random
import colour

pygame.init()
window = pygame.display.set_mode( [1500, 800] )

clock = pygame.time.Clock()


rect_x = 1450

rect_color = (200, 200, 100)

moving_left = False
moving_right = False
is_drawing = False
is_released = False
old_mouse = (0,0)
times_drawn = 0

gravity = 1

mouse_list = []

iteration = 0

rand = random.randint(0, 255)
rand1 = random.randint(0,255)
rand2 = random.randint(0,255)

fColor = colour.Color("black")

while True:
    mouse_pos = pygame.mouse.get_pos()
    window.fill([0,0,0])
    #draw slab character
    pygame.draw.rect(window, rect_color, pygame.Rect(rect_x, 700, 250, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                is_drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            is_drawing = False
            is_released = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                moving_left = True

            elif event.key == pygame.K_d:
                moving_right = True




            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False

            elif event.key == pygame.K_d:
                moving_right = False



    if moving_right:
        rect_x += 10

    elif moving_left:
        rect_x -= 10

    elif is_drawing:
        #list of all previous locations?
        #print("drawing")


        n = len(mouse_list)

        #RGB
        color_r = min(  int( rand ), 255 )
        color_g = min(  int( rand1 ), 255 )
        color_b = min(  int( rand2 ), 255 )
        #r = max(color_r, color_g, color_b)
        #for i in range(255-r):
        color = ( color_r, color_g, color_b )
        
        mouse_list.append( [mouse_pos[0], mouse_pos[1], 0.1, color ] )
        #print(mouse_list)
        times_drawn += 1
        pygame.draw.circle(window, (255, 255, 255), mouse_pos, 5)


    
    
    n = len(mouse_list)

    color_list = list(fColor.range_to("cyan", max(n, 1)))
    
    newmouse_list = []
    for i in range( n ):                #2D array order because its a 2D array need to access second array (mouse_list)
        x = mouse_list[i][0]
        y = mouse_list[i][1]
        speed = mouse_list[i][2]
        #color = mouse_list[i][3]
        color = color_list[i]
        r = int(color.get_red() * 255)
        g = int(color.get_green() * 255)
        b = int(color.get_blue() * 255)
        

        mouse_list[i][1] = y + speed


        
        
        

        #print( f'color = ({color_r}, {color_g}, {color_b})')
        if y <= 800 and y >= 0:
            newmouse_list.append( mouse_list[i] )

        pygame.draw.circle(window, [r, g, b], ( mouse_list[i][0], y  ), 5)

        if speed >0 and x >= rect_x and x <= rect_x + 250 and y >= 700 and y <= 730:
            mouse_list[i][2] = -0.1


    mouse_list = newmouse_list

        
        

    iteration += 1
    #elif is_released:
        #print("released")
    #pygame.draw.circle(window, (255, 255, 255), mouse_pos , 5)
    #pygame.draw.circle(window, (255, 255, 255), ch, 5)
        
    clock.tick(120)

    pygame.display.flip()
