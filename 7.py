spisok = (1,2,3,4,5,6,7,8) 
print([spisok[i-1] if i % 2 else spisok[i+1] for i in range(len(spisok))])