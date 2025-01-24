from pathlib import Path
import sys

from ccaerrors import errorExit, errorNotify, errorRaise
import ccalogging
import platformdirs

from ccacards import __appname__, __carddir__, __version__

log = ccalogging.log


class Card:
    """Representation of a Playing Card."""

    valueNames = [
        "Ace",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
    ]

    suitNames = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self, index, facedown=False):
        """Initialises the Card

        args:
            index: int 0 - 52
                0 is a placeholder for 'no card' i.e. blank space
                1 == Ace of Spades
                13 == King of Spades
                14 == Ace of Hearts
                26 == King of Hearts
                27 == Ace of Diamonds
                39 == King of Diamonds
                40 == Ace of Clubs
                52 == King of Clubs
        """
        try:
            if index < 0 or index > 52:
                raise ValueError(f"Card index out of range: {index}")
            self._facedown = facedown
            self._index = index
            if self._index == 0:
                self._value = 0
                self._valuename = "Blank"
                self._suit = "Blank"
            else:
                self._suitindex, self._value = divmod(self._index - 1, 13)
                self._valuename = self.valueNames[self._value]
                self._suit = self.suitNames[self._suitindex]
            self._imagefile = Path(__carddir__, f"{self._index}.png")
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __str__(self):
        try:
            return (
                "Face Down" if self.facedown else f"{self._valuename} of {self._suit}"
            )
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __repr__(self):
        try:
            return f"Card({self._index})"
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    @property
    def value(self):
        """Returns the value of the card 1 - 13"""
        return self._value

    @property
    def valuename(self):
        """Returns the string name of the card value"""
        return self._valuename

    @property
    def suit(self):
        """Returns the string name of the card suit"""
        return self._suit

    @property
    def imagefile(self):
        """Returns the path to the image file for this card"""
        return self._imagefile

    @property
    def facedown(self):
        """Returns True if the card is face down"""
        return self._facedown

    def flip(self):
        """Flips the card face up or face down"""
        self._facedown = not self._facedown


if __name__ == "__main__":
    card = Card(1)
    print(card)
    card = Card(52)
    print(card)
    card = Card(0)
    print(card)
    card = Card(13)
    print(card)
    card = Card(14)
    print(card)
    card = Card(26)
    print(card)
    card = Card(27)
    print(card)
    card = Card(39)
    print(card)
    card = Card(40)
    print(card)
    card = Card(51)
    print(card)
    card = Card(52)
    print(card)
    card = Card(53)
    print(card)
