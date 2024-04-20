import unittest
from RolePolicy import role_policy_check


class UnittestRolePolicy(unittest.TestCase):

    def test_role_policy(self):
        self.assertEqual(role_policy_check("../RolePolicyFiles/test_policy_1.json"), False)
        self.assertEqual(role_policy_check("../RolePolicyFiles/test_policy_2.json"), True)
        self.assertEqual(role_policy_check("../RolePolicyFiles/test_policy_3.json"), True)
        self.assertEqual(role_policy_check("../RolePolicyFiles/test_policy_4.json"), False)
        self.assertEqual(role_policy_check("../RolePolicyFiles/test_policy_5.json"), False)
        self.assertEqual(role_policy_check("../RolePolicyFiles/test_policy_6.json"), False)
        self.assertEqual(role_policy_check("../RolePolicyFiles/test_policy_7.json"), True)


if __name__ == "__main__":
    unittest.main()
