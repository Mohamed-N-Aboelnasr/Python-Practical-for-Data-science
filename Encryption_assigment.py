def encryptFunc(Text, key):
	encryption = ""
	for c in Text:
		if c.isupper():
			c_index=ord(c)-ord("A")
			new_index= (key + c_index) % 26 +ord("A")
			new_c=chr(new_index)
			encryption += new_c
		elif c.islower():
			c_index = ord(c) - ord("a")
			new_index = (key + c_index) % 26 + ord("a")
			new_c = chr(new_index)
			encryption += new_c
		elif c.isdigit():
			new_c=(int(c)+key)%10
			encryption+=str(new_c)
		else:
			encryption+=c
	return encryption

def decryptionFunc(Text,key):
	decryption=""
	for c in Text:
		if c.isupper():
			c_index = ord(c) - ord('A')
			new_index = (c_index - key) % 26 + ord('A')
			new_c = chr(new_index)
			decryption += new_c
		elif c.islower():
			c_index = ord(c) - ord('a')
			new_index = (c_index - key) % 26 + ord('a')
			new_c = chr(new_index)
			decryption += new_c
		elif c.isdigit():
			new_c=(int(c)-key)%10
			decryption+=str(new_c)
		else:
			decryption+=c
	return decryption



Text=input("Please enter your text : ")
encryptedText=encryptFunc(Text,4)
print("This is original text : "+Text)
print("This is the encrypted text : "+encryptedText)
print("********************************************************")
decryptedText=decryptionFunc(encryptedText,4)
print("This is the decrypted text : "+decryptedText)


