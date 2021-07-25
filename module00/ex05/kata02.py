import datetime

if __name__ == "__main__":
    t = (3, 30, 2019, 9, 25)
    print(datetime.datetime.strftime(datetime.datetime.strptime(' '.join(map(str, t)), "%H %M %Y %m %d"), "%m/%d/%Y %H:%M"))