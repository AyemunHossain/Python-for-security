import random 

#->Generate a ten-character password with 
	#one lowercase character
	#one uppercase characteR
	#one digits 
	#one special character.
sr = random.SystemRandom()

list_ascii=string.ascii_letters+string.digits+string.punctuation
passo=sr.choice(string.punctuation)
passo+=sr.choice(string.ascii_letters)
passo+=sr.choice(string.digits)
passo+="".join(sr.sample(list_ascii,7))
pass_list = list(passo)
sr.shuffle(pass_list)
print("".join(pass_list))