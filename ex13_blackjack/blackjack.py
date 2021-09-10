"""Simple game of blackjack."""
from textwrap import dedent
import requests


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str):
        """Card description."""
        self.value = value
        self.suit = suit
        self.code = code

    def __repr__(self):
        """Card representation."""
        return self.code


class Hand:
    """Simple class for holding hand information."""

    def __init__(self):
        """Hand description."""
        self.cards = []
        self.score = 0
        self.ace = []

    def add_card(self, card: Card):
        """Add card to the hand."""
        self.cards.append(card)
        if card.value in ['JACK', 'QUEEN', 'KING']:
            self.score += 10
        elif card.value == "ACE":
            if self.score <= 10:
                self.score += 11
                self.ace.append("A")
            elif self.score > 10:
                self.score += 1
        else:
            self.score += int(card.value)
        if self.score > 21:
            if len(self.ace) > 0:
                self.score -= 10
                self.ace.pop()


class Deck:
    """Deck of cards. Provided via api over the network."""

    def __init__(self, shuffle=False):
        """
        Tell api to create a new deck.

        :param shuffle: if shuffle option is true, make new shuffled deck.
        """
        if shuffle is False:
            self.deck = requests.get("https://deckofcardsapi.com/api/deck/new").json()
            self.is_shuffled = False
        else:
            self.deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle").json()
            self.is_shuffled = True
        self.deck_id = self.deck["deck_id"]

    def shuffle(self):
        """Shuffle the deck."""
        self.deck = requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/shuffle").json()
        self.is_shuffled = True

    def draw(self) -> Card:
        """
        Draw card from the deck.

        :return: card instance.
        """
        card = requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw").json()
        return Card(str(card["cards"][0]["value"]), str(card["cards"][0]["suit"]), str(card["cards"][0]["code"]))
        pass


class BlackjackController:
    """Blackjack controller. For controlling the game and data flow between view and database."""

    def __init__(self, deck: Deck, view: 'BlackjackView'):
        """
        Start new blackjack game.

        :param deck: deck to draw cards from.
        :param view: view to communicate with.
        """
        self.deck = deck
        self.view = view
        self.state = {}
        if self.deck.is_shuffled is False:
            self.deck.shuffle()
        self.start(view)

    def start(self, view: 'BlackjackView'):
        """Start game."""
        dealer = Hand()
        player = Hand()
        for i in range(2):
            player.add_card(self.deck.draw())
            dealer.add_card(self.deck.draw())
        self.state["dealer"] = dealer
        self.state["player"] = player
        self.player_turn(view, player, dealer)

    def player_turn(self, view: 'BlackjackView', player: Hand, dealer: Hand):
        """Player takes card."""
        while True:
            del self.state["player"]
            self.state["player"] = player
            if player.score == 21:
                view.player_won(self.state)
                break
            if player.score > 21:
                view.player_lost(self.state)
                break
            if player.score < 21:
                if view.ask_next_move(self.state) == "H":
                    player.add_card(self.deck.draw())
                else:
                    break
        self.dealer_turn(view, player, dealer)

    def dealer_turn(self, view: 'BlackjackView', player: Hand, dealer: Hand):
        """Dealer takes card."""
        while True:
            del self.state["dealer"]
            self.state["dealer"] = dealer
            if player.score < 21:
                if dealer.score == 21 or player.score < dealer.score < 22:
                    view.player_lost(self.state)
                    break
                if dealer.score > 21:
                    view.player_won(self.state)
                    break
                if dealer.score < player.score:
                    dealer.add_card(self.deck.draw())
            else:
                break


class BlackjackView:
    """Minimalistic UI/view for the blackjack game."""

    def ask_next_move(self, state: dict) -> str:
        """
        Get next move from the player.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :return: parsed command that user has choses. String "H" for hit and "S" for stand
        """
        self.display_state(state)
        while True:
            action = input("Choose your next move hit(H) or stand(S) > ")
            if action.upper() in ["H", "S"]:
                return action.upper()
            print("Invalid command!")

    def player_lost(self, state):
        """
        Display player lost dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You lost")

    def player_won(self, state):
        """
        Display player won dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You won")

    def display_state(self, state, final=False):
        """
        Display state of the game for the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :param final: boolean if the given state is final state. True if game has been lost or won.
        """
        dealer_score = state["dealer"].score if final else "??"
        dealer_cards = state["dealer"].cards
        if not final:
            dealer_cards_hidden_last = [c.__repr__() for c in dealer_cards[:-1]] + ["??"]
            dealer_cards = f"[{','.join(dealer_cards_hidden_last)}]"

        player_score = state["player"].score
        player_cards = state["player"].cards
        print(dedent(
            f"""
            {"Dealer score":<15}: {dealer_score}
            {"Dealer hand":<15}: {dealer_cards}

            {"Your score":<15}: {player_score}
            {"Your hand":<15}: {player_cards}
            """
        ))


if __name__ == '__main__':
    BlackjackController(Deck(), BlackjackView())  # start the game.
