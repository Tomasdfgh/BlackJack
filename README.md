# BlackJack

This project implements 5 principles of blackjack:

1. Bet
2. Hit
3. Stay
4. Double Down
5. Split

This application allows the user to interact with an automatic dealer. Inorder to download, download the BlackJackwithPythonCodeInstaller.exe application

After each round, the user is asked to place a new bet with the total amount of money appearing to the user
![image](https://user-images.githubusercontent.com/86145397/197316582-3e47d8c2-f465-4d69-9584-0c9106301549.png)
The user is allowed to place a range of betting amount from 20 to 800 dollars

The Hit function allows the user to draw a card, and add it to their hand
![image](https://user-images.githubusercontent.com/86145397/197316286-74c1bfbc-ead9-4a75-b515-12dfb0e54585.png)
This example shows that after hitting, the user has gained a two of spades

Stay would allow the dealer to show its hand and compare it to the user's hand
![image](https://user-images.githubusercontent.com/86145397/197316359-ab162622-6eb0-4425-9b56-5d33f58e30ef.png)
This example shows that after staying, the dealer dealt and busted its hand. The user have won

Double down allows the user to hit once before staying. The requirement is that the user will have to place down another betting amount that is 0.5 times the initial betting amount
![image](https://user-images.githubusercontent.com/86145397/197316673-b3727495-b0a5-4064-b788-a899912d8a74.png)
This example shows the user using double down and bust. The initial bet was 200 dollars. Since the user busted, they had to pay 300 dollars instead

Split allows the user to split the two cards into two different hands. The splitting function can be called 4 times if the user happened to constantly draw cards with the same value.
![image](https://user-images.githubusercontent.com/86145397/197316858-eb8db2d5-6295-463a-800f-8c5dbdc67270.png)
This example shows the user drawing two cards with a value of 7. After calling split, the user has their cards seperated into two hands

![image](https://user-images.githubusercontent.com/86145397/197316883-7b69c9fa-5375-4c03-98ba-9a807273805c.png)
After calling split, user can continue to draw more cards for their individual hands. This example demonstrates that
