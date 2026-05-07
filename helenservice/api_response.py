from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SpotPriceChartSeries:
    start: str
    stop: str
    electricity: float | None = None
    electricity_spot_prices_vat: float | None = None
    electricity_spot_prices: float | None = None
    electricity_spot_prices_hour_average_vat: float | None = None
    electricity_spot_prices_hour_average: float | None = None

    def __init__(
        self,
        start: str,
        stop: str,
        electricity: float | None = None,
        electricity_spot_prices_vat: float | None = None,
        electricity_spot_prices: float | None = None,
        electricity_spot_prices_hour_average_vat: float | None = None,
        electricity_spot_prices_hour_average: float | None = None,
        **_: Any,
    ):
        self.start = start
        self.stop = stop
        self.electricity = electricity
        self.electricity_spot_prices_vat = electricity_spot_prices_vat
        self.electricity_spot_prices = electricity_spot_prices
        self.electricity_spot_prices_hour_average_vat = electricity_spot_prices_hour_average_vat
        self.electricity_spot_prices_hour_average = electricity_spot_prices_hour_average


@dataclass
class SpotPriceChartResponse:
    start: str
    stop: str
    resolution: str
    units: dict[str, Any]
    ids: dict[str, Any]
    data_start_times: dict[str, Any]
    data_stop_times: dict[str, Any]
    series: list[SpotPriceChartSeries] = field(default_factory=list)
    missing_series: list[Any] = field(default_factory=list)

    def __init__(
        self,
        start: str,
        stop: str,
        resolution: str,
        units: dict[str, Any],
        ids: dict[str, Any],
        data_start_times: dict[str, Any],
        data_stop_times: dict[str, Any],
        series: list[dict[str, Any]] | None = None,
        missing_series: list[Any] | None = None,
        **_: Any,
    ):
        self.start = start
        self.stop = stop
        self.resolution = resolution
        self.units = units
        self.ids = ids
        self.data_start_times = data_start_times
        self.data_stop_times = data_stop_times
        self.series = [SpotPriceChartSeries(**s) for s in (series or [])]
        self.missing_series = missing_series if missing_series is not None else []


@dataclass
class MeasurementsWithSpotPriceSeries:
    start: str
    stop: str
    electricity: float | None = None
    electricity_spot_prices_vat: float | None = None
    electricity_spot_prices: float | None = None
    ambient_temperature: float | None = None
    ambient_humidity: float | None = None

    def __init__(
        self,
        start: str,
        stop: str,
        electricity: float | None = None,
        electricity_spot_prices_vat: float | None = None,
        electricity_spot_prices: float | None = None,
        ambient_temperature: float | None = None,
        ambient_humidity: float | None = None,
        **_: Any,
    ):
        self.start = start
        self.stop = stop
        self.electricity = electricity
        self.electricity_spot_prices_vat = electricity_spot_prices_vat
        self.electricity_spot_prices = electricity_spot_prices
        self.ambient_temperature = ambient_temperature
        self.ambient_humidity = ambient_humidity


@dataclass
class MeasurementsWithSpotPriceResponse:
    start: str
    stop: str
    resolution: str
    units: dict[str, Any]
    ids: dict[str, Any]
    data_start_times: dict[str, Any]
    data_stop_times: dict[str, Any]
    series: list[MeasurementsWithSpotPriceSeries] = field(default_factory=list)
    missing_series: list[Any] = field(default_factory=list)

    def __init__(
        self,
        start: str,
        stop: str,
        resolution: str,
        units: dict[str, Any],
        ids: dict[str, Any],
        data_start_times: dict[str, Any],
        data_stop_times: dict[str, Any],
        series: list[dict[str, Any]] | None = None,
        missing_series: list[Any] | None = None,
        **_: Any,
    ):
        self.start = start
        self.stop = stop
        self.resolution = resolution
        self.units = units
        self.ids = ids
        self.data_start_times = data_start_times
        self.data_stop_times = data_stop_times
        self.series = [MeasurementsWithSpotPriceSeries(**s) for s in (series or [])]
        self.missing_series = missing_series if missing_series is not None else []
