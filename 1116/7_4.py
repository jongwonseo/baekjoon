s1, s2 = input().split()

s2_index = 0
search_chr = None
for idx, chr in enumerate(s1):
  if chr in s2:
    s1_index = idx
    search_chr = chr
    break


s2_index = s2.index(search_chr)

for y in range(len(s2)):
  if y == s2_index:
    print(s1)
  else:
    print("."*s1_index+s2[y]+"."*(len(s1)-s1_index-1))