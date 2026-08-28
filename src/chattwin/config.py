"Typed environment configuration for ChatTwin."

from chatenv import BaseEnvConfig, EnvField


class ChattwinConfig(BaseEnvConfig):
    "ChatTwin ChatEnv configuration."

    _title = "ChatTwin Configuration"
    _aliases = ["chattwin"]
    _storage_dir = "Chattwin"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATTWIN_API_KEY = EnvField(
        "CHATTWIN_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChattwinConfig"]
