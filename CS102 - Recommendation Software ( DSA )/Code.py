def initialize_data():
    """Initialize movie data."""
    return {
        'action': ['Mission Impossible', 'John Wick', 'Fast and Furious', 'The Dark Knight', 'Top Gun: Maverick', 'Logan'],
        'comedy': ['The Scary Movie', 'Road Trip', 'Paul', 'Kung fu panda', 'Bad Boys', 'Deadpool'],
        'drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather', 'Fight Club'],
        'horror': ['The Shining', 'IT', 'Paranormal Activity', 'The Conjuring', 'The Exorcist'],
        'sci-fi': ['Blade Runner 2049', 'Inception', 'Interstellar', 'The Matrix']
    }

def display_categories(data):
    """Display available categories to the user."""
    print("Available categories:")
    for category in data.keys():
        print(f"- {category}")

def get_category_suggestion(user_input, data):
    """Suggest a category based on user input."""
    suggested_categories = [cat for cat in data if user_input.lower() in cat]
    return suggested_categories

def main():
    data = initialize_data()
    
    while True:
        display_categories(data)
        user_input = input("Enter a letter or word to find a category (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        suggested_categories = get_category_suggestion(user_input, data)
        
        if not suggested_categories:
            print("No categories found. Please try again.")
        else:
            print("Suggested categories:")
            for cat in suggested_categories:
                print(f"- {cat}")
            
            for cat in suggested_categories:
                print(f"\nRecommendations for {cat}:")
                for movie in data[cat]:
                    print(f"- {movie}")

if __name__ == "__main__":
    main()
