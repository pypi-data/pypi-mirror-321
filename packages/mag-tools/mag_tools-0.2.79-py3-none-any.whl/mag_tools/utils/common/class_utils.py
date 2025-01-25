from typing import Any, Optional, Tuple, Type


class ClassUtils:
    @staticmethod
    def isinstance(bean: Any, cls_types: Tuple[Type,...])->bool:
        return any(isinstance(bean, cls_type) for cls_type in cls_types)

    @staticmethod
    def get_field_type(bean_class: Type, field_name: str) -> Optional[Type]:
        """
        根据对象和字段名获取字段的类型

        :param bean_class: 对象类型
        :param field_name: 字段名
        :return: 字段的类型
        """
        # 获取对象的类型注解
        annotations = getattr(bean_class, '__annotations__', {})

        # 返回字段的类型
        return annotations.get(field_name, None)

if __name__ == '__main__':
    # 示例使用
    class MyClass:
        name: str
        age: int

    obj = MyClass()
    field_type = ClassUtils.get_field_type(obj.__class__, 'name')
    print(field_type)
