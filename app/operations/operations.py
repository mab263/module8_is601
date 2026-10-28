
import logging

logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    result = a + b
    logger.info("Addition performed")
    return result


def subtract(a: float, b: float) -> float:
    result = a - b
    logger.info("Subtraction performed")
    return result


def multiply(a: float, b: float) -> float:
    result = a * b
    logger.info("Multiplication performed")
    return result


def divide(a: float, b: float) -> float:
    if b == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero!")
    result = a / b
    logger.info("Division performed")
    return result
