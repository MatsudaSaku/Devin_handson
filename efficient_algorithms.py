"""
Optimized versions of the inefficient algorithms.
This file demonstrates the improved implementations.
"""

import time
from typing import List, Dict, Set
from collections import deque, Counter


class EfficientDataProcessor:
    """A class demonstrating optimized coding patterns."""
    
    def __init__(self):
        self.data = []
        self.processed_data = []
    
    def efficient_duplicate_detection(self, data: List[int]) -> List[int]:
        """
        OPTIMIZED VERSION: O(n) duplicate detection using set
        Uses a set to track seen elements for O(1) lookup time.
        """
        seen = set()
        duplicates = set()
        
        for item in data:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        
        return list(duplicates)
    
    def efficient_string_concatenation(self, words: List[str]) -> str:
        """
        OPTIMIZED VERSION: String join instead of concatenation
        Uses str.join() which is O(n) instead of O(n²).
        """
        return " ".join(words)
    
    def efficient_list_operations(self, numbers: List[int]) -> List[int]:
        """
        OPTIMIZED VERSION: Using deque for efficient operations
        Uses deque for O(1) operations at both ends.
        """
        temp_deque = deque(numbers)
        result = deque()
        
        while temp_deque:
            first_element = temp_deque.popleft()
            result.appendleft(first_element * 2)
        
        return list(result)
    
    def efficient_dictionary_lookup(self, items: List[str]) -> Dict[str, int]:
        """
        OPTIMIZED VERSION: Using Counter for efficient counting
        Uses Counter which handles the counting logic efficiently.
        """
        return dict(Counter(items))
    
    def efficient_sorting(self, data: List[int]) -> List[int]:
        """
        OPTIMIZED VERSION: Built-in sort
        Uses Python's built-in sort which is O(n log n).
        """
        return sorted(data)
    
    def efficient_set_operations(self, list1: List[int], list2: List[int]) -> List[int]:
        """
        OPTIMIZED VERSION: Set intersection
        Uses set intersection for O(n) complexity.
        """
        return list(set(list1) & set(list2))
    
    def efficient_file_processing(self, filename: str) -> List[str]:
        """
        OPTIMIZED VERSION: Single file read
        Reads file once and processes all lines.
        """
        try:
            with open(filename, 'r') as f:
                return [line.strip() for line in f]
        except FileNotFoundError:
            return []
    
    def efficient_calculation_caching(self, n: int, memo: Dict[int, int] = None) -> int:
        """
        OPTIMIZED VERSION: Fibonacci with memoization
        Uses memoization to avoid redundant calculations.
        """
        if memo is None:
            memo = {}
        
        if n in memo:
            return memo[n]
        
        if n <= 1:
            result = n
        else:
            result = self.efficient_calculation_caching(n - 1, memo) + self.efficient_calculation_caching(n - 2, memo)
        
        memo[n] = result
        return result
    
    def efficient_data_structure_choice(self, data: List[int], targets: List[int]) -> List[bool]:
        """
        OPTIMIZED VERSION: Set for membership testing
        Uses set for O(1) membership testing.
        """
        lookup_set = set(data)
        return [target in lookup_set for target in targets]
    
    def efficient_loop_invariant(self, matrix: List[List[int]]) -> int:
        """
        OPTIMIZED VERSION: Extract loop invariants
        Calculates invariants outside the loops.
        """
        total = 0
        matrix_half = len(matrix) // 2
        
        for i in range(min(matrix_half, len(matrix))):
            row_half = len(matrix[i]) // 2
            for j in range(min(row_half, len(matrix[i]))):
                total += matrix[i][j]
        
        return total


def compare_performance():
    """Compare performance between inefficient and efficient implementations."""
    from inefficient_algorithms import DataProcessor
    
    inefficient = DataProcessor()
    efficient = EfficientDataProcessor()
    
    test_data = list(range(1000)) + list(range(500))
    
    print("Performance Comparison:")
    print("=" * 50)
    
    start_time = time.time()
    inefficient_result = inefficient.inefficient_nested_loops(test_data)
    inefficient_time = time.time() - start_time
    
    start_time = time.time()
    efficient_result = efficient.efficient_duplicate_detection(test_data)
    efficient_time = time.time() - start_time
    
    print(f"Duplicate Detection:")
    print(f"  Inefficient: {inefficient_time:.6f}s")
    print(f"  Efficient:   {efficient_time:.6f}s")
    print(f"  Speedup:     {inefficient_time / efficient_time:.2f}x")
    print(f"  Results match: {set(inefficient_result) == set(efficient_result)}")
    
    words = ["test"] * 1000
    
    start_time = time.time()
    inefficient.inefficient_string_concatenation(words)
    inefficient_time = time.time() - start_time
    
    start_time = time.time()
    efficient.efficient_string_concatenation(words)
    efficient_time = time.time() - start_time
    
    print(f"\nString Concatenation:")
    print(f"  Inefficient: {inefficient_time:.6f}s")
    print(f"  Efficient:   {efficient_time:.6f}s")
    print(f"  Speedup:     {inefficient_time / efficient_time:.2f}x")


if __name__ == "__main__":
    compare_performance()
