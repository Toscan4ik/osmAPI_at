import requests
import json

class Seeker:

    url = "https://nominatim.openstreetmap.org"
    _s = requests.session()
    headers = {"Accept-Language": "ru-RU"}


    def search_by_text(self, text):

        """Поиск по адресу"""

        url = f"{self.url}/search?q={text}&format=json"

        _r = self._s.get(url, headers=self.headers)

        return {"text": json.loads(_r.text)}

    def search_by_coords(self, lat, lon):

        """Поиск по координатам"""

        url = f"{self.url}/reverse?lat={lat}&lon={lon}&format=json"

        _r = self._s.get(url, headers=self.headers)

        return {'text': json.loads(_r.text)}


# class FileReader:
#
#     def __init__(self, file):
#         self.file = file
#
#     def read(self):
#
#         with open(self.file, newline='') as csvfile:
#             fieldnames = [
#                 'region',
#                 'municipality',
#                 'settlement',
#                 'latitude',
#                 'longitude'
#             ]
#             reader = csv.DictReader(csvfile, fieldnames=fieldnames)
#             settlements = []
#             for row in reader:
#                 settlements.append(row)
#
#             return settlements
