"""
Sample code with various efficiency issues for analysis and improvement.
This file demonstrates common performance bottlenecks in Python code.
"""

import time
import random
from typing import List, Dict, Set


class DataProcessor:
    """A class demonstrating various inefficient coding patterns."""
    
    def __init__(self):
        self.data = []
        self.processed_data = []
    
    def inefficient_nested_loops(self, data: List[int]) -> List[int]:
        """
        EFFICIENCY ISSUE #1: Nested loops with O(n²) complexity
        This function finds duplicates using nested loops instead of a set.
        """
        duplicates = []
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] == data[j] and data[i] not in duplicates:
                    duplicates.append(data[i])
        return duplicates
    
    def inefficient_string_concatenation(self, words: List[str]) -> str:
        """
        EFFICIENCY ISSUE #2: String concatenation in a loop
        Creates new string objects repeatedly instead of using join().
        """
        result = ""
        for word in words:
            result = result + word + " "
        return result.strip()
    
    def inefficient_list_operations(self, numbers: List[int]) -> List[int]:
        """
        EFFICIENCY ISSUE #3: Inefficient list operations
        Uses list.remove() and list.insert(0) which are O(n) operations.
        """
        result = []
        temp_list = numbers.copy()
        
        while temp_list:
            first_element = temp_list[0]
            temp_list.remove(first_element)
            result.insert(0, first_element * 2)
        
        return result
    
    def inefficient_dictionary_lookup(self, items: List[str]) -> Dict[str, int]:
        """
        EFFICIENCY ISSUE #4: Repeated dictionary key checks
        Checks if key exists multiple times instead of using get() or setdefault().
        """
        counts = {}
        for item in items:
            if item in counts:
                if item in counts:
                    counts[item] = counts[item] + 1
            else:
                if item not in counts:
                    counts[item] = 1
        return counts
    
    def inefficient_sorting(self, data: List[int]) -> List[int]:
        """
        EFFICIENCY ISSUE #5: Bubble sort instead of built-in sort
        Implements O(n²) bubble sort instead of using Python's O(n log n) sort.
        """
        result = data.copy()
        n = len(result)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        
        return result
    
    def inefficient_set_operations(self, list1: List[int], list2: List[int]) -> List[int]:
        """
        EFFICIENCY ISSUE #6: Manual set operations instead of using set data structure
        Finds intersection using nested loops instead of set intersection.
        """
        intersection = []
        for item1 in list1:
            for item2 in list2:
                if item1 == item2 and item1 not in intersection:
                    intersection.append(item1)
        return intersection
    
    def inefficient_file_processing(self, filename: str) -> List[str]:
        """
        EFFICIENCY ISSUE #7: Reading file line by line in a loop
        Opens and closes file multiple times instead of reading once.
        """
        lines = []
        
        line_count = 0
        try:
            with open(filename, 'r') as f:
                for line in f:
                    line_count += 1
        except FileNotFoundError:
            return []
        
        try:
            with open(filename, 'r') as f:
                for i in range(line_count):
                    line = f.readline()
                    if line:
                        lines.append(line.strip())
        except FileNotFoundError:
            return []
        
        return lines
    
    def inefficient_calculation_caching(self, n: int) -> int:
        """
        EFFICIENCY ISSUE #8: Redundant calculations without memoization
        Calculates Fibonacci numbers recursively without caching.
        """
        if n <= 1:
            return n
        return self.inefficient_calculation_caching(n - 1) + self.inefficient_calculation_caching(n - 2)
    
    def inefficient_data_structure_choice(self, data: List[int], targets: List[int]) -> List[bool]:
        """
        EFFICIENCY ISSUE #9: Wrong data structure choice
        Uses list for membership testing instead of set.
        """
        lookup_list = []
        for item in data:
            if item not in lookup_list:
                lookup_list.append(item)
        
        results = []
        for target in targets:
            results.append(target in lookup_list)
        
        return results
    
    def inefficient_loop_invariant(self, matrix: List[List[int]]) -> int:
        """
        EFFICIENCY ISSUE #10: Loop invariant calculation
        Calculates the same value repeatedly inside nested loops.
        """
        total = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i < len(matrix) // 2 and j < len(matrix[i]) // 2:
                    total += matrix[i][j]
        return total


def demonstrate_inefficiencies():
    """Demonstrate the inefficient functions with sample data."""
    processor = DataProcessor()
    
    numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7, 8, 4]
    words = ["hello", "world", "this", "is", "inefficient", "code"]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print("Demonstrating inefficient algorithms...")
    
    start_time = time.time()
    duplicates = processor.inefficient_nested_loops(numbers)
    print(f"Duplicates found: {duplicates} (Time: {time.time() - start_time:.4f}s)")
    
    start_time = time.time()
    sentence = processor.inefficient_string_concatenation(words)
    print(f"Concatenated string: {sentence} (Time: {time.time() - start_time:.4f}s)")
    
    start_time = time.time()
    processed = processor.inefficient_list_operations(numbers[:5])
    print(f"Processed list: {processed} (Time: {time.time() - start_time:.4f}s)")
    
    start_time = time.time()
    counts = processor.inefficient_dictionary_lookup(words)
    print(f"Word counts: {counts} (Time: {time.time() - start_time:.4f}s)")
    
    start_time = time.time()
    sorted_nums = processor.inefficient_sorting(numbers[:8])
    print(f"Sorted numbers: {sorted_nums} (Time: {time.time() - start_time:.4f}s)")


if __name__ == "__main__":
    demonstrate_inefficiencies()
