

class Entity:
    '''    
    - **Attributes:** It should have `name` (string) and `health` (integer).

    - **Methods:** `take_damage(amount)`: This subtracts the amount from the entity's health and prints a message saying how much damage was taken and how much health remains.
    
    `attack(target)`: This takes another Entity as a parameter. It prints a message that the player is attacking with their specific weapon, and then calls the target's `take_damage` method.
    '''
