import logging
import os
import time
from pathlib import Path

import yaml
from torch.utils.tensorboard.writer import SummaryWriter

from audiozen.accelerate import is_rank_zero


class TensorboardLogger(SummaryWriter):
    def __init__(self, log_dir: str = "") -> None:
        super().__init__(log_dir=log_dir, max_queue=5, flush_secs=30)

    def log_config(self, config: dict) -> None:
        self.add_text(tag="Configuration", text_string=f"<pre>  \n{yaml.dump(config)}  \n</pre>", global_step=1)


def init_logging_logger(output_dir):
    """Initialize logging logger with `console` and `file` handlers.

    Args:
        log_fpath: Path to save log file.

    Examples:
    ```
    # Call this function at the beginning of main file.
    init_logger(log_fpath="log_path")
    # Use this logger in other modules.
    import logging

    logger = logging.getLogger(__name__)
    logger.info("info message")
    ```
    """
    # Parse log_fpath
    output_dir = Path(output_dir) if isinstance(output_dir, str) else output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # disable logging for libraries that use standard logging module
    logging.getLogger("matplotlib").setLevel(logging.WARNING)
    logging.getLogger("numba").setLevel(logging.ERROR)

    # Create logger
    logger = logging.getLogger()

    # Set the lowest level of root logger and controls logging via handlers' level
    logger.setLevel(logging.DEBUG)

    # Get log level from environment variable
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()

    # Create a console handler and set level to info
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level=log_level)

    # Create a file handler and set the logger level to debug
    time_now = time.strftime("%Y_%m_%d--%H_%M_%S")
    file_handler = logging.FileHandler(str(output_dir / f"{time_now}.log"))
    file_handler.setLevel(level=log_level)

    # Create formatters (file logger have more info)
    console_formatter = logging.Formatter(
        "%(asctime)s: %(message)s",
        datefmt="%m-%d %H:%M:%S",
    )
    file_formatter = logging.Formatter(
        "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]: %(message)s",
        datefmt="%m-%d %H:%M:%S",
    )

    # Add formatter to ch
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)

    # Add ch to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    if is_rank_zero():
        logger.info(f"Initialized logger with log file in {output_dir.as_posix()}.")
