# a simple ideas on how to make the script work

# // The Input Function //
# Asks for
# Date = Have the Date Automatically Tracked - (figure it out)


# // Game Number //

games = []
game = input('\nGame Number: ')
games.append(game)

# // Hero Picked //

heroes = []
hero = input('\nHero Played: ')
heroes.append(hero)

# Information About What to Improve // 3 Ideas //

information_short = []
information_long = []
information = {'short': information_short, 'long': information_long}

# Needs to run 3 Times


for idea in range(3):
    main_idea_prompt = f'\nMain Idea {idea + 1:02}: '  # Using f-string for formatting
    short = input(main_idea_prompt)
    information_short.append(short)

    description_prompt = f'\nDescription {idea + 1:02}: '
    long = input(description_prompt)
    information_long.append(long)


# // Store the Input Function //
# Make a Data Base


# Call Function // Data Base // For Information


# // Call Certain Hero //
# Receive Information on the tips written on that specific Hero.


# // Testing The Results Only //
print(f'Game Numbers = {games}.')
print(f'Heroes Picked = {heroes}')
print(f'Info To Improve = {information}')

print('\n\n\n')
print(f'short list: {information_short}.')
print(f'long list: {information_long}.')


