import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
	'''
	file_name (string): the name of the file containing
	the list of words to load

	Returns: a list of valid words. Words are strings of lowercase letters.

	Depending on the size of the word list, this function may
	take a while to finish.
	'''
	print('Loading word list from file...')
	# inFile: file
	in_file = open(file_name, 'r')
	# line: string
	line = in_file.readline()
	# word_list: list of strings
	word_list = line.split()
	print('  ', len(word_list), 'words loaded.')
	in_file.close()
	return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
	"""
	Determines if word is a valid word, ignoring
	capitalization and punctuation

	word_list (list): list of words in the dictionary.
	word (string): a possible word.

	Returns: True if word is in word_list, False otherwise

	Example:
	#>>> is_word(word_list, 'bat') returns
	True
	#>>> is_word(word_list, 'asdf') returns
	False
	"""
	word = word.lower()
	word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
	return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
	"""
	Returns: a joke in encrypted text.
	"""
	f = open("story.txt", "r")
	story = str(f.read())
	f.close()
	return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
	### DO NOT MODIFY THIS METHOD ###
	def __init__(self, text):
		"""
		Initializes a Message object

		text (string): the message's text

		a Message object has two attributes:
			self.message_text (string, determined by input text)
			self.valid_words (list, determined using helper function load_words
		"""
		self.message_text = text
		self.valid_words = load_words(WORDLIST_FILENAME)

	### DO NOT MODIFY THIS METHOD ###
	def get_message_text(self):
		"""
		Used to safely access self.message_text outside of the class

		Returns: self.message_text
		"""
		return self.message_text

	### DO NOT MODIFY THIS METHOD ###
	def get_valid_words(self):
		"""
		Used to safely access a copy of self.valid_words outside of the class

		Returns: a COPY of self.valid_words
		"""
		return self.valid_words[:]

	def build_shift_dict(self, shift):
		"""
		Creates a dictionary that can be used to apply a cipher to a letter.
		The dictionary maps every uppercase and lowercase letter to a
		character shifted down the alphabet by the input shift. The dictionary
		should have 52 keys of all the uppercase letters and all the lowercase
		letters only.

		shift (integer): the amount by which to shift every letter of the
		alphabet. 0 <= shift < 26

		Returns: a dictionary mapping a letter (string) to
				 another letter (string).
		"""
		lowerDict = {}
		upperDict = {}
		lowerAlpha = string.ascii_lowercase
		letterLocation = shift
		for letter in lowerAlpha:
			if letterLocation == 26:
				letterLocation = 0
			lowerDict[letter] = lowerAlpha[letterLocation]
			letterLocation += 1
		for key, value in lowerDict.items():
			upperDict[key.upper()] = value.upper()
		comboDict = lowerDict.copy()
		comboDict.update(upperDict)

		return comboDict

	def apply_shift(self, shift):
		"""
		Applies the Caesar Cipher to self.message_text with the input shift.
		Creates a new string that is self.message_text shifted down the
		alphabet by some number of characters determined by the input shift

		shift (integer): the shift with which to encrypt the message.
		0 <= shift < 26

		Returns: the message text (string) in which every character is shifted
			 down the alphabet by the input shift
		"""
		#grab the shifted alphabet dict in build_shift_dict(self,shift)
		shiftedDict = self.build_shift_dict(shift)
		#create a blank string
		encString = ""
		#iterate over self.message_text,
		for item in self.message_text:
			# if the item is a key in the shifted dict
			if item in shiftedDict:
				#add it to the string with teh value from the shifted dict
				encString = encString + shiftedDict[item]
			# otherwise add the item as is, to the string
			else:
				encString = encString + item
		#return the string
		return encString


class PlaintextMessage(Message):
	def __init__(self, text, shift):
		"""
		Initializes a PlaintextMessage object

		text (string): the message's text
		shift (integer): the shift associated with this message

		A PlaintextMessage object inherits from Message and has five attributes:
			self.message_text (string, determined by input text)
			self.valid_words (list, determined using helper function load_words)
			self.shift (integer, determined by input shift)
			self.encrypting_dict (dictionary, built using shift)
			self.message_text_encrypted (string, created using shift)

		Hint: consider using the parent class constructor so less
		code is repeated
		"""
		Message.__init__(self, text)
		self.shift = shift
		self.encrypting_dict = Message.build_shift_dict(self, self.shift)
		self.message_text_encrypted = Message.apply_shift(self, self.shift)


	def get_shift(self):
		"""
		Used to safely access self.shift outside of the class

		Returns: self.shift
		"""
		return self.shift

	def get_encrypting_dict(self):
		"""
		Used to safely access a copy self.encrypting_dict outside of the class

		Returns: a COPY of self.encrypting_dict
		"""
		return self.encrypting_dict.copy()

	def get_message_text_encrypted(self):
		"""
		Used to safely access self.message_text_encrypted outside of the class

		Returns: self.message_text_encrypted
		"""
		return self.message_text_encrypted

	def change_shift(self, shift):
		"""
		Changes self.shift of the PlaintextMessage and updates other
		attributes determined by shift (ie. self.encrypting_dict and
		message_text_encrypted).

		shift (integer): the new shift that should be associated with this message.
		0 <= shift < 26

		Returns: nothing
		"""
		self.shift = shift
		self.encrypting_dict = Message.build_shift_dict(self, self.shift)
		self.message_text_encrypted = Message.apply_shift(self, self.shift)


class CiphertextMessage(Message):
	def __init__(self, text):
		"""
		Initializes a CiphertextMessage object

		text (string): the message's text

		a CiphertextMessage object has two attributes:
			self.message_text (string, determined by input text)
			self.valid_words (list, determined using helper function load_words)
		"""
		Message.__init__(self, text)
		#self.message_text = text

	def decrypt_message(self):
		"""
		Decrypt self.message_text by trying every possible shift value
		and find the "best" one. We will define "best" as the shift that
		creates the maximum number of real words when we use apply_shift(shift)
		on the message text. If s is the original shift value used to encrypt
		the message, then we would expect 26 - s to be the best shift value
		for decrypting it.

		Note: if multiple shifts are  equally good such that they all create
		the maximum number of you may choose any of those shifts (and their
		corresponding decrypted messages) to return

		Returns: a tuple of the best shift value used to decrypt the message
		and the decrypted message text using that shift value - int, string
		"""
		result = {}
		bestShift = 0
		highestWords = 0
		realWords = Message.get_valid_words(self)
		for counter in range(26):
			count = 0
			#check each word in the split string to determine if it's a word
			message_text_encrypted = Message.apply_shift(self, counter)
			result[counter] = message_text_encrypted

			words = message_text_encrypted.split(' ')
			for word in words:
				if is_word(realWords,word):
					count += 1
			if count > highestWords:
				highestWords = count
				bestShift = counter

		output = (bestShift, result[bestShift])
		return output

def decrypt_story():
	"""
	Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. The file ps6.py
	contains a helper function get_story_string() that returns the encrypted version of the story as a string.
	Create a CiphertextMessage object using the story string and use decrypt_message to return the appropriate
	shift value and unencrypted story string.

	returns: string - story in plain text
	"""

	text = get_story_string()
	ciphertext = CiphertextMessage(text)
	return ciphertext.decrypt_message()

#Example test case (PlaintextMessage)
#plaintext = PlaintextMessage('hello world how are you today', 2)
#print('Expected Output: jgnnq')
#print('Actually expected output: jgnnq yqtnf jqy ctg aqw vqfca')
#print('Actual Output:', plaintext.get_message_text_encrypted())

#Example test case (CiphertextMessage)
#ciphertextO = CiphertextMessage('jgnnq yqtnf jqy ctg aqw vqfca')
#print('Expected Output:', (24, 'hello'))
#print('Actually expected output: (24, hello world how are you today)')
#print('Actual Output:', ciphertextO.decrypt_message())

print(decrypt_story())
