letters = 'abcdefghijklmnopqrstuvwxyz '
numbers = [2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999,0]
numbers_str = [str(num) for num in numbers]
letter_array = [letter for letter in letters]
encode_dict = dict(zip(letter_array, numbers_str))
decode_dict = dict(zip(numbers_str, letter_array))

# print(letter_dict)

message = 'What is your message'
decode = '8 44 444 7777 0 444 7777 0 6 999 0 6 33 7777 7777 2 4 33'


def encode_message(message):
	code_array = []
	for letter in message:
		code_array.append(encode_dict[letter.lower()])
	return str.join(' ', code_array)
	
	
def decode_message(message):
	message_array = message.split(" ")
	response_array = []
	for letter in message_array:
		response_array.append(decode_dict[letter])
	return str.join('', response_array)
	
print(encode_message(message))
print(decode_message(decode))
