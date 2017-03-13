def check_permutation(str1, str2):
	if len(set(str1)) != len(set(str2)):
		return "'%s' is not the permuation of '%s'"%("".join(str1),"".join(str2))
	else:
		str1_set = list(set(str1))
		str2_set = list(set(str2))
		for i in range(len(str1_set)):
			if str1_set[i] != str2_set[i]:
				return "'%s' is not the permuation of '%s'"%("".join(str1),"".join(str2))
				break
		return  "'%s' is the permuation of '%s'"%("".join(str1),"".join(str2))

str1 = list(raw_input())
str2 = list(raw_input())
print(check_permutation(str1,str2))
