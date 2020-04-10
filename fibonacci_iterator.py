class FibonacciIterable:

    def __init__(self, iterations_num):
        self.iterations_num = iterations_num
        self.start = 0

        self.cache = {}
        for n in range(self.iterations_num + 1):
            if n == 0:
                self.cache[n] = 0
                continue
            if n in (1, 2):
                self.cache[n] = 1
                continue
            self.cache[n] = self.cache[n - 2] + self.cache[n - 1]

    def print_cache(self):
        return self.cache

    def __iter__(self):
        """New definition of iter."""
        return self

    def __next__(self):
        """New definition of next method."""
        if self.start >= len(self.cache):
            raise StopIteration
        current = self.start
        self.start += 1
        return self.cache[current]


if __name__ == '__main__':

    fibonacci = FibonacciIterable(11)
    print(fibonacci.print_cache())
    for value in fibonacci:
        print(value)

    # fib1 = fibonacci.__next__()
    # fib2 = fibonacci.__next__()
    # fib3 = fibonacci.__next__()
    # fib4 = fibonacci.__next__()
    # fib5 = fibonacci.__next__()

    # for i in range(11):
    #     print(f'fib{i}: {fibonacci.__next__()}')
