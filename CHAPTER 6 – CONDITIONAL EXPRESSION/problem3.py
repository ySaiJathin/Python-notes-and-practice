# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

text=input("Enter the sentence: ").lower()
words=["Make a lot of money", "buy now", "subscribe this", "click this"]

if "Make a lot od money" in text or 'buy now' in text or "subscribe this" in text or "click this" in text:
    print("Scam!")
else:
    print("Not spam.")
