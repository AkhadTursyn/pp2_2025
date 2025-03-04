def palindrom(soilem,teris_soilem):
    for i in soilem:
        for j in teris_soilem:
            if i!=j:
                return False
                break
            return True
        
    

sentence=str(input("enter sentence:"))
soilem_reverse=''.join(reversed(sentence))
print(palindrom(sentence,soilem_reverse))
