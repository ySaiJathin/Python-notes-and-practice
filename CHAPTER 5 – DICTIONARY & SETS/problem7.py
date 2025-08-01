# If the names of 2 friends are same; what will happen to the program in problem 
# 6? 

fri1=input()
fri2=input()
fri3=input()
fri4=input()

dic={
    'jonny':"",
    'jathin':'',
    'jathin':'',
    'rahul':''
}
dic.update({'jonny':fri1})
dic.update({'jathin':fri2})
dic.update({'jathin':fri3})
dic.update({'rahul':fri4})

print(dic)
print(dic.get('jathin'))
