from . import hello_also
from .greetings import hello_also as patrick

if __name__ == '__main__':
    hello_also()

    if hello_also == patrick:
        print("woah they're the same function")
