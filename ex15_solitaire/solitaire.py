"""Golf solitaire."""

from itertools import zip_longest
from textwrap import dedent
from cards import Deck


class Solitaire:
    """Solitaire class representing a game of Golf Solitaire."""

    columns = 7
    cards_in_column = 5

    def __init__(self):
        """Constructor, do the setup here."""
        # your code, replace with proper setup
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.tableau = [[] for x in range(self.columns)]
        for i in self.tableau:
            for x in range(self.cards_in_column):
                i.append(self.deck.cards[-1])
                self.deck.deal_card()
        self.waste = [self.deck.cards[-1]]
        self.deck.deal_card()
        self.stock = []
        for i in range(len(self.deck.cards)):
            self.stock.append(self.deck.cards[-1])
            self.deck.deal_card()

    def can_move(self, card) -> bool:
        """Validate if a card from the tableau can be moved to the waste pile."""
        last_cards = [x[-1] for x in self.tableau if len(x) > 0]
        return abs(card.rank - self.waste[-1].rank) == 1 and card in last_cards

    def move_card(self, col: int):
        """Move a card from the tableau to the waste pile."""
        self.waste.append(self.tableau[col][-1])
        self.tableau[col].pop()

    def deal_from_stock(self):
        """Deal last card from stock pile to the waste pile."""
        if len(self.stock) > 0:
            self.waste.append(self.stock[-1])
            self.stock.pop()

    def has_won(self) -> bool:
        """Check for the winning position - no cards left in tableau."""
        return False if [x for x in self.tableau if len(x) > 0] else True

    def has_lost(self) -> bool:
        """Check for the losing position."""
        test = [x[-1] for x in self.tableau if len(x) > 0]
        moves = [x for x in test if self.can_move(x)]
        return len(self.stock) == 0 and len(moves) == 0

    def print_game(self):
        """Print the game."""
        print(f" {'    '.join(list('0123456'))}")
        print('-' * 34)
        print("\n".join([(" ".join((map(str, x)))) for x in (zip_longest(*self.tableau, fillvalue="    "))]))
        print()
        print(f"Stock pile: {len(self.stock)} card{'s' if len(self.stock) != 1 else ''}")
        print(f"Waste pile: {self.waste[-1] if self.waste else 'Empty'}")

    @staticmethod
    def rules():
        """Print the rules of the game."""
        print("Rules".center(40, "-"))
        print(dedent("""
                Objective: Move all the cards from each column to the waste pile.

                A card can be moved from a column to the waste pile if the
                rank of that card is one higher or lower than the topmost card
                of the waste pile. Only the first card of each column can be moved.

                You can deal cards from the stock to the waste pile.
                The game is over if the stock is finished and
                there are no more moves left.

                The game is won once the tableau is empty.

                Commands:
                  (0-6) - integer of the column, where the topmost card will be moved
                  (d) - deal a card from the stock
                  (r) - show rules
                  (q) - quit
                  """))

    def play(self):
        """Play a game of Golf Solitaire."""
        while True:
            if self.has_won():
                print("YOU WIN!")
                break
            if self.has_lost():
                print("YOU LOST!")
                break
            self.print_game()
            a = input("[COL : 0-6, DEAL : d, RULES: r, QUIT: q] : ")
            if a == "d":
                self.deal_from_stock()
            if a == "r":
                print(self.rules())
            if a == "q":
                print("Good bye!")
                break
            if a.isdigit():
                if int(a) in [0, 1, 2, 3, 4, 5, 6]:
                    if self.can_move(self.tableau[int(a)][-1]) and len(self.tableau[int(a)]) > 0:
                        self.move_card(int(a))


if __name__ == '__main__':
    s = Solitaire()
    s.play()
