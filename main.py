import random

# Define a class for the player's movement
class Movement:
    def __init__(self, direction):
        self.direction = direction

    def go(self):
        if self.direction == "north":
            print("You head north.")
        elif self.direction == "south":
            print("You head south.")
        elif self.direction == "east":
            print("You head east.")
        elif self.direction == "west":
            print("You head west.")
        else:
            print("Invalid direction.")


# Define a class for the player's inventory
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to your inventory.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from your inventory.")
        else:
            print(f"{item} not found in your inventory.")

    def view_inventory(self):
        if len(self.items) == 0:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in self.items:
                print(item)


# Define a class for the enemy
class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        return random.randint(1, self.damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated.")
            return True
        else:
            print(f"{self.name} has {self.health} health remaining.")
            return False


# Define the game loop
def game_loop():
    # Create the player's inventory and set their starting location
    inventory = Inventory()
    location = "forest"

    # Create the enemy
    enemy = Enemy("Goblin", 10, 3)

    # Loop until the player either defeats the enemy or dies
    while True:
        # Display the player's options and get their choice
        print(f"You are in the {location}.")
        print("Options:")
        print("1. Move")
        print("2. View inventory")
        print("3. Attack enemy")
        print("4. Quit game")

        choice = input("Enter your choice: ")

        # Process the player's choice
        if choice == "1":
            # Allow the player to move in different directions
            direction = input("Enter a direction (north, south, east, west): ")
            movement = Movement(direction)
            movement.go()
            location = "cave"
        elif choice == "2":
            # View the player's inventory
            inventory.view_inventory()
        elif choice == "3":
            # Combat with the enemy
            print("You attack the Goblin.")
            enemy.take_damage(random.randint(1, 5))
            if enemy.take_damage(random.randint(1, 5)):
                print("You have defeated the Goblin.")
                break
            print(f"The Goblin attacks you for {enemy.attack()} damage.")
        elif choice == "4":
            # Quit the game
            print("Thanks for playing!")
            break
        else:
            # Invalid choice
            print("Invalid choice.")


# Start the game
game_loop()
