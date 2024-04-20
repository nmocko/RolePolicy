import json


def role_policy_check(path_to_file):

    try:
        file = open(path_to_file)
    except IOError:
        print(f"Error: File {path_to_file} does not exist.")
        return False

    data = json.load(file)
    file.close()

    try:
        statement = data["PolicyDocument"]["Statement"]
    except KeyError:
        print("Error: No statement field in AWS::IAM::Role Policy")
        return False

    for i in statement:
        if "Resource" in i:
            if isinstance(i["Resource"], str):
                if i["Resource"] == "*":
                    return False
            elif isinstance(i["Resource"], list):
                for j in i["Resource"]:
                    if j == "*":
                        return False

    return True
