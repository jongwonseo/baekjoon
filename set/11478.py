str = input()
length =len(str)
lst = [[str[j:j+i] for j in range(length-i+1)] for i in range(1, len(str)+1)]
lst = sum(lst, [])
print(len(set(lst)))