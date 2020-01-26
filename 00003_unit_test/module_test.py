import unittest
import module


class ModuleTest(unittest.TestCase):
    def testGreeting(self):
        self.assertEqual("Hello, John", module.greeting("John"))
        self.assertNotEqual("Hello, Jane", module.greeting("Jena"))


if __name__ == "__main__":
    unittest.main()
