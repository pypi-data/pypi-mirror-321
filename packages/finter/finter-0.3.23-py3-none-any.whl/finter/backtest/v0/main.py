from datetime import datetime
from typing import Optional, cast

import pandas as pd
from typing_extensions import Literal, TypedDict, Unpack

from finter.backtest.v0.templates import MarketTemplates
from finter.data.data_handler.main import DataHandler


# Todo: Dividend, Cuerrency
class SimulatorConfig(TypedDict, total=False):
    start: int
    end: int

    buy_fee_tax: float
    sell_fee_tax: float
    slippage: float

    initial_cash: float
    resample_period: Literal[None, "W", "M", "Q"]
    rebalancing_method: Literal["auto", "W", "M", "Q", "by_position"]
    volume_capacity_ratio: float
    core_type: Literal["basic", "id_fund"]

    debug: bool


class Simulator:
    def __init__(
        self,
        market_type: Literal["kr_stock", "id_fund"],
        data_handler: Optional[DataHandler] = None,
        **kwargs,
    ):
        self.market_type = market_type
        self.builder = MarketTemplates.create_simulator(
            cast(Literal["kr_stock", "id_fund"], self.market_type)
        )
        self.set_market_builder(data_handler)
        self.builder.update(**kwargs)

    def set_market_builder(self, data_handler: Optional[DataHandler] = None):
        self.data_handler = data_handler or DataHandler(
            start=20000101,
            end=int(datetime.now().strftime("%Y%m%d")),
            cache_timeout=300,
        )

        if self.market_type == "kr_stock":
            self.builder.update_data(
                price=self.data_handler.kr_stock.price().dropna(how="all"),
            )
        elif self.market_type == "id_fund":
            self.builder.update_data(
                price=self.data_handler.id_fund.price().dropna(how="all"),
            )

    def run(self, position: pd.DataFrame, **kwargs: Unpack[SimulatorConfig]):
        self.builder.update(**kwargs)
        simulator = self.builder.build(position)
        simulator.run()
        return simulator


if __name__ == "__main__":
    from finter.data import ModelData

    position = ModelData.load("content.bareksa.ftp.price_volume.nav.1d")
    simulator = Simulator("id_fund")

    res = simulator.run(
        position,
        start=20210101,
    )
    res.summary
