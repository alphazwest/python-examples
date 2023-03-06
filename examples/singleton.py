import threading


class Singleton:
    """
    Custom implementation of a singleton class that creates an initial instance
    in a thread-safe manner.
    """
    # defines the instance reference
    _instance = None
    
    # gets a lock
    _lock = threading.Lock()

    def __new__(cls):
        """
        Defines the construction of a new Instance of the object which is 
        equivalent to `get_instance()` approaches taken in other languages.
        """
        if cls._instance is None:
            with cls._lock:
                # gets a lock on the object to ensure thread-safety; will 
                # create a new instance if none already exists
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    
        # returns the instance of the object - new or existing.
        return cls._instance
