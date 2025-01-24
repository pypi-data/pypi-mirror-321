import pytest
import json
import os
import logging
from datetime import datetime
from setlogging.logger import get_logger, setup_logging, TimezoneFormatter


class LogCapture:
    def __init__(self):
        self.records = []

    def __enter__(self):
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.records = []
        self.handler.emit = lambda record: self.records.append(record)
        logging.getLogger().addHandler(self.handler)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.getLogger().removeHandler(self.handler)


def test_basic_logger():
    """Test basic logger initialization"""
    logger = get_logger()
    assert logger is not None
    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.DEBUG


def test_json_logging(tmp_path):
    """Test JSON format logging"""
    # Create a temporary file for logging
    log_file = tmp_path / "test_json_format.log"

    # Initialize the logger with JSON format and specify the log file
    logger = get_logger(json_format=True, log_file=str(log_file))
    test_message = "Test JSON logging"

    # Log a test message
    logger.info(test_message)

    # Read the log file line by line and parse each line as JSON
    with open(log_file) as f:
        for line in f:
            # Parse each line as a JSON object
            log_entry = json.loads(line.strip())

            # Validate the parsed JSON structure for each log entry
            # Focus on the test message entry
            if log_entry.get("message") == test_message:
                assert "message" in log_entry  # Check if "message" key exists
                # Verify the message content
                assert log_entry["message"] == test_message
                assert "level" in log_entry  # Check if "level" key exists
                # Verify the log level is "INFO"
                assert log_entry["level"] == "INFO"


def test_timezone_awareness():
    """Test timezone information in logs"""
    logger = get_logger()
    formatter = next((h.formatter for h in logger.handlers
                     if isinstance(h.formatter, TimezoneFormatter)), None)
    assert formatter is not None
    assert formatter.local_timezone is not None


def test_file_rotation(tmp_path):
    """Test log file rotation"""
    log_file = tmp_path / "rotate.log"
    max_size_mb = 1  # 1MB
    backup_count = 3
    logger = get_logger(
        log_file=str(log_file),
        max_size_mb=max_size_mb,
        backup_count=backup_count
    )

    # Write enough data to trigger rotation
    for i in range(104):
        logger.info("x" * 1024 * 10)  # 10KB per log entry

    assert os.path.exists(log_file)
    assert os.path.exists(f"{log_file}.1")

    # Check the size of the rotated log file
    log_file_size = os.path.getsize(f"{log_file}.1")  # Size in bytes
    expected_size = max_size_mb * 1024 * 1024  # Convert MB to bytes

    # Allow a 5% margin of error
    margin = expected_size * 0.05
    assert abs(log_file_size - expected_size) <= margin, (
        f"Expected size around {expected_size} bytes (±{margin:.0f}), "
        f"but got {log_file_size} bytes"
    )


def test_invalid_parameters():
    """Test error handling for invalid parameters"""
    with pytest.raises(ValueError):
        get_logger(max_size_mb=-1)

    with pytest.raises(ValueError):
        get_logger(backup_count=-1)

    with pytest.raises(ValueError):
        get_logger(indent=2, json_format=False)


def test_console_output(capsys):
    """Test console output"""
    logger = get_logger(console_output=True)
    test_message = "Test console output"
    logger.info(test_message)
    captured = capsys.readouterr()
    assert test_message in captured.err or test_message in captured.out


def test_json_indent(tmp_path):
    """Test JSON indentation formatting"""
    log_file = tmp_path / "test_indent.json"
    indent = 4
    logger = get_logger(
        json_format=True,
        indent=indent,
        log_file=str(log_file)
    )

    # Generate some log entries
    test_message = "Test indent"
    logger.info(test_message)
    logger.info("Another message")

    # Validate the indentation of the log file
    with open(log_file) as f:
        for line_number, line in enumerate(f, start=1):
            # Skip empty lines
            if not line.strip():
                continue

            # Count the number of leading spaces
            leading_spaces = len(line) - len(line.lstrip())

            # Ensure the leading spaces are a multiple of the specified indent
            assert leading_spaces % indent == 0, (
                f"Line '{line.strip()}' has incorrect indentation: "
                f"{leading_spaces} spaces (expected multiple of {indent}). "
                f"The line number is: {line_number}"
            )


def test_invalid_json_parameters():
    """Test invalid JSON parameters"""
    # Test invalid indent with json_format=False
    with pytest.raises(ValueError, match="indent parameter is only valid"):
        get_logger(json_format=False, indent=2)


def test_log_level_configuration():
    """Test different log levels"""
    logger = get_logger(log_level=logging.WARNING)
    assert logger.level == logging.WARNING

    # Debug shouldn't log
    with LogCapture() as capture:
        logger.debug("Debug message")
        assert len(capture.records) == 0

        # Warning should log
        logger.warning("Warning message")
        assert len(capture.records) == 1


def test_custom_date_format(tmp_path):
    """Test custom date format"""
    log_file = tmp_path / "date_format.log"
    date_format = "%Y-%m-%d"
    logger = get_logger(
        log_file=str(log_file),
        date_format=date_format
    )
    logger.info("Test message")

    with open(log_file) as f:
        content = f.read()
        assert datetime.now().strftime(date_format) in content


def test_custom_log_format():
    """Test custom log format"""
    custom_format = "%(levelname)s - %(message)s"
    logger = get_logger(log_format=custom_format)
    print(f"logger.handlers: {logger.handlers}")

    with LogCapture() as capture:
        logger.info("Test message")

        # Get the first captured log record
        log_record = capture.records[0]

        # Format the LogRecord using the custom format
        formatter = logging.Formatter(custom_format)
        formatted_message = formatter.format(log_record)

        # Assert the formatted message matches the expected output
        assert formatted_message == "INFO - Test message", (
            f"Expected 'INFO - Test message' but got '{formatted_message}'"
        )


def test_multiple_handlers():
    """Test multiple handlers configuration"""
    logger = get_logger(console_output=True)

    # Ensure at least two handlers are present (e.g., console and file)
    assert len(
        logger.handlers) >= 2, "Expected at least 2 handlers (file and console)"

    # Check handler types
    handler_types = [type(h) for h in logger.handlers]
    assert logging.StreamHandler in handler_types, "StreamHandler (console) is missing"
    assert any(
        issubclass(h, logging.FileHandler) for h in handler_types
    ), "No FileHandler or RotatingFileHandler found in logger handlers"


@ pytest.fixture(autouse=True)
def cleanup():
    """Clean up log files after tests"""
    yield
    for handler in logging.getLogger().handlers[:]:
        handler.close()
        logging.getLogger().removeHandler(handler)
