import csv
from dataclasses import field
import Instance_Functions

index = 0

#Creates the logins.csv file as a dictionary readable file and creates the fields 'Username' and 'Password'
if __name__ == '__main__':
    with open('logins.csv', 'w') as login_csv:
        fieldnames = ['username', 'password']

        csv_writer = csv.DictWriter(login_csv, fieldnames=fieldnames)

        csv_writer.writeheader()

        login_csv.close()

#Creates the players.csv as a dictionary readable file and creates the fields for the file as the different attributes of the Player class
    with open('players.csv', 'w') as players_csv:
        player_fieldnames =  ['username','avatar', 'streak','score','languages']
        csv_writer_players = csv.DictWriter(players_csv, fieldnames=player_fieldnames)
        csv_writer_players.writeheader()
        players_csv.close()

'''
This opens the logins.csv again. It:
    - calls the add_to_logins() function to get user input to create the dictionary entry for their username and password 
        -this returns that dictionary input to use in the next function
    - calls the players_iterator() function that uses the returned dictionary to log into duolingo, return the player info, and append it to the player list
'''
def make_login():
    with open('logins.csv', 'a', newline='') as login_csv:
        fieldnames = ['username', 'password']
        csv_writer = csv.DictWriter(login_csv, fieldnames=fieldnames)
        temp_value = Instance_Functions.add_to_logins()
        x = temp_value['username']
        y = temp_value['password']
        print(x,y, "We got it")
        test_dict = {'username': x, 'password': y}
        csv_writer.writerow(test_dict)
        Instance_Functions.players_iterator(temp_value)
        print('Done')
        login_csv.close()
        return [x,y]

def make_player(func):
    x = func[0]
    y = func[1]
    with open('players.csv', 'a', newline='') as players_csv:
        player_fieldnames =  ['username','avatar', 'streak','score','languages']
        csv_writer_players = csv.DictWriter(players_csv, fieldnames=player_fieldnames)
        csv_writer_players.writerow(Instance_Functions.player_gen_csv(x,y))
        players_csv.close()
