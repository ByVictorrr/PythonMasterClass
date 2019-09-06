import random
try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter



def load_images(card_images):
    suits=['heart','club','diamond',"spade"]
    face_cards =['jack','queen','king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
    
    # for each suit, retrive the image for the cards
    for suit in suits:
        # first load the cards 1 to 10
        for card in range(1,11):
            name = 'cards/{}_{}.{}'.format(str(card),suit,extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card,image))
        
        # next load face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(card,suit,extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10,image))
        
        

def deal_card(frame):
    # pop the next card off the deck 
    next_card = deck.pop(0)
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the cards face value
    return next_card


def score_hand(hand):
    # calculate the total score of all cards in the list thats passed to it
    # only one ace can have the value 11, and this will be reduced to 1 if the hand woudl bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
           ace = True 
           card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score

    

def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 <= dealer_score < 17:
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
        dealer_hand.append(deal_card(dealer_card_frame))

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins")
    elif dealer_score > player_score:
        result_text.set("Dealer wins")
    else:
        result_text.set("DRAW")

    

def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand) 

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins")

    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # # initally treat an ace = 11
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we should bust, check if there is an ace and subtract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if(player_score > 21):
    #     result_text.set("Dealer winds!")
    # print(locals())



if __name__ == "__main__":

    mainWindow = tkinter.Tk()
    mainWindow.title("Black Jack")
    mainWindow.geometry("640x480")
    mainWindow.configure(background='green')

    # result label
    result_text = tkinter.StringVar()
    result = tkinter.Label(mainWindow, textvariable=result_text)
    result.grid(row=0, column=0, columnspan=3)

    # Game frame card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
    card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1,background='green')
    card_frame.grid(row=1, column=0, sticky='nw')


    ########################### Dealer Frame ########################################

    dealer_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
    tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

    # embedded frame hold the card images
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)


    #################### Player card ################################################


    player_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text="Player", background='green', fg='white').grid(row=2, column=0)
    tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)


    # embedded frame to hold the card images
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)


    # Button frame
    btn_frame = tkinter.Frame(mainWindow)
    btn_frame.grid(row=3, column=0, sticky='w')


    dealer_btn = tkinter.Button(btn_frame, text="Dealer", command=deal_dealer)
    dealer_btn.grid(row=0, column=0)

    player_btn = tkinter.Button(btn_frame, text="Player", command=deal_player)
    player_btn.grid(row=0, column=1)


    ####################################

    # load cards
    cards = []
    load_images(cards)
    # print(cards)

    # Create a new deck of cards and shuffle them
    deck = list(cards)
    random.shuffle(deck)

    # Create the list to store the dealer and and players hands
    dealer_hand = []
    player_hand = []


    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()



    mainWindow.mainloop()


    
