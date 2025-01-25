from dataclasses import dataclass, fields
from enum import Enum
from typing import ClassVar, Dict, Literal, Union

from typing_extensions import Literal

from finter.backtest.v0.builder import SimulatorBuilder


@dataclass
class MarketConfig:
    initial_cash: float
    buy_fee_tax: float
    sell_fee_tax: float
    slippage: float
    dividend_tax: float

    core_type: Literal["basic", "id_fund"]
    adj_dividend: bool
    base_currency: Literal["KRW", "IDR"]


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
            dividend_tax=1540,
            core_type="basic",
            adj_dividend=False,
            base_currency="KRW",
        ),
        MarketType.ID_FUND: MarketConfig(
            initial_cash=1_000_000_000,
            buy_fee_tax=40,
            sell_fee_tax=50,
            slippage=10,
            dividend_tax=0,
            core_type="id_fund",
            adj_dividend=False,
            base_currency="IDR",
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
                dividend_tax=config.dividend_tax,
            )
            .update_execution(
                initial_cash=config.initial_cash,
                core_type=config.core_type,
            )
        )

    @classmethod
    def get_config_value(
        cls,
        market_type: Literal["kr_stock", "id_fund"],
        config_key: str,  # type hint를 직접 지정하는 대신 실제 필드에서 가져옴
    ) -> Union[float, bool, Literal["basic", "id_fund"], Literal["KRW", "IDR"]]:
        # Validate config_key
        valid_keys = {field.name for field in fields(MarketConfig)}
        if config_key not in valid_keys:
            raise ValueError(
                f"Invalid config key: {config_key}. "
                f"Valid keys are: {', '.join(valid_keys)}"
            )

        try:
            market_enum = MarketType(market_type)
        except ValueError:
            raise ValueError(f"Unsupported market type: {market_type}")

        if market_enum not in cls.CONFIGS:
            raise ValueError(f"Unsupported market type: {market_enum}")

        return getattr(cls.CONFIGS[market_enum], config_key)
