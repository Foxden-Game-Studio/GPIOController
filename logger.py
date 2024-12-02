import logging
import os
from datetime import datetime
import subprocess

log_dir = "logs"  # Directory to store logs
max_files = 5 # Max file count

# removing old log files
def cleanup_old_logs():
    """Ensure that only the newest 'max_files' log files are kept."""
    log_files = sorted(
        [f for f in os.listdir(log_dir) if f.startswith("log_") and f.endswith(".log")],
        key=lambda f: os.path.getmtime(os.path.join(log_dir, f)),
        reverse=True,
    )

    # Remove older files if the count exceeds max_files
    for old_file in log_files[max_files:]:
        os.remove(os.path.join(log_dir, old_file))
        logging.info(f"Deleted old log file: {old_file}")

# setup logging
def setuplogger():
    # Define file paths
    latest_log_file = os.path.join(log_dir, "latest.log")
    last_run_file = os.path.join(log_dir, "last_run.txt")

    # Ensure the log directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Load the last run time if available
    last_run_time = None
    if os.path.exists(last_run_file):
        with open(last_run_file, "r") as f:
            last_run_time = f.read().strip()

    # Rename the latest.log file if it exists
    if os.path.exists(latest_log_file):
        if last_run_time:
            timestamp = datetime.strptime(last_run_time, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d_%H-%M-%S")
            old_log_file = os.path.join(log_dir, f"log_{timestamp}.log")
            os.rename(latest_log_file, old_log_file)
        else:
            # If no last run time is available, use a fallback timestamp
            fallback_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            old_log_file = os.path.join(log_dir, f"log_{fallback_timestamp}.log")
            os.rename(latest_log_file, old_log_file)

    # Save the current run time for future reference
    current_run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(last_run_file, "w") as f:
        f.write(current_run_time)

    # Create a logger
    logger = logging.getLogger("dual_logger")
    logger.setLevel(logging.DEBUG)
    
    # Prevent propagation to the root logger
    logger.propagate = False

    # Log formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # File handler for logging to a file
    file_handler = logging.FileHandler(latest_log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Create a second terminal for logging
    second_terminal = subprocess.Popen(
        ["x-terminal-emulator", "-e", "tail -f /tmp/log_output"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    # Log to the second terminal
    temp_log_path = '/tmp/log_output'
    with open(temp_log_path, 'w') as temp_log_file:
        temp_log_file.write("")  # Ensure the file is created/cleared
    terminal_handler = logging.FileHandler(temp_log_path)
    terminal_handler.setFormatter(formatter)
    logger.addHandler(terminal_handler)

    logger.info("Logger initialized. Logging to 'latest.log'.")
    
    return logger