# Mens Basketball Roster --> https://goheels.com/sports/mens-basketball/roster

# Import Pandas
import pandas as pd

# Create the list of the different players (I choose to do 14 instead of at least 10)
players = ['Claude', 'Brown', 'Cadeau', 'Davis',
            'Tyson', 'Davis', 'Trimble', 'Powell',
              'Jackson', 'Washington', 'Hawkins', 'Holbrook',
                'Lubin', "Withers", 'Mayo Jr.']
list = {"Last Name": players}

data = pd.DataFrame(list)
print(data)
'''# Create the For loop
for player in players:
    print(players)'''
