def load_instructions(file_path):
    with open(file_path, 'r') as file:
        instructions = file.readlines()
    return [instruction.strip() for instruction in instructions]

def load_memory_init(file_path):
    memory_values = {}
    with open(file_path, 'r') as file:
        for line in file:
            address, value = map(int, line.strip().split())
            memory_values[address] = value
    return memory_values
