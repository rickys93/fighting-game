from characters import (
    Knight,
    Wizard,
    Assassin,
    Troll,
    Dragon
)


class Player:
    def __init__(self, character) -> None:
        self.character = character


class Game:
    def __init__(self) -> None:
        self.players = []
        self.possible_characters = [
            "Knight", "Wizard", "Assassin", "Troll", "Dragon"]
        self.possible_choices = ["k", "w", "a", "t", "d"]
        self.characters = {
            "k": Knight,
            "w": Wizard,
            "a": Assassin,
            "t": Troll,
            "d": Dragon,
        }

    def start(self):
        self.choose_characters()

        self.start_round()

    def choose_characters(self):
        while len(self.players) < 2:
            self.players.append(self.player_choice())

    def all_players_alive(self):
        for player in self.players:
            if not player.is_alive():
                return False
        return True

    def player_choice(self):
        player = None
        while not player:
            message = f"Player {len(self.players) + 1}, choose from (" + ", ".join(self.possible_characters) + \
                "). Type (" + ", ".join([c[0]
                                         for c in self.possible_characters]) + "): "
            choice = input(message).lower()
            if choice in self.possible_choices:
                player = self.characters[choice]()
                character_name = player.name
                self.possible_characters.remove(character_name)
                self.possible_choices.remove(choice)
                print(
                    f"Player {len(self.players) + 1}, choose {player.name}. Great choice!")
                return player

    def determine_result(self):
        if self.players[0].choice == "a" and self.players[1].choice == "a":
            for player in self.players:
                pass

    def start_fight(self):
        while self.all_players_alive():
            for player in self.players:
                player.choose_action()

            self.determine_result()


game = Game()
game.start()
