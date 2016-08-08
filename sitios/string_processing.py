# -*- coding: utf-8 -*-


def create_accents_regular_expression(word):
	expressions_group = {"a":"[aáàäâ]", "e": "[eèêéë]","i":"[iîïìí]","o":"[oóòöô]","u":"[uúùüû]"};

	for  vowel, expression in expressions_group.iteritems():
		if vowel in word:
			word=word.replace(vowel,expression)

	return word


def remove_accents(word):
	word = word.lower()
	word = word.decode('utf-8')
	vowel_accents_group = {u"àáÀÁ":"a",u"èéÈÉ":"e",u"ìíÌÍ":"i",u"òóÒÓ":"o",u"ùúÙÚ":"u"}
	for character in word:
		for vowel_accents,vowel in vowel_accents_group.iteritems():
			if character in  vowel_accents:
				word = word.replace(character, vowel)

	return word.encode('utf-8')



