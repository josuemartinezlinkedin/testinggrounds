def generateDocument(characters, document):
    # Write your code here.
    sorted_characters = sorted(characters)
    sorted_document = sorted(document)
    if sorted_document == sorted_characters:
		return True
    else:
		characters_found = 0
		for chars in sorted_document:
				if chars in sorted_characters:
					characters_found+=1
                    sorted_characters.remove(chars)
		if characters_found == len(sorted_document):
			return True
		return False
generateDocument("aheaolabbhb")

#testing edge case
som = "aheaolabbhb"
newnew = sorted(som)
print(newnew)
newnew.remove('a')
print(newnew)
