import datetime

for i in range(int(input())):
    dt1 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(int(abs((dt1-dt2).total_seconds())))