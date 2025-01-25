from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Dict

from typing_extensions import Literal

from finter.backtest.v0.builder import SimulatorBuilder


@dataclass
class MarketConfig:
    initial_cash: float
    buy_fee_tax: float
    sell_fee_tax: float
    slippage: float
    core_type: Literal["basic", "id_fund"]
    adj_dividend: bool


class MarketType(Enum):
    KR_STOCK = "kr_stock"
    ID_FUND = "id_fund"


@dataclass
class MarketTemplates:
    # Class variable to store all market configurations
    CONFIGS: ClassVar[Dict[MarketType, MarketConfig]] = {
        MarketType.KR_STOCK: MarketConfig(
            initial_cash=100_000_000,  # 1억원
            buy_fee_tax=1.2,
            sell_fee_tax=31.2,
            slippage=10,
            core_type="basic",
            adj_dividend=False,
        ),
        MarketType.ID_FUND: MarketConfig(
            initial_cash=1_000_000_000,
            buy_fee_tax=40,
            sell_fee_tax=50,
            slippage=10,
            core_type="id_fund",
            adj_dividend=False,
        ),
    }

    @classmethod
    def create_simulator(
        cls,
        market_type: Literal["kr_stock", "id_fund"],
    ) -> SimulatorBuilder:
        # Convert string to MarketType
        try:
            market_enum = MarketType(market_type)
        except ValueError:
            raise ValueError(f"Unsupported market type: {market_type}")

        if market_enum not in cls.CONFIGS:
            raise ValueError(f"Unsupported market type: {market_enum}")

        config = cls.CONFIGS[market_enum]
        return (
            SimulatorBuilder()
            .update_cost(
                buy_fee_tax=config.buy_fee_tax,
                sell_fee_tax=config.sell_fee_tax,
                slippage=config.slippage,
            )
            .update_execution(
                initial_cash=config.initial_cash,
                core_type=config.core_type,
            )
        )
