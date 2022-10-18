#Black Jack
#Finished! Maybe add some decorations when you have time!

from random import seed
from random import shuffle
from tkinter import *

import os

seed()
deck = list(range(52))
#Test decks:
#[0,5,12,18,7,2,35,7,8,3,1,2,45] You get black Jack
#[4,1,7,14,27,40,2,0,13,26,39,15] max number of cards dealer could get
#[4,17,7,20,3,16] tied for double down
#[20,5,7,18,39,33,1,46,8,3,0,2,45] Elligible for splitting
#[1,5,14,18,27,40,20,46,8,3,0,2,45] Another version for splitting
#[1,5,14,18,27,40,20,46,8,3,0,2,45,26,4,30,36,39,44,51,22,19,15] Another version for splitting
shuffle(deck)

#Player's Hand
yourCardInd = []
yourCardDsp = []
yourCardVal = []
yourScore = 0.0

betAmountUse = 0
yourCardInd2 = []
yourCardDsp2 = []
yourCardVal2 = []
yourScore2 = 0.0
betAmount2 = 0.0

yourCardInd3 = []
yourCardDsp3 = []
yourCardVal3 = []
yourScore3 = 0.0
betAmount3 = 0.0

yourCardInd4 = []
yourCardDsp4 = []
yourCardVal4 = []
yourScore4 = 0.0
betAmount4 = 0.0

#Dealer's Hand
dealersCardInd = []
dealersCardVal = []
dealersCardDsp = []
dealersScore = 0.0

#=============================================Frame and Beginning Mechanics of the Game===================================================|
def startProgram():
    global madeByLabel
    global welcomeLabel
    global cardOutline
    global deck
    global yourCardInd
    global yourCardDsp
    global dealersScore
    global yourScore
    global dealButton
    global noDealButton
    global bettingSystemlbl
    global yourScoreInGamelbl
    global dealersScoreInGamelbl
    global noDealButton
    global dealButton
    global shuffleButton
    global dealersHandLbl
    global yourHandLbl
    global yourScoreInGameActuallbl
    global yourMoney
    global betAmount
    global reBet
    global yourMoneylbl
    global yourMoneyActuallbl
    global betAmountlbl
    global betAmountActuallbl
    global betAmountActualText
    global n
    global deck_split
    deck_split = 0
    n = 0
    reBet = "Yes"
    bettingSystemlbl.destroy()
    madeByLabel.destroy()
    welcomeLabel.destroy()
    startButton.destroy()
    instructionsButton.destroy()
    bettinglbl.pack()
    bettinglbl.pack_forget()
    yourScoreInGamelbl = Label(root, text = "Your Score:")
    yourScoreInGamelbl.place(x = 1240, y = 330, anchor = "center")
    dealersScoreInGamelbl = Label(root, text = "Dealer's Score:")
    dealersScoreInGamelbl.place(x = 1237, y = 20, anchor = "center")
    dealersScoreUse.set("?")
    dealersScoreInGameActuallbl.place(x = 1285, y = 20, anchor = "center")
    noDealButton = Button(root, text = "Stay", command = noDeal, width = 12, height = 3)
    dealButton = Button(root, text = "Hit", command = deal, width = 12, height = 3)
    doubleDownButton.place(x = 280, y = 700, anchor = "center")
    splitButton.place(x = 390, y = 700, anchor = "center")
    dealButton.place(x = 60, y = 700, anchor = "center")
    noDealButton.place(x = 170, y = 700, anchor = "center")
    shuffleButton = Button(root, text = "Shuffle", command = reset, width = 12, height = 3)
    shuffleButton.place(x = 1280, y = 700, anchor = "center")
    dealersHandLbl = Label(root, text = "Dealer's Hand")
    dealersHandLbl.place (x = 50, y = 20, anchor = "center")
    yourHandLbl = Label(root, text = "Your Hand")
    yourHandLbl.place(x = 40, y = 330, anchor = "center")
    casinoGreenlbl.place(x= 675, y = 375, anchor = "center")
    
                                            #----------------Initial 2 Cards-----------------#
    card = deck.pop(0)
    yourCardInd.append(card)
    yourCardDsp.append(cardDisplay(card))
    yourCardVal.append(min((card % 13) + 1, 10))
    displayCard(yourCardDsp[0],0,0,0,0,1) #displayCard(card,n,d,s,n_s,deck)
    
    card = deck.pop(0)
    dealersCardInd.append(card)
    dealersCardDsp.append(cardDisplay(card))
    dealersCardVal.append(min((card % 13) + 1, 10))
    
                                            #----------------Final 2 Cards-----------------#
    
    card = deck.pop(0)
    yourCardInd.append(card)
    yourCardDsp.append(cardDisplay(card))
    yourCardVal.append(min((card % 13) + 1, 10))
    n += 1
    displayCard(yourCardDsp[1],1,0,0,0,1)
    yourScore = sumCards(yourCardVal)
    yourScoreUse.set(yourScore)
    yourScoreInGameActuallbl.place(x = 1290, y = 330, anchor = "center")
    displayCard("Hidden",0,1,0,0,1) #displayCard(card,n,d,s,n_s,deck)
    
    card = deck.pop(0)
    dealersCardInd.append(card)
    dealersCardDsp.append(cardDisplay(card))
    dealersCardVal.append(min((card % 13) + 1, 10))
    displayCard(dealersCardDsp[1],1,1,0,0,1)
    dealersScore = sumCards(dealersCardVal)
    yourMoneylbl.place(x = 875, y = 715, anchor = "w")
    yourMoneyActuallbl.place(x = 1010, y = 715, anchor = "e")
    betAmountlbl = Label(root, text = "Betting Amount: ")
    betAmountlbl.place(x= 875, y = 685, anchor = "w")
    betAmountActualText = StringVar()
    betAmountActualText.set(betAmount)
    betAmountActuallbl = Label(root, textvariable = betAmountActualText)
    betAmountActuallbl.place(x = 1010, y = 685, anchor = "e")
    if (yourScore == 21) and (len(yourCardInd) == 2):
        endGame()



def displayCard(card,n,d,s,n_s,deck): #if d = 0 for player and d = 1 for dealer s = 0 for not split and s= 1 for split, n_s for number of splits
    if d == 0 and s == 0 and deck == 1: # normal case for player with no splitting
        x_0 = 125*n + 75
        y_0 = 475
    if d == 1 and s == 0 and deck == 1: # normal case for dealer with no splitting
        x_0 = 125*n + 75
        y_0 = 170
    if d == 0 and s == 1 and deck == 1: # case for player with splitting (first deck)
        x_0 = 25*n + 75
        y_0 = 475
    if d == 0 and s == 1 and deck == 2: # case for player with splitting (second deck)
        x_0 = 25*n + 350
        y_0 = 475
    if d == 0 and s == 1 and deck == 3: # case for player with splitting (third deck)
        x_0 = 25*n + 625
        y_0 = 475
    if d == 0 and s == 1 and deck == 4: # case for player with splitting (fourth deck)
        x_0 = 25*n + 900
        y_0 = 475
        
    if card == "2♥":
        twoHeartslbl.lift()
        twoHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "2♦":
        twoDiamondslbl.lift()
        twoDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "2♣":
        twoClubslbl.lift()
        twoClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "2♠":
        twoSpadeslbl.lift()
        twoSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "3♥":
        threeHeartslbl.lift()
        threeHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "3♦":
        threeDiamondslbl.lift()
        threeDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "3♣":
        threeClubslbl.lift()
        threeClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "3♠":
        threeSpadeslbl.lift()
        threeSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "4♥":
        fourHeartslbl.lift()
        fourHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "4♦":
        fourDiamondslbl.lift()
        fourDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "4♣":
        fourClubslbl.lift()
        fourClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "4♠":
        fourSpadeslbl.lift()
        fourSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "5♥":
        fiveHeartslbl.lift()
        fiveHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "5♦":
        fiveDiamondslbl.lift()
        fiveDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "5♣":
        fiveClubslbl.lift()
        fiveClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "5♠":
        fiveSpadeslbl.lift()
        fiveSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "6♥":
        sixHeartslbl.lift()
        sixHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "6♦":
        sixDiamondslbl.lift()
        sixDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "6♣":
        sixClubslbl.lift()
        sixClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "6♠":
        sixSpadeslbl.lift()
        sixSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "7♥":
        sevenHeartslbl.lift()
        sevenHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "7♦":
        sevenDiamondslbl.lift()
        sevenDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "7♣":
        sevenClubslbl.lift()
        sevenClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "7♠":
        sevenSpadeslbl.lift()
        sevenSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "8♥":
        eightHeartslbl.lift()
        eightHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "8♦":
        eightDiamondslbl.lift()
        eightDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "8♣":
        eightClubslbl.lift()
        eightClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "8♠":
        eightSpadeslbl.lift()
        eightSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "9♥":
        nineHeartslbl.lift()
        nineHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "9♦":
        nineDiamondslbl.lift()
        nineDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "9♣":
        nineClubslbl.lift()
        nineClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "9♠":
        nineSpadeslbl.lift()
        nineSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "10♥":
        tenHeartslbl.lift()
        tenHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "10♦":
        tenDiamondslbl.lift()
        tenDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "10♣":
        tenClubslbl.lift()
        tenClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "10♠":
        tenSpadeslbl.lift()
        tenSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "J♥":
        jackHeartslbl.lift()
        jackHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "J♦":
        jackDiamondslbl.lift()
        jackDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "J♣":
        jackClubslbl.lift()
        jackClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "J♠":
        jackSpadeslbl.lift()
        jackSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "Q♥":
        queenHeartslbl.lift()
        queenHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "Q♦":
        queenDiamondslbl.lift()
        queenDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "Q♣":
        queenClubslbl.lift()
        queenClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "Q♠":
        queenSpadeslbl.lift()
        queenSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "K♥":
        kingHeartslbl.lift()
        kingHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "K♦":
        kingDiamondslbl.lift()
        kingDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "K♣":
        kingClubslbl.lift()
        kingClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "K♠":
        kingSpadeslbl.lift()
        kingSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "A♥":
        aceHeartslbl.lift()
        aceHeartslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "A♦":
        aceDiamondslbl.lift()
        aceDiamondslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "A♣":
        aceClubslbl.lift()
        aceClubslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "A♠":
        aceSpadeslbl.lift()
        aceSpadeslbl.place(x = x_0, y = y_0, anchor = "center")
    elif card == "Hidden":
        cardBacklbl.lift()
        cardBacklbl.place(x = x_0, y = y_0, anchor = "center")
            
        
#================================================================================================================================|
def deal():
    global DoneDeal
    global deck
    global yourCardDsp
    global yourCardInd
    global yourCardVal
    global yourScore
    global n
    global n_2
    global n_3
    global n_4
    global deck_split
    global num_split
    global yourScore
    global yourScore2
    global yourScore3
    global yourScore4
    global dd
    #(card,n,d,s,n_s,deck)
    if(DoneDeal == "Yes"):
        globalMessageText.set("Deal is over! Cannot deal anymore!")
    else:
        if deck_split == 1 or num_split == 0:
            if (n < 4):
                yourNextCard = deck.pop(0)
                yourCardInd.append(yourNextCard)
                yourCardDsp.append(cardDisplay(yourNextCard))
                yourCardVal.append(min((yourNextCard % 13) + 1, 10))
                yourScore = sumCards(yourCardVal)
                yourScoreUse.set(yourScore)
                yourScoreInGameActuallbl.place(x = 1290, y = 330, anchor = "center")
                if (yourScore > 21) and dd != "Yes":
                    noDeal()
                n += 1
                if num_split == 0:
                    displayCard(cardDisplay(yourNextCard),n,0,0,0,1)
                else:
                    displayCard(cardDisplay(yourNextCard),n,0,1,num_split,1)
                
            if ((yourScore <= 21) and (len(yourCardInd) == 5)) and dd != "Yes":
                noDeal()
        elif deck_split == 2:
            if (n_2 < 4):
                yourNextCard = deck.pop(0)
                yourCardInd2.append(yourNextCard)
                yourCardDsp2.append(cardDisplay(yourNextCard))
                yourCardVal2.append(min((yourNextCard % 13) + 1, 10))
                yourScore2 = sumCards(yourCardVal2)
                yourScoreUse.set(yourScore2)
                yourScoreInGameActuallbl.place(x = 1290, y = 330, anchor = "center")
                if (yourScore2 > 21) and dd != "Yes":
                    print("Here")
                    noDeal()
                n_2 += 1
                displayCard(cardDisplay(yourNextCard),n_2,0,1,num_split,2)
                
            if ((yourScore2 <= 21) and (len(yourCardInd2) == 5)) and dd != "Yes":
                noDeal()
        elif deck_split == 3:
            if (n_3 < 4):
                yourNextCard = deck.pop(0)
                yourCardInd3.append(yourNextCard)
                yourCardDsp3.append(cardDisplay(yourNextCard))
                yourCardVal3.append(min((yourNextCard % 13) + 1, 10))
                yourScore3 = sumCards(yourCardVal3)
                yourScoreUse.set(yourScore3)
                yourScoreInGameActuallbl.place(x = 1290, y = 330, anchor = "center")
                if (yourScore3 > 21) and dd != "Yes":
                    noDeal()
                n_3 += 1
                displayCard(cardDisplay(yourNextCard),n_3,0,1,num_split,3)
                
            if ((yourScore3 <= 21) and (len(yourCardInd3) == 5)) and dd != "Yes":
                noDeal()
                
        elif deck_split == 4:
            if (n_4 < 4):
                yourNextCard = deck.pop(0)
                yourCardInd4.append(yourNextCard)
                yourCardDsp4.append(cardDisplay(yourNextCard))
                yourCardVal4.append(min((yourNextCard % 13) + 1, 10))
                yourScore4 = sumCards(yourCardVal4)
                yourScoreUse.set(yourScore4)
                yourScoreInGameActuallbl.place(x = 1290, y = 330, anchor = "center")
                if (yourScore4 > 21) and dd != "Yes":
                    noDeal()
                n_4 += 1
                displayCard(cardDisplay(yourNextCard),n_4,0,1,num_split,4)
                
            if ((yourScore4 <= 21) and (len(yourCardInd4) == 5)) and dd != "Yes":
                noDeal()


def noDeal():
    global DoneDeal
    global deck
    global dealersCardDsp
    global dealersCardInd
    global dealersCardVal
    global dealersScore
    global dealButton
    global noDealButton
    global deck_split
    global num_split
    global dd
    if(DoneDeal == "Yes"):
        globalMessageText.set("Deal is over! cannot stay!")
    else:
        if num_split == 0 or deck_split == num_split + 1:
            z = 1
            DoneDeal = "Yes"
            dealersScoreUse.set(dealersScore)
            dealersScoreInGameActuallbl.place(x = 1300, y = 20, anchor = "center")
            cardBacklbl.pack()
            cardBacklbl.pack_forget()
            displayCard(dealersCardDsp[1],1,1,0,0,1)
            if (dealersScore == 21) and (len(dealersCardInd) == 2):
                endGame()
            while (dealersScore <= 16):
                    dealersScoreUse.set(dealersScore)
                    card = deck.pop(0)
                    dealersCardInd.append(card)
                    dealersCardDsp.append(cardDisplay(card))
                    dealersCardVal.append(min((card % 13) + 1, 10))
                    dealersScore = sumCards(dealersCardVal)
                    dealersScoreUse.set(dealersScore)
                    dealersScoreInGameActuallbl.place(x = 1300, y = 20, anchor = "center")
                    z += 1
                    displayCard(cardDisplay(card),z,1,0,0,1)
            print("Dealer's New Score: " + str(dealersScore))
            print("Dealer's New Hand: " + str(dealersCardDsp))
            endGame()
        else:
            deck_split += 1
            globalMessageText.set("From the order of left to right. You are currently on Hand " + str(deck_split))
            globalMessagelbl.place(x = 20, y = 640, anchor = "w")
            if num_split == 1:
                if deck_split == 1:
                    resetField()
                    handOne2lbl.place(x = 675, y = 375, anchor = "center")
                    yourScoreUse.set(yourScore1)
                if deck_split == 2:
                    resetField()
                    hand1Twolbl.place(x = 675, y = 375, anchor = "center")
                    yourScoreUse.set(yourScore2)
            if num_split == 2:
                if deck_split == 1:
                    resetField()
                    handOne23lbl.place(x = 675, y = 375, anchor = "center")
                    yourScoreUse.set(yourScore1)
                if deck_split == 2:
                    resetField()
                    hand1Two3lbl.place(x = 675, y = 375, anchor = "center")
                    yourScoreUse.set(yourScore2)
                if deck_split == 3:
                    resetField()
                    hand12Threelbl.place(x = 675, y = 375, anchor = "center")
                    yourScoreUse.set(yourScore3)
            if num_split == 3:
                if deck_split == 1:
                    resetField()
                    handOne234lbl.place(x = 675, y = 375, anchor = "center")
                    yourScoreUse.set(yourScore1)
                if deck_split == 2:
                    resetField()
                    hand1Two34lbl.place(x = 675, y = 375, anchor = "center")
                    yourScoreUse.set(yourScore2)
                if deck_split == 3:
                    resetField()
                    hand12Three4lbl.place(x = 675, y = 375, anchor = "center")
                    yourScoreUse.set(yourScore3)
                if deck_split == 4:
                    resetField()
                    hand123Fourlbl.place(x = 675, y = 375, anchor = "center")
                    yourScoreUse.set(yourScore4)
def doubleDown():
    global betAmount
    global yourMoney
    global betAmount2
    global betAmount3
    global betAmount4
    global betAmountUse
    global doubleDAct
    global dd
    global deck_split
    global n
    global n_2
    global n_3
    global n_4
    #add the function to deny dd if money is not enough
    if(DoneDeal == "Yes"):
        globalMessageText.set("Deal is over! Cannot use double down anymore!")
    else:
        yourMoney -= betAmount
        if deck_split == 1 and n == 1:
            betAmountUse = 2*betAmount
            dd = "Yes"
        elif deck_split == 2 and n_2 == 1:
            betAmount2 += betAmount
        elif deck_split == 3 and n_3 == 1:
            betAmount3 += betAmount
        elif deck_split == 4 and n_4 == 1:
            betAmount4 += betAmount
        elif deck_split == 0 and n == 1:
            betAmount = 2*betAmount
        else:
            globalMessageText.set("You have already dealt. You can no longer double down")
            globalMessagelbl.place(x = 20, y = 640, anchor = "w")
            return None
        deal()
        if DoneDeal != "Yes":
            noDeal()
        if dd == "Yes":
            betAmountActualText.set(betAmountUse + betAmount2 + betAmount3 + betAmount4)
        else:
            betAmountActualText.set(betAmount + betAmount2 + betAmount3 + betAmount4)
    yourMoneyActualText.set(yourMoney)

def split():
    global betAmount
    global betAmount2
    global betAmount3
    global betAmount4
    global yourMoney
    global yourCardInd
    global yourCardDsp
    global yourCardVal
    global yourScore
    global yourScore2
    global yourScore3
    global yourScore4
    global yourCardInd2
    global yourCardDsp2
    global yourCardVal2
    global yourScore2
    global num_split
    global n_2
    global n_3
    global n_4
    global n
    global deck_split
    #(card,n,d,s,n_s,deck)
    if(DoneDeal == "Yes"):
        globalMessageText.set("Deal is over! Cannot split anymore!")
    else:
        if num_split == 0:
            if len(yourCardDsp) != 2:
                globalMessageText.set("You do not have the requirements for a split")
                globalMessagelbl.place(x = 20, y = 640, anchor = "w")
            elif (yourCardDsp[0])[0] != (yourCardDsp[1])[0]:
                globalMessageText.set("Your cards are not the same. Cannot Split")
                globalMessagelbl.place(x = 20, y = 640, anchor = "w")
            else:
                yourMoney -= betAmount
                betAmount2 = betAmount
                deck_split = 1
                yourCardInd2.append(yourCardInd.pop(1))
                yourCardDsp2.append(yourCardDsp.pop(1))
                yourCardVal2.append(yourCardVal.pop(1))
                yourScore2 = sumCards(yourCardVal2)
                n = 0
                n_2 = 0
                num_split = 1
                globalMessageText.set("From the order of left to right. You are currently on Hand " + str(deck_split))
                globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                resetField()
                handOne2lbl.place(x= 675, y = 375, anchor = "center")
                yourScoreUse.set(sumCards(yourCardVal))
        else:
            if deck_split == 1:
                if len(yourCardDsp) != 2:
                    globalMessageText.set("You do not have the requirements for a split")
                    globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                elif (yourCardDsp[0])[0] != (yourCardDsp[1])[0]:
                    globalMessageText.set("Your cards are not the same. Cannot Split")
                    globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                else:
                    yourMoney -= betAmount
                    if num_split == 1:
                        yourCardDsp3.append(yourCardDsp.pop(1))
                        yourCardInd3.append(yourCardInd.pop(1))
                        yourCardVal3.append(yourCardVal.pop(1))
                        yourScore3 = sumCards(yourCardVal3)
                        resetField()
                        handOne23lbl.place(x= 675, y = 375, anchor = "center")
                        betAmount3 = betAmount
                        n_3 = 0
                    if num_split == 2:
                        yourCardDsp4.append(yourCardDsp.pop(1))
                        yourCardInd4.append(yourCardInd.pop(1))
                        yourCardVal4.append(yourCardVal.pop(1))
                        yourScore4 = sumCards(yourCardVal4)
                        resetField()
                        handOne234lbl.place(x = 675, y = 375, anchor = "center")
                        betAmount4 = betAmount
                        n_4 = 0
                    n = 0
                    num_split += 1
                    globalMessageText.set("From the order of left to right. You are currently on Hand " + str(deck_split))
                    globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                    yourScoreUse.set(sumCards(yourCardVal))
                           
            if deck_split == 2:
                if len(yourCardDsp2) != 2:
                    globalMessageText.set("You do not have the requirements for a split")
                    globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                elif (yourCardDsp2[0])[0] != (yourCardDsp2[1])[0]:
                    globalMessageText.set("Your cards are not the same. Cannot Split")
                    globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                else:
                    yourMoney -= betAmount
                    if num_split == 1:
                        yourCardDsp3.append(yourCardDsp2.pop(1))
                        yourCardInd3.append(yourCardInd2.pop(1))
                        yourCardVal3.append(yourCardVal2.pop(1))
                        yourScore3 = sumCards(yourCardVal3)
                        n_3 = 0
                        resetField()
                        hand1Two3lbl.place(x= 675, y = 375, anchor = "center")
                        betAmount3 = betAmount2
                    if num_split == 2:
                        yourCardDsp4.append(yourCardDsp2.pop(1))
                        yourCardInd4.append(yourCardInd2.pop(1))
                        yourCardVal4.append(yourCardVal2.pop(1))
                        yourScore4 = sumCards(yourCardVal4)
                        resetField()
                        hand1Two34lbl.place(x = 675, y = 375, anchor = "center")
                        betAmount4 = betAmount2
                        n_4 = 0
                    n_2 = 0  
                    num_split += 1
                    globalMessageText.set("From the order of left to right. You are currently on Hand " + str(deck_split))
                    globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                    yourScoreUse.set(sumCards(yourCardVal2))
                    
            if deck_split == 3:
                if len(yourCardDsp3) != 2:
                    globalMessageText.set("You do not have the requirements for a split")
                    globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                elif (yourCardDsp3[0])[0] != (yourCardDsp3[1])[0]:
                    globalMessageText.set("Your cards are not the same. Cannot Split")
                    globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                else:
                    num_split += 1
                    yourMoney -= betAmount3
                    betAmount4 = betAmount3
                    yourCardDsp4.append(yourCardDsp3.pop(1))
                    yourCardInd4.append(yourCardInd3.pop(1))
                    yourCardVal4.append(yourCardVal3.pop(1))
                    yourScore4 = sumCards(yourCardVal4)
                    n_3 = 0
                    n_4 = 0
                    resetField()
                    hand12Three4lbl.place(x= 675, y = 375, anchor = "center")
                    yourScoreUse.set(sumCards(yourCardVal3))
            if deck_split == 4:
                globalMessageText.set("You can no longer split")
                globalMessagelbl.place(x = 20, y = 640, anchor = "w")
                yourScoreUse.set(sumCards(yourCardVal4))
        if num_split != 0:
            resetCards()
            displayCard(dealersCardDsp[1],1,1,0,num_split,1)
            n_sub = 0
            i = 0
            while i in range(len(yourCardDsp)):
                displayCard(yourCardDsp[i],n_sub,0,1,num_split,1)
                n_sub += 1
                i += 1
            n_sub = 0
            i = 0
            while i in range(len(yourCardDsp2)):
                displayCard(yourCardDsp2[i],n_sub,0,1,num_split,2)
                n_sub += 1
                i += 1
            n_sub = 0
            i = 0
            while i in range(len(yourCardDsp3)):
                displayCard(yourCardDsp3[i],n_sub,0,1,num_split,3)
                n_sub += 1
                i += 1
            n_sub = 0
            i = 0
            while i in range(len(yourCardDsp4)):
                displayCard(yourCardDsp4[i],n_sub,0,1,num_split,4)
                n_sub += 1
                i += 1
    yourMoneyActualText.set(yourMoney)
    betAmountActualText.set(betAmount + betAmount2 + betAmount3 + betAmount4)
    
    
def reset():
    global yourMoney
    global bettingSystemlbl
    global deck
    global n
    global n_2
    global n_3
    global n_4
    global yourScore
    global dealersScore
    global DoneDeal
    global num_split
    global deck_split
    global dd
    global betAmount
    global betAmount2
    global betAmount3
    global betAmount4
    deck = list(range(52))
    #Test decks:
    #[0,5,12,18,7,2,35,7,8,3,1,2,45] You get black Jack
    #[4,1,7,14,27,40,2,0,13,26,39,15] max number of cards dealer could get
    #[4,17,7,20,3,16] tied for double down
    shuffle(deck)
    del yourCardInd[:]   
    del yourCardDsp[:]
    del yourCardVal[:]
    del yourCardInd2[:]   
    del yourCardDsp2[:]
    del yourCardVal2[:]
    del yourCardInd3[:]   
    del yourCardDsp3[:]
    del yourCardVal3[:]
    del yourCardInd4[:]   
    del yourCardDsp4[:]
    del yourCardVal4[:]
    del dealersCardInd[:]
    del dealersCardVal[:]
    del dealersCardDsp[:]
    DoneDeal = " "
    n = 0
    n_2 = 0
    n_3 = 0
    n_4 = 0
    betAmount = 0
    betAmount2 = 0
    betAmount3 = 0
    betAmount4 = 0
    dd = ""
    deck_split = 0
    num_split = 0
    dealersScore = 0.0
    yourScore = 0.0
    doubleDAct = ""
    bettinglbl.pack()
    bettinglbl.pack_forget()
    casinoGreenlbl.pack()
    casinoGreenlbl.pack_forget()
    yourMoneylbl.destroy()
    yourMoneyActuallbl.destroy()
    betAmountlbl.destroy()
    betAmountActuallbl.destroy()
    globalMessageText.set(" ")
    cardBacklbl.pack()
    cardBacklbl.pack_forget()
    globalMessagelbl.pack()
    globalMessagelbl.pack_forget()
    splitButton.pack()
    splitButton.pack_forget()
    doubleDownButton.pack()
    doubleDownButton.pack_forget()
    resetField()
    resetCards()
    bettingSystem()
    print(" --------------------------------------------- ") #Take this out when finish program

def resetField():
    casinoGreenlbl.pack()
    casinoGreenlbl.pack_forget()
    hand1Two3lbl.pack()
    hand1Two3lbl.pack_forget()
    handOne2lbl.pack()
    handOne2lbl.pack_forget()
    hand1Twolbl.pack()
    hand1Twolbl.pack_forget()
    hand1Two3lbl.pack()
    hand1Two3lbl.pack_forget()
    hand12Threelbl.pack()
    hand12Threelbl.pack_forget()
    hand12Three4lbl.pack()
    hand12Three4lbl.pack_forget()
    hand123Fourlbl.pack()
    hand123Fourlbl.pack_forget()
    handOne23lbl.pack()
    handOne23lbl.pack_forget()
    hand1Two34lbl.pack()
    hand1Two34lbl.pack_forget()
    handOne234lbl.pack()
    handOne234lbl.pack_forget()

def resetCards():
    twoClubslbl.pack()
    twoClubslbl.pack_forget()
    twoDiamondslbl.pack()
    twoDiamondslbl.pack_forget()
    twoHeartslbl.pack()
    twoHeartslbl.pack_forget()
    twoSpadeslbl.pack()
    twoSpadeslbl.pack_forget()
    threeClubslbl.pack()
    threeClubslbl.pack_forget()
    threeDiamondslbl.pack()
    threeDiamondslbl.pack_forget()
    threeHeartslbl.pack()
    threeHeartslbl.pack_forget()
    threeSpadeslbl.pack()
    threeSpadeslbl.pack_forget()
    fourClubslbl.pack()
    fourClubslbl.pack_forget()
    fourDiamondslbl.pack()
    fourDiamondslbl.pack_forget()
    fourHeartslbl.pack()
    fourHeartslbl.pack_forget()
    fourSpadeslbl.pack()
    fourSpadeslbl.pack_forget()
    fiveClubslbl.pack()
    fiveClubslbl.pack_forget()
    fiveDiamondslbl.pack()
    fiveDiamondslbl.pack_forget()
    fiveHeartslbl.pack()
    fiveHeartslbl.pack_forget()
    fiveSpadeslbl.pack()
    fiveSpadeslbl.pack_forget()
    sixClubslbl.pack()
    sixClubslbl.pack_forget()
    sixDiamondslbl.pack()
    sixDiamondslbl.pack_forget()
    sixHeartslbl.pack()
    sixHeartslbl.pack_forget()
    sixSpadeslbl.pack()
    sixSpadeslbl.pack_forget()
    sevenClubslbl.pack()
    sevenClubslbl.pack_forget()
    sevenDiamondslbl.pack()
    sevenDiamondslbl.pack_forget()
    sevenHeartslbl.pack()
    sevenHeartslbl.pack_forget()
    sevenSpadeslbl.pack()
    sevenSpadeslbl.pack_forget()
    eightClubslbl.pack()
    eightClubslbl.pack_forget()
    eightDiamondslbl.pack()
    eightDiamondslbl.pack_forget()
    eightHeartslbl.pack()
    eightHeartslbl.pack_forget()
    eightSpadeslbl.pack()
    eightSpadeslbl.pack_forget()
    nineClubslbl.pack()
    nineClubslbl.pack_forget()
    nineDiamondslbl.pack()
    nineDiamondslbl.pack_forget()
    nineHeartslbl.pack()
    nineHeartslbl.pack_forget()
    nineSpadeslbl.pack()
    nineSpadeslbl.pack_forget()
    tenClubslbl.pack()
    tenClubslbl.pack_forget()
    tenDiamondslbl.pack()
    tenDiamondslbl.pack_forget()
    tenHeartslbl.pack()
    tenHeartslbl.pack_forget()
    tenSpadeslbl.pack()
    tenSpadeslbl.pack_forget()
    aceClubslbl.pack()
    aceClubslbl.pack_forget()
    aceDiamondslbl.pack()
    aceDiamondslbl.pack_forget()
    aceHeartslbl.pack()
    aceHeartslbl.pack_forget()
    aceSpadeslbl.pack()
    aceSpadeslbl.pack_forget()
    jackClubslbl.pack()
    jackClubslbl.pack_forget()
    jackDiamondslbl.pack()
    jackDiamondslbl.pack_forget()
    jackHeartslbl.pack()
    jackHeartslbl.pack_forget()
    jackSpadeslbl.pack()
    jackSpadeslbl.pack_forget()
    kingClubslbl.pack()
    kingClubslbl.pack_forget()
    kingDiamondslbl.pack()
    kingDiamondslbl.pack_forget()
    kingHeartslbl.pack()
    kingHeartslbl.pack_forget()
    kingSpadeslbl.pack()
    kingSpadeslbl.pack_forget()
    queenClubslbl.pack()
    queenClubslbl.pack_forget()
    queenDiamondslbl.pack()
    queenDiamondslbl.pack_forget()
    queenHeartslbl.pack()
    queenHeartslbl.pack_forget()
    queenSpadeslbl.pack()
    queenSpadeslbl.pack_forget()
    
def instructionButton():
    global backToMainMenuButton
    instructionlbl.place(x= 675, y = 375, anchor = "center")
    titleText.set( '''
        Rules for Blackjack!
1.  First card is dealt to player, then to dealer,
    back to player, and finally to dealer.
2.  Only dealer's second card faces up. Player's cards
    can both be faced up.
3.  Player wins automatically if they get blackjack
    (unless dealer also gets blackjack: push = tie)
    ** Player wins 3:2 ($2 bet wins $3)
    Dealer wins with blackjack automatically over player's
    five card or 21 (unless player has blackjack).
    
4.  ** Player beats dealer if the player has five cards
    under 21 (i.e. five card Charlie) UNLESS DEALER HAS BJ
5.  Dealer wins if player busts (i.e. over 21)
6.  After player stays (i.e. no more cards), dealer
    must take a card if the total is 16 or under; stay
    if 17 or over.
7.  ** Opt SPLIT: If you get two cards of the same rank.
    Once split, the hands will be played from left to right
8.  ** Opt DOUBLE DOWN: Take one more card and stay.
9.  ** Dealer can hit on SOFT 17 (ace)  ''')
    welcomeLabel.place (x = 675, y = 190, anchor = "n") # meant for Instructions Text
    madeByLabel.destroy()
    instructionsButton.destroy()
    startButton.destroy()
    menulbl.pack()
    menulbl.pack_forget()
    backToMainMenuButton = Button(root, text = "Back", command = backToMenu, width = 10, height = 2)
    backToMainMenuButton.place(x = 675, y = 650, anchor = "center")

def backToMenu():
    global startButton
    global instructionsButton
    global instructions
    global madeByLabel
    titleText.set("")
    instructionlbl.pack()
    instructionlbl.pack_forget()
    welcomeLabel.place (x = 675, y = 20, anchor = "center")
    startButton = Button(root, text = "Start", command = bettingSystem, width = 15, height = 3, justify = CENTER,)
    startButton.place(x = 675, y = 350, anchor = "center")
    instructionsButton = Button(root, text = "Instructions", command = instructionButton, width = 15, height = 3)
    instructionsButton.place(x = 675, y = 420, anchor = "center")
    backToMainMenuButton.destroy()
    madeByLabel = Label(root, text = "Made by Thomas Nguyen")
    madeByLabel.place (x = 675, y = 730, anchor = "center")
    menulbl.place(x= 675, y = 375, anchor = "center")
    

def cardDisplay(cardIndex):
    # converts cardIndex to cardDsp, e.g. 16 -> '4D'
    suit = ""
    if (cardIndex // 13 == 0):
        suit = "♥"
    elif (cardIndex // 13 == 1):
        suit = "♦"
    elif (cardIndex // 13 == 2):
        suit = "♣"
    elif (cardIndex // 13 == 3):
        suit = "♠"

    rank = (cardIndex % 13) + 1
    if (rank == 1):
        rank = "A"
    if (rank == 11):    
        rank = "J"
    if (rank == 12):
        rank = "Q"
    if (rank == 13):
        rank = "K"

    card = str(rank) + str(suit)
    return card

def sumCards(hand):
    total = sum(hand)
    if (hand.count(1) > 0):
        # check if any Ace on hand
        if (total + 10 <= 21):
            total = total + 10
    return total

def endGame():
    global yourScore
    global dealersScore
    global DoneDeal
    global yourCardInd
    global dealerCardInd
    global yourMoney
    global betAmount
    global yourScore2
    global yourScore3
    global yourScore4
    global betAmount
    global betAmount2
    global betAmount3
    global betAmount4
    global num_split
    global dd
    global betAmountUse
    globalMessageText.set(" ")
    globalMessagelbl.place(x = 20, y = 640, anchor = "w") #Use this for Message location!
    cardBacklbl.pack()
    cardBacklbl.pack_forget()
    displayCard(dealersCardDsp[0],0,1,0,0,1) #displayCard(card,n,d,s,n_s,deck)

    totalscore = []
    totalscore.append(yourScore)
    if yourScore2 != 0:
        totalscore.append(yourScore2)
    if yourScore3 != 0: 
        totalscore.append(yourScore3)
    if yourScore4 != 0:
        totalscore.append(yourScore4)

    totalBets = []
    if dd == "Yes":
        totalBets.append(betAmountUse)
    else:
        totalBets.append(betAmount)
    if betAmount2 != 0:
        totalBets.append(betAmount2)
    if betAmount3 != 0:
        totalBets.append(betAmount3)
    if betAmount4 != 0:
        totalBets.append(betAmount4)
    print(totalBets)

    yourCardIndList = []
    yourCardIndList.append(yourCardInd)
    if yourCardInd2 != []:
        yourCardIndList.append(yourCardInd2)
    if yourCardInd3 != []:
        yourCardIndList.append(yourCardInd3)
    if yourCardInd4 != []:
        yourCardIndList.append(yourCardInd4)
    
    result = []
    i = 0
    while i in range(len(totalscore)):
        if (totalscore[i] > 21):
            globalMessageText.set("Bust! You Lost! Click Shuffle to restart!")
            result.append("Busted")
        elif (totalscore[i] == 21) and (len(yourCardIndList[i]) == 2) and (dealersScore == 21) and (len(dealersCardInd) == 2):
            globalMessageText.set("You and Dealer got Black Jack! You tied!")
            yourMoney = yourMoney + totalBets[i]
            result.append("Tied Black Jack")
        elif (totalscore[i] == 21) and (len(yourCardIndList[i]) == 2):
            globalMessageText.set("Black Jack! You Won! Click Shuffle to restart!")
            yourMoney = yourMoney + (2.5 * totalBets[i])
            result.append("BlackJack")
        elif (dealersScore > 21):
            globalMessageText.set("Dealer Busted! You Won! Click Shuffle to restart!")
            yourMoney = yourMoney + (2 * totalBets[i])
            result.append("Dealer Busted")
        elif ((totalscore[i] <= 21) and (len(yourCardIndList[i]) == 5) and (dealersScore == 21) and (len(dealersCardInd) == 2)):
            globalMessageText.set("Five Card Charlie, but Dealer got Black Jack! You lost! Click Shuffle to restart!")
            result.append("Dealer got BlackJack")
        elif ((totalscore[i] <= 21) and (len(yourCardIndList[i]) == 5)):
            globalMessageText.set("Five Card Charlie! You Won! Click Shuffle to restart!")
            yourMoney = yourMoney + (2 * totalBets[i])
            result.append("Five Card Charlie")
        elif (dealersScore == 21) and (len(dealersCardInd) == 2):
            globalMessageText.set("Dealer got Black Jack! You lost! Click Shuffle to restart!")
            result.append("Dealer got BlackJack")
        elif (dealersScore > totalscore[i]):
            globalMessageText.set("Dealer beat you! Click Shuffle to restart!")
            result.append("Dealer beat you")
        elif (totalscore[i] > dealersScore) and totalscore[i] <= 21:
            globalMessageText.set("You beat Dealer! Click Shuffle to restart!")
            yourMoney = yourMoney + (2 * totalBets[i])
            result.append("You beat dealer")
        elif (totalscore[i] == dealersScore):
            globalMessageText.set("Push! You and Dealer Tied! Click Shuffle to restart!") 
            yourMoney = yourMoney + totalBets[i]
            result.append("You and dealer tied")
        DoneDeal = "Yes"
        dealersScoreUse.set(dealersScore)
        i += 1

    if num_split != 0:
        if i == 2:
            text = "Hand 1: " + str(result[0]) + " Hand 2: " + str(result[1])
            globalMessageText.set(text)
        if i == 3:
            text = "Hand 1: " + str(result[0]) + " Hand 2: " + str(result[1]) + " Hand 3: " + str(result[2])
            globalMessageText.set(text)
        if i == 4:
            text = "Hand 1: " + str(result[0]) + " Hand 2: " + str(result[1]) + " Hand 3: " + str(result[2]) + " Hand 4: " + str(result[3])
            globalMessageText.set(text)
    yourMoneyActualText.set(yourMoney)
    betAmountActualText.set(betAmount + betAmount2 + betAmount3 + betAmount4)

def ggwp():
    global gameOverlbl
    global restartBtn
    dealButton.pack()
    dealButton.pack_forget()
    noDealButton.pack()
    noDealButton.pack_forget()
    shuffleButton.pack()
    shuffleButton.pack_forget()
    dealersScoreInGamelbl.pack()
    yourScoreInGamelbl.pack()
    dealersHandLbl.pack()
    yourHandLbl.pack()
    yourScoreInGameActuallbl.pack()
    dealersScoreInGamelbl.pack_forget()
    yourScoreInGamelbl.pack_forget()
    dealersHandLbl.pack_forget()
    yourHandLbl.pack_forget()
    yourScoreInGameActuallbl.pack_forget()
    dealersScoreInGameActuallbl.pack()
    dealersScoreInGameActuallbl.pack_forget()
    gameOverlbl = Label(root, text = "Game Over! Click Restart if you want to play again!")
    gameOverlbl.place(x = 675, y = 300, anchor = "center")
    restartBtn = Button(root, text = "Restart", command = restartGame, width = 10, height = 2)
    restartBtn.place(x = 675, y = 700, anchor = "center")
    
def restartGame():
    global yourMoney
    gameOverlbl.destroy()
    restartBtn.destroy()
    yourMoney = 2000.0
    bettingSystem()
    
#========================================================Betting Complex=============================================================|
def bettingSystem():
    global twentyDollarsBettingOptionButton
    global fiftyDollarsBettingOptionButton
    global oneHundredDollarsBettingOptionButton
    global oneHundredAndFiftyDollarsBettingOptionButton
    global twoHundredDollarsBettingOptionButton
    global threeHundredDollarsBettingOptionButton
    global fourHundredDollarsBettingOptionButton
    global sixHundredDollarsBettingOptionButton
    global eightHundredDollarsBettingOptionButton
    global twoHundredAndFiftyDollarsBettingOptionButton
    global bettingSystemlbl
    global yourMoneylbl
    global yourMoneyActuallbl
    global yourScoreInGamelbl
    global dealersScoreInGamelbl
    global noDealButton
    global dealButton
    global shuffleButton
    global dealersHandLbl
    global yourHandLbl
    global yourScore
    global yourScoreInGameActuallbl
    global yourMoney
    global yourMoneyActualText
    global reBet
    if (yourMoney <= 0.0):
        ggwp()
        return None
    menulbl.pack()
    menulbl.pack_forget()
    madeByLabel.destroy()
    welcomeLabel.destroy()
    startButton.destroy()
    instructionsButton.destroy()
    bettinglbl.place(x= 675, y = 375, anchor = "center")
    yourMoneylbl = Label(root, text = "Your Money: ")
    yourMoneyActualText= StringVar()
    yourMoneyActualText.set(yourMoney)
    yourMoneyActuallbl = Label(root, textvariable = yourMoneyActualText)
    bettingSystemlbl = Label(root, text = "Select the Amount you want to Bet!")
    twentyDollarsBettingOptionButton = Button(root, text = "$20", command = twentyDollarsBettingOptionProgram, width = 10, height = 2)
    fiftyDollarsBettingOptionButton = Button(root, text = "$50", command = fiftyDollarsBettingOptionProgram, width = 10, height = 2)
    oneHundredDollarsBettingOptionButton = Button(root, text = "$100", command = oneHundredDollarsBettingOptionProgram, width = 10, height = 2)
    oneHundredAndFiftyDollarsBettingOptionButton = Button(root, text = "$150", command = oneHundredAndFiftyDollarsBettingOptionProgram, width = 10, height = 2)
    twoHundredDollarsBettingOptionButton = Button(root, text = "$200", command = twoHundredDollarsBettingOptionProgram, width = 10, height = 2)
    twoHundredAndFiftyDollarsBettingOptionButton = Button(root, text = "$250", command = twoHundredAndFiftyDollarsBettingOptionProgram, width = 10, height = 2)
    threeHundredDollarsBettingOptionButton = Button(root, text = "$300", command = threeHundredDollarsBettingOptionProgram, width = 10, height = 2)
    fourHundredDollarsBettingOptionButton = Button(root, text = "$400", command = fourHundredDollarsBettingOptionProgram, width = 10, height = 2)
    sixHundredDollarsBettingOptionButton = Button(root, text = "$600", command = sixHundredDollarsBettingOptionProgram, width = 10, height = 2)
    eightHundredDollarsBettingOptionButton = Button(root, text = "$800", command = eightHundredDollarsBettingOptionProgram, width = 10, height = 2)
    bettingSystemlbl.place(x = 675, y = 300, anchor = "center")
    yourMoneylbl.place(x = 685, y = 200, anchor = "e")
    yourMoneyActuallbl.place(x = 686, y = 200, anchor = "w")
    twentyDollarsBettingOptionButton.place(x = 225, y = 350, anchor = "center")
    fiftyDollarsBettingOptionButton.place(x = 325, y = 350, anchor = "center")
    oneHundredDollarsBettingOptionButton.place(x = 425, y= 350, anchor = "center")
    oneHundredAndFiftyDollarsBettingOptionButton.place(x = 525,y = 350, anchor = "center")
    twoHundredDollarsBettingOptionButton.place(x = 625, y = 350, anchor = "center")
    twoHundredAndFiftyDollarsBettingOptionButton.place(x = 725, y = 350, anchor = "center")
    threeHundredDollarsBettingOptionButton.place(x = 825, y = 350, anchor = "center")
    fourHundredDollarsBettingOptionButton.place(x = 925, y = 350, anchor = "center")
    sixHundredDollarsBettingOptionButton.place(x = 1025, y = 350, anchor = "center")
    eightHundredDollarsBettingOptionButton.place(x = 1125, y = 350, anchor = "center")
    if (reBet == "Yes"):
        yourScoreInGamelbl.destroy()
        dealersScoreInGamelbl.destroy()
        dealersScoreUse.set(" ")
        noDealButton.destroy()
        dealButton.destroy()
        shuffleButton.destroy()
        dealersHandLbl.destroy()
        yourHandLbl.destroy()
        yourScoreUse.set(" ")
    
    
def destroyBetOptionButtons():
    twentyDollarsBettingOptionButton.destroy()
    fiftyDollarsBettingOptionButton.destroy()
    oneHundredDollarsBettingOptionButton.destroy()
    oneHundredAndFiftyDollarsBettingOptionButton.destroy()
    twoHundredDollarsBettingOptionButton.destroy()
    threeHundredDollarsBettingOptionButton.destroy()
    fourHundredDollarsBettingOptionButton.destroy()
    sixHundredDollarsBettingOptionButton.destroy()
    eightHundredDollarsBettingOptionButton.destroy()
    twoHundredAndFiftyDollarsBettingOptionButton.destroy()
    startProgram()

def twentyDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 20
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()

def fiftyDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 50
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()


def oneHundredDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 100
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()

def oneHundredAndFiftyDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 150
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()

def twoHundredDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 200
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()

def twoHundredAndFiftyDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 250
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()

def threeHundredDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 300
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()

def fourHundredDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 400
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()

def sixHundredDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 600
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()

def eightHundredDollarsBettingOptionProgram():
    global betAmount
    global yourMoney
    betAmount = 800
    if (yourMoney < betAmount):
        globalMessageText.set("You don't have enough Money! Select another option!")
        globalMessagelbl.place(x = 20, y = 640, anchor = "w")
    elif (yourMoney >= betAmount):
        yourMoney = yourMoney - betAmount
        yourMoneyActualText.set(yourMoney)
        destroyBetOptionButtons()

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

def repath(a):
    last = a.rfind("\\")
    a = a[:last+1] + "\\Images" + a[last:]
    b = "\\"
    c = "\\\\"
    a = a.replace(b,c)
    return a
#====================================================================================================================================|
'''
def runThis():
    for i in range(52):
        print(str(i) + ":" + cardDisplay(i))

runThis()
'''
#===============================================Main Menu Global Variable Set========================================================|

root = Tk()
icon = repath(resource_path("Icon.ico"))
root.iconbitmap(icon)
root.geometry("1350x750")
root.title("Blackjack Casino")
root.resizable(False,False)

yourMoney = 2000.0
betAmount = 0.0

n = 0

reBet = " "
doubleDAct = ""
dd = ""
deck_split = 0

num_split = 0

instruction = repath(resource_path("Instruction.png"))
instructionImage = PhotoImage(file = instruction)
instructionlbl = Label(root, image = instructionImage)

titleText = StringVar()
titleText.set("Welcome to Black Jack Casino!")

welcomeLabel = Label(root, textvariable = titleText) #Interchangable with instructions Text

menu = repath(resource_path("Menu.png"))
menuImage = PhotoImage(file = menu)
menulbl = Label(root, image = menuImage)
menulbl.place(x= 675, y = 375, anchor = "center")

betting = repath(resource_path("Betting.png"))
bettingImage = PhotoImage(file = betting)
bettinglbl = Label(root, image = bettingImage)


madeByText = StringVar()
madeByText.set("Made by Thomas Nguyen")

madeByLabel = Label(root, textvariable = madeByText)
madeByLabel.place (x = 675, y = 730, anchor = "center")

startButton = Button(root, text = "Start", command = bettingSystem, width = 15, height = 3, justify = CENTER) #Inside Main Menu
startButton.place(x = 675, y = 350, anchor = "center")

instructionsButton = Button(root, text = "Instructions", command = instructionButton, width = 15, height = 3) #Inside Main Menu
instructionsButton.place(x = 675, y = 420, anchor = "center")

casinoGreen = repath(resource_path("CasinoGreen.png"))
casinoGreenImage = PhotoImage(file = casinoGreen)
casinoGreenlbl = Label(root, image = casinoGreenImage)

#====================================================================================================================================|

DoneDeal = ""



handOne2 = repath(resource_path("HandOne2.png"))
handOne2Image = PhotoImage(file = handOne2)
handOne2lbl = Label(root,image = handOne2Image)

hand1Two = repath(resource_path("Hand1Two.png"))
hand1TwoImage = PhotoImage(file = hand1Two)
hand1Twolbl = Label(root,image = hand1TwoImage)

hand1Two3 = repath(resource_path("Hand1Two3.png"))
hand1Two3Image = PhotoImage(file = hand1Two3)
hand1Two3lbl = Label(root,image = hand1Two3Image)

hand12Three = repath(resource_path("Hand12Three.png"))
hand12ThreeImage = PhotoImage(file = hand12Three)
hand12Threelbl = Label(root,image = hand12ThreeImage)

hand12Three4 = repath(resource_path("Hand12Three4.png"))
hand12Three4Image = PhotoImage(file = hand12Three4)
hand12Three4lbl = Label(root,image = hand12Three4Image)

hand123Four = repath(resource_path("Hand123Four.png"))
hand123FourImage = PhotoImage(file = hand123Four)
hand123Fourlbl = Label(root,image = hand123FourImage)

handOne23 = repath(resource_path("HandOne23.png"))
handOne23Image = PhotoImage(file = handOne23)
handOne23lbl = Label(root, image = handOne23Image)

handOne234 = repath(resource_path("HandOne234.png"))
handOne234Image = PhotoImage(file = handOne234)
handOne234lbl = Label(root, image = handOne234Image)

hand1Two34 = repath(resource_path("Hand1Two34.png"))
hand1Two34Image = PhotoImage(file = hand1Two34)
hand1Two34lbl = Label(root, image = hand1Two34Image)

yourScoreUse = StringVar()
yourScoreUse.set(0.0)
yourScoreInGameActuallbl = Label(root, textvariable = yourScoreUse)

yourScoreUse2 = StringVar()
yourScoreUse2.set(0.0)
yourScore2lbl = Label(root, textvariable = yourScoreUse2)

yourScoreUse3 = StringVar()
yourScoreUse3.set(0.0)
yourScore3lbl = Label(root, textvariable = yourScoreUse3)

yourScoreUse4 = StringVar()
yourScoreUse4.set(0.0)
yourScore4lbl = Label(root, textvariable = yourScoreUse4)


dealersScoreUse = StringVar()
dealersScoreUse.set(0.0)
dealersScoreInGameActuallbl = Label(root, textvariable = dealersScoreUse)

globalMessageText = StringVar()
globalMessageText.set("")
globalMessagelbl = Label(root, textvariable = globalMessageText)

twoClubs = repath(resource_path("2_of_clubs.png"))
twoClubsImage = PhotoImage(file = twoClubs)
twoClubslbl = Label(root, image = twoClubsImage, borderwidth =0, highlightthickness = 0)

twoDiamonds = repath(resource_path("2_of_diamonds.png"))
twoDiamondsImage = PhotoImage(file = twoDiamonds)
twoDiamondslbl = Label(root, image = twoDiamondsImage, borderwidth =0, highlightthickness = 0)

twoHearts = repath(resource_path("2_of_hearts.png"))
twoHeartsImage = PhotoImage(file = twoHearts)
twoHeartslbl = Label(root, image = twoHeartsImage, borderwidth =0, highlightthickness = 0)

twoSpades = repath(resource_path("2_of_spades.png"))
twoSpadesImage = PhotoImage(file = twoSpades)
twoSpadeslbl = Label(root, image = twoSpadesImage, borderwidth =0, highlightthickness = 0)

threeClubs = repath(resource_path("3_of_clubs.png"))
threeClubsImage = PhotoImage(file = threeClubs)
threeClubslbl = Label(root, image = threeClubsImage, borderwidth =0, highlightthickness = 0)

threeDiamonds = repath(resource_path("3_of_diamonds.png"))
threeDiamondsImage = PhotoImage(file = threeDiamonds)
threeDiamondslbl = Label(root, image = threeDiamondsImage, borderwidth =0, highlightthickness = 0)

threeHearts = repath(resource_path("3_of_hearts.png"))
threeHeartsImage = PhotoImage(file = threeHearts)
threeHeartslbl = Label(root, image = threeHeartsImage, borderwidth =0, highlightthickness = 0)

threeSpades = repath(resource_path("3_of_spades.png"))
threeSpadesImage = PhotoImage(file = threeSpades)
threeSpadeslbl = Label(root, image = threeSpadesImage, borderwidth =0, highlightthickness = 0)

fourClubs = repath(resource_path("4_of_clubs.png"))
fourClubsImage = PhotoImage(file = fourClubs)
fourClubslbl = Label(root, image = fourClubsImage, borderwidth =0, highlightthickness = 0)

fourDiamonds = repath(resource_path("4_of_diamonds.png"))
fourDiamondsImage = PhotoImage(file = fourDiamonds)
fourDiamondslbl = Label(root, image = fourDiamondsImage, borderwidth =0, highlightthickness = 0)

fourHearts = repath(resource_path("4_of_hearts.png"))
fourHeartsImage = PhotoImage(file = fourHearts)
fourHeartslbl = Label(root, image = fourHeartsImage, borderwidth =0, highlightthickness = 0)

fourSpades = repath(resource_path("4_of_spades.png"))
fourSpadesImage = PhotoImage(file = fourSpades)
fourSpadeslbl = Label(root, image = fourSpadesImage, borderwidth =0, highlightthickness = 0)

fiveClubs = repath(resource_path("5_of_clubs.png"))
fiveClubsImage = PhotoImage(file = fiveClubs)
fiveClubslbl = Label(root, image = fiveClubsImage, borderwidth =0, highlightthickness = 0)

fiveDiamonds = repath(resource_path("5_of_diamonds.png"))
fiveDiamondsImage = PhotoImage(file = fiveDiamonds)
fiveDiamondslbl = Label(root, image = fiveDiamondsImage, borderwidth =0, highlightthickness = 0)

fiveHearts = repath(resource_path("5_of_hearts.png"))
fiveHeartsImage = PhotoImage(file = fiveHearts)
fiveHeartslbl = Label(root, image = fiveHeartsImage, borderwidth =0, highlightthickness = 0)

fiveSpades = repath(resource_path("5_of_spades.png"))
fiveSpadesImage = PhotoImage(file = fiveSpades)
fiveSpadeslbl = Label(root, image = fiveSpadesImage, borderwidth =0, highlightthickness = 0)

sixClubs = repath(resource_path("6_of_clubs.png"))
sixClubsImage = PhotoImage(file = sixClubs)
sixClubslbl = Label(root, image = sixClubsImage, borderwidth =0, highlightthickness = 0)

sixDiamonds = repath(resource_path("6_of_diamonds.png"))
sixDiamondsImage = PhotoImage(file = sixDiamonds)
sixDiamondslbl = Label(root, image = sixDiamondsImage, borderwidth =0, highlightthickness = 0)

sixHearts = repath(resource_path("6_of_hearts.png"))
sixHeartsImage = PhotoImage(file = sixHearts)
sixHeartslbl = Label(root, image = sixHeartsImage, borderwidth =0, highlightthickness = 0)

sixSpades = repath(resource_path("6_of_spades.png"))
sixSpadesImage = PhotoImage(file = sixSpades)
sixSpadeslbl = Label(root, image = sixSpadesImage, borderwidth =0, highlightthickness = 0)

sevenClubs = repath(resource_path("7_of_clubs.png"))
sevenClubsImage = PhotoImage(file = sevenClubs)
sevenClubslbl = Label(root, image = sevenClubsImage, borderwidth =0, highlightthickness = 0)

sevenDiamonds = repath(resource_path("7_of_diamonds.png"))
sevenDiamondsImage = PhotoImage(file = sevenDiamonds)
sevenDiamondslbl = Label(root, image = sevenDiamondsImage, borderwidth =0, highlightthickness = 0)

sevenHearts = repath(resource_path("7_of_hearts.png"))
sevenHeartsImage = PhotoImage(file = sevenHearts)
sevenHeartslbl = Label(root, image = sevenHeartsImage, borderwidth =0, highlightthickness = 0)

sevenSpades = repath(resource_path("7_of_spades.png"))
sevenSpadesImage = PhotoImage(file = sevenSpades)
sevenSpadeslbl = Label(root, image = sevenSpadesImage, borderwidth =0, highlightthickness = 0)

eightClubs = repath(resource_path("8_of_clubs.png"))
eightClubsImage = PhotoImage(file = eightClubs)
eightClubslbl = Label(root, image = eightClubsImage, borderwidth =0, highlightthickness = 0)

eightDiamonds = repath(resource_path("8_of_diamonds.png"))
eightDiamondsImage = PhotoImage(file = eightDiamonds)
eightDiamondslbl = Label(root, image = eightDiamondsImage, borderwidth =0, highlightthickness = 0)

eightHearts = repath(resource_path("8_of_hearts.png"))
eightHeartsImage = PhotoImage(file = eightHearts)
eightHeartslbl = Label(root, image = eightHeartsImage, borderwidth =0, highlightthickness = 0)

eightSpades = repath(resource_path("8_of_spades.png"))
eightSpadesImage = PhotoImage(file = eightSpades)
eightSpadeslbl = Label(root, image = eightSpadesImage, borderwidth =0, highlightthickness = 0)

nineClubs = repath(resource_path("9_of_clubs.png"))
nineClubsImage = PhotoImage(file = nineClubs)
nineClubslbl = Label(root, image = nineClubsImage, borderwidth =0, highlightthickness = 0)

nineDiamonds = repath(resource_path("9_of_diamonds.png"))
nineDiamondsImage = PhotoImage(file = nineDiamonds)
nineDiamondslbl = Label(root, image = nineDiamondsImage, borderwidth =0, highlightthickness = 0)

nineHearts = repath(resource_path("9_of_hearts.png"))
nineHeartsImage = PhotoImage(file = nineHearts)
nineHeartslbl = Label(root, image = nineHeartsImage, borderwidth =0, highlightthickness = 0)

nineSpades = repath(resource_path("9_of_spades.png"))
nineSpadesImage = PhotoImage(file = nineSpades)
nineSpadeslbl = Label(root, image = nineSpadesImage, borderwidth =0, highlightthickness = 0)

tenClubs = repath(resource_path("10_of_clubs.png"))
tenClubsImage = PhotoImage(file = tenClubs)
tenClubslbl = Label(root, image = tenClubsImage, borderwidth =0, highlightthickness = 0)

tenDiamonds = repath(resource_path("10_of_diamonds.png"))
tenDiamondsImage = PhotoImage(file = tenDiamonds)
tenDiamondslbl = Label(root, image = tenDiamondsImage, borderwidth =0, highlightthickness = 0)

tenHearts = repath(resource_path("10_of_hearts.png"))
tenHeartsImage = PhotoImage(file = tenHearts)
tenHeartslbl = Label(root, image = tenHeartsImage, borderwidth =0, highlightthickness = 0)

tenSpades = repath(resource_path("10_of_spades.png"))
tenSpadesImage = PhotoImage(file = tenSpades)
tenSpadeslbl = Label(root, image = tenSpadesImage, borderwidth =0, highlightthickness = 0)

aceClubs = repath(resource_path("ace_of_clubs.png"))
aceClubsImage = PhotoImage(file = aceClubs)
aceClubslbl = Label(root, image = aceClubsImage, borderwidth =0, highlightthickness = 0)

aceDiamonds = repath(resource_path("ace_of_diamonds.png"))
aceDiamondsImage = PhotoImage(file = aceDiamonds)
aceDiamondslbl = Label(root, image = aceDiamondsImage, borderwidth =0, highlightthickness = 0)

aceHearts = repath(resource_path("ace_of_hearts.png"))
aceHeartsImage = PhotoImage(file = aceHearts)
aceHeartslbl = Label(root, image = aceHeartsImage, borderwidth =0, highlightthickness = 0)

aceSpades = repath(resource_path("ace_of_spades.png"))
aceSpadesImage = PhotoImage(file = aceSpades)
aceSpadeslbl = Label(root, image = aceSpadesImage, borderwidth =0, highlightthickness = 0)

jackClubs = repath(resource_path("jack_of_clubs.png"))
jackClubsImage = PhotoImage(file = jackClubs)
jackClubslbl = Label(root, image = jackClubsImage, borderwidth =0, highlightthickness = 0)

jackDiamonds = repath(resource_path("jack_of_diamonds.png"))
jackDiamondsImage = PhotoImage(file = jackDiamonds)
jackDiamondslbl = Label(root, image = jackDiamondsImage, borderwidth =0, highlightthickness = 0)

jackHearts = repath(resource_path("jack_of_hearts.png"))
jackHeartsImage = PhotoImage(file = jackHearts)
jackHeartslbl = Label(root, image = jackHeartsImage, borderwidth =0, highlightthickness = 0)

jackSpades = repath(resource_path("jack_of_spades.png"))
jackSpadesImage = PhotoImage(file = jackSpades)
jackSpadeslbl = Label(root, image = jackSpadesImage, borderwidth =0, highlightthickness = 0)

kingClubs = repath(resource_path("king_of_clubs.png"))
kingClubsImage = PhotoImage(file = kingClubs)
kingClubslbl = Label(root, image = kingClubsImage, borderwidth =0, highlightthickness = 0)

kingDiamonds = repath(resource_path("king_of_diamonds.png"))
kingDiamondsImage = PhotoImage(file = kingDiamonds)
kingDiamondslbl = Label(root, image = kingDiamondsImage, borderwidth =0, highlightthickness = 0)

kingHearts = repath(resource_path("king_of_hearts.png"))
kingHeartsImage = PhotoImage(file = kingHearts)
kingHeartslbl = Label(root, image = kingHeartsImage, borderwidth =0, highlightthickness = 0)

kingSpades = repath(resource_path("king_of_spades.png"))
kingSpadesImage = PhotoImage(file = kingSpades)
kingSpadeslbl = Label(root, image = kingSpadesImage, borderwidth =0, highlightthickness = 0)

queenClubs = repath(resource_path("queen_of_clubs.png"))
queenClubsImage = PhotoImage(file = queenClubs)
queenClubslbl = Label(root, image = queenClubsImage, borderwidth =0, highlightthickness = 0)

queenDiamonds = repath(resource_path("queen_of_diamonds.png"))
queenDiamondsImage = PhotoImage(file = queenDiamonds)
queenDiamondslbl = Label(root, image = queenDiamondsImage, borderwidth =0, highlightthickness = 0)

queenHearts = repath(resource_path("queen_of_hearts.png"))
queenHeartsImage = PhotoImage(file = queenHearts)
queenHeartslbl = Label(root, image = queenHeartsImage, borderwidth =0, highlightthickness = 0)

queenSpades = repath(resource_path("queen_of_spades.png"))
queenSpadesImage = PhotoImage(file = queenSpades)
queenSpadeslbl = Label(root, image = queenSpadesImage, borderwidth =0, highlightthickness = 0)

cardBack = repath(resource_path("cardBack.png"))
cardBackImage =  PhotoImage(file = cardBack)
cardBacklbl = Label(root, image = cardBackImage, borderwidth =0, highlightthickness = 0)

doubleDownButton = Button(root, text = "Double Down", command = doubleDown, width = 12, height = 3)
splitButton = Button(root, text = "Split", command = split, width = 12, height = 3)

root.mainloop()
