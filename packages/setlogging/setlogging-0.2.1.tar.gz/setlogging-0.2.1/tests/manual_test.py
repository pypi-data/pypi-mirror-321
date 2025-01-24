import os
import shutil
from pathlib import Path
from setlogging.logger import get_logger
import json
import logging

# Define a global temp_path for storing log files
temp_path = Path("/tmp/setlogging")
temp_path.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists


def get_log_file_for_function(func_name: str) -> str:
    """
    Generate a log file path for a given function name.
    """
    return str(temp_path / f"{func_name}.log")


def cleanup_temp_path():
    """
    Remove all files in the temp_path directory after testing.
    """
    print("\nCleaning up temporary log files...")
    if temp_path.exists():
        shutil.rmtree(temp_path)
        print(f"All files in {temp_path} have been removed.")


def test_log_rotation():
    """
    Test log rotation functionality.
    """
    log_file = get_log_file_for_function("test_log_rotation")
    logger = get_logger(
        log_level=logging.INFO,
        log_file=log_file,
        max_size_mb=1,  # 1MB log file size
        backup_count=3,  # Keep 3 backup files
        console_output=True,
        json_format=True,
        indent=4
    )

    message = "This is a test log message. " * 500  # Approx 2KB per log
    for i in range(1000):  # Write enough logs to trigger rotation
        logger.info(f"{i}: {message}")

    print(f"Log files created for test_log_rotation: {
          list(temp_path.glob('*'))}")


def test_json_indent():
    """
    Test JSON indentation functionality.
    """
    log_file = get_log_file_for_function("test_json_indent")
    logger = get_logger(
        json_format=True,
        indent=2,
        log_file=log_file
    )

    logger.info("Test indent message")
    logger.info("Another JSON log message")

    # Read and print log entries
    with open(log_file) as f:
        for line in f:
            print(f"Log entry: {line.strip()}")


def test_file_rotation():
    """
    Test log file rotation functionality.
    """
    log_file = get_log_file_for_function("test_file_rotation")
    logger = get_logger(
        log_level=logging.INFO,
        log_file=log_file,
        max_size_mb=1,  # 1MB log file size
        backup_count=3  # Keep 3 backup files
    )

    for i in range(104):  # Write enough logs to trigger rotation
        logger.info("x" * 1024 * 10)  # Each log is ~10KB

    print(f"Log rotation files for test_file_rotation: {
          list(temp_path.glob('*'))}")


def test_json():
    """
    Test JSON logging functionality.
    """
    log_file = get_log_file_for_function("test_json")
    logger = get_logger(
        log_level=logging.DEBUG,
        log_file=log_file,
        max_size_mb=1,
        backup_count=3,
        json_format=True,
        indent=2
    )

    logger.debug("This DEBUG message will not be printed.")
    logger.info("This is an INFO message.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")
    logger.critical("This is a CRITICAL message.")
    logger.info("Test custom field", extra={"custom_field": "value"})


def test_plain_log():
    """
    Test non-JSON logging functionality.
    """
    log_file = get_log_file_for_function("test_plain_log")
    logger = get_logger(
        log_level=logging.CRITICAL,
        log_file=log_file,
        max_size_mb=1,
        backup_count=3,
        json_format=False
    )

    logger.debug("This is a DEBUG message.")
    logger.info("This is an INFO message.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")
    logger.critical("This is a CRITICAL message.")


def manual_test_json_structure():
    """
    Manually test JSON log entry structure.
    """
    log_file = get_log_file_for_function("manual_test_json_structure")
    logger = get_logger(
        json_format=True,
        log_file=log_file
    )

    logger.info("Structured log message", extra={
                "custom_field": "custom_value"})

    # Validate JSON structure
    required_fields = ["time", "level", "message", "name"]
    with open(log_file) as f:
        for line_number, line in enumerate(f, start=1):
            print(f"\nProcessing line {line_number}: {line.strip()}")
            try:
                log_entry = json.loads(line.strip())
                missing_fields = [
                    field for field in required_fields if field not in log_entry]
                if missing_fields:
                    print(f"❌ Missing fields: {missing_fields}")
                else:
                    print(f"✅ Log entry is valid.")
            except json.JSONDecodeError as e:
                print(f"❌ JSON decoding error: {e}")


def manual_test_custom_log_format():
    """
    Test custom log format functionality.
    """
    log_file = get_log_file_for_function("manual_test_custom_log_format")
    custom_format = "%(levelname)s - %(message)s"
    logger = get_logger(
        log_format=custom_format,
        log_file=log_file
    )

    logger.info("Test message")
    print(f"Log file for custom log format created: {log_file}")


def main():
    print("Manual testing started...")

    # Call all test functions
    test_log_rotation()
    test_json_indent()
    test_file_rotation()
    test_json()
    test_plain_log()
    manual_test_json_structure()
    manual_test_custom_log_format()

    # Cleanup
    # cleanup_temp_path()


if __name__ == "__main__":
    main()
