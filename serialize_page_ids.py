import codecs
import redis

ds = redis.StrictRedis(host="localhost", port=6379, db=0)
ds.flushdb()

with codecs.open('page_ids_en.tql', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i != 0:
            try:
                k = line.split()[0].split('resource/')[1][:-1]
                v = int(line.split('?oldid=')[1][:-4]) #
                ds.set(k, v)
            except IndexError:                            #
                print(line)
        if i%10000 == 0:
            print("{} done".format(i))


#################################################
# for i, (k, v) in enumerate(page_ids.items()): #
#     print(k,v)                                #
#     if i == 20:                               #
#         break                                 #
# print(len(page_ids))                          #
#                                               #
# with open('page_ids_en.pickle', 'wb') as f:   #
#     pickle.dump(page_ids, f)                  #
#                                               #
# with open('page_ids_en.pickle', 'rb') as f:   #
#     page_ids = pickle.load(f)                 #
#                                               #
# for i, (k, v) in enumerate(page_ids.items()): #
#     print(k, v)                               #
#     if i == 20:                               #
#         break                                 #
# print(len(page_ids))                          #
#################################################


