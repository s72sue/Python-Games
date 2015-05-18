# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global deck_of_cards, card1_Index, card2_index, state, exposed, turns
    card1_index, card2_index, state, turns, = -1, -1, 0, 0
    deck_of_cards = range(8)*2
    exposed = [False]*16 
    random.shuffle(deck_of_cards)
    
     
# define event handlers
def mouseclick(pos):
    global state, turns, card1_index, card2_index
    card_index = list(pos)[0]//50
    
    if not exposed[card_index]:
        # case when the game has just started
        if state == 0: 
            card1_index = card_index
            exposed[card_index] = True
            state = 1
        # case when one card has been flipped by the player    
        elif state == 1: 
            card2_index = card_index
            exposed[card_index] = True
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
        # case when two cards have been flipped by the player       
        else: 
            if deck_of_cards[card1_index] != deck_of_cards[card2_index]:
                exposed[card1_index], exposed[card2_index] = False, False
                card1_index, card2_index = -1, -1
            card1_index = card_index
            exposed[card_index] = True
            state = 1 
    
                        
# each card is 50 pixels wide   
def draw(canvas):
    for index in range(16):
        if exposed[index]:
            canvas.draw_polygon([[index*50, 0], [(index+1)*50, 0], [(index+1)*50, 100], [index*50, 100]], 1, "Black", "White")
            canvas.draw_text(str(deck_of_cards[index]), (index*50+10, 70), 50, "Black")
        else:
            canvas.draw_polygon([[index*50, 0], [(index+1)*50, 0], [(index+1)*50, 100], [index*50, 100]], 1, "Black", "Green")
    label.set_text("Turns = " + str(turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
