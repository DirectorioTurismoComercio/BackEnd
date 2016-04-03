



class SearchedString:
	def __init__(self,token,string):
		self.token = token.upper();
		self.string = string.upper();
		self.number_spaces = token.count(' ');	
		self.position = string.upper().find(token.upper());
		
	
	def is_only_one_word(self):  
		print self.number_spaces   
		return self.number_spaces==0
    
	def is_at_the_begining(self):
		return self.position==0

	def is_at_the_end_of_word(self):
		return self.string[self.position+len(self.token)]==' '

	def number_of_words(self):
		return 	self.number_spaces

class Sentence:
	def __init__(self,token,string):
		self.string =string
		self.token=token
		self.space_indexes=find_character_indexes(self.string[token.position:],' ')
	
	def is_only_one_word(self):
		return len(self.space_indexes)==1
    
	def rest_of_the_sentence(self):
		return self.string[self.token.position:]

	def rest_of_the_word_and_next_word(self):
		return self.string[self.token.position:self.token.position+self.space_indexes[1]]

	def rest_of_the_word(self):	
		return self.string[self.token.position:self.token.position+self.space_indexes[0]]

	def number_of_words(self):
		return len(self.space_indexes)	



def generate_string_suggestions(string, string_array):
	sugerencias=[]
	token=string
	number_spaces_token = token.count(' ');
     
	for string in string_array:
    		position = string.upper().find(token.upper());   
    		term = SearchedString(token,string) 
    		space_indexes=find_character_indexes(string[position:],' ')
    		sentence = Sentence(term,string)

    		if term.is_at_the_begining() or not has_spaces(string): 
	        	if has_spaces(string): 
					if term.is_only_one_word():
						if term.is_at_the_end_of_word():
							if sentence.is_only_one_word():
								suggestion = sentence.rest_of_the_sentence()                
							else:
								suggestion = sentence.rest_of_the_word_and_next_word()  
								print ("i1",suggestion)         
						else: 
							suggestion = sentence.rest_of_the_word()
							print ("i0",suggestion)  
					else:
						if term.number_of_words()+1<sentence.number_of_words(): 
							suggestion = string[position:position+space_indexes[number_spaces_token+1]]
							print("i2",suggestion)
						else:
							suggestion = sentence.rest_of_the_sentence()
	        	else:
	        		if position>=0:
					suggestion = string[position:]  
					print("i6",suggestion,position)
			if position>=0 and suggestion not in sugerencias: 
				sugerencias.append(suggestion)	

	return sugerencias



def find_character_indexes(string,searched_character):
	indexes=[index for index, character in enumerate(string) if character == searched_character]
	return indexes

def has_spaces(string):
    return ' ' in string
