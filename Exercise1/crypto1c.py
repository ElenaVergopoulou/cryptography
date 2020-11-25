def bob(Text,Key1,KeyShift):
    charText=[x for x in Text]
    charKey=[y for y in Key1]
    keyLength=len(charKey)
    for x in range(keyLength):
        charKey[x] = chr(((ord(charKey[x])+KeyShift)-ord('a'))%26+ord('a'))
    i=0
    for t in charText:
        if t.isalpha():
            if ord(t)>=ord('a'):
                print(chr(((ord(t.lower())+ord(charKey[i%keyLength])-2*ord('a'))%26+ord('a'))), end="")
            else:
                print(chr(((ord(t.lower())+ord(charKey[i%keyLength])-2*ord('a'))%26+ord('A'))), end="")
            i=i+1
        else:
            print(t, end="")
    print("")

bob("Hi Eve!You are very naive to think that we have outsmarted Eve. Your plan was dumb. If you insist on using Vigenere Cipher we should use a random key that is at least as big as our messages.","cryptography", 4)
