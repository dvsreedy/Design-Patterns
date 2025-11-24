""""
Problem Statement:
Design and implement a Logger subsystem that supports multiple types of loggers and 
ensures that only one instance of each logger type is created throughout the application’s lifecycle.


Factory Requirement

Add a LoggerFactory that:

Accepts a logger type (e.g., "console", "file", "db")

Returns the correct logger instance

Ensures the Singleton constraint is respected
"""

from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

class FileLogger(Logger):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FileLogger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str) -> None:
        print(f"FileLogger: {message}")

class ConsoleLogger(Logger):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConsoleLogger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str) -> None:
        print(f"ConsoleLogger: {message}")

class DatabaseLogger(Logger):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseLogger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str) -> None:
        print(f"DatabaseLogger: {message}")

class LoggerFactory():
    def get_logger(self, logger_type: str) -> Logger:
        if logger_type == "file":
            return FileLogger()
        elif logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "db":
            return DatabaseLogger()
        else:
            raise ValueError(f"Unknown logger type: {logger_type}")


if __name__ == "__main__":

    factory = LoggerFactory()

    file_logger1 = factory.get_logger("file")
    file_logger2 = factory.get_logger("file")
    console_logger1 = factory.get_logger("console")
    console_logger2 = factory.get_logger("console")
    db_logger1 = factory.get_logger("db")
    db_logger2 = factory.get_logger("db")

    file_logger1.log("This is a file log message.")
    console_logger1.log("This is a console log message.")
    db_logger1.log("This is a database log message.")

    print(f"FileLogger instances are the same: {file_logger1 is file_logger2}")
    print(f"ConsoleLogger instances are the same: {console_logger1 is console_logger2}")
    print(f"DatabaseLogger instances are the same: {db_logger1 is db_logger2}")