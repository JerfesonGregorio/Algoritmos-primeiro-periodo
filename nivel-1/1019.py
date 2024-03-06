x = int(input())
hh, mm, ss = (x//3600), ((x%3600)//60), (x%60)
print(f'{hh}:{mm}:{ss}')
