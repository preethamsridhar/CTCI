def is_unique_character_check(String1):
	is_unique_all = [None] * 128
	if len(String1) > 128:
		return "strings are not unique"
	else:
		for i in range(len(String1)):
			if is_unique_all[ord(String1[i])] == 1:
				return "strings are not unique"
			else:
				is_unique_all[ord(String1[i])] = 1
		return "strings are unique"


String1 = raw_input()
print(is_unique_character_check(String1))	
