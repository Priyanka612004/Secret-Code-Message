# SECRETE CODING MESSAGE

st=input ('enter your message: ')
words=st.split(" ")
s=input("Want to Encode or Decode: ")
if (s=="Encode"):
    newwords=[]
    for word in words:
        if (len(word)>=3):
            r1=input("write any 3 alphabet word: ")
            r2=input("again write any 3 alphabet word: ")
            stnew=r1+word[1:]+word[0]+r2
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])
        
    print(" ".join(newwords))

elif(s=="Decode"):
    newwords=[]
    for word in words:
        if (len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])
    print(" ".join(newwords))

else:
    pass

# i ma werriyankapdfg