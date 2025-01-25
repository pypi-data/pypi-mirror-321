"""An example of a custom formatter that formats log messages with HTML parse mode and with custom emojis."""

import logging

from python_telegram_logging import ParseMode, QueuedTelegramHandler, SyncTelegramHandler


class TelegramHTMLFormatter(logging.Formatter):
    """Custom formatter that creates HTML-formatted messages for Telegram."""

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record as HTML with custom emojis."""
        # Add HTML formatting for different log levels.
        level_colors = {"DEBUG": "⚪️", "INFO": "🔵", "WARNING": "🟡", "ERROR": "🔴", "CRITICAL": "⛔️"}

        # Get the emoji for the log level
        level_emoji = level_colors.get(record.levelname, "⚪️")

        # Format timestamp.
        timestamp = self.formatTime(record, self.datefmt)

        # Format the basic message.
        message = super().format(record)

        # Create HTML-formatted message.
        html_message = (
            f"{level_emoji} <b>{record.levelname}</b> " f"[{timestamp}]\n" f"<code>{record.name}</code>\n" f"{message}"
        )

        # Add exception info if present.
        if record.exc_info:
            html_message += f"\n\n<pre>{self.formatException(record.exc_info)}</pre>"

        return html_message


# Usage example for SyncTelegramHandler wrapped with QueuedTelegramHandler.
if __name__ == "__main__":
    # Create base handler.
    base_handler = QueuedTelegramHandler(
        handler=SyncTelegramHandler(token="YOUR_BOT_TOKEN", chat_id="YOUR_CHAT_ID", parse_mode=ParseMode.HTML)
    )

    # Wrap with queued handler.
    handler = QueuedTelegramHandler(handler=base_handler)

    # Create and set custom formatter.
    formatter = TelegramHTMLFormatter()
    handler.setFormatter(formatter)

    # Set up logger.
    logger = logging.getLogger("MyApp")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    # Test logging.
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")

    try:
        raise ValueError("Something went wrong!")
    except ValueError:
        logger.exception("An error occurred")
