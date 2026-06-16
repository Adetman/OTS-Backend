class CountDown:
    def __init__(self):
        self.current = 11

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current < 1:
            raise StopIteration
        return self.current

# Using the iterator
result = CountDown()
for number in result:
    print(number)