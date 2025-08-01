letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

letter2=letter.replace('<|Name|>','Jathin').replace('<|Date|>','18/07/25')
print(letter2)