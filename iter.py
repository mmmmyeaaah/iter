class FlatIterator:

    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        self.count += 1
        new_list = sum(self.list_, [])
        if self.count == len(new_list):
            raise StopIteration   
        return new_list[self.count]

nested_list = [
	['a', 'b', 'c', [11111]],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
	    print(item) 
    # flat_list = [item for item in FlatIterator(nested_list)]    
    # print(flat_list)