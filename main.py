import sys
from RolePolicy import role_policy_check


if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print(f"Usage: main.py [file ...]")
        exit(0)

    for file in sys.argv[1:]:
        print(role_policy_check(file))
