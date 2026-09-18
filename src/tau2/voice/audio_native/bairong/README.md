# BaiRong Voice Realtime provider

`br` reuses tau2's OpenAI Realtime event and tick implementation and connects
it to BaiRong's OpenAI-Realtime-compatible voice service.

The default endpoint is the local development server:

```text
ws://127.0.0.1:8765/v1/realtime
```

Configure a local or future public deployment without changing tau2 code:

```bash
export BAIRONG_REALTIME_BASE_URL=wss://voice.example.com/v1/realtime
export BAIRONG_REALTIME_API_KEY=...
export BAIRONG_REALTIME_MODEL=BaiRong-Voice-Realtime
```

Run a tau-voice evaluation with:

```bash
tau2 run --domain retail --audio-native \
  --audio-native-provider BaiRong \
  --audio-native-model BaiRong-Voice-Realtime \
  --num-tasks 1 --verbose-logs
```

The endpoint must implement the subset used by tau2's OpenAI provider:
`session.created`, `session.updated`, `input_audio_buffer.append`, response
audio deltas, response transcripts, speech-started events, response completion,
and function-call argument events.
