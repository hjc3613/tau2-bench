"""BaiRong OpenAI-Realtime-compatible WebSocket provider.

The protocol implementation is inherited from the OpenAI provider. Only the
endpoint, credential, and default model are provider-specific, so the same
event parser and interruption/tool-call behavior are exercised by tau-voice.

Environment variables:
    BAIRONG_REALTIME_BASE_URL: WebSocket endpoint. Defaults to the local service.
    BAIRONG_REALTIME_API_KEY: Bearer token. Defaults to ``EMPTY`` for local use.
    BAIRONG_REALTIME_MODEL: Model query parameter. Defaults to ``BaiRong-Voice-Realtime``.
"""

from __future__ import annotations

import os
from typing import Optional

import websockets

from tau2.config import (
    DEFAULT_BAIRONG_REALTIME_API_KEY,
    DEFAULT_BAIRONG_REALTIME_BASE_URL,
    DEFAULT_BAIRONG_REALTIME_MODEL,
)
from tau2.data_model.audio import TELEPHONY_AUDIO_FORMAT, AudioFormat
from tau2.voice.audio_native.openai.provider import (
    OpenAIRealtimeProvider,
    OpenAIVADConfig,
)


class BaiRongRealtimeProvider(OpenAIRealtimeProvider):
    """OpenAI-Realtime-compatible client for BaiRong's voice service."""

    BASE_URL = DEFAULT_BAIRONG_REALTIME_BASE_URL
    DEFAULT_MODEL = DEFAULT_BAIRONG_REALTIME_MODEL

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        reasoning_effort: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        self.model = model or os.getenv("BAIRONG_REALTIME_MODEL", self.DEFAULT_MODEL)
        self.base_url = base_url or os.getenv(
            "BAIRONG_REALTIME_BASE_URL", self.BASE_URL
        )
        self.api_key = api_key or os.getenv(
            "BAIRONG_REALTIME_API_KEY", DEFAULT_BAIRONG_REALTIME_API_KEY
        )
        self.reasoning_effort = reasoning_effort
        self.ws: Optional[websockets.WebSocketClientProtocol] = None
        self._current_vad_config: Optional[OpenAIVADConfig] = None
        self._audio_format: AudioFormat = TELEPHONY_AUDIO_FORMAT
        self.session_id: Optional[str] = None


__all__ = [
    "BaiRongRealtimeProvider",
    "DEFAULT_BAIRONG_REALTIME_API_KEY",
    "DEFAULT_BAIRONG_REALTIME_BASE_URL",
    "DEFAULT_BAIRONG_REALTIME_MODEL",
]
