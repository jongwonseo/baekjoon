n, m = map(int, input().split())
pocketmon = [ input() for _ in range(n)]

lst = [input() for _ in range(m)]

for question in lst:
  try:
    question = int(question)
    print(pocketmon[question-1])

  except:
    for i,data in enumerate(pocketmon):
      if question == data:
        print(i+1)
        break;