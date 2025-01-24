import sys

from ccaerrors import errorExit, errorNotify, errorRaise
import ccalogging

log = ccalogging.log


class Pile:
    """Representation of a Pile of Playing Cards."""

    def __init__(self):
        """Initialises an empty Pile."""
        try:
            self.cards = []
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __repr__(self):
        """Placeholder repr(Pile) function."""
        try:
            return f"Pile()"
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __str__(self):
        """Placeholder str(Pile) function. LIFO ordering."""
        try:
            return str([str(c) for c in reversed(self.cards)])
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def __len__(self):
        """returns the length of this Pile."""
        try:
            return len(self.cards)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def append(self, card):
        """Adds a card to the top of this Pile."""
        try:
            self.cards.append(card)
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def pop(self):
        """Removes the top card and returns it, or None if Pile is empty."""
        try:
            if len(self) > 0:
                return self.cards.pop()
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)

    def peek(self):
        """Returns the top card without removing it from the Pile, or None if Pile is empty."""
        try:
            if len(self) > 0:
                return self.cards[-1]
        except Exception as e:
            errorRaise(sys.exc_info()[2], e)


if __name__ == "__main__":
    # ccalogging.setDebug()
    # ccalogging.setConsoleOut()
    # log.info("Pile object.")
    s = Pile()
    [s.append(c) for c in range(1, 11)]
    print(s)
    print(f"pop: {s.pop()}")
    print(f"pop: {s.pop()}")
    print(f"pop: {s.pop()}")
    print(f"peek: {s.peek()}")
    print(s)
