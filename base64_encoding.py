#python version 3.9.5
#Base64 Encoding/Decoding

import base64

userInput = input("Enter string to convert to base64: ")
userInputAscii = userInput.encode('ascii')
base64Encoding = base64.b64encode(userInputAscii)
base64Complete = base64Encoding.decode('ascii')

print(base64Complete)

#base64 Decoding

userInputDecode = base64.b64decode(base64Complete)
userInputyeet = userInputDecode.decode('ascii')
print (userInputyeet)
