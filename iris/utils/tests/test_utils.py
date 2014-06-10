from unittest import TestCase

from iris.utils import import_object, Undefined


class ImportTests(TestCase):

    def test_import_object(self):
        from iris.core.container import ServiceContainer
        cls = import_object('iris.core.container:ServiceContainer')
        self.assertIs(cls, ServiceContainer)

    def test_import_object_without_colon(self):
        self.assertRaises(ImportError, import_object, 'iris.core.container.ServiceContainer')

    def test_allows_to_import_plain_modules(self):
        import iris.utils as expected_mod
        mod = import_object('iris.utils')
        self.assertIs(mod, expected_mod)


class UndefinedTests(TestCase):
    def test_properties(self):
        self.assertNotEqual(Undefined, None)
        self.assertNotEqual(Undefined, False)
        self.assertFalse(bool(Undefined))
        self.assertEqual(str(Undefined), 'Undefined')
