class Fibonacci:
    def __init__(self, n: int):
        """
        Custom Iterable implementation for generating members of the Fibonacci
        sequence via Python's Iterable Protocol.
        Args:
            n: The number in the Fibonacci sequence that is to be calculated.
        """
        # the final digit to calculate
        self.n = n
        
        # the number of members generated
        self._i = 0
        
        # references to the current and next members
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        """Calculates and returns the next value in the Fibonacci sequence."""

        # returns next digit until the n-th digit is reached
        if self._i < self.n:

            # increases reference to members
            self._i += 1

            # gets the current value
            fib = self._current

            # gets next values in sequence
            self._current, self._next = self._next, self._current + self._next
            return fib

        # raises the StopIteration error which Python uses to end e.g. for loops
        else:
            raise StopIteration
        
    @staticmethod
    def get_nth(n: int) -> int:
        """
        Returns the nth member in the Fibonacci sequence
        Args:
            n: an integer representing the n-th digit in the sequence.
        """
        return list(Fibonacci(n))[-1]
