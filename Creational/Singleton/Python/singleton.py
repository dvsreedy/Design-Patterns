class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.value = value
            self.initialized = True

# Example usage:
if __name__ == "__main__":
    singleton1 = Singleton("First Instance")
    print(singleton1.value)  # Output: First Instance

    singleton2 = Singleton("Second Instance")
    print(singleton2.value)  # Output: First Instance

    print(singleton1 is singleton2)  # Output: True
# singleton.py
