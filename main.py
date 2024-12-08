import random

# Base Character class
class Character:
    def __init__(self, name, health, attackPower):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.maxHealth = health

    def attack(self, opponent):
        damage = random.randint(self.attackPower - 5, self.attackPower + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        healAmount = random.randint(10, 20)
        self.health = min(self.maxHealth, self.health + healAmount)
        print(f"{self.name} heals for {healAmount} health. Current health: {self.health}/{self.maxHealth}")

    def displayStats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.maxHealth}, Attack Power: {self.attackPower}")

# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attackPower=25)

    def specialAbility(self, opponent):
        print(f"{self.name} uses 'Power Strike'!")
        damage = self.attackPower * 2
        opponent.health -= damage
        print(f"{self.name} deals {damage} damage to {opponent.name}!")

# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attackPower=35)

    def specialAbility(self, opponent):
        print(f"{self.name} uses 'Fireball'!")
        damage = self.attackPower + 10
        opponent.health -= damage
        print(f"{self.name} deals {damage} damage to {opponent.name}!")

# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attackPower=20)

    def specialAbility(self, opponent):
        print(f"{self.name} uses 'Quick Shot'!")
        for _ in range(2):
            damage = self.attackPower
            opponent.health -= damage
            print(f"{self.name} shoots for {damage} damage!")

# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attackPower=15)

    def specialAbility(self, opponent):
        print(f"{self.name} uses 'Holy Strike'!")
        damage = self.attackPower + 15
        opponent.health -= damage
        print(f"{self.name} deals {damage} damage to {opponent.name}!")

# Evil Wizard class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attackPower=15)

    def regenerate(self):
        regenAmount = 5
        self.health += regenAmount
        print(f"{self.name} regenerates {regenAmount} health! Current health: {self.health}")

def createCharacter():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    classChoice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")
    if classChoice == '1':
        return Warrior(name)
    elif classChoice == '2':
        return Mage(name)
    elif classChoice == '3':
        return Archer(name)
    elif classChoice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        choice = input("Choose an action: ")
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.specialAbility(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.displayStats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

        if wizard.health <= 0:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = createCharacter()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
