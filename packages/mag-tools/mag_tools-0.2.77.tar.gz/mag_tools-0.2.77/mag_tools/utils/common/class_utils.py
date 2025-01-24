from typing import Any, Tuple, Type


class ClassUtils:
    @staticmethod
    def isinstance(obj: Any, cls_types: Tuple[Type,...])->bool:
        return any(isinstance(obj, cls_type) for cls_type in cls_types)