import redis
import pickle
ds = redis.Redis(host="localhost", port=6379)

with open('page_ids_en.pickle', 'rb') as f:
    page_ids = pickle.load(f)
    for k,v in page_ids.items():
        ds.set(k,v)
    
