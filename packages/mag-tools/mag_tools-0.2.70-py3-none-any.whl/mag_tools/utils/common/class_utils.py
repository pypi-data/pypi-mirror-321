from typing import Any, Set, Type


class ClassUtils:
    @staticmethod
    def isinstance_in(obj: Any, keywords: Set[Type])-> bool:
        return any(isinstance(obj, keyword) for keyword in keywords)