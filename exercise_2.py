# 2. A travel agency has a special offer for traveling in any season of 2024. Their destinations are:

# Winter: Andorra and Switzerland. In Andorra, there are skiing activities, and in Switzerland, there's a tour of the Swiss Alps.
# Summer: Spain and Portugal. In Spain, there are hiking and extreme sports activities. In Portugal, there are activities on the beaches.
# Spring: France and Italy. In France, there are extreme sports activities, and in Italy, there's a cultural and historical tour.
# Autumn: Belgium and Austria. In Belgium, there are hiking and extreme sports activities, and in Austria, there are cultural and historical activities.
# Note: Traveling in winter costs $100, in autumn $200, in spring $300, and in summer $400.

# Design a system that helps users choose their best destination according to their personal preferences and the season they want to travel in.
# 12. Important: With the information you have, you should ask the user the right questions and display on screen what their best destination would be.

# Clue: You could consider the user's budget

season_destinations = {
    "Winter": {
        "Andorra": {"activities": ["skiing"], "cost": 100},
        "Switzerland": {"activities": ["tour of the Swiss Alps"], "cost": 100}
    },
    "Summer": {
        "Spain": {"activities": ["hiking", "extreme sports"], "cost": 400},
        "Portugal": {"activities": ["beach activities"], "cost": 400}
    },
    "Spring": {
        "France": {"activities": ["extreme sports"], "cost": 300},
        "Italy": {"activities": ["cultural and historical tour"], "cost": 300}
    },
    "Autumn": {
        "Belgium": {"activities": ["hiking", "extreme sports"], "cost": 200},
        "Austria": {"activities": ["cultural and historical activities"], "cost": 200}
    }
}

def filter_destinations(preferred_season, preferred_activities, budget):
    filtered_destinations = {}
    for destination, info in season_destinations[preferred_season].items():
        if all(activity in info["activities"] for activity in preferred_activities) and info["cost"] <= budget:
            filtered_destinations[destination] = info
    return filtered_destinations

def display_recommendations(recommendations):
    if recommendations:
        print("Based on your preferences and budget, we recommend the following destinations:")
        for destination, info in recommendations.items():
            print(f"Destination: {destination}")
            print(f"Activities: {', '.join(info['activities'])}")
            print(f"Cost: ${info['cost']}")
            print()
    else:
        print("Sorry, we couldn't find any destinations matching your preferences and budget.")

def main():
    print("Welcome to the Travel Destination Recommender!")
    print("Please answer the following questions to help us recommend the best destination for you:")
    while True:
        try:
            print("Which season would you like to travel in?")
            for i, season in enumerate(season_destinations.keys(), start=1):
                print(f"{i}. {season}")
            choice = int(input("Enter the number corresponding to the season you would like to travel in: "))
            seasons = list(season_destinations.keys())

            if choice < 1 or choice > len(seasons):
                raise ValueError("Invalid choice. Please enter a number corresponding to the displayed seasons.")
            
            preferred_season = seasons[choice - 1]
            
            if preferred_season not in season_destinations:
                raise ValueError("Invalid season. Please enter Winter, Spring, Summer, or Autumn.")
            
            preferred_activities = input("What activities are you interested in? (e.g., hiking, beach activities, skiing) ").split(", ")
            
            budget = int(input("What is your budget for the trip? $"))
            if budget < 0:
                raise ValueError("Invalid budget. Please enter a positive number.")
            
            recommendations = filter_destinations(preferred_season, preferred_activities, budget)
            display_recommendations(recommendations)
            break 
        except ValueError as ve:
            print(ve)

if __name__ == "__main__":
    main()
