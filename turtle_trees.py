from turtle import *
import random

def draw_tree():
    width(6)
    seth(90)
    #Begin drawing
    fd(random.randint(90, 130))

    for i in range (0, 7):
        my_pos = pos() #Store initial position
        
        #Move to postition
        penup()
        goto(my_pos)
        pendown()
        
        #Draw
        draw_branch()
        draw_twig()
        
        #Go back to position
        penup()
        goto(my_pos)
        pendown()

def draw_branch():
    seth(random.randint(10, 180)) #set branch angle
    width(4)
    fd(random.randint(30, 40))
    draw_twig()
    
def draw_twig():
    my_pos = pos() #Store initial position
    
    #Move to postition
    penup()
    goto(my_pos)
    pendown()
        
    seth(random.randint(10,180)) #set twig angle
    width(2)
    fd(random.randint(10, 20))
    color('#0a9b2a', '#0a9b2a')
    width(5)
    fd(1)
    
    #Go back to position
    penup()
    goto(my_pos)
    pendown()

    #Reset vars
    color('#703008', '#703008')
    width(2)
    

def main():
    #Setup variables
    bgcolor('#ffffff')
    color('#703008', '#703008')
    width(6)
    seth(90)
    speed(10)
    hideturtle()

    num_trees = 10
    
    for i in range(0,num_trees):
        penup()
        setpos(random.randint(-200, 200),random.randint(-30, 30))
        pendown()
        
        draw_tree()
    
    done()

if __name__ == '__main__':
    main()
    
