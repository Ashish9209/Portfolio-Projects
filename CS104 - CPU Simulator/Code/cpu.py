class CPU:
    def __init__(self, cache, memory_bus):
        self.cache = cache
        self.memory_bus = memory_bus

    def fetch_instruction(self, instruction):
        print(f"Fetching instruction: {instruction}")
        # Process the instruction (this is a simplified version)
        if instruction.startswith("LOAD"):
            _, address = instruction.split()
            value = self.memory_bus.read(int(address))
            self.cache.write(int(address), value)
        elif instruction.startswith("ADD"):
            _, address1, address2 = instruction.split()
            value1 = self.cache.read(int(address1))
            value2 = self.cache.read(int(address2))
            result = value1 + value2
            print(f"ADD result: {result}")
        else:
            print(f"Unknown instruction: {instruction}")

class Cache:
    def __init__(self):
        self.data = {}

    def read(self, address):
        return self.data.get(address, 0)

    def write(self, address, value):
        self.data[address] = value

class MemoryBus:
    def __init__(self):
        self.memory = {}

    def initialize(self, values):
        self.memory = values

    def read(self, address):
        return self.memory.get(address, 0)
