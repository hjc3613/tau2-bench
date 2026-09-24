from tau2.config import (
    DEFAULT_BAIRONG_REALTIME_BASE_URL,
    DEFAULT_BAIRONG_REALTIME_MODEL,
)
from tau2.voice.audio_native.adapter import create_adapter
from tau2.voice.audio_native.bairong import BaiRongRealtimeProvider
from tau2.voice.audio_native.bairong.discrete_time_adapter import (
    DiscreteTimeBaiRongRealtimeAdapter,
)


def test_provider_uses_hosted_service_without_credentials(monkeypatch):
    monkeypatch.setenv("BAIRONG_REALTIME_BASE_URL", "ws://127.0.0.1:8765")
    monkeypatch.setenv("BAIRONG_REALTIME_API_KEY", "should-not-be-used")

    provider = BaiRongRealtimeProvider()

    assert provider.base_url == DEFAULT_BAIRONG_REALTIME_BASE_URL
    assert provider.model == DEFAULT_BAIRONG_REALTIME_MODEL
    assert provider.api_key == "EMPTY"
    assert provider.base_url.startswith("wss://")


def test_factory_builds_bairong_adapter():
    adapter, model = create_adapter("bairong", tick_duration_ms=200)

    assert isinstance(adapter, DiscreteTimeBaiRongRealtimeAdapter)
    assert model == DEFAULT_BAIRONG_REALTIME_MODEL
    adapter.disconnect()
