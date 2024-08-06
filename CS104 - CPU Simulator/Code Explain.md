Break down the `Code.py` script, which simulates the workings of a CPU using Python. This script ties together the components of the CPU simulation project: the CPU, cache, memory bus, and file handling.

### Explanation of the Code

#### Imports

```python
import sys
from cpu import CPU, Cache, MemoryBus
from file_handler import load_instructions, load_memory_init
```

- **`import sys`**: Imports the `sys` module, which provides access to command-line arguments.
- **`from cpu import CPU, Cache, MemoryBus`**: Imports the `CPU`, `Cache`, and `MemoryBus` classes from the `cpu` module. These classes define the simulation components.
- **`from file_handler import load_instructions, load_memory_init`**: Imports the `load_instructions` and `load_memory_init` functions from the `file_handler` module. These functions handle reading from input files.

#### Main Function

```python
def main(instructions_file, memory_init_file):
    # Initialize Cache and Memory Bus
    cache = Cache()
    memory_bus = MemoryBus()

    # Load data
    memory_init_values = load_memory_init(memory_init_file)
    instructions = load_instructions(instructions_file)

    # Initialize Memory Bus with values
    memory_bus.initialize(memory_init_values)

    # Create CPU instance
    cpu = CPU(cache, memory_bus)

    # Process instructions
    for instruction in instructions:
        cpu.fetch_instruction(instruction)
```

- **`def main(instructions_file, memory_init_file):`**: Defines the `main` function that takes two parameters: `instructions_file` and `memory_init_file`, which are paths to the input files.
  
  - **`cache = Cache()`**: Creates an instance of the `Cache` class.
  - **`memory_bus = MemoryBus()`**: Creates an instance of the `MemoryBus` class.

  - **`memory_init_values = load_memory_init(memory_init_file)`**: Loads initial memory values from the specified file using the `load_memory_init` function.
  - **`instructions = load_instructions(instructions_file)`**: Loads instructions from the specified file using the `load_instructions` function.

  - **`memory_bus.initialize(memory_init_values)`**: Initializes the memory bus with the values loaded from the file.
  
  - **`cpu = CPU(cache, memory_bus)`**: Creates an instance of the `CPU` class, passing the cache and memory bus as parameters.
  
  - **`for instruction in instructions:`**: Iterates through each instruction in the instructions list.
    - **`cpu.fetch_instruction(instruction)`**: Processes each instruction using the `fetch_instruction` method of the `CPU` class.

#### Command-Line Argument Handling

```python
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <instructions_file> <memory_init_file>")
        sys.exit(1)

    instructions_file = sys.argv[1]
    memory_init_file = sys.argv[2]

    main(instructions_file, memory_init_file)
```

- **`if __name__ == "__main__":`**: Ensures that the script runs only when executed directly, not when imported as a module.
  
  - **`if len(sys.argv) != 3:`**: Checks if exactly two command-line arguments (besides the script name) are provided.
    - **`print("Usage: python main.py <instructions_file> <memory_init_file>")`**: Prints the correct usage of the script.
    - **`sys.exit(1)`**: Exits the program with a non-zero status code indicating an error.

  - **`instructions_file = sys.argv[1]`**: Retrieves the first command-line argument as the path to the instructions file.
  - **`memory_init_file = sys.argv[2]`**: Retrieves the second command-line argument as the path to the memory initialization file.

  - **`main(instructions_file, memory_init_file)`**: Calls the `main` function with the provided file paths.

### Summary

- **Imports**: Necessary modules and classes for the simulation.
- **`main` Function**:
  - Initializes the cache and memory bus.
  - Loads data from input files.
  - Initializes and uses the CPU to process instructions.
- **Command-Line Argument Handling**: Ensures proper execution and provides usage instructions if incorrect arguments are supplied.


