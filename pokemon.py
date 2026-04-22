# Write code below 💖

class Pokemon():
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        duplicate = self.name + self.name
        return duplicate

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {', '.join(self.types)}")  # joins list into a string
        print(f"Description: {self.description}")
        caught_text = "already been caught!" if self.is_caught else "not caught yet."
        print(f"{self.name} has {caught_text}")

beedrill = Pokemon(15, 'BeeDrill', ['Poison'], 'It has three poisonous stingers on its forelegs and its tail. They are used to jab its enemy repeatedly.', False)
pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on its cheeks. If threatened, it looses electric charges from the sacs.', True)
charmander = Pokemon(4, 'Charmander', ['Fire'], 'It has a flame on the tip of its tail that burns brightly when it is happy or angry.', False)

beedrill.speak()
beedrill.display_details()

pikachu.speak()
pikachu.display_details()

charmander.speak()
charmander.display_details()