# eng_to_sp
code={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','p':'s','q':'t','r':'u':'s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}


word=input('Enter a word')

for letter in word:
    codeword=codeword+code[letter]


    print(codeword)
