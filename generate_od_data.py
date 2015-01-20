import random
from multiprocessing.dummy import Pool

def generate_id(n):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ids = list(map(lambda i: 
        str(random.randint(100000, 999999)) + ''.join(random.sample(abc, 6)), 
        range(n)))
    for i in range(len(ids)):
        chars = list(ids[i])
        random.shuffle(chars)
        ids[i] = ''.join(chars)
    return ids

def get_city(current_city=''):
    city_list = ['bj', 'cq', 'sh', 'sz', 'hz', 'cd', 'dl']
    result_city = current_city if random.random() > 0.05 and \
            current_city != '' else random.choice(city_list)
    return result_city

def get_time():
    time_list = range(100, 999)
    n = random.randint(5, 30)
    time_list = random.sample(time_list, n)
    time_list = map(lambda x: str(x), sorted(time_list))
    return time_list

def generate_data():
    ids = generate_id(100)
    tms = get_time()
    for iid in ids:
        tm_city = ''
        for tm in tms:
            tm_city = get_city(current_city=tm_city)
            print '\t'.join([iid, tm, tm_city])

if __name__ == '__main__':
    generate_data()
