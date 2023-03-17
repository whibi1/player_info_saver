print("Player Information Saving Code")

info = [] # Creating an empty list to store informations.

name =  input("player's Name:") # Getting the Player's Name Information from the User.

surname = input("player's Surname:") # Getting the Player's Surname Information from the User.

team = input("player's Team:") # Getting the Player's Team Information from the User.

info = [name,surname,team] # We transfer the information we receive from the user to the list


print("Saving the informations...\n")

print("Player Name: {}\nPlayer Surname: {}\nTeam: {}\n".format(info[0],info[1],info[2]))


print("İnformations saved...")
