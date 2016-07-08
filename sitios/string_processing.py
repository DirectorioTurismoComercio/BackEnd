# -*- coding: utf-8 -*-


def create_regular_expression_with_accents(word):
	expressions = {"aàá":"[àá]", "eèêéë": "[eèêéë]"};

	for  accents in expressions:
		position=0
		for character in word:
			if character in accents:
				word[position]=expressions[accents]
		position=position+1


	return word


def remove_accents(word):
	vowel_accents_group = {"àá":"a","èé":"e"}
	for character in word:
		for vowel, vowel_accents in vowel_accents_group.iteritems():
			if character in  vowel_accents:
				word = word.replace(character, '*')

	return word



