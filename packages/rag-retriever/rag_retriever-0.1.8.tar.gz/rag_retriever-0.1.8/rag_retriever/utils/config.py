"""Configuration management for the RAG retriever application."""

import os
from pathlib import Path
from typing import Dict, Any, Optional
from importlib.resources import files
import logging
import shutil
import stat

import yaml
from dotenv import load_dotenv
from platformdirs import user_config_dir, user_data_dir

logger = logging.getLogger(__name__)


def secure_file_permissions(file_path: Path) -> None:
    """Set secure file permissions (600) on the given file."""
    if os.name != "nt":  # Skip on Windows
        os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)


def get_config_dir() -> Path:
    """Get user-specific config directory path."""
    return Path(user_config_dir("rag-retriever", appauthor=False))


def get_data_dir() -> Path:
    """Get user-specific data directory path."""
    return Path(user_data_dir("rag-retriever", appauthor=False))


def get_user_config_path() -> Path:
    """Get user-specific config file path."""
    return get_config_dir() / "config.yaml"


def get_user_env_path() -> Path:
    """Get user-specific .env file path."""
    return get_config_dir() / ".env"


def ensure_user_directories() -> None:
    """Create and verify user config and data directories."""
    config_dir = get_config_dir()
    data_dir = get_data_dir()

    # Function to verify directory creation
    def verify_directory(path: Path, dir_type: str) -> None:
        try:
            # Attempt to create
            path.mkdir(parents=True, exist_ok=True)

            # Verify it exists
            if not path.exists():
                raise RuntimeError(
                    f"{dir_type} directory does not exist after creation: {path}"
                )

            # Verify it's a directory
            if not path.is_dir():
                raise RuntimeError(
                    f"{dir_type} path exists but is not a directory: {path}"
                )

            # Verify we can write to it
            test_file = path / ".write_test"
            try:
                test_file.write_text("test")
                test_file.unlink()
            except Exception as e:
                raise RuntimeError(f"Cannot write to {dir_type} directory {path}: {e}")

            logger.info(f"Verified {dir_type} directory at: {path}")

        except Exception as e:
            raise RuntimeError(
                f"Failed to create/verify {dir_type} directory at {path}\n"
                f"Error: {e}\n"
                "Please check permissions and try again."
            )

    # Verify both directories
    verify_directory(config_dir, "config")
    verify_directory(data_dir, "data")


def create_user_env() -> None:
    """Create a new .env file in user config directory using the example template."""
    env_path = get_user_env_path()

    # Check if .env exists and has content
    if env_path.exists():
        with open(env_path, "r") as f:
            content = f.read().strip()
            if content:  # File exists and has content
                # Check if it has a valid API key
                if "OPENAI_API_KEY" in content and not content.endswith(
                    "your-api-key-here"
                ):
                    logger.info(
                        "User .env already exists with API key at: %s", env_path
                    )
                    return
                else:
                    logger.warning("Existing .env found but no valid API key detected")
                    logger.warning(
                        "Please edit %s to add your OpenAI API key", env_path
                    )
                    return

    # Create new .env or overwrite empty one
    with files("rag_retriever.config").joinpath(".env.example").open("r") as src:
        with open(env_path, "w") as dst:
            dst.write(src.read())

    logger.info("Created .env file at: %s", env_path)
    logger.warning("Please edit this file to add your OpenAI API key")


def create_user_config() -> None:
    """Create a new user config file by copying the default."""
    config_path = get_user_config_path()

    try:
        # Ensure parent directory exists and is writable
        parent_dir = config_path.parent
        if not parent_dir.exists():
            parent_dir.mkdir(parents=True, exist_ok=True)
            if not parent_dir.exists():
                raise RuntimeError(f"Failed to create directory {parent_dir}")

        # Verify directory is writable
        test_file = parent_dir / ".write_test"
        try:
            test_file.touch()
            test_file.unlink()
        except Exception as e:
            raise RuntimeError(f"Directory {parent_dir} is not writable. Error: {e}")

        # Copy the default config file with explicit checks
        with files("rag_retriever.config").joinpath("config.yaml").open("r") as src:
            with open(config_path, "w", encoding="utf-8") as dst:
                content = src.read()
                dst.write(content)
                dst.flush()  # Ensure content is written to disk

        # Verify file was created and has content
        if not config_path.exists():
            raise RuntimeError(f"Config file {config_path} was not created")
        if config_path.stat().st_size == 0:
            raise RuntimeError(f"Config file {config_path} was created but is empty")

        logger.info("Created user config file at: %s", config_path)
    except Exception as e:
        raise RuntimeError(
            f"Failed to create configuration file at {config_path}.\n"
            f"Error: {e}\n"
            "Please ensure you have write permissions to this location."
        )


def initialize_user_files() -> None:
    """Initialize all user-specific files in standard locations."""
    # Force directory creation first and verify
    try:
        ensure_user_directories()
    except Exception as e:
        raise RuntimeError(
            "Failed to create required directories. "
            f"Error: {e}\n"
            "Please check your permissions and try again."
        )

    # Only proceed with file creation if directories exist
    try:
        create_user_config()
        create_user_env()
    except Exception as e:
        raise RuntimeError(
            "Failed to create configuration files. "
            f"Error: {e}\n"
            "Please check your permissions and try again."
        )


def get_env_value(key: str, default: Any = None) -> Any:
    """Get config value from environment variable."""
    env_key = f"RAG_RETRIEVER_{key.upper()}"
    return os.environ.get(env_key, default)


def mask_api_key(key: str) -> str:
    """Mask an API key showing only first 4 and last 4 characters."""
    if not key or len(key) < 8:
        return "not set"
    return f"{key[:4]}...{key[-4:]}"


def log_env_source() -> None:
    """Log information about where environment variables are loaded from."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.warning("OPENAI_API_KEY is not set in any environment file")
        return

    # Check each possible source
    env_sources = [
        (Path("~/.env").expanduser(), "home directory (~/.env)"),
        (get_user_env_path(), "user config directory"),
        (Path(".env"), "current directory"),
    ]

    for env_path, description in env_sources:
        if env_path.exists():
            with open(env_path) as f:
                if "OPENAI_API_KEY" in f.read():
                    logger.info(
                        "Using OPENAI_API_KEY from %s (key: %s)",
                        description,
                        mask_api_key(api_key),
                    )
                    return

    logger.info(
        "Using OPENAI_API_KEY from environment variables (key: %s)",
        mask_api_key(api_key),
    )


class Config:
    """Configuration manager for the application."""

    def __init__(self, config_path: str | None = None):
        """Initialize configuration manager."""
        self._config_path = None
        self._env_path = None

        # Debug path resolution
        config_dir = get_config_dir()
        user_config_path = get_user_config_path()
        logger.debug("Config directory resolved to: %s", config_dir)
        logger.debug("User config path resolved to: %s", user_config_path)

        # First ensure user config exists
        if not user_config_path.exists():
            logger.debug("User config not found - creating it")
            create_user_config()
            # Verify creation
            if not user_config_path.exists():
                raise RuntimeError(
                    f"Installation failed: Could not create configuration file at {user_config_path}. "
                    "Please check your permissions and try again."
                )

        # Load user config first
        try:
            with open(user_config_path, "r", encoding="utf-8") as f:
                self._config = yaml.safe_load(f)
                self._config_path = str(user_config_path)
                logger.debug("Loaded user config from: %s", user_config_path)
        except Exception as e:
            logger.error("Failed to load user config: %s", e)
            raise

        # If explicit config path provided, load and merge it
        if config_path:
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    explicit_config = yaml.safe_load(f)
                self._merge_configs(explicit_config)
                self._config_path = config_path
                logger.debug("Merged explicit config from %s", config_path)
            except Exception as e:
                logger.error("Failed to load explicit config: %s", e)
                raise

        # Apply environment variable overrides
        self._apply_env_overrides()

    def _apply_env_overrides(self) -> None:
        """Apply environment variable overrides to config."""
        # Vector store overrides
        if embed_model := get_env_value("EMBEDDING_MODEL"):
            self._config["vector_store"]["embedding_model"] = embed_model
        if embed_dim := get_env_value("EMBEDDING_DIMENSIONS"):
            self._config["vector_store"]["embedding_dimensions"] = int(embed_dim)

        # Search overrides
        if default_limit := get_env_value("DEFAULT_LIMIT"):
            self._config["search"]["default_limit"] = int(default_limit)
        if score_threshold := get_env_value("SCORE_THRESHOLD"):
            self._config["search"]["default_score_threshold"] = float(score_threshold)

    def _merge_configs(self, override_config: Dict[str, Any]) -> None:
        """Recursively merge override config into base config."""
        for key, value in override_config.items():
            if (
                key in self._config
                and isinstance(self._config[key], dict)
                and isinstance(value, dict)
            ):
                self._config[key].update(value)
            else:
                self._config[key] = value

    @property
    def vector_store(self) -> Dict[str, Any]:
        """Get vector store configuration."""
        return self._config["vector_store"]

    @property
    def content(self) -> Dict[str, Any]:
        """Get content processing configuration."""
        return self._config["content"]

    @property
    def search(self) -> Dict[str, Any]:
        """Get search configuration."""
        return self._config["search"]

    @property
    def browser(self) -> Dict[str, Any]:
        """Get browser configuration."""
        return self._config.get("browser", {})

    @property
    def config_path(self) -> str:
        """Get the path to the active configuration file."""
        return self._config_path or "using default configuration"

    @property
    def env_path(self) -> str:
        """Get the path to the active environment file."""
        return self._env_path or "environment variables not loaded from file"

    @property
    def api(self) -> Dict[str, Any]:
        """Get API configuration."""
        return self._config.get("api", {})

    def get_openai_api_key(self) -> Optional[str]:
        """Get OpenAI API key from config or environment."""
        logger.debug("Attempting to get OpenAI API key...")
        logger.debug("Config keys available: %s", list(self._config.keys()))

        if "api" in self._config:
            logger.debug("API section found in config")
            logger.debug("API section keys: %s", list(self._config["api"].keys()))
            if "openai_api_key" in self._config["api"]:
                logger.debug("openai_api_key found in config")
                api_key = self._config["api"]["openai_api_key"]
                logger.debug("API key type: %s", type(api_key))
                logger.debug(
                    "API key starts with sk-: %s",
                    str(api_key).startswith("sk-") if api_key else False,
                )
        else:
            logger.debug("No api section found in config")

        # First try config file (takes precedence)
        if api_key := self.api.get("openai_api_key"):
            logger.debug("Found API key in config file")
            if isinstance(api_key, str) and api_key.startswith("sk-"):
                logger.debug("Using API key from config file")
                return api_key
            else:
                logger.debug("API key in config is invalid format: %s", type(api_key))

        # Then try environment variable as fallback
        if api_key := os.getenv("OPENAI_API_KEY"):
            logger.debug("Found API key in environment")
            if api_key.startswith("sk-"):
                logger.debug("Using API key from environment variable")
                return api_key
            else:
                logger.debug("API key in environment is invalid format")

        logger.debug("No valid API key found in config or environment")
        return None


# Global config instance
config = Config()
