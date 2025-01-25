from constattr.const_enforcer_meta import ConstantEnforcerMeta


def constclassattrs(cls: type):
    cls_has_metaclass = type(cls) != type
    if cls_has_metaclass:
        constant_enforcer_metaclass = __combine__with_constant_enforcer_meta(type(cls))
    else:
        constant_enforcer_metaclass = ConstantEnforcerMeta
    return constant_enforcer_metaclass(cls.__name__, cls.__bases__, dict(cls.__dict__))


def __combine__with_constant_enforcer_meta(cls):
    return type(
        'ConstantEnforcerCombinedMeta',
        (ConstantEnforcerMeta,) + cls.__bases__,
        dict(cls.__dict__)
    )
