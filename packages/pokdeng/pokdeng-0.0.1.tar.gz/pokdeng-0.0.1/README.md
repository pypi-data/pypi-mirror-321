# pokdeng

[pokdeng](https://pypi.org/project/pokdeng/) is a Python package for simulating rounds of pokdeng games!

[Visit repository on Github](https://github.com/papillonbee/pokdeng)

## Quick Guide
Create player ```Kanye``` where he will
- place bet amount = 2 if his pocket has a minimum balance of 3 after deducting the bet amount
- draw the third card if his two cards on hand are not two deng or score less than 4
```python
from pokdeng.cardholder import Dealer, Player
from pokdeng.hand import Hand
from pokdeng.game import Game
from pokdeng.pocket import Pocket
from decimal import Decimal

class Kanye(Player):
    def place_bet(self, round: int, pocket: Pocket) -> Decimal:
        bet = Decimal("2")
        if pocket.total_amount - bet >= Decimal("3"):
            return bet
        return None
    def draw_card(self, round: int, pocket: Pocket, hand: Hand) -> bool:
        return hand.deng() != 2 or hand.score() < 4
```

```
kanye = Kanye()
```

Create player ```Ben``` where he will
- place bet amount = 1 if his pocket has a minimum balance of 0 after deducting the bet amount
- draw the third card if his two cards on hand score lesss than 5

```
ben = Player()
```

Create dealer ```Anita``` where she will
- fight her two cards on hand with three cards on other player's hands if two deng and score more than 4
- draw the third card if her two cards on hand score less than 3
```python
class Anita(Dealer):
    def two_fight_three(self, round: int, pocket: Pocket, hand: Hand) -> bool:
        return hand.deng() == 2 and hand.score() > 4
    def draw_card(self, round: int, pocket: Pocket, hand: Hand) -> bool:
        return hand.score() < 3
```

```
anita = Anita()
```

Create dealer ```Dixon``` where he will
- fight his two cards on hand with three cards on other player's hands if score more than 5
- draw the third card if his two cards on hand score less than 5

```
dixon = Dealer()
```

Create pocket for each dealer/player with some amount where dealer's pocket usually starts with 0 amount while player's pocket starts with positive amount
```python
kanye_pocket = Pocket(kanye.card_holder_id, Decimal(10))
ben_pocket = Pocket(ben.card_holder_id, Decimal(10))
anita_pocket = Pocket(anita.card_holder_id, Decimal(0))
```

Create a collection of pockets by dealer/player
```
pockets = {kanye.card_holder_id: kanye_pocket, ben.card_holder_id: ben_pocket, anita.card_holder_id: anita_pocket}
```

Create a game of 1 dealer, a list of players, and a collection of pockets by dealer/player
```python
game = Game(dealer = anita, players = [kanye, ben], pockets = pockets)
```

Play the game for 200 rounds
```python
game.play(200)
```

Check total amount in each pocket afterwards
```python
[(str(card_holder_id.value), pocket.total_amount) for card_holder_id, pocket in pockets.items()]
```

Pokdeng is a zero sum game, meaning the total amount in each pocket should sum to zero
