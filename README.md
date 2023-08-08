# Dart-Board-Investing
A notion in investing is that a monkey selecting stocks by throwing darts at a dartboard blindfolded can outperform a carefully selected portfolio devised by experts in the industry. To entertain the concept, I connected an electronic dartboard to a Raspberry Pi 4 and used the Alpaca Trading API to develop a stock portfolio exclusively through throwing darts at a dartboard. This was accomplished by using alligator clips to attach the matrix in the back of the board to the Raspberry Pi’s GPIO pins and reading the inputs for ten consecutive throws. Prior to selection, each spot on the dartboard (positions 1 through 20 and the inner and outer bullseyes) was assigned a random fractionable stock from the NASDAQ, and the amount of money you chose for each throw’s investment was subject to the dartboard’s point modifier (outer circle and outer bullseye is 2x, inner circle and inner bullseye is 3x).

The stocks chosen and their proportion of the developed portfolio were: 

AMR - 18.18%
DLB - 9.09%
AZN - 9.09%
VERX - 9.09%
TREE - 9.09%
SSP - 9.09%
PDSB - 9.09%
BDTX - 9.09%
PTVE - 18.18%

![IMG_7158](https://github.com/NickCoding22/Dart-Board-Investing/assets/105902020/2c7c92c3-093c-43ff-9c43-1bbe8d082c47)
