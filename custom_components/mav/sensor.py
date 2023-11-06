from homeassistant.helpers.entity import Entity
import requests
from datetime import datetime

class MavSensor(Entity):
    def __init__(self, name, state, station):
        self._name = name
        self._state = state
        self._station = station

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def station(self):
        ''' Returns the station code, e.g., 005503178 '''
        return self._station

    @property
    def departures(self):
        return self.stationInfo['stationSchedulerDetails']['departureScheduler']

    @property
    def arrivals(self):
        return self.stationInfo['stationSchedulerDetails']['arrivalScheduler']

    @property
    def stationInfo(self):
        return self._stationInfo

    def update(self):
        # Update the state of the sensor
        # This is where you would add your logic to fetch the new state
        payload = {
            "type": "StationInfo",
            "stationNumberCode": self.station,
            "travelDate": datetime.now().isoformat(),
            "minCount": "0",
            "maxCount": "12"
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Language": "hu"
        }
        stationInfo = requests.post("https://jegy-a.mav.hu/IK_API_PROD/api/InformationApi/GetTimetable", json=payload, headers=headers).json()
        self.stationInfo = stationInfo

    @property
    def stationInfo(self):
        return self._stationInfo

    @stationInfo.setter
    def stationInfo(self, value):
        self._stationInfo = value

    def getMarkdown(self, type):
        if type == "arrivals":
            return self.getMarkdownArrivals()
        elif type == "departures":
            return self.getMarkdownDepartures()
        else:
            return ""
    
    def getMarkdownDepartures(self):
        markdown =  "|Indulás|Késés|Jel|Hová|\n"
        markdown += "|-------|-----|:-:|----|\n"
        for departure in self.departures:
            aktualisKeses = str(int(departure['havarianInfok']['aktualisKeses'])) + ' perc' if int(departure['havarianInfok']['aktualisKeses']) > 0 else ''
            markdown += f"|{datetime.fromisoformat(departure['start']).strftime('%H:%M')} | { aktualisKeses } | {departure['viszonylatiJel']['jel']} | **{departure['endStation']['name']}** |\n"
        return markdown

    def getMarkdownArrivals(self):
        markdown =  "|Érkezés|Késés|Jel|Honnan|\n"
        markdown += "|-------|-----|:-:|------|\n"
        for arrival in self.arrivals:
            aktualisKeses = str(int(arrival['havarianInfok']['aktualisKeses'])) + ' perc' if int(arrival['havarianInfok']['aktualisKeses']) > 0 else ''
            markdown += f"|{datetime.fromisoformat(arrival['arrive']).strftime('%H:%M')} | { aktualisKeses } | {arrival['viszonylatiJel']['jel']} | **{arrival['startStation']['name']}** |\n"
        return markdown

