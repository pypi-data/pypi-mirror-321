from datetime import datetime

import pandas as pd
from typing_extensions import Literal

from finter.backtest.v0.templates import MarketTemplates
from finter.data.data_handler.main import DataHandler


# Todo: Dividend
class Simulator:
    def __init__(
        self,
        market_type: Literal["kr_stock", "id_fund"],
        data_handler: DataHandler = None,
        **kwargs,
    ):
        self.data_handler = data_handler or DataHandler(
            start=20000101,
            end=int(datetime.now().strftime("%Y%m%d")),
            cache_timeout=300,
        )

        self.builder = MarketTemplates.create_simulator(market_type)
        if market_type == "kr_stock":
            self.builder.update_data(
                price=self.data_handler.kr_stock.price().dropna(how="all"),
            )
        elif market_type == "id_fund":
            self.builder.update_data(
                price=self.data_handler.id_fund.price().dropna(how="all"),
            )
        self.builder.update(**kwargs)

    def run(self, position: pd.DataFrame, **kwargs):
        self.builder.update(**kwargs)
        simulator = self.builder.build(position)
        simulator.run()
        return simulator


if __name__ == "__main__":
    from finter.data import ModelData

    position = ModelData.load("content.bareksa.ftp.price_volume.nav.1d")
    simulator = Simulator("id_fund")

    res = simulator.run(position, rebalancing_method="M", start=20230101, end=20230201)
    print(res.summary)
