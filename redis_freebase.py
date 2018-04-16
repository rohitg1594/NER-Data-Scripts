import redis
import pickle
ds = redis.Redis(host="localhost", port=6380)

with open('freebase_ids_en.pickle', 'rb') as f:
    freebase_ids = pickle.load(f)
    for i, (k,v) in enumerate(freebase_ids.items()):
        ds.set(k,v)
        if i %10000 == 0:
            print("{} done".format(i))
    
