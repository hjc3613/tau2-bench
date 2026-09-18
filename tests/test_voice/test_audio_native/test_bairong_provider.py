from tau2.config import (
    DEFAULT_BAIRONG_REALTIME_BASE_URL,
    DEFAULT_BAIRONG_REALTIME_MODEL,
)
from tau2.voice.audio_native.adapter import create_adapter
from tau2.voice.audio_native.bairong import BaiRongRealtimeProvider
from tau2.voice.audio_native.bairong.discrete_time_adapter import (
    DiscreteTimeBaiRongRealtimeAdapter,
)


def test_provider_defaults_to_local_service(monkeypatch):
    monkeypatch.delenv("BAIRONG_REALTIME_BASE_URL", raising=False)
    monkeypatch.delenv("BAIRONG_REALTIME_API_KEY", raising=False)
    monkeypatch.delenv("BAIRONG_REALTIME_MODEL", raising=False)

    provider = BaiRongRealtimeProvider()

    assert provider.base_url == DEFAULT_BAIRONG_REALTIME_BASE_URL
    assert provider.model == DEFAULT_BAIRONG_REALTIME_MODEL
    assert provider.api_key == "EMPTY"


def test_provider_environment_overrides(monkeypatch):
    monkeypatch.setenv("BAIRONG_REALTIME_BASE_URL", "wss://voice.example/realtime")
    monkeypatch.setenv("BAIRONG_REALTIME_API_KEY", "secret")
    monkeypatch.setenv("BAIRONG_REALTIME_MODEL", "production-model")

    provider = BaiRongRealtimeProvider()

    assert provider.base_url == "wss://voice.example/realtime"
    assert provider.api_key == "secret"
    assert provider.model == "production-model"


def test_factory_builds_bairong_adapter():
    adapter, model = create_adapter("BaiRong", tick_duration_ms=200)

    assert isinstance(adapter, DiscreteTimeBaiRongRealtimeAdapter)
    assert model == DEFAULT_BAIRONG_REALTIME_MODEL
    adapter.disconnect()
