import sys
from RolePolicy import role_policy_check

if __name__ == '__main__':
    print(role_policy_check("RolePolicyFiles/test_policy_2.json"))
    # if len(sys.argv) == 1:
    #     print(f"Usage: main.py [file ...]")
    #     exit(0)
    #
    # for i in sys.argv[1:]:

