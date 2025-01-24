from typing import Any, Type


class ClassUtils:
    @staticmethod
    def instance(obj: Any, cls_types: tuple[Type])->bool:
        return any(isinstance(obj, cls_type) for cls_type in cls_types)