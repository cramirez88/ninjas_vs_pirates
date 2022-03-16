class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        import random 
        ninja_strength = random.randint(0, self.strength)
        pirate_strength = random.randint(0, self.strength)
        if pirate_strength > ninja_strength:
             ninja.health -= self.strength
             print(f'The ninja got recked! {self.health} remaining')
        elif pirate_strength > ninja_strength:
            print(f'The ninja took no damage {self.health} remaining')
        else:
            print(f'The ninja and pirate took equal amounts of damage, which cancel each other out: {self.health} remaining')
        return self

