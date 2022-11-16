s1, s2 = input().split()

s2_index = 0
search_chr = None
for idx, chr in enumerate(s2):
  if chr in s1:
    s2_index = idx
    search_chr = chr
    break


s1_index = s1.index(search_chr)

for y in range(len(s2)):
  if y == s2_index:
    print(s1)
  else:
    print("."*s1_index+s2[y]+"."*(len(s1)-s1_index-1))