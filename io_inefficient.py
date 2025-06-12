"""
Examples of I/O inefficient code patterns.
"""

import json
import os
import time
from typing import List, Dict


class IOInefficient:
    """Examples of I/O inefficient patterns."""
    
    def inefficient_file_writing(self, data: List[str], filename: str) -> None:
        """
        EFFICIENCY ISSUE #15: Opening and closing files repeatedly
        Opens file for each write operation instead of batching.
        """
        for item in data:
            with open(filename, 'a') as f:
                f.write(item + '\n')
                f.flush()
    
    def inefficient_json_processing(self, json_files: List[str]) -> Dict:
        """
        EFFICIENCY ISSUE #16: Processing files one by one instead of batching
        Reads and processes JSON files individually.
        """
        all_data = {}
        
        for filename in json_files:
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                
                for key, value in data.items():
                    if key in all_data:
                        all_data[key].append(value)
                    else:
                        all_data[key] = [value]
                
                temp_file = f"temp_{filename}.json"
                with open(temp_file, 'w') as f:
                    json.dump(all_data, f)
                
            except FileNotFoundError:
                continue
        
        return all_data
    
    def inefficient_database_simulation(self, records: List[Dict]) -> None:
        """
        EFFICIENCY ISSUE #17: Individual database operations instead of batch
        Simulates individual database inserts instead of batch operations.
        """
        db_file = "simulated_db.txt"
        
        for record in records:
            time.sleep(0.001)
            
            with open(db_file, 'a') as f:
                f.write(f"{record['id']},{record['name']},{record['value']}\n")
            
            time.sleep(0.001)
    
    def inefficient_log_processing(self, log_file: str) -> Dict[str, int]:
        """
        EFFICIENCY ISSUE #18: Reading file multiple times
        Reads the same file multiple times for different analyses.
        """
        error_count = 0
        warning_count = 0
        info_count = 0
        
        try:
            with open(log_file, 'r') as f:
                for line in f:
                    if 'ERROR' in line:
                        error_count += 1
        except FileNotFoundError:
            pass
        
        try:
            with open(log_file, 'r') as f:
                for line in f:
                    if 'WARNING' in line:
                        warning_count += 1
        except FileNotFoundError:
            pass
        
        try:
            with open(log_file, 'r') as f:
                for line in f:
                    if 'INFO' in line:
                        info_count += 1
        except FileNotFoundError:
            pass
        
        return {
            'errors': error_count,
            'warnings': warning_count,
            'info': info_count
        }
    
    def create_sample_files(self) -> None:
        """Create sample files for testing."""
        sample_data = [
            {"users": [{"name": "Alice", "age": 30}], "count": 1},
            {"users": [{"name": "Bob", "age": 25}], "count": 1},
            {"products": [{"name": "Widget", "price": 10.99}], "count": 1}
        ]
        
        for i, data in enumerate(sample_data):
            with open(f"sample_{i}.json", 'w') as f:
                json.dump(data, f)
        
        log_entries = [
            "2024-01-01 10:00:00 INFO Application started",
            "2024-01-01 10:01:00 WARNING Low memory",
            "2024-01-01 10:02:00 ERROR Database connection failed",
            "2024-01-01 10:03:00 INFO User logged in",
            "2024-01-01 10:04:00 ERROR File not found",
            "2024-01-01 10:05:00 WARNING Disk space low"
        ]
        
        with open("sample.log", 'w') as f:
            for entry in log_entries:
                f.write(entry + '\n')


def demonstrate_io_issues():
    """Demonstrate I/O inefficient patterns."""
    io_inefficient = IOInefficient()
    
    io_inefficient.create_sample_files()
    
    sample_data = ["line1", "line2", "line3", "line4", "line5"]
    start_time = time.time()
    io_inefficient.inefficient_file_writing(sample_data, "output.txt")
    print(f"File writing took: {time.time() - start_time:.4f}s")
    
    json_files = ["sample_0.json", "sample_1.json", "sample_2.json"]
    start_time = time.time()
    result = io_inefficient.inefficient_json_processing(json_files)
    print(f"JSON processing took: {time.time() - start_time:.4f}s")
    
    start_time = time.time()
    log_stats = io_inefficient.inefficient_log_processing("sample.log")
    print(f"Log processing took: {time.time() - start_time:.4f}s")
    print(f"Log stats: {log_stats}")
    
    for file in ["output.txt", "sample_0.json", "sample_1.json", "sample_2.json", 
                 "sample.log", "simulated_db.txt"] + [f"temp_sample_{i}.json" for i in range(3)]:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    demonstrate_io_issues()
