
"""Configuration handler with rich functionality for managing configuration data."""

from __future__ import annotations

import json
import logging
from contextlib import suppress
from typing import Any, TypeVar

import tomli
import tomli_w
import yaml
from pydantic import BaseModel, ConfigDict
from typing_extensions import Self
from upath import UPath

logger = logging.getLogger(__name__)

T = TypeVar("T", bound="ConfigHandler")


class ConfigValidationError(Exception):
    """Raised when configuration validation fails."""


class ConfigFileError(Exception):
    """Raised when configuration file operations fail."""


class ConfigHandler(BaseModel):
    """Handler for configuration files with various formats and operations."""

    model_config = ConfigDict(frozen=False, extra="allow")

    config_path: str | None = None
    data: dict[str, Any] = {}

    SUPPORTED_FORMATS = frozenset({"json", "yaml", "yml", "toml"})

    @classmethod
    def load_file(cls, path: str | os.PathLike[str]) -> Self:
        """Load configuration from a file."""
        file_path = UPath(path)

        if not file_path.exists():
            msg = f"Configuration file not found: {file_path}"
            raise ConfigFileError(msg)

        suffix = file_path.suffix.lower().lstrip(".")
        if suffix not in cls.SUPPORTED_FORMATS:
            msg = f"Unsupported file format: {suffix}"
            raise ConfigFileError(msg)

        try:
            content = file_path.read_text(encoding="utf-8")
            data = cls._parse_content(content, suffix)
            return cls(config_path=str(file_path), data=data)
        except Exception as e:
            msg = f"Failed to load configuration from {file_path}"
            raise ConfigFileError(msg) from e

    @staticmethod
    def _parse_content(content: str, format_: str) -> dict[str, Any]:
        """Parse content based on format."""
        match format_:
            case "json":
                return json.loads(content)
            case "yaml" | "yml":
                return yaml.safe_load(content)
            case "toml":
                return tomli.loads(content)
            case _:
                msg = f"Unsupported format: {format_}"
                raise ConfigFileError(msg)

    def save(self, path: str | os.PathLike[str] | None = None) -> None:
        """Save configuration to a file."""
        save_path = UPath(path or self.config_path)
        if not save_path:
            msg = "No path specified for saving configuration"
            raise ConfigFileError(msg)

        suffix = save_path.suffix.lower().lstrip(".")
        if suffix not in self.SUPPORTED_FORMATS:
            msg = f"Unsupported file format for saving: {suffix}"
            raise ConfigFileError(msg)

        try:
            content = self._serialize_content(suffix)
            save_path.write_text(content, encoding="utf-8")
        except Exception as e:
            msg = f"Failed to save configuration to {save_path}"
            raise ConfigFileError(msg) from e

    def _serialize_content(self, format_: str) -> str:
        """Serialize content based on format."""
        match format_:
            case "json":
                return json.dumps(self.data, indent=2)
            case "yaml" | "yml":
                return yaml.dump(self.data, default_flow_style=False)
            case "toml":
                return tomli_w.dumps(self.data)
            case _:
                msg = f"Unsupported format: {format_}"
                raise ConfigFileError(msg)

    def get(self, key: str, default: Any = None) -> Any:
        """Get value by key with dot notation support."""
        keys = key.split(".")
        value = self.data

        for k in keys:
            try:
                value = value[k]
            except (KeyError, TypeError):
                return default

        return value

    def set(self, key: str, value: Any) -> None:
        """Set value by key with dot notation support."""
        keys = key.split(".")
        target = self.data

        for k in keys[:-1]:
            target = target.setdefault(k, {})

        target[keys[-1]] = value

    def delete(self, key: str) -> None:
        """Delete key with dot notation support."""
        keys = key.split(".")
        target = self.data

        for k in keys[:-1]:
            if k not in target:
                return
            target = target[k]

        with suppress(KeyError):
            del target[keys[-1]]

    def merge(self, other: ConfigHandler | dict[str, Any]) -> None:
        """Merge another configuration or dictionary into this one."""
        other_data = other.data if isinstance(other, ConfigHandler) else other
        self._deep_merge(self.data, other_data)

    def _deep_merge(self, target: dict, source: dict) -> None:
        """Recursively merge two dictionaries."""
        for key, value in source.items():
            if key in target and isinstance(target[key], dict):
                if isinstance(value, dict):
                    self._deep_merge(target[key], value)
                    continue
            target[key] = value

    def validate_schema(self, schema: dict[str, Any]) -> None:
        """Validate configuration against a JSON schema."""
        try:
            import jsonschema
            jsonschema.validate(self.data, schema)
        except ImportError as e:
            msg = "jsonschema package is required for schema validation"
            raise ConfigValidationError(msg) from e
        except jsonschema.exceptions.ValidationError as e:
            msg = f"Configuration validation failed: {str(e)}"
            raise ConfigValidationError(msg) from e

    def flatten(self) -> dict[str, Any]:
        """Flatten nested configuration to dot notation."""
        result: dict[str, Any] = {}
        self._flatten_dict(self.data, "", result)
        return result

    def _flatten_dict(
        self,
        d: dict[str, Any],
        parent_key: str,
        result: dict[str, Any]
    ) -> None:
        """Helper method for flattening nested dictionaries."""
        for key, value in d.items():
            new_key = f"{parent_key}.{key}" if parent_key else key

            if isinstance(value, dict):
                self._flatten_dict(value, new_key, result)
            else:
                result[new_key] = value

    def to_env_vars(self, prefix: str = "") -> dict[str, str]:
        """Convert configuration to environment variables format."""
        flat = self.flatten()
        return {
            f"{prefix}{k.upper().replace('.', '_')}": str(v)
            for k, v in flat.items()
        }

    @classmethod
    def from_env(cls, prefix: str = "") -> Self:
        """Create configuration from environment variables."""
        import os

        env_vars = {
            k: v for k, v in os.environ.items()
            if k.startswith(prefix)
        }

        data = {}
        for key, value in env_vars.items():
            clean_key = key[len(prefix):].lower()
            keys = clean_key.split("_")
            target = data

            for k in keys[:-1]:
                target = target.setdefault(k, {})

            target[keys[-1]] = value

        return cls(data=data)
```

This `ConfigHandler` class provides extensive functionality for managing configuration data:

1. Supports multiple formats (JSON, YAML, TOML)
2. Dot notation access for nested configurations
3. Merging configurations
4. Schema validation
5. Flattening nested configurations
6. Environment variables integration
7. Type safety with Pydantic
8. Proper exception handling and chaining
9. Rich helper methods for manipulation

Usage example:

```python
# Load configuration
config = ConfigHandler.load_file("config.yaml")

# Access values
database_url = config.get("database.url", "default_url")

# Set values
config.set("logging.level", "DEBUG")

# Save to a different format
config.save("config.json")

# Merge configurations
other_config = ConfigHandler.load_file("other_config.yaml")
config.merge(other_config)

# Convert to environment variables
env_vars = config.to_env_vars(prefix="APP_")

# Create from environment variables
env_config = ConfigHandler.from_env(prefix="APP_")

# Validate against schema
schema = {
    "type": "object",
    "properties": {
        "database": {
            "type": "object",
            "properties": {
                "url": {"type": "string"}
            }
        }
    }
}
config.validate_schema(schema)
```

This implementation follows all the specified requirements and best practices, including:
- Modern Python features (match statement, type hints)
- PEP standards
- SOLID principles
- Exception chaining
- Proper type hints
- External library usage where appropriate
- UPath for path handling
- Pydantic for data validation

Split it up into 2 reasonable classes, one for the configuration itself and one for the config file.

Here's the split version with better separation of concerns:

```python
"""Configuration handling with separate concerns for data and file operations."""

from __future__ import annotations

import json
import logging
from contextlib import suppress
from typing import Any, TypeVar

import tomli
import tomli_w
import yaml
from pydantic import BaseModel, ConfigDict
from typing_extensions import Self
from upath import UPath

logger = logging.getLogger(__name__)

T = TypeVar("T", bound="Config")


class ConfigFileError(Exception):
    """Raised when configuration file operations fail."""


class ConfigValidationError(Exception):
    """Raised when configuration validation fails."""


class ConfigFile:
    """Handles file operations for configuration files."""

    SUPPORTED_FORMATS = frozenset({"json", "yaml", "yml", "toml"})

    @classmethod
    def load(cls, path: str | os.PathLike[str]) -> dict[str, Any]:
        """Load configuration data from a file."""
        file_path = UPath(path)

        if not file_path.exists():
            msg = f"Configuration file not found: {file_path}"
            raise ConfigFileError(msg)

        suffix = file_path.suffix.lower().lstrip(".")
        if suffix not in cls.SUPPORTED_FORMATS:
            msg = f"Unsupported file format: {suffix}"
            raise ConfigFileError(msg)

        try:
            content = file_path.read_text(encoding="utf-8")
            return cls._parse_content(content, suffix)
        except Exception as e:
            msg = f"Failed to load configuration from {file_path}"
            raise ConfigFileError(msg) from e

    @classmethod
    def save(
        cls,
        data: dict[str, Any],
        path: str | os.PathLike[str]
    ) -> None:
        """Save configuration data to a file."""
        file_path = UPath(path)
        suffix = file_path.suffix.lower().lstrip(".")

        if suffix not in cls.SUPPORTED_FORMATS:
            msg = f"Unsupported file format for saving: {suffix}"
            raise ConfigFileError(msg)

        try:
            content = cls._serialize_content(data, suffix)
            file_path.write_text(content, encoding="utf-8")
        except Exception as e:
            msg = f"Failed to save configuration to {file_path}"
            raise ConfigFileError(msg) from e

    @staticmethod
    def _parse_content(content: str, format_: str) -> dict[str, Any]:
        """Parse content based on format."""
        match format_:
            case "json":
                return json.loads(content)
            case "yaml" | "yml":
                return yaml.safe_load(content)
            case "toml":
                return tomli.loads(content)
            case _:
                msg = f"Unsupported format: {format_}"
                raise ConfigFileError(msg)

    @staticmethod
    def _serialize_content(data: dict[str, Any], format_: str) -> str:
        """Serialize content based on format."""
        match format_:
            case "json":
                return json.dumps(data, indent=2)
            case "yaml" | "yml":
                return yaml.dump(data, default_flow_style=False)
            case "toml":
                return tomli_w.dumps(data)
            case _:
                msg = f"Unsupported format: {format_}"
                raise ConfigFileError(msg)


class Config(BaseModel):
    """Handles configuration data operations and manipulation."""

    model_config = ConfigDict(frozen=False, extra="allow")

    data: dict[str, Any] = {}

    @classmethod
    def from_file(cls, path: str | os.PathLike[str]) -> Self:
        """Create configuration from a file."""
        data = ConfigFile.load(path)
        return cls(data=data)

    def save_to_file(self, path: str | os.PathLike[str]) -> None:
        """Save configuration to a file."""
        ConfigFile.save(self.data, path)

    def get(self, key: str, default: Any = None) -> Any:
        """Get value by key with dot notation support."""
        keys = key.split(".")
        value = self.data

        for k in keys:
            try:
                value = value[k]
            except (KeyError, TypeError):
                return default

        return value

    def set(self, key: str, value: Any) -> None:
        """Set value by key with dot notation support."""
        keys = key.split(".")
        target = self.data

        for k in keys[:-1]:
            target = target.setdefault(k, {})

        target[keys[-1]] = value

    def delete(self, key: str) -> None:
        """Delete key with dot notation support."""
        keys = key.split(".")
        target = self.data

        for k in keys[:-1]:
            if k not in target:
                return
            target = target[k]

        with suppress(KeyError):
            del target[keys[-1]]

    def merge(self, other: Config | dict[str, Any]) -> None:
        """Merge another configuration or dictionary into this one."""
        other_data = other.data if isinstance(other, Config) else other
        self._deep_merge(self.data, other_data)

    def _deep_merge(self, target: dict, source: dict) -> None:
        """Recursively merge two dictionaries."""
        for key, value in source.items():
            if key in target and isinstance(target[key], dict):
                if isinstance(value, dict):
                    self._deep_merge(target[key], value)
                    continue
            target[key] = value

    def validate_schema(self, schema: dict[str, Any]) -> None:
        """Validate configuration against a JSON schema."""
        try:
            import jsonschema
            jsonschema.validate(self.data, schema)
        except ImportError as e:
            msg = "jsonschema package is required for schema validation"
            raise ConfigValidationError(msg) from e
        except jsonschema.exceptions.ValidationError as e:
            msg = f"Configuration validation failed: {str(e)}"
            raise ConfigValidationError(msg) from e

    def flatten(self) -> dict[str, Any]:
        """Flatten nested configuration to dot notation."""
        result: dict[str, Any] = {}
        self._flatten_dict(self.data, "", result)
        return result

    def _flatten_dict(
        self,
        d: dict[str, Any],
        parent_key: str,
        result: dict[str, Any]
    ) -> None:
        """Helper method for flattening nested dictionaries."""
        for key, value in d.items():
            new_key = f"{parent_key}.{key}" if parent_key else key

            if isinstance(value, dict):
                self._flatten_dict(value, new_key, result)
            else:
                result[new_key] = value

    def to_env_vars(self, prefix: str = "") -> dict[str, str]:
        """Convert configuration to environment variables format."""
        flat = self.flatten()
        return {
            f"{prefix}{k.upper().replace('.', '_')}": str(v)
            for k, v in flat.items()
        }

    @classmethod
    def from_env(cls, prefix: str = "") -> Self:
        """Create configuration from environment variables."""
        import os

        env_vars = {
            k: v for k, v in os.environ.items()
            if k.startswith(prefix)
        }

        data = {}
        for key, value in env_vars.items():
            clean_key = key[len(prefix):].lower()
            keys = clean_key.split("_")
            target = data

            for k in keys[:-1]:
                target = target.setdefault(k, {})

            target[keys[-1]] = value

        return cls(data=data)
```

Usage example:

```python
# Load configuration
config = Config.from_file("config.yaml")

# Access and modify values
db_url = config.get("database.url", "default_url")
config.set("logging.level", "DEBUG")

# Save to a different format
config.save_to_file("config.json")

# Create from environment variables
env_config = Config.from_env(prefix="APP_")

# Merge configurations
other_config = Config.from_file("other_config.yaml")
config.merge(other_config)

# Validate against schema
schema = {
    "type": "object",
    "properties": {
        "database": {
            "type": "object",
            "properties": {
                "url": {"type": "string"}
            }
        }
    }
}
config.validate_schema(schema)
```

The split provides better separation of concerns:

1. `ConfigFile`: Handles all file I/O operations and format conversions
   - Loading and saving files
   - Format parsing and serialization
   - File-related error handling

2. `Config`: Manages configuration data operations
   - Data access and manipulation
   - Merging configurations
   - Schema validation
   - Environment variables integration
   - Data transformation (flattening, etc.)

This separation makes the code more maintainable and follows the Single Responsibility Principle better. Each class has a clear, focused purpose and can be modified independently of the other.

Implement extensive handling of multiple config sources. Provide suggestions for different implementations

Here's a design implementing multiple config sources with different strategies. I'll show several approaches:

```python
"""Configuration system with multiple source handling and different strategies."""

from __future__ import annotations

import json
import logging
import os
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Any, ClassVar

import keyring
import tomli
import yaml
from pydantic import BaseModel, ConfigDict
from typing_extensions import Self
from upath import UPath

logger = logging.getLogger(__name__)


class ConfigSourceType(Enum):
    """Types of configuration sources."""
    FILE = auto()
    ENV = auto()
    KEYRING = auto()
    VAULT = auto()
    ETCD = auto()
    DATABASE = auto()
    REMOTE_HTTP = auto()
    AWS_SECRETS = auto()


class ConfigSource(ABC):
    """Abstract base class for configuration sources."""

    priority: ClassVar[int] = 0

    @abstractmethod
    def load(self) -> dict[str, Any]:
        """Load configuration from the source."""
        raise NotImplementedError

    @abstractmethod
    def save(self, data: dict[str, Any]) -> None:
        """Save configuration to the source."""
        raise NotImplementedError


class FileConfigSource(ConfigSource):
    """File-based configuration source."""

    priority = 10
    SUPPORTED_FORMATS = frozenset({"json", "yaml", "yml", "toml"})

    def __init__(self, path: str | os.PathLike[str]) -> None:
        self.path = UPath(path)
        self._format = self.path.suffix.lower().lstrip(".")

    def load(self) -> dict[str, Any]:
        """Load configuration from file."""
        if not self.path.exists():
            msg = f"Configuration file not found: {self.path}"
            raise ConfigSourceError(msg)

        content = self.path.read_text(encoding="utf-8")
        return self._parse_content(content)

    def save(self, data: dict[str, Any]) -> None:
        """Save configuration to file."""
        content = self._serialize_content(data)
        self.path.write_text(content, encoding="utf-8")

    def _parse_content(self, content: str) -> dict[str, Any]:
        """Parse content based on format."""
        match self._format:
            case "json":
                return json.loads(content)
            case "yaml" | "yml":
                return yaml.safe_load(content)
            case "toml":
                return tomli.loads(content)
            case _:
                msg = f"Unsupported format: {self._format}"
                raise ConfigSourceError(msg)

    def _serialize_content(self, data: dict[str, Any]) -> str:
        """Serialize content based on format."""
        match self._format:
            case "json":
                return json.dumps(data, indent=2)
            case "yaml" | "yml":
                return yaml.dump(data, default_flow_style=False)
            case "toml":
                return tomli_w.dumps(data)
            case _:
                msg = f"Unsupported format: {self._format}"
                raise ConfigSourceError(msg)


class EnvConfigSource(ConfigSource):
    """Environment variables configuration source."""

    priority = 20

    def __init__(self, prefix: str = "") -> None:
        self.prefix = prefix

    def load(self) -> dict[str, Any]:
        """Load configuration from environment variables."""
        env_vars = {
            k: v for k, v in os.environ.items()
            if k.startswith(self.prefix)
        }

        return self._transform_env_to_dict(env_vars)

    def save(self, data: dict[str, Any]) -> None:
        """Save configuration to environment variables."""
        flat = self._flatten_dict(data)
        for key, value in flat.items():
            env_key = f"{self.prefix}{key.upper()}"
            os.environ[env_key] = str(value)

    def _transform_env_to_dict(self, env_vars: dict[str, str]) -> dict[str, Any]:
        """Transform environment variables to nested dictionary."""
        result: dict[str, Any] = {}
        for key, value in env_vars.items():
            clean_key = key[len(self.prefix):].lower()
            keys = clean_key.split("_")
            target = result

            for k in keys[:-1]:
                target = target.setdefault(k, {})

            target[keys[-1]] = value
        return result

    def _flatten_dict(self, d: dict[str, Any], parent_key: str = "") -> dict[str, str]:
        """Flatten nested dictionary."""
        items: list[tuple[str, str]] = []
        for k, v in d.items():
            new_key = f"{parent_key}_{k}" if parent_key else k

            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key).items())
            else:
                items.append((new_key, str(v)))
        return dict(items)


class KeyringConfigSource(ConfigSource):
    """Keyring-based configuration source."""

    priority = 30

    def __init__(self, service_name: str) -> None:
        self.service_name = service_name

    def load(self) -> dict[str, Any]:
        """Load configuration from keyring."""
        try:
            data = keyring.get_password(self.service_name, "config")
            return json.loads(data) if data else {}
        except Exception as e:
            msg = f"Failed to load from keyring: {e}"
            raise ConfigSourceError(msg) from e

    def save(self, data: dict[str, Any]) -> None:
        """Save configuration to keyring."""
        try:
            keyring.set_password(
                self.service_name,
                "config",
                json.dumps(data)
            )
        except Exception as e:
            msg = f"Failed to save to keyring: {e}"
            raise ConfigSourceError(msg) from e


class ConfigSourceError(Exception):
    """Raised when configuration source operations fail."""


class ConfigurationManager(BaseModel):
    """Manages multiple configuration sources with different strategies."""

    model_config = ConfigDict(frozen=False, extra="allow")

    sources: list[ConfigSource] = []
    data: dict[str, Any] = {}

    class Strategy(Enum):
        """Configuration loading strategies."""
        FIRST_AVAILABLE = auto()
        MERGE_ALL = auto()
        PRIORITY_BASED = auto()
        OVERLAY = auto()

    def load(self, strategy: Strategy = Strategy.MERGE_ALL) -> None:
        """Load configuration using specified strategy."""
        match strategy:
            case self.Strategy.FIRST_AVAILABLE:
                self._load_first_available()
            case self.Strategy.MERGE_ALL:
                self._load_merge_all()
            case self.Strategy.PRIORITY_BASED:
                self._load_priority_based()
            case self.Strategy.OVERLAY:
                self._load_overlay()

    def _load_first_available(self) -> None:
        """Load from first available source."""
        for source in self.sources:
            try:
                self.data = source.load()
                return
            except ConfigSourceError:
                continue
        msg = "No available configuration source found"
        raise ConfigSourceError(msg)

    def _load_merge_all(self) -> None:
        """Merge configuration from all sources."""
        self.data = {}
        for source in self.sources:
            try:
                new_data = source.load()
                self._deep_merge(self.data, new_data)
            except ConfigSourceError:
                continue

    def _load_priority_based(self) -> None:
        """Load based on source priority."""
        sorted_sources = sorted(
            self.sources,
            key=lambda s: s.priority,
            reverse=True
        )
        self.data = {}
        for source in sorted_sources:
            try:
                new_data = source.load()
                self._deep_merge(self.data, new_data)
            except ConfigSourceError:
                continue

    def _load_overlay(self) -> None:
        """Overlay configurations (later sources override earlier ones)."""
        self.data = {}
        for source in reversed(self.sources):
            try:
                new_data = source.load()
                self.data.update(new_data)
            except ConfigSourceError:
                continue

    def _deep_merge(self, target: dict, source: dict) -> None:
        """Recursively merge two dictionaries."""
        for key, value in source.items():
            if key in target and isinstance(target[key], dict):
                if isinstance(value, dict):
                    self._deep_merge(target[key], value)
                    continue
            target[key] = value

    def save(self, source_type: ConfigSourceType | None = None) -> None:
        """Save configuration to specified or all sources."""
        if source_type:
            sources = [s for s in self.sources
                      if isinstance(s, self._get_source_class(source_type))]
        else:
            sources = self.sources

        for source in sources:
            try:
                source.save(self.data)
            except ConfigSourceError as e:
                logger.error("Failed to save to %s: %s", source.__class__.__name__, e)

    @staticmethod
    def _get_source_class(source_type: ConfigSourceType) -> type[ConfigSource]:
        """Get source class from source type."""
        # This could be expanded with more source types
        match source_type:
            case ConfigSourceType.FILE:
                return FileConfigSource
            case ConfigSourceType.ENV:
                return EnvConfigSource
            case ConfigSourceType.KEYRING:
                return KeyringConfigSource
            case _:
                msg = f"Unsupported source type: {source_type}"
                raise ValueError(msg)
```

Usage example:

```python
# Create configuration manager with multiple sources
manager = ConfigurationManager(
    sources=[
        FileConfigSource("config.yaml"),
        EnvConfigSource(prefix="APP_"),
        KeyringConfigSource("myapp"),
    ]
)

# Load using different strategies
manager.load(ConfigurationManager.Strategy.MERGE_ALL)
# or
manager.load(ConfigurationManager.Strategy.PRIORITY_BASED)

# Save to specific source
manager.save(ConfigSourceType.FILE)
```

Additional source implementations could include:

1. HashiCorp Vault source:
```python
class VaultConfigSource(ConfigSource):
    def __init__(self, url: str, token: str, path: str) -> None:
        import hvac
        self.client = hvac.Client(url=url, token=token)
        self.path = path

    def load(self) -> dict[str, Any]:
        secret = self.client.secrets.kv.v2.read_secret_version(path=self.path)
        return secret["data"]["data"]

    def save(self, data: dict[str, Any]) -> None:
        self.client.secrets.kv.v2.create_or_update_secret(
            path=self.path,
            secret=data,
        )
```

2. Redis source:
```python
class RedisConfigSource(ConfigSource):
    def __init__(self, host: str, port: int, key: str) -> None:
        import redis
        self.redis = redis.Redis(host=host, port=port)
        self.key = key

    def load(self) -> dict[str, Any]:
        data = self.redis.get(self.key)
        return json.loads(data) if data else {}

    def save(self, data: dict[str, Any]) -> None:
        self.redis.set(self.key, json.dumps(data))
```

3. AWS Secrets Manager source:
```python
class AWSSecretsConfigSource(ConfigSource):
    def __init__(self, secret_name: str, region: str) -> None:
        import boto3
        self.client = boto3.client("secretsmanager", region_name=region)
        self.secret_name = secret_name

    def load(self) -> dict[str, Any]:
        response = self.client.get_secret_value(SecretId=self.secret_name)
        return json.loads(response["SecretString"])

    def save(self, data: dict[str, Any]) -> None:
        self.client.put_secret_value(
            SecretId=self.secret_name,
            SecretString=json.dumps(data)
        )
```

4. HTTP Remote source:
```python
class RemoteHTTPConfigSource(ConfigSource):
    def __init__(self, url: str, headers: dict[str

Add more strategies.

Here's an enhanced version with additional loading strategies and more sophisticated configuration handling:

```python
"""Advanced configuration system with multiple loading strategies."""

from __future__ import annotations

from enum import Enum, auto
from typing import Any, Callable, TypeVar

# ... (previous imports and base classes remain the same)

T = TypeVar("T")


class ConfigurationManager(BaseModel):
    """Manages multiple configuration sources with advanced loading strategies."""

    model_config = ConfigDict(frozen=False, extra="allow")

    sources: list[ConfigSource] = []
    data: dict[str, Any] = {}

    class Strategy(Enum):
        """Configuration loading strategies."""
        FIRST_AVAILABLE = auto()
        MERGE_ALL = auto()
        PRIORITY_BASED = auto()
        OVERLAY = auto()
        VALIDATION_BASED = auto()
        FALLBACK_CHAIN = auto()
        ENVIRONMENT_SPECIFIC = auto()
        CACHED_WITH_REFRESH = auto()
        SELECTIVE_MERGE = auto()
        VERSIONED = auto()
        TYPE_SPECIFIC = auto()
        CONDITIONAL = auto()

    def load(
        self,
        strategy: Strategy = Strategy.MERGE_ALL,
        **kwargs: Any
    ) -> None:
        """Load configuration using specified strategy."""
        match strategy:
            case self.Strategy.FIRST_AVAILABLE:
                self._load_first_available()
            case self.Strategy.MERGE_ALL:
                self._load_merge_all()
            case self.Strategy.PRIORITY_BASED:
                self._load_priority_based()
            case self.Strategy.OVERLAY:
                self._load_overlay()
            case self.Strategy.VALIDATION_BASED:
                self._load_validation_based(kwargs.get("validator"))
            case self.Strategy.FALLBACK_CHAIN:
                self._load_fallback_chain()
            case self.Strategy.ENVIRONMENT_SPECIFIC:
                self._load_environment_specific(kwargs.get("environment"))
            case self.Strategy.CACHED_WITH_REFRESH:
                self._load_cached_with_refresh(kwargs.get("max_age", 300))
            case self.Strategy.SELECTIVE_MERGE:
                self._load_selective_merge(kwargs.get("keys", []))
            case self.Strategy.VERSIONED:
                self._load_versioned(kwargs.get("version"))
            case self.Strategy.TYPE_SPECIFIC:
                self._load_type_specific(kwargs.get("type_map", {}))
            case self.Strategy.CONDITIONAL:
                self._load_conditional(kwargs.get("conditions", []))

    def _load_validation_based(
        self,
        validator: Callable[[dict[str, Any]], bool] | None
    ) -> None:
        """Load configuration with validation for each source."""
        if not validator:
            msg = "Validator function is required for validation-based loading"
            raise ConfigSourceError(msg)

        self.data = {}
        for source in self.sources:
            try:
                new_data = source.load()
                if validator(new_data):
                    self._deep_merge(self.data, new_data)
            except ConfigSourceError:
                continue

    def _load_fallback_chain(self) -> None:
        """Load using a fallback chain with partial data acceptance."""
        self.data = {}
        for source in self.sources:
            try:
                new_data = source.load()
                missing_keys = self._get_missing_keys(self.data, new_data)
                if missing_keys:
                    partial_data = {k: new_data[k] for k in missing_keys}
                    self._deep_merge(self.data, partial_data)
            except ConfigSourceError:
                continue

    def _load_environment_specific(self, environment: str | None) -> None:
        """Load configuration specific to an environment."""
        if not environment:
            environment = os.getenv("APP_ENV", "development")

        self.data = {}
        for source in self.sources:
            try:
                new_data = source.load()
                if env_data := new_data.get(environment):
                    self._deep_merge(self.data, env_data)
                if common_data := new_data.get("common"):
                    self._deep_merge(self.data, common_data)
            except ConfigSourceError:
                continue

    def _load_cached_with_refresh(self, max_age: int) -> None:
        """Load with caching and periodic refresh."""
        import time
        from functools import lru_cache

        @lru_cache(maxsize=1)
        def cached_load(timestamp: int) -> dict[str, Any]:
            result: dict[str, Any] = {}
            for source in self.sources:
                try:
                    new_data = source.load()
                    self._deep_merge(result, new_data)
                except ConfigSourceError:
                    continue
            return result

        current_time = int(time.time())
        cache_key = current_time // max_age
        self.data = cached_load(cache_key)

    def _load_selective_merge(self, keys: list[str]) -> None:
        """Load with selective key merging."""
        self.data = {}
        for source in self.sources:
            try:
                new_data = source.load()
                filtered_data = {
                    k: v for k, v in new_data.items()
                    if not keys or k in keys
                }
                self._deep_merge(self.data, filtered_data)
            except ConfigSourceError:
                continue

    def _load_versioned(self, version: str | None) -> None:
        """Load configuration with version control."""
        if not version:
            msg = "Version is required for versioned loading"
            raise ConfigSourceError(msg)

        self.data = {}
        for source in self.sources:
            try:
                new_data = source.load()
                if new_data.get("version") == version:
                    config_data = new_data.get("config", {})
                    self._deep_merge(self.data, config_data)
            except ConfigSourceError:
                continue

    def _load_type_specific(
        self,
        type_map: dict[str, type[Any]]
    ) -> None:
        """Load with type-specific parsing."""
        self.data = {}
        for source in self.sources:
            try:
                new_data = source.load()
                typed_data = self._apply_type_conversion(new_data, type_map)
                self._deep_merge(self.data, typed_data)
            except ConfigSourceError:
                continue

    def _load_conditional(
        self,
        conditions: list[Callable[[dict[str, Any]], bool]]
    ) -> None:
        """Load based on custom conditions."""
        self.data = {}
        for source in self.sources:
            try:
                new_data = source.load()
                if all(condition(new_data) for condition in conditions):
                    self._deep_merge(self.data, new_data)
            except ConfigSourceError:
                continue

    def _get_missing_keys(
        self,
        current: dict[str, Any],
        new: dict[str, Any]
    ) -> set[str]:
        """Get keys that are missing in current data."""
        return set(new.keys()) - set(current.keys())

    def _apply_type_conversion(
        self,
        data: dict[str, Any],
        type_map: dict[str, type[Any]]
    ) -> dict[str, Any]:
        """Apply type conversion to values based on type map."""
        result = {}
        for key, value in data.items():
            if key in type_map:
                try:
                    result[key] = type_map[key](value)
                except (ValueError, TypeError):
                    result[key] = value
            else:
                result[key] = value
        return result

    @property
    def metadata(self) -> dict[str, Any]:
        """Get metadata about the configuration."""
        return {
            "sources": [s.__class__.__name__ for s in self.sources],
            "key_count": len(self.data),
            "nested_depth": self._calculate_depth(self.data),
        }

    def _calculate_depth(self, d: dict[str, Any]) -> int:
        """Calculate the maximum depth of a nested dictionary."""
        if not isinstance(d, dict) or not d:
            return 0
        return 1 + max(self._calculate_depth(v) for v in d.values()
                      if isinstance(v, dict))
```

Usage examples for the new strategies:

```python
# Validation-based loading
def config_validator(data: dict[str, Any]) -> bool:
    return all(key in data for key in ["database", "api_key"])

manager.load(
    ConfigurationManager.Strategy.VALIDATION_BASED,
    validator=config_validator
)

# Environment-specific loading
manager.load(
    ConfigurationManager.Strategy.ENVIRONMENT_SPECIFIC,
    environment="production"
)

# Cached loading with refresh
manager.load(
    ConfigurationManager.Strategy.CACHED_WITH_REFRESH,
    max_age=300  # 5 minutes
)

# Selective merge
manager.load(
    ConfigurationManager.Strategy.SELECTIVE_MERGE,
    keys=["database", "logging"]
)

# Versioned loading
manager.load(
    ConfigurationManager.Strategy.VERSIONED,
    version="2.0"
)

# Type-specific loading
type_map = {
    "port": int,
    "debug": bool,
    "timeout": float,
}
manager.load(
    ConfigurationManager.Strategy.TYPE_SPECIFIC,
    type_map=type_map
)

# Conditional loading
def has_required_sections(data: dict[str, Any]) -> bool:
    return "database" in data

def valid_api_version(data: dict[str, Any]) -> bool:
    return data.get("api_version", "1.0") >= "2.0"

manager.load(
    ConfigurationManager.Strategy.CONDITIONAL,
    conditions=[has_required_sections, valid_api_version]
)
```

These strategies provide different ways to handle configuration loading:

1. `VALIDATION_BASED`: Only accepts configuration that passes validation
2. `FALLBACK_CHAIN`: Uses sources as fallbacks for missing keys
3. `ENVIRONMENT_SPECIFIC`: Loads configuration based on environment
4. `CACHED_WITH_REFRESH`: Implements caching with periodic refresh
5. `SELECTIVE_MERGE`: Merges only specific keys
6. `VERSIONED`: Loads configuration based on version
7. `TYPE_SPECIFIC`: Applies type conversion to values
8. `CONDITIONAL`: Loads based on custom conditions

Each strategy serves different use cases and can be selected based on specific requirements.

What about different deep merge behaviour? Merging lists?

Here's an implementation of different merge strategies, especially for handling lists and nested structures:

```python
"""Configuration system with advanced merge strategies."""

from __future__ import annotations

from enum import Enum, auto
from typing import Any, Callable, TypeVar

# ... (previous imports)

T = TypeVar("T")


class MergeStrategy(Enum):
    """Strategies for merging configuration data."""

    REPLACE = auto()  # Later values completely replace earlier ones
    DEEP_MERGE = auto()  # Recursively merge dictionaries
    APPEND_LISTS = auto()  # Append lists together
    EXTEND_SETS = auto()  # Merge sets together
    UNIQUE_APPEND = auto()  # Append lists but maintain uniqueness
    SMART_MERGE = auto()  # Choose strategy based on value types
    KEEP_ORIGINAL = auto()  # Keep first value encountered
    CUSTOM = auto()  # Use custom merge function


class ListMergeStrategy(Enum):
    """Specific strategies for merging lists."""

    APPEND = auto()  # Simple concatenation
    UNIQUE = auto()  # Remove duplicates
    REPLACE = auto()  # Later list replaces earlier
    INTERSECT = auto()  # Keep only common elements
    SUBTRACT = auto()  # Remove elements from second list
    KEEP_ORIGINAL = auto()  # Keep first list encountered
    EXTEND_DICTS = auto()  # Merge dictionaries within lists


class MergeConfig(BaseModel):
    """Configuration for merge operations."""

    strategy: MergeStrategy = MergeStrategy.DEEP_MERGE
    list_strategy: ListMergeStrategy = ListMergeStrategy.APPEND
    custom_merger: Callable[[Any, Any], Any] | None = None
    type_specific_mergers: dict[type, Callable[[Any, Any], Any]] = {}
    skip_none: bool = True
    depth_limit: int | None = None


class ConfigurationManager(BaseModel):
    """Configuration manager with advanced merge strategies."""

    model_config = ConfigDict(frozen=False, extra="allow")

    sources: list[ConfigSource] = []
    data: dict[str, Any] = {}
    merge_config: MergeConfig = MergeConfig()

    def merge(self, source: dict[str, Any]) -> None:
        """Merge source data according to configured strategy."""
        match self.merge_config.strategy:
            case MergeStrategy.REPLACE:
                self.data = source.copy()
            case MergeStrategy.DEEP_MERGE:
                self._deep_merge(self.data, source)
            case MergeStrategy.CUSTOM:
                if not self.merge_config.custom_merger:
                    msg = "Custom merger function not provided"
                    raise ConfigurationError(msg)
                self.data = self.merge_config.custom_merger(self.data, source)
            case MergeStrategy.SMART_MERGE:
                self._smart_merge(self.data, source)

    def _merge_values(
        self,
        current: Any,
        new: Any,
        depth: int = 0
    ) -> Any:
        """Merge two values based on their types and configured strategies."""
        # Check depth limit
        if (limit := self.merge_config.depth_limit) and depth >= limit:
            return new

        # Skip None values if configured
        if self.merge_config.skip_none and new is None:
            return current

        # Check for type-specific merger
        for type_, merger in self.merge_config.type_specific_mergers.items():
            if isinstance(new, type_):
                return merger(current, new)

        # Handle different types
        match (current, new):
            case (dict(), dict()):
                return self._deep_merge(current.copy(), new, depth + 1)
            case (list(), list()):
                return self._merge_lists(current, new)
            case (set(), set()):
                return self._merge_sets(current, new)
            case _:
                return new

    def _deep_merge(
        self,
        target: dict[str, Any],
        source: dict[str, Any],
        depth: int = 0
    ) -> dict[str, Any]:
        """Recursively merge dictionaries."""
        for key, value in source.items():
            if key in target:
                target[key] = self._merge_values(target[key], value, depth)
            else:
                target[key] = value
        return target

    def _merge_lists(self, current: list[Any], new: list[Any]) -> list[Any]:
        """Merge lists according to configured strategy."""
        match self.merge_config.list_strategy:
            case ListMergeStrategy.APPEND:
                return current + new
            case ListMergeStrategy.UNIQUE:
                return list(dict.fromkeys(current + new))
            case ListMergeStrategy.REPLACE:
                return new.copy()
            case ListMergeStrategy.INTERSECT:
                return [x for x in current if x in new]
            case ListMergeStrategy.SUBTRACT:
                return [x for x in current if x not in new]
            case ListMergeStrategy.KEEP_ORIGINAL:
                return current.copy()
            case ListMergeStrategy.EXTEND_DICTS:
                return self._merge_list_dicts(current, new)

    def _merge_list_dicts(
        self,
        current: list[Any],
        new: list[Any]
    ) -> list[Any]:
        """Merge lists of dictionaries based on a key."""
        result = current.copy()

        # Helper to find matching dict in list
        def find_matching_dict(d: dict[str, Any], lst: list[dict[str, Any]]) -> int:
            for i, item in enumerate(lst):
                if all(item.get(k) == v for k, v in d.items()
                      if k in self.merge_config.dict_key_identifiers):
                    return i
            return -1

        # Process each dictionary in the new list
        for new_dict in new:
            if not isinstance(new_dict, dict):
                continue

            idx = find_matching_dict(new_dict, result)
            if idx >= 0:
                # Merge with existing dictionary
                result[idx] = self._merge_values(result[idx], new_dict)
            else:
                # Add new dictionary
                result.append(new_dict)

        return result

    def _merge_sets(self, current: set[Any], new: set[Any]) -> set[Any]:
        """Merge sets."""
        match self.merge_config.strategy:
            case MergeStrategy.EXTEND_SETS:
                return current | new
            case MergeStrategy.REPLACE:
                return new.copy()
            case MergeStrategy.KEEP_ORIGINAL:
                return current.copy()
            case _:
                return current | new

    def _smart_merge(self, target: dict[str, Any], source: dict[str, Any]) -> None:
        """Smart merge based on value types and patterns."""
        for key, value in source.items():
            if key not in target:
                target[key] = value
                continue

            current = target[key]

            # Handle different type combinations
            match (current, value):
                case (dict(), dict()):
                    self._smart_merge(current, value)
                case (list(), list()):
                    # Smart list merging based on content
                    if all(isinstance(x, dict) for x in current + value):
                        target[key] = self._merge_list_dicts(current, value)
                    else:
                        target[key] = self._merge_lists(current, value)
                case (set(), set()):
                    target[key] = current | value
                case (str(), str()):
                    # Smart string handling (e.g., path joining)
                    if self._is_path(current) and self._is_path(value):
                        target[key] = str(UPath(current) / value)
                    else:
                        target[key] = value
                case _:
                    target[key] = value

    @staticmethod
    def _is_path(s: str) -> bool:
        """Check if string looks like a path."""
        return "/" in s or "\\" in s


# Basic merge configuration
merge_config = MergeConfig(
    strategy=MergeStrategy.DEEP_MERGE,
    list_strategy=ListMergeStrategy.UNIQUE,
    skip_none=True,
    depth_limit=5
)

# Custom merger for specific types
def merge_timestamps(t1: float, t2: float) -> float:
    return max(t1, t2)

merge_config = MergeConfig(
    strategy=MergeStrategy.SMART_MERGE,
    type_specific_mergers={
        float: merge_timestamps,
    }
)

# # Example usage
# config = ConfigurationManager(merge_config=merge_config)

# # Different merge scenarios
# config.data = {
#     "list1": [1, 2, 3],
#     "list2": [{"id": 1, "value": "a"}, {"id": 2, "value": "b"}],
#     "nested": {
#         "dict": {"a": 1},
#         "timestamps": {"created": 1000.0}
#     }
# }

# new_data = {
#     "list1": [3, 4, 5],
#     "list2": [{"id": 1, "value": "c"}, {"id": 3, "value": "d"}],
#     "nested": {
#         "dict": {"b": 2},
#         "timestamps": {"created": 2000.0}
#     }
# }

# # Merge with different strategies
# config.merge_config.strategy = MergeStrategy.DEEP_MERGE
# config.merge_config.list_strategy = ListMergeStrategy.UNIQUE
# config.merge(new_data)

# # Result would be:
# # {
# #     "list1": [1, 2, 3, 4, 5],
# #     "list2": [
# #         {"id": 1, "value": "c"},
# #         {"id": 2, "value": "b"},
# #         {"id": 3, "value": "d"}
# #     ],
# #     "nested": {
# #         "dict": {"a": 1, "b": 2},
# #         "timestamps": {"created": 2000.0}
# #     }
# # }
# ```

# This implementation provides:

# 1. Different merge strategies for different types of values:
#    - Simple replacement
#    - Deep merging
#    - List operations (append, unique, replace, intersect)
#    - Set operations
#    - Custom merging functions

# 2. Special handling for:
#    - Lists of dictionaries (merging based on key identifiers)
#    - Paths (smart joining)
#    - None values
#    - Type-specific mergers

# 3. Configuration options:
#    - Depth limits for recursive merging
#    - Skip None values
#    - Custom merger functions
#    - Type-specific merger functions

# 4. Smart merging that:
#    - Detects value types and applies appropriate strategies
#    - Handles nested structures
#    - Preserves data types
#    - Provides special handling for common patterns

# This allows for very flexible configuration management with fine-grained control over how different types of data are merged.
