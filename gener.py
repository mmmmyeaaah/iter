def flat_generator(list_):
    new_list = sum(list_, [])
    for words in new_list:
        if isinstance(words, list):
            for word in words:
                yield word
        else:
            yield words


nested_list = [
	['a', 'b', 'c', [111,[2222]]],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

if __name__ == '__main__':
    for item in flat_generator(nested_list):
	    print(item) 