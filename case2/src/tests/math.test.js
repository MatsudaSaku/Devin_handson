import { average } from '../utils/math.js';

describe('average function', () => {
  test('should return 0 for empty array', () => {
    expect(average([])).toBe(0);
  });

  test('should return the single value for array with one element', () => {
    expect(average([5])).toBe(5);
    expect(average([42])).toBe(42);
    expect(average([0])).toBe(0);
  });

  test('should calculate correct average for multiple positive numbers', () => {
    expect(average([1, 2, 3])).toBe(2);
    expect(average([2, 4, 6, 8])).toBe(5);
    expect(average([10, 20, 30])).toBe(20);
  });

  test('should calculate correct average for negative numbers', () => {
    expect(average([-1, -2, -3])).toBe(-2);
    expect(average([-5, -10])).toBe(-7.5);
  });

  test('should calculate correct average for mixed positive and negative numbers', () => {
    expect(average([-1, 1])).toBe(0);
    expect(average([-2, 0, 2])).toBe(0);
    expect(average([-5, 5, 10])).toBe(3.333333333333333);
  });

  test('should handle decimal numbers correctly', () => {
    expect(average([1.5, 2.5, 3.5])).toBe(2.5);
    expect(average([0.1, 0.2, 0.3])).toBeCloseTo(0.2, 5);
  });

  test('should handle large arrays', () => {
    const largeArray = Array.from({ length: 100 }, (_, i) => i + 1);
    expect(average(largeArray)).toBe(50.5);
  });

  test('should handle arrays with duplicate values', () => {
    expect(average([5, 5, 5, 5])).toBe(5);
    expect(average([1, 1, 2, 2])).toBe(1.5);
  });
});
