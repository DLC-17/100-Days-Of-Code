def ceasarcypher(message,code):
    crypt=input("Would you like to encrypt or decrypt the message? ")
    cypher=""
    if crypt[0]=='e':
    #This function takes a string and a code and returns the ceasarcyphered string
        for i in range(len(message)):
            cypher+=chr(ord(message[i])+code)  
        return str(cypher)
    else:
        for i in range(len(message)):
            cypher+=chr(ord(message[i])-code)
        return str(cypher)
        
print(ceasarcypher("jkk",2))