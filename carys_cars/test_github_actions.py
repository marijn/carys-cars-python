import unittest


class GithubActionsTest(unittest.TestCase):
    def test_it_breaks_the_build(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
