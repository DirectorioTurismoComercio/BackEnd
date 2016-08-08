

class SearchedString:
	def __init__(self,token,string):
		self.token = token.upper();
		self.string = string.upper();
		self.number_spaces = token.count(' ');	
		self.position = string.upper().find(token.upper());
		self.space_indexes=find_character_indexes(string[position:],' ')
	
	def is_only_one_word():    
		self.number_spaces_token==0
    
	def is_at_the_begining():
		return self.position==0



def generate_string_suggestions(string, string_array):
	sugerencias=[]
	token=string
	number_spaces_token = token.count(' ');
     
	for string in string_array:
    		position = string.upper().find(token.upper());   
    		s=string
    		if position==0 or not has_spaces(string): 
	        	space_indexes=find_character_indexes(string[position:],' ')
	        	if space_indexes: 
					if number_spaces_token==0:
						if string[position+len(token)]==' ':
							if len(space_indexes)>1:
								suggestion = string[position:position+space_indexes[1]]                    
							else:
								suggestion = string[position:]            
						else: 
							suggestion = string[position:position+space_indexes[0]]
					else:
						if number_spaces_token<=len(space_indexes): 
							suggestion = string[position:position+space_indexes[number_spaces_token+1]]
						else:
							suggestion = string[position:]
	        	else:
					suggestion = string[position:]  
			if suggestion not in sugerencias: 
				sugerencias.append(suggestion)	

	return sugerencias



def find_character_indexes(string,searched_character):
	indexes=[index for index, character in enumerate(string) if character == searched_character]
	return indexes

def has_spaces(string):
    return ' ' in string
