import unittest

from constattr.decorators import constclassattrs
from constattr.exceptions import ConstAssignmentError


class TestDecorators(unittest.TestCase):
    def test_cannot_reassign_constant_class_attribute(self):
        @constclassattrs
        class Example:
            MY_CONST1 = '1'
            MY_CONST2 = '2'

        with self.assertRaises(ConstAssignmentError) as context:
            Example.MY_CONST1 = 'new value for the constant'

        self.assertEqual('You cannot set the constant MY_CONST1 in class Example', str(context.exception))

    def test_cannot_reassign_constant_class_attribute_of_class_with_metaclass(self):
        class ExampleMeta(type):
            pass

        @constclassattrs
        class Example(metaclass=ExampleMeta):
            MY_CONST1 = '1'
            MY_CONST2 = '2'

        self.assertEqual('ConstantEnforcerCombinedMeta', type(Example).__name__)
        with self.assertRaises(ConstAssignmentError) as context:
            Example.MY_CONST1 = 'new value for the constant'

        self.assertEqual('You cannot set the constant MY_CONST1 in class Example', str(context.exception))

    def test_can_reassign_class_attribute(self):
        @constclassattrs
        class Example:
            class_attr1 = '1'
            class_attr2 = '2'

            MY_CONST1 = '1'
            MY_CONST2 = '2'

        Example.class_attr1 = 'new value'
        Example.class_attr2 = 'another new value'

        self.assertEqual('new value', Example.class_attr1)
        self.assertEqual('another new value', Example.class_attr2)

    def test_can_reassign_instance_attribute(self):
        @constclassattrs
        class Example:
            MY_CONST1 = '1'
            MY_CONST2 = '2'

            def __init__(self, attr1: str):
                self.attr1 = attr1

        example = Example(attr1='value for instance attribute 1')
        example.attr1 = 'new value for instance attribute 1'

        self.assertEqual('new value for instance attribute 1', example.attr1)
