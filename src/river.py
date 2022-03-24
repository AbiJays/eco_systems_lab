class River:

    def __init__ (self, name, fish):
        self.name = name
        self.fish = fish
    
    def lose_fish(self):
        # breakpoint()
        yummy_fish = self.fish.pop()
        return yummy_fish

    # A river should have a fish_count method
    def fish_count(self):
        return len(self.fish)
    
