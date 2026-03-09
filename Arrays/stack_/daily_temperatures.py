"""
Daily Temperatures

Problem:
Return the number of days until a warmer temperature.

Approach:
Use a monotonic decreasing stack storing indices.
When a warmer temperature appears, resolve previous days.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def daily_temperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            result[prev] = i - prev

        stack.append(i)

    return result


if __name__ == "__main__":
    print(daily_temperatures([73,74,75,71,69,72,76,73]))