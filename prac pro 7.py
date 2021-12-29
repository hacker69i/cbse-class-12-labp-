file=open("data.txt","r")
content=file.read()
print(content)
vowels=0
consonants=0
lower_case_letters =0
upper_case_letters=0
for ch in content:
  if(ch.lower()):
    lower_case_letters+=1
  elif(ch.isupper()):
    upper_case_letters+=1
  ch=(ch.lower())
  if (ch in['a','e','i','o','u']):
    vowels+=1
  elif(ch in [ " b","c","d","f","g","h","k","j","l","m","n","p","q","r","s","t","v","w","x","y","z", ]):
    consonants+=1
file.close()
print("no of vowel ", vowels)
print("no of consonants", consonants)
print("no of  lower case", lower_case_letters)
print("no of  upper case", upper_case_letters) 
  
  
      
