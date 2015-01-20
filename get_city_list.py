import sys
import re
import collections

id_idx = 0
time_idx = 1
city_idx = 2

current_id = ''
tm_data = []
for l in sys.stdin:
    clms = re.split('\t', l.strip('\n'))
    tmp_id, tmp_city, tmp_time = clms[id_idx], clms[city_idx], clms[time_idx]
    if current_id != tmp_id:
        if len(tm_data) != 0:
            city_list = map(lambda x: x[2], sorted(tm_data, 
                key=lambda x: x[1]))
            cities = [city_list[0]]
            home_cities = filter(lambda c: c[1]>'100' and c[1]<'400', city_list)
            for city in city_list:
                if city != cities[-1]:
                    cities.append(city)
            if len(home_cities) > 1:
                home_city = collections.Counter(home_cities).most_common(1)[0]
            else:
                home_city = cities[0]
            print '\t'.join([current_id, home_city, ','.join(cities)])
        current_id = tmp_id
        tm_data = [(current_id, tmp_time, tmp_city)]
    tm_data.append((current_id, tmp_time, tmp_city))

        

