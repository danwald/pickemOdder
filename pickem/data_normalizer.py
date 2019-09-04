from abc import ABC, abstractmethod
import json


class DataNormalizer(ABC):
    @abstractmethod
    def normalize_data(self):
        pass


class MirrorData(DataNormalizer):
    def __init__(self, infile_stream):
        self.infile_stream = infile_stream
        self.data = None

    def normalize_data(self):
        if not self.data:
            data = json.loads(self.infile_stream)
        return data


class OddsAPIData(MirrorData):
    # Uses stats from https://the-odds-api.com/
    pass


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
