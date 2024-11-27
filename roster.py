# Mens Basketball Roster --> https://goheels.com/sports/mens-basketball/roster

# Import Pandas
import pandas as pd

# Create the list of the different players (I choose to do 14 instead of at least 10)
roster = ['Claude', 'Brown', 'Cadeau', 'Davis',
            'Tyson', 'Davis', 'Trimble', 'Powell',
              'Jackson', 'Washington', 'Hawkins', 'Holbrook',
                'Lubin', "Withers", 'Mayo Jr.']
player = {"Last Name": roster,
          "First Initial": ["T.", "J.", "E.", "R.", "C.", "E.", "S.", "D.", "I.", "J.", "R.", "J.", "V.", "J.", "D."],
          "Height (inches)": [79, 82, 73, 72, 79, 75, 75, 78, 76, 82, 73, 80, 80, 81, 73],
          "Weight (pounds)": [230, 215, 180, 180, 200, 215, 195, 195, 190, 235, 175, 230, 230, 220, 175,]}

data = pd.DataFrame(player)
print(data)
'''# Create the For loop
for player in players:
    print(players)'''
