from api.client import Seeker

def test_search_by_coords(test_data):

    seeker = Seeker()

    lat = test_data.get('latitude')
    lon = test_data.get('longitude')


    res = seeker.search_by_coords(lat, lon).get('text')


    assert test_data.get('region') in res.get('display_name') and \
           test_data.get('municipality') in res.get('display_name') and \
           test_data.get('settlement') in res.get('display_name')
