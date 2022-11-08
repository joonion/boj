for _ in[0]*int(input()):
 k,s=int(input()),""
 while k:t=k-1;s=chr(65+t%26)+s;k=t//26
 print(s)