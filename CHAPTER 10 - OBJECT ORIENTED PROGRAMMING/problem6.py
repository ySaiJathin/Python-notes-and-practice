# Can you change the self-parameter inside a class to something else (say “harry”). 
# Try changing self to “slf” or “harry” and see the effects.

class parameter:
    def __init__(slf):
        slf.name="harry"


f=parameter()
print(f.name)

