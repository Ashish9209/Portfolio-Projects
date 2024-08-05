Certainly! This code provides a command-line tool for finding the shortest metro route between landmarks in Vancouver using graph search algorithms. Here’s a breakdown of each component:

### Imports

```python
from graph_search import bfs, dfs
from SkyRocket.Code.vc_metro import vc_metro
from SkyRocket.Code.vc_landmarks import vc_landmarks
from SkyRocket.Code.landmark_choices import landmark_choices
```

- **`bfs`, `dfs`**: Functions for Breadth-First Search (BFS) and Depth-First Search (DFS) from the `graph_search` module.
- **`vc_metro`**: A dictionary representing the metro system of Vancouver, presumably where keys are station names and values are sets of neighboring stations.
- **`vc_landmarks`**: A dictionary mapping landmarks to sets of metro stations.
- **`landmark_choices`**: A dictionary mapping letters to landmark names.

### Global Variables

```python
landmark_string = ''
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)
stations_under_construction = ['Richmond-Brighouse']
```

- **`landmark_string`**: A formatted string listing all landmarks and their corresponding letters.
- **`stations_under_construction`**: A list of stations currently under construction.

### Functions

1. **`greet()`**:
   ```python
   def greet():
     print('hi there and welcome to SkyRoute!\nWe\'ll help you find the shortest route between the following Vancouver landmarks:\n {}'.format(landmark_string))
   ```
   - Prints a welcome message and lists available landmarks.

2. **`skyroute()`**:
   ```python
   def skyroute():
     greet()
     new_route()
     goodbye()
   ```
   - Calls `greet()`, `new_route()`, and `goodbye()` functions in sequence.

3. **`set_start_and_end(start_point, end_point)`**:
   ```python
   def set_start_and_end(start_point, end_point):
     if start_point:
       change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both':")
       if change_point == 'b':
         start_point = get_start()
         end_point = get_end()
       elif change_point == 'o':
         start_point = get_start()
       elif change_point == 'd':
         end_point = get_end()
       else:
         print("Oops, that isn't 'o', 'd', or 'b'...")
         set_start_and_end(start_point, end_point)
     else:
       start_point = get_start()
       end_point = get_end()
     return start_point, end_point
   ```
   - Asks the user if they want to change the origin, destination, or both, and updates the `start_point` and `end_point` accordingly.

4. **`get_start()`**:
   ```python
   def get_start():
     start_point_letter = input('Where are you coming from? Type in the corresponding letter: ')
     if start_point_letter in landmark_choices:
       start_point = landmark_choices[start_point_letter]
     else:
       print("Sorry, that's not a landmark we have data on. Let's try this again...")
       get_start()
     return start_point
   ```
   - Prompts the user for the starting point of their journey, verifying that the input is a valid landmark letter.

5. **`get_end()`**:
   ```python
   def get_end():
     end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
     if end_point_letter in landmark_choices:
       end_point = landmark_choices[end_point_letter]
     else:
       print("Ok, where are you headed? Type in the corresponding letter: ")
       get_end()
     return end_point
   ```
   - Prompts the user for the destination of their journey, ensuring it is a valid landmark.

6. **`new_route(start_point=None, end_point=None)`**:
   ```python
   def new_route(start_point=None, end_point=None):
     start_point, end_point = set_start_and_end(start_point, end_point)
     shortest_route = get_route(start_point, end_point)
     if shortest_route:
       shortest_route_string = '\n'.join(shortest_route)
       print('The shortest metro route from {} to {} is:\n{}'.format(start_point, end_point, shortest_route_string))
     else:
       print('Unfortunately, there is currently no path between {0} and {1} due to maintenance'.format(start_point, end_point))
     again = input('Would you like to see another route? Enter y/n: ')
     if again == 'y':
       show_landmarks()
       new_route(start_point, end_point)
   ```
   - Finds and prints the shortest route between the start and end points. Asks the user if they want to find another route.

7. **`show_landmarks()`**:
   ```python
   def show_landmarks():
     see_landmarks = input('Would you like to see the list of landmarks again? Enter y/n: ')
     if see_landmarks == 'y':
       print(landmark_string)
   ```
   - Provides the user with an option to see the list of landmarks again.

8. **`goodbye()`**:
   ```python
   def goodbye():
     print('Thanks for using SkyRoute developed by Akshar!')
   ```
   - Prints a thank-you message when the program ends.

9. **`get_active_stations()`**:
   ```python
   def get_active_stations():
     updated_metro = vc_metro
     for station_under_construction in stations_under_construction:
       for current_station, neighboring_stations in vc_metro.items():
         if current_station != station_under_construction:
           updated_metro[current_station] -= set(stations_under_construction)
         else:
           updated_metro[current_station] = set([])
     return updated_metro
   ```
   - Updates the metro system to reflect stations under construction, removing connections to these stations.

10. **`get_route(start_point, end_point)`**:
    ```python
    def get_route(start_point, end_point):
      start_stations = vc_landmarks[start_point]
      end_stations = vc_landmarks[end_point]
      routes = []
      for start_station in start_stations:
        for end_station in end_stations:
          metro_system = get_active_stations() if stations_under_construction else vc_metro
          if stations_under_construction:
            possible_route = dfs(metro_system, start_station, end_station)
            if not possible_route:
              return None
          route = bfs(metro_system, start_station, end_station)
          if route:
            routes.append(route)
      shortest_route = min(routes, key=len)
      return shortest_route
    ```
    - Computes the shortest route between the start and end points using BFS or DFS. Takes into account stations under construction by calling `get_active_stations()`.

### Execution

```python
skyroute()
```

- Starts the program, which will:
  - Greet the user.
  - Allow the user to find routes.
  - Provide options to view landmarks or search for another route.
  - Print a goodbye message when finished.

### Summary

This code creates an interactive tool for finding the shortest metro routes in Vancouver based on user input. It utilizes graph search algorithms (BFS, DFS) to compute routes and handles cases where stations are under construction. The user is guided through a series of prompts to select starting and ending landmarks, and the program displays the shortest path between them.