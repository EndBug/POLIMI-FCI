import requests

# Scrivere uno script che stampi il nome della
# pagina col miglior tempo di risposta medio tra 2
# siti Internet.
# • Numero di richieste = 5
# • Siti internet:
# 1. http://www.google.com
# 2. http://www.youtube.com

if __name__ == '__main__':
    urls = ['https://www.google.com', 'https://www.youtube.com']
    res = []

    urlA = 'https://www.google.com'
    tmpTimes = []
    for _ in range(5):
        r = requests.get(urlA)
        tmpTimes.append(r.elapsed.microseconds / 1000)
    timeA = sum(tmpTimes) / len(tmpTimes)

    urlB = 'https://www.youtube.com'
    tmpTimes = []
    for _ in range(5):
        r = requests.get(urlB)
        tmpTimes.append(r.elapsed.microseconds / 1000)
    timeB = sum(tmpTimes) / len(tmpTimes)

    if timeA < timeB:
        print(urlA)
    else:
        print(urlB)
