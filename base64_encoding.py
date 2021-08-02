#python version 3.9.5
#Base64 Encoding/Decoding

import base64

decision = input("Would you like to encode or decode Base64? (encode/decode) ")
decision = decision.upper()


if (decision == 'ENCODE'):
    #base64 Encoding
    userInput = input("Enter string to convert to base64: ")
    userInputAscii = userInput.encode('ascii')
    base64Encoding = base64.b64encode(userInputAscii)
    base64Complete = base64Encoding.decode('ascii')
    print(base64Complete)

elif (decision == 'DECODE'):
    #base64 Decoding
    userInput = input("Enter string to convert to base64: ")
    userInputDecode = base64.b64decode(userInput)
    userOutput = userInputDecode.decode('ascii')
    print (userOutput)

else:
    print("Invalid Input")
    


    
