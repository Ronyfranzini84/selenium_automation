import logging 
from pathlib import Path

# Create the logs folder
logs_folder = Path("logs")
logs_folder.mkdir(parents=True, exist_ok=True)

# Configure Logging
logging.basicConfig(
    filename=logs_folder / "selenium.logs",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

# Register events
logging.info("Starting Selenium automation")
logging.info("Browser opened successfully")
logging.warning("Example warning message")
logging.error("Example error message")
logging.info("Automation finished")

print("Log file created successfully")