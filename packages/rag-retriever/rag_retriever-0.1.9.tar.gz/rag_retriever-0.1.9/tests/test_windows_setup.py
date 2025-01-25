import os
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_directory_creation():
    """Test Windows directory creation and verification."""
    from rag_retriever.utils.config import get_config_dir, get_data_dir

    # Get paths
    config_dir = get_config_dir()
    data_dir = get_data_dir()

    logger.debug(f"Config dir resolved to: {config_dir}")
    logger.debug(f"Data dir resolved to: {data_dir}")

    # Test directory creation
    try:
        config_dir.mkdir(parents=True, exist_ok=True)
        data_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logger.error(f"Failed to create directories: {e}")
        raise

    # Verify directories exist
    if not config_dir.exists():
        raise RuntimeError(f"Config dir not created: {config_dir}")
    if not data_dir.exists():
        raise RuntimeError(f"Data dir not created: {data_dir}")

    # Test write permissions
    test_file = config_dir / "test.txt"
    try:
        test_file.write_text("test")
        test_file.unlink()
    except Exception as e:
        logger.error(f"Failed write test: {e}")
        raise


if __name__ == "__main__":
    test_directory_creation()
