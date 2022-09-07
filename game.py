"""
Do not remove this file. Ensure your main function is in this file.

I will execute your game like this:

python3 game.py

Yes, you may add additional files to this folder.
"""
import random
import itertools
import sys


def create_classes() -> tuple:
    """
    Create a tuple of attributes of the four character classes.

    :postcondition: must correctly create a tuple of four dictionaries, each representing the attributes of a class
    :return: a tuple of four dictionaries
    """
    return (
        {'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'), 'max_HP': (100, 150, 200),
         'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6, 'special_attack': bash,
         'special_attack_name': 'Bash'},
        {'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'), 'max_HP': (100, 120, 150),
         'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5, 'special_attack': confusion,
         'special_attack_name': 'Confusion'},
        {'class name': 'Amazon', 'class levels': ('Archer', 'Ranger', 'Demon Hunter'),
         'max_HP': (100, 140, 180),
         'levelup_XP': (100, 160), 'max_damage': (30, 40, 50), 'accuracy': 0.8, 'special_attack': focus,
         'special_attack_name': 'Focus'},
        {'class name': 'Thief', 'class levels': ('Bandit', 'Assassin', 'Night Lord'),
         'max_HP': (100, 130, 160),
         'levelup_XP': (100, 150), 'max_damage': (20, 30, 40), 'accuracy': 0.9, 'special_attack': terror,
         'special_attack_name': 'Terror'})


def create_foe() -> dict:
    """
    Create a nested dictionary of attributes of the nine types of foes.

    :postcondition: must correctly create a nested dictionary which contains 9 key value pairs, each value is a
                    dictionary that stores the information of a specific type of foe
    :return: a nested dictionary
    """
    return {'Spider': {'HP': 30, 'max_damage': 10, 'accuracy': 0.5, 'XP': 10},
            'Ghoul': {'HP': 35, 'max_damage': 12, 'accuracy': 0.5, 'XP': 15},
            'Skeleton': {'HP': 40, 'max_damage': 14, 'accuracy': 0.5, 'XP': 20},
            'Deceiver': {'HP': 45, 'max_damage': 16, 'accuracy': 0.6, 'XP': 30},
            'Succubus': {'HP': 50, 'max_damage': 18, 'accuracy': 0.6, 'XP': 40},
            'Berserker': {'HP': 60, 'max_damage': 20, 'accuracy': 0.6, 'XP': 50},
            'Death maiden': {'HP': 80, 'max_damage': 22, 'accuracy': 0.7, 'XP': 60},
            'Corrupted angel': {'HP': 90, 'max_damage': 24, 'accuracy': 0.7, 'XP': 70},
            'Soul reaper': {'HP': 100, 'max_damage': 26, 'accuracy': 0.7, 'XP': 80}}


def create_boss() -> dict:
    """
    Create a dictionary of attributes of the final boss.

    :postcondition: must correctly create a dictionary which contains 5 key value pairs storing the boss information
    :return: a single dictionary
    """
    return {'name': 'Diablo', 'HP': 150, 'max_damage': 30, 'accuracy': 0.8, 'special_attack': 'Thunder'}


def make_board(rows: int, columns: int) -> dict:
    """
    Create a dictionary to represent a 2D game board of rows x columns.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows and columns must be positive, non-zero integers that are greater than or equal to 2
    :postcondition: must correctly generate a dictionary that contains rows * columns keys, where each key is a tuple
                    that contains a set of coordinates of indices, and each value is a description of the room
    :return: a dictionary of board locations and room description messages
    """
    room_description = ['There is nothing in this room', 'You found a goblin merchant', 'You found 50 gold!',
                        'You found a tavern', 'You found a weapon!', 'You found a piece of armor!',
                        'You found a health potion!', 'This is a training field', 'You found some beautiful thistles',
                        'There are some small animals']
    return {(row, column): random.choice(room_description) for row in range(rows) for column in range(columns)}


def get_character_name() -> str:
    """
    Acquire the character name from the user.

    :postcondition: must correctly get the character name from user
    :return: a string that represents the name of the character
    """
    print('\nPlease create a name for your character: ')
    character_name = input()
    return character_name


def get_character_class() -> str:
    """
    Acquire the character class choice from the user.

    :postcondition: must correctly get the character class number from user
    :return: a string of number 1 or 2 or 3 or 4 that represents Warrior, Sorcerer, Amazon and Thief respectively
    """
    class_number = input()
    return class_number


def valid_user_choice(number_input: str, choice_length: int) -> bool:
    """
    Determine if user's input choice is valid or not.

    :param number_input: a string of a single character of number 1 or 2 or 3 or 4
    :param choice_length: an integer that is either 2 or 4
    :precondition: number_input is a single character string of integer 1 or 2 or 3 or 4, it cannot be anything else
    :precondition: choice_length must be an integer of either 2 or 4, it cannot be anything else
    :postcondition: must correctly generate a boolean representing the validity of user's input choice
    :return: True or False
`
    >>> valid_user_choice('2', 2)
    True
    >>> valid_user_choice('5', 4)
    False
    """
    return number_input in map(str, list(range(1, choice_length + 1)))


def determine_class_type(class_number: str) -> str:
    """
    Determine the corresponding class name for the user entered class choice.

    :param class_number: a string which is '1', '2', '3', or '4' representing user's preferred class for the game
    :precondition: class_number must be a string of '1', '2', '3', or '4', it cannot be an integer or any other string
    :postcondition: must correctly calculate the corresponding string of class name based on user's choice
    :return: a string of one of the four classes

    >>> determine_class_type('2')
    'Sorcerer'
    """
    four_class_types = ['Warrior', 'Sorcerer', 'Amazon', 'Thief']
    index_class_dict = dict((index, element) for index, element in enumerate(four_class_types))
    return index_class_dict[int(class_number) - 1]


def extract_class_attributes(classes_info: tuple, class_number: str) -> dict:
    """
    Generate a dictionary of class attributes using the class number.

    :param classes_info: a tuple of four dictionaries, each representing the attributes of a class
    :param class_number: a string which is '1', '2', '3', or '4' representing user's preferred class for the game
    :precondition: classes_info must be a tuple of four dictionaries where each dictionary contains 8 key value pairs
    :precondition: class_number must be a string and not an integer or other data types
    :postcondition: must correctly calculate the corresponding dictionary based on user's class choice
    :return: a dictionary representing the attributes of one of the four classes
    """
    return classes_info[int(class_number) - 1]


def make_character(character_name: str, class_attributes: dict) -> dict:
    """
    Create a dictionary which represents a character starting at coordinate(0, 0) who has an HP of 100.

    :param character_name: a string representing the character name chosen by the user
    :param class_attributes: a dictionary that contains all the information about the character's class
    :precondition: character_name must be the correct name that the user chose
    :precondition: class_attributes must be the correct corresponding class attributes that the user chose
    :postcondition: must correctly generate a dictionary of all the information about the character, including non-class
                    related and class related
    :return: a dictionary of 14 key-value pairs
    """
    character_without_class = {'name': character_name, 'level': 1, 'Current HP': 100, 'Current XP': 0,
                               'X-coordinate': 0, 'Y-coordinate': 0}
    return character_without_class | class_attributes


def get_user_direction_choice() -> str:
    """
    Acquire the moving direction from the user.

    :postcondition: must correctly get the direction as a string of number 1 or 2 or 3 or 4 from user
    :return: a string of a single character of number 1 or 2 or 3 or 4
    """
    print('\nWhich direction would you like to go? Please choose: \n 1. North \n 2. East \n 3. South \n 4. West\n'
          'Enter quit to end the game')
    direction = input()
    return direction


def validate_move(character: dict, direction: str) -> bool:
    """
    Examine if the character goes off board or not.

    :param character: a dictionary representing the playable character
    :param direction: a string of a single character of number 1 or 2 or 3 or 4
    :precondition: character is a nested dictionary of 14 key-value pairs that stores the x, y coordinates and other
                   information about the character
    :precondition: direction is a single character string representing North, East, South and West respectively
    :postcondition: must correctly determine whether the move is valid i.e. the character does not go off board
    :return: True or False
    """
    rows = 10
    columns = 10
    if (direction == '1' and character['Y-coordinate'] == 0) or \
            (direction == '2' and character['X-coordinate'] == columns - 1) or \
            (direction == '3' and character['Y-coordinate'] == rows - 1) or \
            (direction == '4' and character['X-coordinate'] == 0):
        return False
    return True


def move_character(character: dict, direction: str) -> dict:
    """
    Update the coordinates of the character after movement according to user's direction input.

    :param character: a dictionary that stores the information of the playable character
    :param direction: a string of a single character of number 1 or 2 or 3 or 4
    :precondition: character is a nested dictionary of 14 key-value pairs that store the x, y coordinates and other
                   information about the character
    :precondition: direction is a single character string representing North, East, South and West respectively
    :postcondition: must correctly update the location inside the character dictionary after user makes move
    :return: the character dictionary with updated x and y coordinates
    """
    if direction == '1':
        character['Y-coordinate'] -= 1
    elif direction == '2':
        character['X-coordinate'] += 1
    elif direction == '3':
        character['Y-coordinate'] += 1
    else:
        character['X-coordinate'] -= 1
    return character


def show_navigation_map(rows: int, columns: int, character: dict):
    """
    Show a navigation map showing the location of character on the game board.

    :param rows: an integer of how many rows there are in a game board
    :param columns: an integer of how many columns there are in a game board
    :param character: a dictionary representing the playable character
    :precondition: rows and columns must be positive, non-zero integers that are greater than or equal to 2
    :precondition: character is a nested dictionary of 14 key-value pairs that store the x, y coordinates and other
                   information about the character
    :postcondition: must correctly illustrate on an ASCII map where each [] denotes a room, [@] denoting the
                    character, where @ is the first letter of the character's name, and [D] denotes the boss Diablo
    :return: no return statement
    """
    character_coordinate = (character['X-coordinate'], character['Y-coordinate'])
    character_symbol = character['name'][0]
    map_dict = {(row, column): '[ ]' for row in range(rows) for column in range(columns)}
    for key in map_dict:
        if key == (9, 9):
            map_dict[key] = '[D]'
        if key == character_coordinate:
            map_dict[key] = f'[{character_symbol}]'
    for row in range(rows):
        for column in range(columns):
            print(map_dict[(column, row)], end=' ')
        print()


def describe_current_location(board: dict, character: dict):
    """
    Print the coordinate and description of character's current location.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the playable character
    :precondition: board is a dictionary that contains rows * columns keys, where each key is a tuple
                    that contains a set of coordinates of indices, and each value is a string description
    :precondition: character is a dictionary of 14 key-value pairs that store all applicable character information
    :postcondition: must print a message telling the user the correct coordinate the user is on, and also print a
                    randomly generated room description
    :return: no return statement
    """
    x_coordinate = character['X-coordinate']
    y_coordinate = character['Y-coordinate']
    print(f'You are on room coordinate({x_coordinate}, {y_coordinate})')
    print(board[(character['Y-coordinate'], character['X-coordinate'])])


def check_for_foes():
    """
    Determine if the character will encounter a foe in the current location.

    :postcondition: must correctly generate a boolean showing if there is a foe in the current coordinate
    :return: True or False
    """
    chance_encounter_foe = random.randint(1, 100)
    return chance_encounter_foe <= 20


def determine_foe_in_same_area(character: dict) -> list:
    """
    Determine the foe type character might encounter on different areas of the map.

    :param character: a dictionary that stores the information of the playable character, including the x,y coordinates
    :precondition: character is a nested dictionary of 14 key-value pairs that store the x, y coordinates and other
                   information about the character
    :postcondition: must correctly generate one of the three possible foes in the current row number
    :return: a list of all possible foe types in an area

    >>> determine_foe_in_same_area({'name': 'Joker', 'level': 2, 'Current HP': 150, 'Current XP': 150, \
    'X-coordinate': 0, 'Y-coordinate': 8, 'class name': 'Sorcerer', 'class levels': ('Mage', 'Wizard', 'Archmage'), \
    'max_HP': (100, 120, 150), 'levelup_XP': (100, 150), 'max_damage': (40, 60, 80), 'accuracy': 0.5, \
    'special_attack': confusion, 'special_attack_name': 'Confusion'})
    ['Death maiden', 'Corrupted angel', 'Soul reaper']
    """
    if character['Y-coordinate'] in [0, 1, 2, 3]:
        return ['Spider', 'Ghoul', 'Skeleton']
    elif character['Y-coordinate'] in [4, 5, 6, 7]:
        return ['Deceiver', 'Succubus', 'Berserker']
    else:
        return ['Death maiden', 'Corrupted angel', 'Soul reaper']


def determine_foe_type(foe_of_same_level: list) -> str:
    """
    Generate a random foe type for the character in the current map area.

    :param foe_of_same_level: a list of all possible foe types in an area
    :precondition: foe_of_the_same_level must be a list of 3 elements containing all possible foe types character might
                   encounter in the current area of the map
    :postcondition: must randomly generate one of the three foe types in the current map area
    :return: a string indicating a foe type in the character's current location
    """
    foe_list = []
    foe_generator = itertools.cycle(foe_of_same_level)
    for _ in range(999):
        foe_list.append(next(foe_generator))
    return foe_list[random.randint(0, 100)]


def extract_foe_attributes(foe_data: dict, foe_type: str) -> dict:
    """
    Generate the corresponding foe attributes given the foe type.

    :param foe_data: a nested dictionary which contains 9 key value pairs, each value is a dictionary that stores the
                     information of a specific type of foe
    :param foe_type: a string indicating the type of the foe
    :precondition: foe_data must be one of the 9 dictionaries generated by the create_foe function
    :precondition: foe_type must be a string of one of the 9 foe types
    :postcondition: must correctly generate the foe attributes which is a dictionary of 4 key value pairs
    :return: a single dictionary

    >>> extract_foe_attributes(create_foe(), 'Corrupted angel')
    {'HP': 90, 'max_damage': 22, 'accuracy': 0.7, 'XP': 70}
    """
    return foe_data[foe_type]


def get_user_choice_runaway() -> str:
    """
    Acquire the user's choice of running away or fighting in a battle.

    :postcondition: must correctly generate the user's choice number
    :return: a string of a number representing user's choice of fighting the foe or running away
    """
    print("Do you want to fight your foe or run away? \n [1] Fight the foe \n [2] Run away")
    user_choice = input()
    return user_choice


def get_user_attack_type(character: dict) -> str:
    """
    Acquire the user's choice of using the class special attack or not in the first round of a battle.

    :param character: a dictionary that stores the information of the playable character, including the name of the
                      special attack
    :precondition: character is a nested dictionary of 14 key-value pairs that store the special attack information and
                   other information about the character
    :postcondition: must correctly generate the user's choice number
    :return: a string of a number representing user's choice of using the special attack or not using it
    """
    special_attack = character['special_attack_name']
    print(f'Do you want to use your special skill: {special_attack}? \n [1] Yes \n [2] No')
    user_input = input()
    return user_input


def bash(character: dict, foe: dict, foe_type: str):
    """
    Perform the bash special attack by the warrior class.

    :param character: a dictionary representing the playable character
    :param foe: a dictionary that stores the information of the foe encountered
    :param foe_type: a string representing the type of the foe
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :precondition: foe is a dictionary storing foe attributes in 4 key value pairs
    :precondition: foe_type is a string of one of the nine types of foe
    :postcondition: must correctly deal the expected damage to the foe in the current round of battle
    :return: no return statement
    """
    level = character['level']
    damage_to_foe = character['max_damage'][level - 1] * 1.3
    modify_foe_hp(foe, damage_to_foe)
    print(f'Your Bash caused 1.3X ({damage_to_foe}) damage to {foe_type}!')


def confusion(character: dict, foe: dict, foe_type: str):
    """
    Perform the confusion special attack by the sorcerer class.

    :param character: a dictionary representing the playable character
    :param foe: a dictionary that stores the information of the foe encountered
    :param foe_type: a string representing the type of the foe
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :precondition: foe is a dictionary storing foe attributes in 4 key value pairs
    :precondition: foe_type is a string of one of the nine types of foe
    :postcondition: must correctly lower the foe's accuracy by 50% in the battle
    :return: no return statement
    """
    foe['accuracy'] *= 0.5
    skill = character['special_attack_name']
    print(f"Your skill {skill} reduced {foe_type}'s accuracy by 50%! ")


def focus(character: dict, foe: dict, foe_type: str):
    """
    Perform the focus special attack by the amazon class.

    :param character: a dictionary representing the playable character
    :param foe: a dictionary that stores the information of the foe encountered
    :param foe_type: a string representing the type of the foe
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :precondition: foe is a dictionary storing foe attributes in 4 key value pairs
    :precondition: foe_type is a string of one of the nine types of foe
    :postcondition: must correctly increase the character's accuracy to 100% in the battle
    :return: no return statement
    """
    character['accuracy'] = 1
    foe['accuracy'] *= 1
    print(f'Focus activated, you now have 100% accuracy against {foe_type}')


def terror(character: dict, foe: dict, foe_type: str):
    """
    Perform the terror special attack by the thief class.

    :param character: a dictionary representing the playable character
    :param foe: a dictionary that stores the information of the foe encountered
    :param foe_type: a string representing the type of the foe
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :precondition: foe is a dictionary storing foe attributes in 4 key value pairs
    :precondition: foe_type is a string of one of the nine types of foe
    :postcondition: must correctly reduce the foe's maximum damage by 50% in the battle
    :return: no return statement
    """
    skill = character['special_attack_name']
    foe['max_damage'] *= 0.5
    print(f'{skill} worked, {foe_type} will only deal half the damage from now on')


def attack_hit_foe(character: dict) -> bool:
    """
    Determine whether character's attack hits the foe.

    :param character: a dictionary that stores the information of the playable character
    :precondition: character must be a nested dictionary of 14 key-value pairs that store the attack accuracy and
                   other information about the character
    :postcondition: must correctly generate a boolean indicating whether character hits the foe or not
    :return: True or False
    """
    return random.random() < character['accuracy']


def character_damage_foe(character: dict) -> int:
    """
    Calculate the amount of damage the character caused the foe.

    :param character: a dictionary that stores the information of the playable character
    :precondition: character must be a nested dictionary of 14 key-value pairs that store the maximum damage, the level
                   and other information about the character
    :postcondition: must correctly calculate the damage as an integer, randomly generated within a specific range
    :return: an integer representing the amount of damage caused to the foe
    """
    return random.randrange(character['max_damage'][character['level'] - 1] - 5,
                            character['max_damage'][character['level'] - 1] + 1)


def modify_foe_hp(foe: dict, damage_to_foe: int) -> dict:
    """
    Reduce the HP of foe during a battle.

    :param foe: a dictionary that stores the information of the foe encountered
    :param damage_to_foe: an integer representing the damage caused to the character
    :precondition: foe must be a dictionary storing foe attributes in 4 key value pairs
    :precondition: damage_to_foe must be an integer within the damage range of [max_damage - 5, max_damage]
    :postcondition: must correctly adjust the foe's current HP according to the damage amount
    :return: updated foe dictionary with reduced HP

    >>> modify_foe_hp({'HP': 50, 'max_damage': 15, 'accuracy': 0.6, 'XP': 40}, 30)
    {'HP': 20, 'max_damage': 15, 'accuracy': 0.6, 'XP': 40}
    """
    foe['HP'] -= damage_to_foe
    return foe


def foe_runaway() -> bool:
    """
    Determine whether the foe will run away at the end of each turn of the battle.

    :postcondition: must correctly return a boolean representing the foe's behavior with a 20% chance of running away
    :return: True or False
    """
    return random.random() < 0.2


def attack_hit_character(foe: dict) -> bool:
    """
    Determine whether foe's attack hits the character.

    :param foe: a dictionary that stores the information of one of the 9 foe types
    :precondition: foe must be a single dictionary of 4 key-value pairs that store all information about a foe
    :postcondition: must correctly generate a boolean indicating whether the foe hits the character or not
    :return: True or False
    """
    return random.random() < foe['accuracy']


def foe_damage_character(foe: dict) -> int:
    """
    Calculate the amount of damage the foe caused the character.

    :param foe: a dictionary that stores the information of the foe encountered
    :precondition: foe must be a dictionary storing foe attributes in 4 key value pairs
    :postcondition: must correctly calculate the damage as an integer, randomly generated within a specific range
    :return: an integer representing the amount of damage caused to the character
    """
    return random.randrange(int(foe['max_damage'] - 3), int(foe['max_damage'] + 1))


def modify_character_hp(character: dict, damage_to_character: int) -> dict:
    """
    Reduce the HP of character during a battle.

    :param character: a dictionary representing the playable character
    :param damage_to_character: an integer representing the damage caused to the character
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :precondition: damage_to_character must be an integer within the damage range of [max_damage - 5, max_damage]
    :postcondition: must correctly adjust the character's current HP according to the damage amount
    :return: updated character dictionary with reduced HP
    """
    character['Current HP'] -= damage_to_character
    return character


def is_character_alive(character: dict) -> bool:
    """
    Determine if the character is alive or dead.

    :param character: a dictionary representing the playable character
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :postcondition: correctly generate a boolean checking if the character's HP is greater than 0 (alive) or not (dead)
    :return: True or False

    >>> is_character_alive({'name': 'Stefan', 'level': 1, 'Current HP': 0, 'Current XP': 120, 'X-coordinate': 0, \
    'Y-coordinate': 0, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'), 'max_HP': \
    (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6, 'special_attack': bash, \
    'special_attack_name': 'Bash'})
    False
    """
    return character["Current HP"] > 0


def is_foe_alive(foe: dict) -> bool:
    """
    Determine if the foe is alive or dead.

    :param foe: a dictionary that stores the information of the foe encountered
    :precondition: foe is a nested dictionary of 9 key-value pairs that stores the foe data
    :postcondition: correctly generate a boolean checking if the foe's HP is greater than 0 (alive) or not (dead)
    :return: True or False

    >>> is_foe_alive({'HP': 20, 'max_damage': 6, 'accuracy': 0.5, 'XP': 10})
    True
    >>> is_foe_alive({'HP': 0, 'max_damage': 20, 'accuracy': 0.7, 'XP': 60})
    False
    """
    return foe["HP"] > 0


def gain_xp(character: dict, foe: dict) -> dict:
    """
    Increase the character XP after winning a battle.

    :param character: a dictionary representing the playable character
    :param foe: a dictionary that stores the information of the foe encountered
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :precondition: foe is a dictionary storing foe attributes in 4 key value pairs
    :postcondition: must correctly adjust the character's current XP with the foe's XP amount
    :return: the updated character dictionary with the new 'Current XP' value
    """
    character['Current XP'] += foe['XP']
    return character


def is_level_up(character: dict) -> bool:
    """
    Check if the character has enough XP to level up.

    :param character: a dictionary representing the playable character
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :postcondition: must correctly check if the character has enough XP to rise to the next level
    :return: True or False

    >>> is_level_up({'name': 'Stefan', 'level': 1, 'Current HP': 100, 'Current XP': 120, 'X-coordinate': 0, \
    'Y-coordinate': 0, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'), 'max_HP': \
    (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6, 'special_attack': bash, \
    'special_attack_name': 'Bash'})
    True
    """
    return character['Current XP'] >= character['levelup_XP'][character['level'] - 1]


def level_up(character: dict) -> dict:
    """
    Raise the character level up by 1 and adjust the new current XP.

    :param character: a dictionary representing the playable character
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :postcondition: must correctly raise the character level by 1 until level 3, and calculate the new current XP
                    after leveling up
    :return: the updated character dictionary with new level and current XP
    """
    character['Current XP'] -= character['levelup_XP'][character['level'] - 1]
    character['level'] += 1
    return character


def recover_character_hp(character: dict):
    """
    Recover the character HP to the maximum of the new level when leveling up.

    :param character: a dictionary representing the playable character
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :postcondition: must correctly increase the character's current HP to the new maximum HP at a higher level
    :return: no return statement
    """
    character['Current HP'] = character['max_HP'][character['level'] - 1]


def character_regular_attack(character: dict, foe: dict, foe_type: str):
    """
    Perform regular attack to the foe by the character.

    :param character: a dictionary representing the playable character
    :param foe: a dictionary that stores the information of the foe encountered
    :param foe_type: a string representing the type of the foe
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :precondition: foe is a dictionary storing foe attributes in 4 key value pairs
    :precondition: foe_type is a string of one of the nine types of foe
    :postcondition: must correctly modify foe HP when attack hits the foe, and print corresponding message. Otherwise,
                    print a message of character's missing attack
    :return: no return statement
    """
    if attack_hit_foe(character):
        damage_to_foe = character_damage_foe(character)
        modify_foe_hp(foe, damage_to_foe)
        print(f'You caused {damage_to_foe} damage to {foe_type}')
    else:
        print("You missed the attack")


def foe_attack(foe: dict, foe_type: str, character: dict):
    """
    Perform attack on the character by the foe.

    :param foe: a dictionary that stores the information of the foe encountered
    :param foe_type: a string representing the type of the foe
    :param character: a dictionary representing the playable character
    :precondition: foe is a dictionary storing foe attributes in 4 key value pairs
    :precondition: foe_type is a string of one of the nine types of foe
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :postcondition: must correctly modify character's current HP when attack hits the character, and print the
                    corresponding message. Otherwise, print a message of foe's missing attack
    :return: no return statement
    """
    if attack_hit_character(foe):
        damage_to_character = foe_damage_character(foe)
        modify_character_hp(character, damage_to_character)
        print(f"{foe_type} caused {damage_to_character} damage to you!")
        if not is_character_alive(character):
            sys.exit('Sorry, you died. Game over:(')
    else:
        print(f"Lucky, {foe_type} missed the attack on you")


def show_character_status(character: dict):
    """
    Print a status bar showing character's current information.

    :param character: a dictionary representing the playable character
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :postcondition: must correctly print out a multi-line string showing character's attributes
    :return: no return statement
    """
    class_name = character['class name']
    level = character['level']
    occupation = character['class levels'][level - 1]
    current_hp = character['Current HP']
    max_hp = character['max_HP'][level - 1]
    current_xp = character['Current XP']
    xp_needed_to_levelup = character['levelup_XP'][level - 1]
    max_damage = character['max_damage'][level - 1]
    accuracy = character['accuracy']
    print(f'\nClass: {class_name}  Occupation: {occupation}  Current HP: {current_hp}  Max HP: {max_hp}  Current XP: '
          f'{current_xp}  Levelup XP: {xp_needed_to_levelup}  Max Damage: {max_damage}  Accuracy: {accuracy}')


def fight_foe(character: dict, foe: dict, foe_type: str):
    """
    Perform the fighting loop against a regular foe (not boss).

    :param character: a dictionary representing the playable character
    :param foe: a dictionary that stores the information of the foe encountered
    :param foe_type: a string representing the type of the foe
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :precondition: foe is a dictionary storing foe attributes in 4 key value pairs
    :precondition: foe_type is a string of one of the nine types of foe
    :postcondition: must correctly perform every part of the fighting loop based on game design
    :return: no return statement
    """
    foe_xp = foe['XP']
    character_special_attack_exists = True
    while is_character_alive(character):
        user_input = get_user_choice_runaway()
        while not valid_user_choice(user_input, 2):
            print("This is not a valid choice for run away, please choose again")
            user_input = get_user_choice_runaway()
        if user_input.strip() == '1':  # user chooses to fight
            show_character_status(character)
            if character_special_attack_exists is True:  # at the first round
                user_input = get_user_attack_type(character)
                while not valid_user_choice(user_input, 2):
                    print("This is not a valid choice for special attack, please choose again")
                    get_user_attack_type(character)
                if user_input.strip() == '1':  # user chooses special attack
                    character['special_attack'](character, foe, foe_type)
                    if not is_foe_alive(foe):
                        print(f'You have defeated {foe_type} and gained {foe_xp} XP')
                        gain_xp(character, foe)
                        break
                    foe_attack(foe, foe_type, character)
                    show_character_status(character)
                    if foe_runaway():
                        print(f"You are too powerful! {foe_type} has run away. You gained {foe_xp} XP")
                        gain_xp(character, foe)
                        break
                else:
                    character_regular_attack(character, foe, foe_type)
                    if not is_foe_alive(foe):
                        print(f'You have defeated {foe_type} and gained {foe_xp} XP')
                        gain_xp(character, foe)
                        break
                    foe_attack(foe, foe_type, character)
                    show_character_status(character)
                    if foe_runaway():
                        print(f"You are too powerful! {foe_type} has run away. You gained {foe_xp} XP")
                        gain_xp(character, foe)
                        break
                character_special_attack_exists = False
            else:
                character_regular_attack(character, foe, foe_type)
                if not is_foe_alive(foe):
                    print(f'You have defeated {foe_type} and gained {foe_xp} XP')
                    gain_xp(character, foe)
                    break
                foe_attack(foe, foe_type, character)
                show_character_status(character)
                if foe_runaway():
                    print(f"You are too powerful! {foe_type} has run away. You gained {foe_xp} XP")
                    gain_xp(character, foe)
                    break
        else:  # user chooses to flee
            if random.random() <= 0.2:
                damage_to_character = foe_damage_character(foe)
                modify_character_hp(character, damage_to_character)
                print(f"{foe_type} attacked you and caused {damage_to_character} damage while you were running away!")
                show_character_status(character)
                break
            else:
                print(f"You have successfully run away from {foe_type} without being attacked")
                break


def check_if_last_room_reached(character: dict) -> bool:
    """
    Check if the character was on the bottom right room of the game board.

    :param character: a dictionary representing the playable character
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :postcondition: must correctly check if the character has reached the bottom right-hand corner i.e. the (X, Y)
                    coordinates are (9, 9)
    :return: True or False

    >>> check_if_last_room_reached({'name': 'Stefan', 'level': 1, 'Current HP': 0, 'Current XP': 120, \
    'X-coordinate': 9, 'Y-coordinate': 8, 'class name': 'Warrior', 'class levels': ('Barbarian', 'Monk', 'Crusader'), \
    'max_HP': (100, 150, 200), 'levelup_XP': (100, 160), 'max_damage': (30, 45, 60), 'accuracy': 0.6, \
    'special_attack': bash, 'special_attack_name': 'Bash'})
    False
    """
    return (character['X-coordinate'], character['Y-coordinate']) == (9, 9)


def boss_special_attack(boss: dict, foe_type: str, character: dict):
    """
    Perform boss special attack on the character.

    :param boss: a dictionary that stores the boss's attributes
    :param foe_type: a string representing the name of the boss
    :param character: a dictionary representing the playable character
    :precondition: boss is a dictionary of 5 key value pairs containing boss's attributes
    :precondition: foe_type is a string of the boss name, Diablo
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :postcondition: must correctly modify the character's current HP and print corresponding messages, must exit the
                    game if character was killed by the boss
    :return: no return statement
    """
    damage_to_character = int(boss['max_damage'] * 1.2)
    modify_character_hp(character, damage_to_character)
    print(f'{foe_type} used special attack Thunder on you and caused more damage!')
    print(f"You received {damage_to_character} damage")
    if not is_character_alive(character):
        sys.exit('Sorry, you died. Game over:(')


def fight_boss(character: dict, boss: dict, foe_type: str):
    """
    Perform the fighting loop against the boss Diablo.

    :param character: a dictionary representing the playable character
    :param boss: a dictionary that stores the boss's attributes
    :param foe_type: a string representing the type of the foe
    :precondition: character is a dictionary of 14 key-value pairs that store all attributes of the character
    :precondition: boss is a dictionary of 5 key value pairs containing boss's attributes
    :precondition: foe_type is a string of one of the nine types of foe
    :postcondition: must correctly perform every part of the fighting loop based on game design
    :return: no return statement
    """
    character_name = character['name']
    foe = boss
    character_special_attack_right = True
    while is_character_alive(character):
        if character_special_attack_right is True:  # at the first round
            user_input = get_user_attack_type(character)
            while not valid_user_choice(user_input, 2):
                print("This is not a valid choice for special attack, please choose again")
                get_user_attack_type(character)
            if user_input.strip() == '1':  # user choose special attack
                character['special_attack'](character, foe, foe_type)
                if not is_foe_alive(boss):
                    print(f'Fantastic! You have defeated {foe_type}!')
                    print(f"Congratulations {character_name}, you've made it through the game, "
                          f"you are the savior of the world!")
                    break
                boss_special_attack(boss, foe_type, character)
            else:  # user forfeits the right to special attack
                character_regular_attack(character, foe, foe_type)
                if not is_foe_alive(boss):
                    print(f'Fantastic! You have defeated {foe_type}!')
                    print(f"Congratulations {character_name}, you've made it through the game, "
                          f"you are the savior of the world!")
                    break
                boss_special_attack(boss, foe_type, character)
            character_special_attack_right = False
        else:  # user can only use regular attack from now on
            character_regular_attack(character, foe, foe_type)
            if not is_foe_alive(foe):
                print(f'Fantastic! You have defeated {foe_type}!')
                print(f"You've made it through the game {character_name}, you are the savior of the world!")
                break
            foe_attack(foe, foe_type, character)


def ascii_congratulation():
    """
    Print a congratulation message in ASCII style when user wins the game.

    :postcondition: must correctly print an ASCII art of a congratulations message
    :return: no return statement
    """
    print(r"""
       ___                            _         _       _   _                 
      / __\___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___ 
     / /  / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
    / /__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \
    \____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                      |___/                                                   
         """)


def game():
    print('\nWelcome to the fantasy world of Diablo X, Nephalem! Start you adventure by exploring the game board.\n'
          'You can win this game by defeating the boss Diablo in the bottom right corner (9, 9) of the map, \nbut make '
          'sure to level up and challenge the boss with a healthy HP. Enjoy!')
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character_name = get_character_name()
    print(f'\nWelcome, {character_name}. Please select a class for your character:\n [1] Warrior \n [2] Sorcerer \n '
          f'[3] Amazon \n [4] Thief')
    class_number = get_character_class()  # choose your class
    while not valid_user_choice(class_number, 4):
        print('This is not a valid class choice, please try again')
        class_number = get_character_class()
    class_type = determine_class_type(class_number)
    class_attributes = extract_class_attributes(create_classes(), class_number)
    occupation = class_attributes['class levels'][0]
    print(f"Good job! You are class {class_type}, your occupation is {occupation}. Good luck on your journey!")
    character = make_character(character_name, class_attributes)
    reached_last_room = False
    show_navigation_map(rows, columns, character)
    describe_current_location(board, character)
    while not reached_last_room:
        direction = get_user_direction_choice()  # which direction should I go?
        if direction.strip().lower() == 'quit':
            sys.exit('Quit successful, the game is ended')
        while not valid_user_choice(direction, 4):
            print('This is not a valid choice, please try again')
            direction = get_user_direction_choice()
        valid_move = validate_move(character, direction)
        if valid_move:  # check that character is not off board
            move_character(character, direction)
            show_navigation_map(rows, columns, character)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()  # check for foe
            if there_is_a_challenger:
                foe_in_same_area = determine_foe_in_same_area(character)
                foe_type = determine_foe_type(foe_in_same_area)
                foe_data = create_foe()
                foe = extract_foe_attributes(foe_data, foe_type)
                print(f"You have encountered {foe_type}!")
                fight_foe(character, foe, foe_type)
                level = character['level']
                if character['level'] < 3 and is_level_up(character):  # character has enough XP to level up?
                    level_up(character)
                    occupation = class_attributes['class levels'][character['level'] - 1]
                    recover_character_hp(character)
                    new_hp = character['max_HP'][character['level'] - 1]
                    print(f'Congratulations you are now level {level + 1}! Your occupation has been upgraded to '
                          f'{occupation}! \nYour HP has fully recovered and your maximum hp value is now {new_hp}')
            reached_last_room = check_if_last_room_reached(character)
        else:
            print(f"Sorry {character_name}, you can't go in that direction")
    boss = create_boss()  # fight the boss
    print('You have met the final boss, Diablo!')
    foe_type = boss['name']
    fight_boss(character, boss, foe_type)
    ascii_congratulation()


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
