from typing import Any, Tuple, Type


class ClassUtils:
    @staticmethod
    def isinstance(obj: Any, cls_types: Tuple[Type,...])->bool:
        return any(isinstance(obj, cls_type) for cls_type in cls_types)

    @staticmethod
    def get_field_type(obj: Any, field_name: str) -> Type:
        """
        根据对象和字段名获取字段的类型

        :param obj: 对象
        :param field_name: 字段名
        :return: 字段的类型
        """
        # 获取对象的类型注解
        annotations = obj.__class__.__annotations__

        # 返回字段的类型
        return annotations.get(field_name, None)
