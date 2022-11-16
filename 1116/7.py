s1, s2 = input().split()

index = 0
search_chr = None
for idx, chr in enumerate(s2):
  if chr in s1:
    index = idx
    search_chr = chr
    break


s2_index = s1.index(search_chr)
for idx, chr in enumerate(s2):
  if index == idx:
    print(s1)
  else:
    for j in range(len(s1)):
      if s2_index== j:
        print(chr, end= '')
      else:
        print('.', end='')
    print()
