#Create an iterator class

class MyNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

#Save the value to return, then increment by 2
        current = self.start
        self.start += 2
        return current

#Create an instance of the MyNumbers class
even_numbers = MyNumbers(2, 20)

#Use a for loop to iterate through the even numbers
for num in even_numbers:
    print(num)
    