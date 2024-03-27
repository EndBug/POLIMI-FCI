import requests

# Scrivere uno script che stampi il nome della pagina col
# miglior tempo di risposta medio tra 6 siti Internet. Per il
# calcolo del tempo medio, si definisca la funzione
# media(list) che ritorna la media dei valori contenuti in list.
# • Numero di richieste = 10
# • Siti internet:
# 1. http://www.google.com
# 2. http://www.youtube.com
# 3. http://www.polimi.it
# 4. http://www.wikipedia.org
# 5. http://www.amazon.com
# 6. http://www.twitter.com

if __name__ == '__main__':
    urls = [
        'https://www.google.com', 'https://www.youtube.com', 'https://www.polimi.it',
        'https://www.wikipedia.org', 'https://www.amazon.com', 'https://www.twitter.com'
    ]
    N_REQS = 10
    avgs = []

    for url in urls:
        times = []

        for _ in range(N_REQS):
            r = requests.get(url)
            times.append(r.elapsed.microseconds / 1000)

        avgs.append(sum(times) / len(times))

    print(urls[avgs.index(min(avgs))], min(avgs))
