import sys
from cpu import CPU, Cache, MemoryBus
from file_handler import load_instructions, load_memory_init

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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <instructions_file> <memory_init_file>")
        sys.exit(1)

    instructions_file = sys.argv[1]
    memory_init_file = sys.argv[2]

    main(instructions_file, memory_init_file)
