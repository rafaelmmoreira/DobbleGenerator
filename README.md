# DobbleGenerator
Generate your own Dobble/Spot It set of cards from your custom images.

## The game
Dobble/Spot It is a game where each card has several symbols. Every two cards has exactly one matching symbol. Players must spot the matching symbol between cards before their opponent does.

A typical Dobble deck features 57 different symbols, and each card has 8 symbols. There are 57 possible cards, although the game comes with only 55 cards (meaning two possible cards have been excluded).

## The algorithm
This piece of code is a just-for-fun attempt at implementing the algorithm described by Matt Parker ([Stand-up Maths](https://www.youtube.com/channel/UCSju5G2aFaWMqn-_0YBtq5A)) on his video [How does Dobble (Spot It) work?](https://www.youtube.com/watch?v=VTDKqW_GLkw). The video, just like most of his channel, introduces some tricky math in a very intuitive way, so check it out to understand better how this code works.

I opted to implement the "grid" algorithm, rather than the fixed intervals one, but both yield the same results. The algorithm itself is very simple and consists of a few for loops adding symbols to each card.

Most of the code are functions using [PIL] (https://pypi.org/project/Pillow/) (required) to draw the cards and export them as PNG. I'll attempt to generate a PDF file with several cards per page to make it easier to print.

## How to use the program
Just add 57 different images to the "img" folder. I included some sample emojis from a pack made by Adrian Garza. Once you're good to go, just run the code and it should create a "cards" folder with 57 different PNGs. It's up to you whether to use all 57 cards or ditch two random ones to make it more like the real game.

## Disclaimer
No copyright infringement is intended. This project was made just for fun, and it's intended exclusively for personal use. Don't sell your versions of the game. And, of course, if you have the opportunity, buy the [real game](https://www.dobblegame.com/en/games/) too. There are several different editions and fun spin-offs.
