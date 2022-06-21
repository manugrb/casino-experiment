# casino-experiment
This is an automated experiment to find out if the strategy to always bet double the last amount in a Casino is a smart idea.

## Idea:
You start to bet with a small amount in a Casino. If you win you go home. If you don't win, you bet double the previos amount to make up for your loss and get a new chance to win something. You repeat the process until you are out of money or have won.
A win means only a small amount of money gained. A loss means to loose all your money. However the probability to loose is really small.

## Script:
To try this experiment you only need one script:

 1. Run `python defeatACasino.py` in your directory.
 2. The program will ask you how many players should play. This means on how many instances the experiment should be carried out. Just enter how many you want
 3. You will then have to insert how much money each player should have. This sets the upper limit to the number of plays. If a player spends all of his money, he looses.
 4. Next you will have to enter the winning probabiltiy for the player in percent. (You can also use floating point percent numbers). (Do not include the "%" char).
 5. The last step is to insert the minimum amount of money the player has to bet in a game. This will also be the starting amount.
 6. Press enter and wait until the program simulated everything. This may take pretty long depending on the values you inserted. When it is done you should see a new window with a graph pop up. This shows the graphic representation of your experiment results. You will also get the results as plain numbers in your terminal window.
