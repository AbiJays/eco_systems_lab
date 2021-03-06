from src.river import River

class Bear:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []
    
# A bear should have a roar method
    def bear_roar (self):
        return "roar"

# A bear should have a food_count method
    def food_count (self):
        return len(self.stomach)

# A bear should be able to take a fish from the river
    def bear_take_fish_from_river(self, river):
        yummy_fish = River.lose_fish(river)
        self.stomach.append(yummy_fish)
