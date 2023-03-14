import math
import random


class Character:
    def __init__(self, name, health_points, energy_points, attack_power, defense_power, special_attack_power, special_attack_energy, winning_message, losing_message) -> None:
        self.name = name
        self.health_points = health_points
        self.energy_points = energy_points
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.special_attack_power = special_attack_power
        self.special_attack_energy = special_attack_energy
        self.winning_message = winning_message
        self.losing_message = losing_message
        self.possible_choice = ["a", "d", "s"]
        self.choice = None
        self.max_health = health_points
        self.max_energy = energy_points

    def win(self):
        print(self.winning_message)

    def is_alive(self):
        return self.health_points > 0

    def print_stats(self):
        print(
            f"{self.name}\nHealth: {self.health_points}\nEnergy: {self.energy_points}")

    def choose_action(self):
        choice_complete = False
        while not choice_complete:
            choice = input(
                f"{self.name}, choose your action (Attack, Defend, Special Attack) (type A, D, S): ")
            if choice in self.possible_choice:
                self.choice = choice
                choice_complete = True

    def regenerate_energy_and_health(self, energy=10, health=10):
        self.energy_points = min(self.max_energy, self.energy_points + energy)
        self.health_points += min(self.max_health, self.health_points + health)

    def get_attack_power(self):
        random_num = (random.random() * 0.4) + 0.8
        return math.floor(self.attack_power * random_num)

    def get_defense_power(self):
        random_num = (random.random() * 0.4) + 0.8
        return math.floor(self.defense_power * random_num)


class Knight(Character):
    def __init__(self) -> None:
        super().__init__("Knight", 100, 50, 20, 30, 20, 30, "Victory is mine, nothing is mightier than the sword!",
                         "I...I cannot believe it. How could I lose?")


class Wizard(Character):
    def __init__(self) -> None:
        super().__init__("Wizard", 70, 100, 30, 10, 40, 30, "Your physical prowess was no match for the power of my spells.",
                         "You may have won this time, but I will return with even greater power!")


class Assassin(Character):
    def __init__(self) -> None:
        super().__init__("Assassin", 80, 60, 25, 20, 15, 20, "Ha, you never saw me coming! Your defeat was inevitable.",
                         "You...you got lucky. I'll be back, and I'll be ready for you.")


class Troll(Character):
    def __init__(self) -> None:
        super().__init__("Troll", 150, 40, 35, 25, 30, 40, "I am the strongest there is! None can stand against my might.",
                         "How...how could I lose? I thought I was invincible.")


class Dragon(Character):
    def __init__(self) -> None:
        super().__init__("Dragon", 120, 80, 40, 35, 50, 60, "I am the master of fire and fury! None can hope to withstand my power.",
                         "What sorcery is this? How could a mere mortal defeat me?")
