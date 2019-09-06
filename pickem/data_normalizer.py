from abc import ABC, abstractmethod
import json
import datetime


class DataNormalizer(ABC):
    @abstractmethod
    def normalize_data(self):
    """Trys all the data sources and returns a generator in csv of SPORT, EVENT_TIME, HOME-TEAM, AWAY-TEAM, HOME-WIN, AWAY-WIN, BOOKY, UPDATED"""
        pass


class MirrorData(DataNormalizer):
    def __init__(self, infile_stream):
        self.infile_stream = infile_stream
        self.data = None

    def normalize_data(self):
        if not self.data:
            self.data = json.loads(self.infile_stream)
        return self.data


class OddsAPIData(MirrorData):
    # Uses stats from https://the-odds-api.com/
    def __init__(self, infile_stream):
        super(infile_stream):

    def normalize_data(self, infile_stream):
        super().normalize_data(infile_stream)
        csv = []
        self.data = self.data['data']
        for game in self.data:
            sport = game['sport_key']
            home, away = game['teams'][home_index], game['teams'][away_index]
            kick_off = datetime.datetime.fromtimestamp(game['commence_time'])
            for booky in game['sites']:
                site = booky['site_key']
                home_win = 1/booky['odds']['h2h'][home_index]*100
                away_win = 1/booky['odds']['h2h'][away_index]*100
                updated = datetime.datetime.fromtimestamp(booky['last_update'])
                csv.append([ sport, kick_off, home, away, home_win, away_win, site, updated])
                return csv

    def get_team_indices(teams, home_team):
        for index, team in enumerate(teams):
            if team == home_team:
                home = index
            else:
                away = index
        return home, away




DATA_SOURCES = (MirrorData, OddsAPIData,)


def get_normed_data(infile_stream):
    for src in DATA_SOURCES:
        try:
            infile_stream.seek(0)
            return src(infile_stream).normalize_data()
        except Exception:
            pass
    else:
        print('Didn\'t parse')
        return None
