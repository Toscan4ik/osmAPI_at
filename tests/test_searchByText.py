from api.client import Seeker

def test_search_by_text(test_data):

    seeker = Seeker()


    text = f"{test_data.get('region')}, {test_data.get('municipality')}, {test_data.get('settlement')}"

    res = seeker.search_by_text(text).get('text')


    assert len(res) != 0 and \
           float(test_data.get('latitude')) >= float(res[0].get('boundingbox')[0]) and \
           float(test_data.get('latitude')) <= float(res[0].get('boundingbox')[1]) and \
           float(test_data.get('longitude')) >= float(res[0].get('boundingbox')[2]) and \
           float(test_data.get('longitude')) <= float(res[0].get('boundingbox')[3])


