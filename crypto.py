# crypto
code={}
for num in range (97,123):
    plaintext_letter=chr(num)
    codetext_letter=chr(num+3)
    code[plaintext_letter]=codetext_letter
    code[' ']='  '


plaintext=input("type a word")
codetext=""
for word in plaintext:
    for letter in word:
        codetext=codetext+code[letter]

[print('f{plaintext}encoded as{codetext}')]


