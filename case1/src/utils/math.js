export function sumNumbers(arr) {
  let total = 0;
  for (const n of arr) {
    total += n;
  }
  return total;
}

export function average(arr) {
  if (arr.length === 0) return 0;
  return sumNumbers(arr) / arr.length;
}
