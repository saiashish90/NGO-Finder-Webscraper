import googlemaps
from pprint import pprint
import pandas as pd
gmaps = googlemaps.Client(key='api_key')
df = pd.read_csv('./all_ngo.csv')
index = []
for ind in df.index:
    address = (df["Address"][ind])
    try:
        geocode_result = gmaps.geocode(address)
        result = (geocode_result[0]['address_components'])
        for i in range(len(result)):
            if(result[i]['types'][0]=='administrative_area_level_2'):
                city = (result[i]['long_name'])
                if(city!="Bangalore Urban" and city!="Bangalore Rural" ):
                    index.append(ind)
    except:
        continue
final = df.drop(index)
print(final)
final.to_csv('./bangalore_ngo.csv', index = False)