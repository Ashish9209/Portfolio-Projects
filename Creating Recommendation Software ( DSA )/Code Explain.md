Break down the provided Python code for a movie recommendation program.

### Code Breakdown

1. **`initialize_data()` Function**
   ```python
   def initialize_data():
       """Initialize movie data."""
       return {
           'action': ['Mission Impossible', 'John Wick', 'Fast and Furious', 'The Dark Knight', 'Top Gun: Maverick', 'Logan'],
           'comedy': ['The Scary Movie', 'Road Trip', 'Paul', 'Kung fu panda', 'Bad Boys', 'Deadpool'],
           'drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather', 'Fight Club'],
           'horror': ['The Shining', 'IT', 'Paranormal Activity', 'The Conjuring', 'The Exorcist'],
           'sci-fi': ['Blade Runner 2049', 'Inception', 'Interstellar', 'The Matrix']
       }
   ```
   - **Purpose**: Initializes and returns a dictionary containing movie categories and their corresponding movie lists.
   - **Details**: 
     - The dictionary keys represent movie categories (e.g., 'action', 'comedy').
     - The values are lists of movie titles associated with each category.

2. **`display_categories(data)` Function**
   ```python
   def display_categories(data):
       """Display available categories to the user."""
       print("Available categories:")
       for category in data.keys():
           print(f"- {category}")
   ```
   - **Purpose**: Prints out all available movie categories.
   - **Details**:
     - Iterates over the keys of the `data` dictionary.
     - Prints each category in a list format.

3. **`get_category_suggestion(user_input, data)` Function**
   ```python
   def get_category_suggestion(user_input, data):
       """Suggest a category based on user input."""
       suggested_categories = [cat for cat in data if user_input.lower() in cat]
       return suggested_categories
   ```
   - **Purpose**: Suggests categories that match the user's input.
   - **Details**:
     - Uses a list comprehension to find categories where the `user_input` (converted to lowercase) is a substring of the category name.
     - Returns a list of matching categories.

4. **`main()` Function**
   ```python
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
   ```
   - **Purpose**: Manages the main interaction loop of the program.
   - **Details**:
     - Calls `initialize_data()` to load the movie data into the `data` variable.
     - Enters a `while` loop that runs continuously until the user decides to exit.
     - Calls `display_categories(data)` to show available categories.
     - Prompts the user for input and processes it:
       - If the input is `'exit'`, the program prints a farewell message and breaks the loop.
       - Calls `get_category_suggestion(user_input, data)` to find matching categories.
       - If no categories are found, prompts the user to try again.
       - If categories are found, prints the suggested categories and their corresponding movie recommendations.

5. **`if __name__ == "__main__":` Block**
   ```python
   if __name__ == "__main__":
       main()
   ```
   - **Purpose**: Ensures that the `main()` function is executed only when the script is run directly, not when imported as a module.
   - **Details**:
     - Calls the `main()` function if the script is executed as the main program.

