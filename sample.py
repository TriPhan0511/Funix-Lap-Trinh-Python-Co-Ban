with open("/usercode/files/books.txt") as f:
   #your code goes here
   i = 1
   for line in f:
      line = line.strip()
      lst = line.split()
      print(f'Line {i}: {len(lst)} words')
      i += 1