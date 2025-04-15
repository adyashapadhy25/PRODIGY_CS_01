#Caesar Cipher program
#this program encrypts and decrypts a message using Caesar logic
def caesar_encrypt(message,shift):
    result=""

    for ch in message:
        if ch.isalpha():  #check if it is a letter
            if ch.isupper():
                new_char=chr((ord(ch)-65+shift)%26+65)
            else:
                new_char=chr((ord(ch)-97+shift)%26+97)
                result=result+new_char
        else:
            result=result+ch
    return result
    
def caesar_decrypt(cipher,shift):
    return caesar_encrypt(cipher,-shift)

#start of the program
print("This will encrypt and decrypt message using a secret number\n")
text=input("Enter your message:")
s=input("Enter a secret shift number:")
if s.isdigit():
    s=int(s)
    encrypted=caesar_encrypt(text,s)
    print("Encrypted message is:",encrypted)
    decrypted=caesar_decrypt(encrypted,s)
    print("Decrypted message is:",decrypted)
else:
    print("oops!please enter a valid number next time:")    

