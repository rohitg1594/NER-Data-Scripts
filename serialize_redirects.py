import codecs
import redis

ds = redis.StrictRedis(host="localhost", port=6379, db=2)
ds.flushdb()

redirects = {}
with codecs.open('redirects_en.tql', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i != 0:
            try:
                split = line.split()
                k = split[0].split('resource/')[1][:-1]
                v = split[2].split('resource/')[1][:-1]
                redirects[k] = v
            except IndexError:                            #
                print(line)
        if i%10000 == 0:
            print("{} done".format(i))

    print("First pass done\n")

    for i, (k, v) in enumerate(redirects.items()):
        if v in redirects:
            redirects[k] = redirects[v]

        ds.set(k, redirects[k])

        if i%10000 == 0:
            print("{} done".format(i))
