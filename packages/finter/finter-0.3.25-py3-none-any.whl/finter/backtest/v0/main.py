from datetime import datetime
from typing import cast

import pandas as pd
from typing_extensions import Literal, TypedDict, Unpack

from finter.backtest.v0.templates import MarketTemplates
from finter.data.data_handler.main import DataHandler


class SimulatorConfig(TypedDict, total=False):
    start: int
    end: int

    buy_fee_tax: float
    sell_fee_tax: float
    slippage: float
    dividend_tax: float

    initial_cash: float
    resample_period: Literal[None, "W", "M", "Q"]
    rebalancing_method: Literal["auto", "W", "M", "Q", "by_position"]
    volume_capacity_ratio: float
    core_type: Literal["basic", "id_fund"]

    debug: bool

    drip: Literal[None, "cash", "reinvest"]
    currency: Literal["USD", "KRW"]


class Simulator:
    _data_handler_instance = None

    @classmethod
    def _get_cached_data_handler(cls, **kwargs):
        if cls._data_handler_instance is None:
            cls._data_handler_instance = DataHandler(**kwargs)
        return cls._data_handler_instance

    def __init__(
        self,
        market_type: Literal["kr_stock", "id_fund", "us_stock", "us_etf"],
    ):
        self.data_handler = self._get_cached_data_handler(
            start=20000101,
            end=int(datetime.now().strftime("%Y%m%d")),
            cache_timeout=300,
        )
        self.market_type = market_type

        self.builder = MarketTemplates.create_simulator(
            cast(Literal["kr_stock", "id_fund", "us_stock", "us_etf"], self.market_type)
        )
        self.set_market_builder()

    def set_market_builder(self):
        price = self.data_handler.universe(self.market_type).price().dropna(how="all")
        if self.market_type in ("us_stock", "us_etf"):
            price = price.ffill()
        self.builder.update_data(price=price)

    def post_init(self):
        if self.use_drip:
            self.builder.update_data(
                dividend_ratio=self.data_handler.universe(self.market_type)
                .dividend_factor()
                .dropna(how="all"),
            )

        if self.use_currency:
            base_currency = MarketTemplates.get_config_value(
                cast(Literal["kr_stock", "id_fund"], self.market_type), "base_currency"
            )
            if base_currency != self.use_currency:
                currency_pair = f"{base_currency}{self.use_currency}"
                inverse_pair = f"{self.use_currency}{base_currency}"

                currency_data = self.data_handler.common.currency()
                if currency_pair in currency_data.columns:
                    exchange_rate = currency_data[[currency_pair]].dropna()
                elif inverse_pair in currency_data.columns:
                    exchange_rate = (1 / currency_data[[inverse_pair]]).dropna()
                else:
                    raise ValueError(
                        f"No exchange rate found for conversion from {base_currency} to {self.use_currency}"
                    )
            else:
                return

            if exchange_rate is not None:
                self.builder.update_data(
                    exchange_rate=exchange_rate,
                )
            else:
                raise ValueError(f"Unsupported currency: {self.use_currency}")

    def run(self, position: pd.DataFrame, **kwargs: Unpack[SimulatorConfig]):
        self.use_currency = kwargs.pop("currency", None)
        self.use_drip = kwargs.get("drip", None)
        self.post_init()

        self.builder.update(**kwargs)
        simulator = self.builder.build(position)
        simulator.run()
        return simulator


if __name__ == "__main__":
    from finter.data import ModelData
    from finter.data.data_handler.main import DataHandler

    position = ModelData.load("alpha.krx.krx.stock.ldh0127.div_new_1")
    simulator = Simulator("kr_stock")

    res = simulator.run(
        position,
        drip="reinvest",
    )
    res.summary

    res.summary.dividend.sum()

    # from finter.backtest.main import Simulator as ss

    # s = ss(20000101, 20250115)
    # res = s.run("kr_stock", position=position)
    # res.summary
