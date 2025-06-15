import random

# Define the board
def create_board():
    return [
        "Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax",
        "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue",
        "Jail", "St. Charles Place", "Electric Company", "States Avenue", "Virginia Avenue",
        "St. James Place", "Tennessee Avenue", "Community Chest", "New York Avenue", "Free Parking",
        "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue", "B&O Railroad",
        "Atlantic Avenue", "Ventnor Avenue", "Water Works", "Marvin Gardens", "Go to Jail",
        "Pacific Avenue", "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue", "Short Line Railroad",
        "Chance", "Park Place", "Luxury Tax", "Boardwalk"
    ]

# Initialize players
def initialize_players():
    return [
        {"name": "You", "money": 1500, "position": 0, "properties": []},
        {"name": "Computer 1", "money": 1500, "position": 0, "properties": []},
        {"name": "Computer 2", "money": 1500, "position": 0, "properties": []},
        {"name": "Computer 3", "money": 1500, "position": 0, "properties": []}
    ]

# Roll the dice
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

# Move a player
def move_player(player, dice_roll, board):
    player["position"] = (player["position"] + sum(dice_roll)) % len(board)
    return board[player["position"]]

# Handle property purchase
def handle_property(player, property_name, properties, property_costs):
    if property_name not in properties:
        cost = property_costs.get(property_name, 0)
        if player["money"] >= cost:
            player["money"] -= cost
            player["properties"].append(property_name)
            properties[property_name] = player["name"]
            print(f'{player["name"]} bought {property_name} for ${cost}.')
        else:
            print(f'{player["name"]} cannot afford {property_name}.')
    else:
        print(f'{property_name} is already owned by {properties[property_name]}.')

# Main game loop
def main():
    print("Welcome to Monopoly!")
    board = create_board()
    players = initialize_players()
    properties = {}  # Tracks ownership of properties
    property_costs = {  # Fixed property costs
        "Mediterranean Avenue": 60, "Baltic Avenue": 60, "Reading Railroad": 200,
        "Oriental Avenue": 100, "Vermont Avenue": 100, "Connecticut Avenue": 120,
        # Add costs for all properties...
    }
    community_chest_cards = ["Win $50", "Lose $50", "Advance to Go", "Go to Jail"]
    chance_cards = ["Win $100", "Lose $100", "Advance to Boardwalk", "Go to Jail"]
    turn = 0

    while True:
        current_player = players[turn % len(players)]
        print(f"\n--- {current_player['name']}'s Turn ---")
        print(f"Money: ${current_player['money']}")
        print(f"Properties: {', '.join(current_player['properties']) if current_player['properties'] else 'None'}")

        # Roll dice
        dice = roll_dice()
        print(f"{current_player['name']} rolled {dice[0]} and {dice[1]} (Total: {sum(dice)}).")

        # Move player
        landed_space = move_player(current_player, dice, board)
        print(f"{current_player['name']} landed on {landed_space}.")

        # Handle special spaces
        if landed_space == "Go":
            print(f"{current_player['name']} collects $200 for passing Go!")
            current_player["money"] += 200
        elif landed_space == "Income Tax":
            tax = min(200, current_player["money"] // 10)
            current_player["money"] -= tax
            print(f"{current_player['name']} paid ${tax} in Income Tax.")
        elif landed_space == "Luxury Tax":
            current_player["money"] -= 100
            print(f"{current_player['name']} paid $100 in Luxury Tax.")
        elif landed_space == "Community Chest":
            card = random.choice(community_chest_cards)
            print(f"{current_player['name']} drew a Community Chest card: {card}.")
            if card == "Win $50":
                current_player["money"] += 50
            elif card == "Lose $50":
                current_player["money"] -= 50
            elif card == "Advance to Go":
                current_player["position"] = 0
                current_player["money"] += 200
            elif card == "Go to Jail":
                current_player["position"] = board.index("Jail")
        elif landed_space == "Chance":
            card = random.choice(chance_cards)
            print(f"{current_player['name']} drew a Chance card: {card}.")
            if card == "Win $100":
                current_player["money"] += 100
            elif card == "Lose $100":
                current_player["money"] -= 100
            elif card == "Advance to Boardwalk":
                current_player["position"] = board.index("Boardwalk")
            elif card == "Go to Jail":
                current_player["position"] = board.index("Jail")
        elif landed_space == "Go to Jail":
            print(f"{current_player['name']} is sent to Jail!")
            current_player["position"] = board.index("Jail")
        elif landed_space == "Free Parking":
            print(f"{current_player['name']} is just visiting Free Parking.")
        elif landed_space == "Jail":
            print(f"{current_player['name']} is just visiting Jail.")
        else:
            # Handle property purchase
            handle_property(current_player, landed_space, properties, property_costs)

        # Check if the player is bankrupt
        if current_player["money"] <= 0:
            print(f"{current_player['name']} is bankrupt and out of the game!")
            players.remove(current_player)
            if len(players) == 1:
                print(f"{players[0]['name']} wins the game!")
                break
            turn -= 1  # Adjust turn to account for the removed player

        # Next player's turn
        turn += 1

if __name__ == "__main__":
    main()