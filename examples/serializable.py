from abc import ABC, abstractmethod


class Serializable(ABC):
    """
    ABC Implementation of a class whereby the methods of serializing and deserializing
    an object are defined. Useful for objects that get transferred via REST APIs where
    a more formalized system/framework does not already define the serialization process.
    """
    @abstractmethod
    def serialize(self) -> str:
        """
        Creates a JSON-formattable serialized version of the object.
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def deserialize(data: str) -> "Serializable":
        """
        Given the serialized representation of a Serializable object,
        return an object of that class.
        """
        raise NotImplementedError
