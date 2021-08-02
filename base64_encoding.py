#python version 3.9.5
#Base64 Encoding/Decoding

import base64

def intro():
    decision = input("Would you like to encode or decode Base64? (encode/decode) ")
    decision = decision.upper()

    if (decision == 'ENCODE'):
        encoding()

    
    elif (decision == 'DECODE'):
        decoding()

    else:
        print("Invalid Input")
    
def encoding():
    #base64 Encoding
    userInput = input("Enter string to convert to base64: ")
    userInputAscii = userInput.encode('ascii')
    base64Encoding = base64.b64encode(userInputAscii)
    base64Complete = base64Encoding.decode('ascii')
    print(base64Complete)


def decoding():
    #base64 Decoding
    userInput = input("Enter string to convert to base64: ")
    userInputDecode = base64.b64decode(userInput)
    userOutput = userInputDecode.decode('ascii')
    print (userOutput)

intro()


    
