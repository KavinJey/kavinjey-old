#Created on 01/02/2017
#Jeyakavin Jeyaranjan
#Purpose: To make a game in compliance with https://docs.google.com/document/d/1ZxVrcnWdsic70nDUe38Cm-nfDJSdX670Ki6vmNpA5aE/edit
#         the above manual. Two player turn based game in which an attack and heal number are randomly generated.

import turtle
from turtle import *
import random



turtle.setup(width=750, height=750, startx=0, starty=0)
turtle = turtle.Turtle()
turtle.speed(0)




#Setting Sentry Variables

#This variable is used to tell the difference between the players, player1 being true and player2 being false
player = True
global player1_hp
global player2_hp
player2_hp = 10
player1_hp = 10



#Creating Character_1
def character1_head():
    turtle.penup()

    turtle.setposition(200,50)
    turtle.pendown()
    turtle.pensize(4)
    turtle.color("#808A87", "#000000")

    #Radius of circle/Size of head
    turtle.circle(35)
def character1_body():

   turtle.right(90)
   turtle.penup()
   turtle.forward(15)
   turtle.left(90)
   turtle.forward(45)
   turtle.right(90)
   turtle.pensize(6)
   turtle.pendown()

   #Width of body
   turtle.forward(100)
   turtle.right(90)

   #Length of body
   turtle.forward(85)
   turtle.right(90)

   turtle.forward(100)
   turtle.right(90)
   turtle.forward(85)
def character1_LeftArm():
    turtle.penup()
    turtle.forward(15)
    turtle.right(90)
    turtle.pendown()
    turtle.pensize(6)

    #Width of arm
    turtle.forward(80)
    turtle.left(90)
    #Length of arm
    turtle.forward(25)
    turtle.left(90)

    turtle.forward(80)
    turtle.left(90)
    turtle.forward(25)
def character1_RightArm():
    turtle.penup()
    turtle.forward(140)
    turtle.left(90)
    turtle.pendown()
    turtle.pensize(6)

    #Width of arm
    turtle.forward(80)
    turtle.left(90)

    #Length of arm
    turtle.forward(25)
    turtle.left(90)

    turtle.forward(80)
    turtle.left(90)
    turtle.forward(25)
def character1_LeftLeg():

    #Positioning
    turtle.penup()
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.pendown()
    turtle.pensize(6)

    #Width of leg
    turtle.forward(80)
    turtle.left(90)

    #Length of leg
    turtle.forward(35)
    turtle.left(90)

    turtle.forward(80)
    turtle.left(90)
    turtle.forward(35)
    turtle.left(90)
def character1_RightLeg():

    #Positioning
    turtle.penup()
    turtle.left(90)
    turtle.forward(55)
    turtle.right(90)
    turtle.pendown()


    #Width of leg
    turtle.forward(80)
    turtle.left(90)

    # Length of leg
    turtle.forward(35)
    turtle.left(90)

    turtle.forward(80)
    turtle.left(90)
    turtle.forward(35)
    turtle.left(90)


def character2_head():
    turtle.right(180)
    turtle.penup()

    turtle.setposition(-200, 50)
    turtle.pendown()
    turtle.pensize(4)
    turtle.color("#808A87", "#000000")

    # Radius of circle/Size of head
    turtle.circle(35)
def character2_body():
   turtle.right(90)
   turtle.penup()
   turtle.forward(15)
   turtle.left(90)
   turtle.forward(45)
   turtle.right(90)
   turtle.pensize(6)
   turtle.pendown()
   turtle.forward(100)
   turtle.right(90)
   turtle.forward(85)
   turtle.right(90)
   turtle.forward(100)
   turtle.right(90)
   turtle.forward(85)
def character2_LeftArm():
    turtle.penup()
    turtle.forward(15)
    turtle.right(90)
    turtle.pendown()
    turtle.pensize(6)

    # Width of arm
    turtle.forward(80)
    turtle.left(90)
    # Length of arm
    turtle.forward(25)
    turtle.left(90)

    turtle.forward(80)
    turtle.left(90)
    turtle.forward(25)
def character2_RightArm():
    turtle.penup()
    turtle.forward(140)
    turtle.left(90)
    turtle.pendown()
    turtle.pensize(6)

    # Width of arm
    turtle.forward(80)
    turtle.left(90)

    # Length of arm
    turtle.forward(25)
    turtle.left(90)

    turtle.forward(80)
    turtle.left(90)
    turtle.forward(25)
def character2_LeftLeg():

    #Positioning
    turtle.penup()
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.pendown()
    turtle.pensize(6)

    #Width of leg
    turtle.forward(80)
    turtle.left(90)

    #Length of leg
    turtle.forward(35)
    turtle.left(90)

    turtle.forward(80)
    turtle.left(90)
    turtle.forward(35)
    turtle.left(90)
def character2_RightLeg():

    #Positioning
    turtle.penup()
    turtle.left(90)
    turtle.forward(55)
    turtle.right(90)
    turtle.pendown()


    #Width of leg
    turtle.forward(80)
    turtle.left(90)

    # Length of leg
    turtle.forward(35)
    turtle.left(90)

    turtle.forward(80)
    turtle.left(90)
    turtle.forward(35)
    turtle.left(90)



#Character Nested Function
def character1():
    character1_head()
    character1_body()
    character1_LeftArm()
    character1_RightArm()
    character1_LeftLeg()
    character1_RightLeg()
def character2():
    character2_head()
    character2_body()
    character1_LeftArm()
    character2_RightArm()
    character2_LeftLeg()
    character2_RightLeg()

def drawing_bar():
    turtle.left(90)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color("black")

    # Length of HP bar
    turtle.forward(200)
    turtle.left(90)

    # Width of HP bar
    turtle.forward(25)
    turtle.left(90)

    turtle.forward(200)
    turtle.left(90)
    turtle.forward(25)

    #Drawing bars
    drawing_bars()
def drawing_bars():

    turtle.color("black")

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)

    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(180)
    turtle.penup()
    turtle.forward(25)


def player1_bar():
    turtle.penup()
    turtle.setposition(100, 200)
    drawing_bar()
def player2_bar():
    turtle.penup()
    turtle.setposition(-300, 200)
    drawing_bar()


def intial_filling():
    turtle.penup()
    turtle.pensize(0)
    turtle.color("red")
    # Filling player 1 bar
    turtle.begin_fill()
    turtle.setposition(100,200)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()
    turtle.penup()

    #Filling player 2 bar
    turtle.begin_fill()
    turtle.setposition(-300, 200)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()
    turtle.penup()



def heal(player):
    turtle.pensize(1)
    if player == True:
        #Player One activates heal
        global player1_hp
        heal_amount = random.randint(1, 8)
        print player1_hp

        hp_bar_status = player1_hp + heal_amount


        if hp_bar_status >= 10:
            hp_bar_status = 10
            player1_hp = 10

        elif hp_bar_status < 10:
            player1_hp = player1_hp + heal_amount
            hp_bar_status = player1_hp


        print player1_hp

        amount_healed = hp_bar_status * 20

        #Drawing of heal
        turtle.penup()
        turtle.setposition(300, 200)
        turtle.color("red")
        turtle.begin_fill()
        turtle.pendown()
        turtle.right(90)
        turtle.forward(amount_healed)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(amount_healed)
        turtle.right(90)
        turtle.forward(25)
        turtle.end_fill()


        #Redrawing bars
        turtle.setposition(100, 200)
        turtle.seth(270)
        drawing_bar()




    elif player == False:
        #player Two activates heal
        global player2_hp
        heal_amount = random.randint(1, 8)
        print player2_hp

        hp_bar_status = player2_hp + heal_amount

        if hp_bar_status >= 10:
            hp_bar_status = 10
            player2_hp = 10

        elif hp_bar_status < 10:
            player2_hp = player2_hp + heal_amount
            hp_bar_status = player2_hp

        print player2_hp

        amount_healed = hp_bar_status * 20
        # Drawing of heal
        turtle.penup()
        turtle.setposition(-300, 200)
        turtle.color("red")
        turtle.begin_fill()
        turtle.pendown()
        turtle.left(90)
        turtle.forward(amount_healed)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(amount_healed)
        turtle.left(90)
        turtle.forward(25)
        turtle.end_fill()

        # Redrawing bars
        turtle.setposition(-300, 200)
        turtle.seth(270)
        drawing_bars()
        turtle.setposition(-300, 200)
        turtle.seth(270)
        drawing_bar()
def attack(player):
    turtle.pensize(1)
    if player == True:
        #Player One activates attack
        global player2_hp

        dmg_amount = random.randint(1, 8)
        print player2_hp

        player2_hp = player2_hp - dmg_amount
        hp_bar_status = 10 - player2_hp


        print player2_hp

        amount_taken = hp_bar_status * 20
        # Drawing of atk
        turtle.penup()
        turtle.begin_fill()
        turtle.setposition(-100, 200)
        turtle.seth(270)
        turtle.color("black")
        turtle.pendown()
        turtle.right(90)
        turtle.forward(amount_taken)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(amount_taken)
        turtle.right(90)
        turtle.forward(25)
        turtle.end_fill()

    elif player == False:
        #Player Two activates attack
        global player1_hp

        dmg_amount = random.randint(1, 8)
        print player1_hp


        player1_hp = player1_hp - dmg_amount
        hp_bar_status = 10 - player1_hp




        print player1_hp

        amount_taken = hp_bar_status * 20

        # Drawing of atk
        turtle.penup()
        turtle.begin_fill()
        turtle.setposition(100, 200)
        turtle.seth(270)
        turtle.color("black")
        turtle.pendown()
        turtle.left(90)
        turtle.forward(amount_taken)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(amount_taken)
        turtle.left(90)
        turtle.forward(25)
        turtle.end_fill()


# Drawing Arrows and text
def arrows():
    # Drawing Arrows
    turtle.penup()
    turtle.seth(0)
    turtle.setposition(50, 50)
    turtle.pendown()
    turtle.pensize(1)
    turtle.begin_fill()
    for i in range(1):
        turtle.right(150)
        turtle.forward(25)

    turtle.left(150)
    turtle.forward(45)
    turtle.end_fill()

    y = turtle.ycor()
    turtle.setposition(50, y)
    turtle.right(90)
    turtle.pensize(10)

    turtle.forward(30)

    # Second

    turtle.penup()
    turtle.seth(0)
    turtle.setposition(-50, 0)
    turtle.pendown()
    turtle.pensize(1)
    turtle.begin_fill()
    for i in range(1):
        turtle.left(150)
        turtle.forward(25)

    turtle.right(150)
    turtle.forward(45)
    turtle.end_fill()

    y = turtle.ycor()
    turtle.setposition(-50, y)
    turtle.right(270)
    turtle.pensize(10)

    turtle.forward(30)
def writing():
    turtle.penup()
    turtle.setposition(-50,-15)
    turtle.pencolor("Blue")
    turtle.write("Heal", True, align="center")

    turtle.penup()
    turtle.setposition(50, -15)
    turtle.pencolor("Red")
    turtle.write("Attack", True, align="center")


#START OF PROGRAM

character1()

#Setting the pen direction before drawing the second character
turtle.right(90)

character2()

#Drawing Health Bars
intial_filling()
player1_bar()
player2_bar()

#Drawing Arrows
arrows()
writing()



#Main Game Loop
while player1_hp > 0 and player2_hp > 0:
    if player == True:
        move = raw_input("Player One. Attack or Heal?\n")

        if move == "Attack" or move == "attack":
            attack(player)
            player = False

        elif move == "Heal" or move== "heal":
            heal(player)
            player = False

        else:
            print "invalid move"
            player = True





    elif player == False:
        move = raw_input("Player Two. Attack or Heal?\n")

        if move == "Attack" or move == "attack":
            attack(player)
            player = True

        elif move == "Heal" or move == "heal":
            heal(player)
            player = True

        else:
            print "invalid move"
            player = False


if player == True:
    print "Player Two Won!"

elif player == False:
    print "Player One Won!"


raw = input("waiting...")