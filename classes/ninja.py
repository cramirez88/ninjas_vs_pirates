class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        # Customize the attack methods on both the ninja and pirate
        import random 
        ninja_strength = random.randint(0, self.strength)
        pirate_strength = random.randint(0, self.strength)
        if ninja_strength > pirate_strength:
             pirate.health -= self.strength
             print(f'The pirate got recked! {self.health} remaining')
        elif pirate_strength > ninja_strength:
            print(f'The pirate took no damage {self.health} remaining')
        else:
            print(f'The ninja and pirate took equal amounts of damage, which cancel each other out: {self.health} remaining')

        return self

