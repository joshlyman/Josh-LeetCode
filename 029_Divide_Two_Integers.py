# offical solution 
# https://leetcode.com/problems/divide-two-integers/solution/


# While you might be tempted to use multiplication and division for a few "simple" tasks, this is unnecessary. Here are some alternatives:
# Instead of a = a * -1 for making numbers negative, use a = -a.
# Instead of using a / 2 for dividing by 2, use the right shift operator; a >> 1.
# Instead of using a * 2 for doubling, use a = a + a, a += a, or even the left shift operator; a << 1.

# Approach 1. Repeated Subtraction


# Time: O(N)
# Space:O(1)

# Approach 2: Repeated Exponential Searches
def divide(self, dividend: int, divisor: int) -> int:

    # Constants.
    MAX_INT = 2147483647        # 2**31 - 1
    MIN_INT = -2147483648       # -2**31
    HALF_MIN_INT = -1073741824  # MIN_INT // 2

    # Special case: overflow.
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    # We need to convert both numbers to negatives.
    # Also, we count the number of negatives signs.
    negatives = 2
    if dividend > 0:
        negatives -= 1
        dividend = -dividend
    if divisor > 0:
        negatives -= 1
        divisor = -divisor

    quotient = 0
    # Once the divisor is bigger than the current dividend,
    # we can't fit any more copies of the divisor into it anymore */
    while divisor >= dividend:
        # We know it'll fit at least once as divivend >= divisor.
        # Note: We use a negative powerOfTwo as it's possible we might have
        # the case divide(INT_MIN, -1). */
        powerOfTwo = -1
        value = divisor
        # Check if double the current value is too big. If not, continue doubling.
        # If it is too big, stop doubling and continue with the next step */
        while value >= HALF_MIN_INT and value + value >= dividend:
            value += value;
            powerOfTwo += powerOfTwo
        # We have been able to subtract divisor another powerOfTwo times.
        quotient += powerOfTwo
        # Remove value so far so that we can continue the process with remainder.
        dividend -= value

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
    return -quotient if negatives != 1 else quotient


 # Time: O(log^2N)
 # Space:O(1)


# use bit shifting

# x << y means multiplying x by 2**y
# x >> y means dividing x by 2**y

 def divide(self, a, b):
        sig = (a < 0) == (b < 0)
        a, b, res = abs(a), abs(b), 0
        while a >= b:
            x = 0
            while a >= b << (x + 1): x += 1
            res += 1 << x
            a -= b << x

        # -2**31 <= dividend, divisor <= 2**31 - 1
        return min(res if sig else -res, 2147483647)


 # Time: O(log^2 N)
 # Space:O(1)

