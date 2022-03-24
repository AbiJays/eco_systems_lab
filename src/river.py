class River:

    def __init__ (self, name, fish):
        self.name = name
        self.fishes = fish
    
    def lose_fish(self, fish):
        fish_index = self.fishes.index(fish)
        yummy_fish = self.fishes.pop(fish_index)
        return yummy_fish
        # return self.fishes.pop

    # A river should have a fish_count method
    def fish_count(self):
        return len(self.fishes)