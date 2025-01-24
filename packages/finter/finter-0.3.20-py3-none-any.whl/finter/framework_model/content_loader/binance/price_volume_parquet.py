from finter.framework_model.content import Loader
import pandas as pd
from finter.settings import logger
import gc
from finter.rest import ApiException

def to_end(dt):
    if dt.minute != 0:
        end_dt = dt.replace(second=59, microsecond=999999)
    elif dt.hour != 0:
        end_dt = dt.replace(minute=59, second=59, microsecond=999999)
    else:
        end_dt = dt.replace(hour=23, minute=59, second=59, microsecond=999999)
    return end_dt

class BinancePriceVolumeLoader(Loader):   
    def __init__(self, cm_name):
        self.__CM_NAME = cm_name
        self.__FREQ = cm_name.split(".")[-1]

    def get_df(self, start: int, end: int, fill_nan=True, columns=None, *args, **kwargs):
        start_dt = pd.to_datetime(str(start))
        end_dt = pd.to_datetime(str(end))
        cm_name = self.__CM_NAME
        
        # single cm
        if start_dt.year == end_dt.year:
            raw = self._load_cache(
                cm_name,
                start,
                end,
                universe="binance-all-spot",
                freq=self.__FREQ,
                fill_nan=fill_nan,
                columns=columns,
                *args,
                **kwargs
            )

        # Over 1 year; needs columns params
        elif bool(columns):
            raw = self._load_cache(
                cm_name,
                start,
                end,
                universe="binance-all-spot",
                freq=self.__FREQ,
                fill_nan=fill_nan,
                columns=columns,
                *args,
                **kwargs
            )
        else:
            raise "Requesting data for more than one year not supported"

        return raw.loc[start_dt:to_end(end_dt)].dropna(how="all")
