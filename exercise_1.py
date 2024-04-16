# 1. Manchester United FC has hired you as a developer. Develop a program that helps the coach identify their fastest player, player with the most goals, assists, passing accuracy, and defensive involvements.
# The system should also allow comparison between two players. Use the following player profiles:

# Bruno Fernandes: 5 goals, 6 points in speed, 9 points in assists, 10 points in passing accuracy, 3 defensive involvements. Corresponds to jersey number 8.
# Rasmus Hojlund: 12 goals, 8 points in speed, 2 points in assists, 6 points in passing accuracy, 2 defensive involvements. Corresponds to jersey number 11.
# Harry Maguire: 1 goal, 5 points in speed, 1 point in assists, 7 points in passing accuracy, 9 defensive involvements. Corresponds to jersey number 5.
# Alejandro Garnacho: 8 goals, 7 points in speed, 8 points in assists, 6 points in passing accuracy, 0 defensive involvements. Corresponds to jersey number 17.
# Mason Mount: 2 goals, 6 points in speed, 4 points in assists, 8 points in passing accuracy, 1 defensive involvement. Corresponds to jersey number 7.
# The program functions as follows: The coach accesses the system and encounters a menu with the following options:

# Player Review: By entering the player's jersey number, they can access the player's characteristics.
# Compare two players: The system prompts for two jersey numbers and displays the data of both players on screen.
# Identify the fastest player: Displays the player with the most points in speed.
# Identify the top goal scorer: Displays the player with the most points in goals.
# Identify the player with the most assists: Displays the player with the most points in assists.
# Identify the player with the highest passing accuracy: Displays the player with the most points in passing accuracy.
# Identify the player with the most defensive involvements: Displays the player with the most points in defensive involvements.
# The system should also allow returning to the main menu.

manchester_united_players = {
    8: {"name": "Bruno Fernandes", "goals": 5, "speed": 6, "assists": 9, "passing_accuracy": 10, "defensive_involvements": 3},
    11: {"name": "Rasmus Hojlund", "goals": 12, "speed": 8, "assists": 2, "passing_accuracy": 6, "defensive_involvements": 2},
    5: {"name": "Harry Maguire", "goals": 1, "speed": 5, "assists": 1, "passing_accuracy": 7, "defensive_involvements": 9},
    17: {"name": "Alejandro Garnacho", "goals": 8, "speed": 7, "assists": 8, "passing_accuracy": 6, "defensive_involvements": 0},
    7: {"name": "Mason Mount", "goals": 2, "speed": 6, "assists": 4, "passing_accuracy": 8, "defensive_involvements": 1}
}

def display_player_info(player):
    print(f"Player: {player['name']}")
    print(f"Goals: {player['goals']}")
    print(f"Speed: {player['speed']}")
    print(f"Assists: {player['assists']}")
    print(f"Passing Accuracy: {player['passing_accuracy']}")
    print(f"Defensive Involvements: {player['defensive_involvements']}")

def player_review(players):
    jersey_number = int(input("Enter the player's jersey number: "))

    player = players.get(jersey_number)
    if player:
        display_player_info(player)
    else:
        print("Player not found.")

def compare_players(players):
    jersey_number1 = int(input("Enter the first player's jersey number: "))
    jersey_number2 = int(input("Enter the second player's jersey number: "))

    if jersey_number1 == jersey_number2:
        print("Players should be different.")
        return
    
    player1 = players.get(jersey_number1)
    player2 = players.get(jersey_number2)

    if player1 and player2:
        display_player_info(player1)
        print("-" * 30)
        display_player_info(player2)
    else:
        print("Player not found.")

def display_menu():
    print("1. Player Review")
    print("2. Compare two players")
    print("3. Identify the fastest player")
    print("4. Identify the top goal scorer")
    print("5. Identify the player with the most assists")
    print("6. Identify the player with the highest passing accuracy")
    print("7. Identify the player with the most defensive involvements")
    print("8. Exit")


def display_max_value(players, key):
    max_player= max(players, key=lambda x: players[x][key])
    print(f"Player with the most {key}: {players[max_player]['name']}")
    print(f"{key.capitalize()}: {players[max_player][key]}")
    

def main():
    while True:
        try:
            display_menu()
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                player_review(manchester_united_players)
            elif choice == 2:
                compare_players(manchester_united_players)
            elif 3 <= choice <= 7:
                stat_options = ['speed', 'goals', 'assists', 'passing_accuracy', 'defensive_involvements']
                display_max_value(manchester_united_players, stat_options[choice - 3])
            elif choice == 8:
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid integer choice.")

if __name__ == "__main__":
    main()