"""
Additional examples of memory-inefficient code patterns.
"""

import sys
from typing import List, Generator


class MemoryInefficient:
    """Examples of memory-inefficient patterns."""
    
    def load_all_data_at_once(self, size: int) -> List[int]:
        """
        EFFICIENCY ISSUE #11: Loading large datasets into memory unnecessarily
        Creates large lists when generators or streaming would be more appropriate.
        """
        large_list = []
        for i in range(size):
            large_list.append(i * i)
        
        processed = []
        for item in large_list:
            if item % 2 == 0:
                processed.append(item)
        
        return processed
    
    def inefficient_list_comprehension(self, data: List[int]) -> List[int]:
        """
        EFFICIENCY ISSUE #12: Nested list comprehensions creating intermediate lists
        Creates unnecessary intermediate data structures.
        """
        squared = [x * x for x in data]
        filtered = [x for x in squared if x > 10]
        doubled = [x * 2 for x in filtered]
        final = [x for x in doubled if x < 1000]
        
        return final
    
    def memory_leak_simulation(self, iterations: int) -> None:
        """
        EFFICIENCY ISSUE #13: Potential memory leaks
        Accumulates data without proper cleanup.
        """
        self.accumulated_data = []
        
        for i in range(iterations):
            large_chunk = [j for j in range(1000)]
            self.accumulated_data.append(large_chunk)
            
            if len(self.accumulated_data) > 100:
                pass
    
    def inefficient_string_operations(self, text: str) -> str:
        """
        EFFICIENCY ISSUE #14: Inefficient string operations
        Multiple string operations creating temporary objects.
        """
        result = text
        
        result = result.replace(" ", "_")
        result = result.upper()
        result = result.replace("_", "-")
        result = result.lower()
        result = result.replace("-", " ")
        result = result.title()
        
        return result
    
    def better_generator_example(self, size: int) -> Generator[int, None, None]:
        """
        This is how the load_all_data_at_once should be implemented.
        Using generators for memory efficiency.
        """
        for i in range(size):
            square = i * i
            if square % 2 == 0:
                yield square


def demonstrate_memory_issues():
    """Demonstrate memory-inefficient patterns."""
    mem_inefficient = MemoryInefficient()
    
    print("Memory usage before operations:", sys.getsizeof([]))
    
    result = mem_inefficient.load_all_data_at_once(10000)
    print(f"Loaded {len(result)} items inefficiently")
    
    sample_data = list(range(100))
    processed = mem_inefficient.inefficient_list_comprehension(sample_data)
    print(f"Processed {len(processed)} items with intermediate lists")
    
    text = "this is a sample text for processing"
    processed_text = mem_inefficient.inefficient_string_operations(text)
    print(f"Processed text: {processed_text}")


if __name__ == "__main__":
    demonstrate_memory_issues()
