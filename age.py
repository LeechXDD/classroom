# -*- coding: UTF-8 -*-
f = open("test.txt","r")
wards =[]
for index in f.readlines():
    wards.append(index.strip())
f.close()

sentences = raw_input("input a paragraph\n")


def returndata(sentence,wards,symbol = "*"):
        sentence = sentence.replace(wards,symbol)
        return sentence

for i in wards:
    sentences = returndata(sentences,i)

print sentences
    

    

    
        
