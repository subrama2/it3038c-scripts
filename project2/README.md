# Documentation:
I coded this without an external resource and just had 2 ideas rock,paper,scissors game and guess number game and i put them together to make this project or script.
I made a 2 simple games that had different rules and implemented them in a manner where the user can choose between the two and play it weather that is rps or rockpaperscissors or guess the number game. There is a score card implemented with the games
so that the user can know how much he won in total playing both games how many every times he wanted.
The Interesting function within the script is i use a random module within both games to be able to create a cpu that will either choose rock,paper,scissors weather the user chooses that game or chooses number
if the user chooses that. There is no real cpu i am creating that effect by randomly choosing number and approiatly assigning that to a value weather it r.p.s or a random number.
If you choose to play rps and input that you will have an option to choose rock,paper, or scissors and when you do that you will get a result weather you won,lost, or tied depending on the randomly generated opposing rock, paper, or scissors
After you get that you get an option to choose to play a game weather that is the same game or the guess game and if you choose rps again then you will go through the same steps until you say the other game or don't want to play anymore where then it will count
how many times you won,lost or tied in both games and print that out.

example of the expectation of script:

After you run the GameProject.py in terminal it will start of by saying "welcome to two game collection
Do you want to play rock,paper,scissors [rps] or choose right number game [n] (Enter one of the two of whats is in bracket):
"
Here we can input rps or n as the game. In our example i will input rps. After that it will say 
"do you choose rock [r], paper [p], or scissors [s]:" here we can input r | p | s only. i will input
r for rock. After this it will give one of three results its a tie, its a win, or its a loss. In my case
i got the result "its a tie  [rock draws against rock]". After this it will ask you "do you want to play rps or number guess game again [y/n]:"
here you can say y or n. I will say y to play again. Then it will say "Do you want to play rock,paper,scissors [rps] or choose right number game [n] (Enter one of the two of whats is in bracket):"
i will imput n this time for the other game. After that it will state "Here is a hint for the game the number is between:  3735 - 3755
you have 5  chance(s) to guess left
guess the number i am thinking it:" the number will be different everytime as it is randomly generated but the number 
of chances will stay the same so you have 5 chances to guess it correct or you will lose. I inputted 3736 and got "you have 4  chance(s) to guess left, guess the number i am thinking :" i inputted 3750 and got it wrong and i tried next time
3755 and got it wrong again and then inputted 3739 and got it wrong and inputted 3745 on my last chance and got the end statement of 
"sorry you guessed wrong the actual number is  3745
do you want to play rps or number guess game again [y/n]:" here i will input n this time after which i will
state "Thanks for playing
You won  0 time(s) but lost  1 time(s) and you draw  1  time(s) out of playing both rps, and n" thus ending the program. 


The goal of the script is having multi simple game platform script:


if you enter any other thing than expected it will return error and it will keep asking you until you enter acceptable values

how to run the script in desktop powershell
download python and put it in path
then open terminal
go to the folder where the script is present
put the command: python GameProject.py
and then the script should run
'''
