f=open('sfzh.txt','r')
for sfzh in f:
    sfzh=sfzh.strip()
    if sfzh[15:18]=='999':
        print sfzh
