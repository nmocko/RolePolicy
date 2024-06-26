# RolePolicy

RolePolicy is a Python program designed to verify whether a given AWS IAM Policy allows the application of all resources. If the policy allows, the function returns True; otherwise, it returns False. </br>
This repository contains the main.py file, which is used to verify whether the files provided in the command line meet the above condition. The "test" directory contains unittests to verify the correctness of the functions in RolePolicy.py file. The RolePolicyFiles directory contains tested JSON files with AWS IAM Role Policies.

## How to run

### On Linux:

&emsp;Download ZIP code  
&emsp;Unzip downloaded code with command:  
&emsp;```unzip RolePolicy-main.zip```

&ensp;Usage:

&emsp;Go to ./RolePolicy-main  
&emsp;```cd ./RolePolicy-main```  
&emsp; Run code with command:  
&emsp; ```python3 ./main.py {names of files}```

&ensp;Running unittest

&emsp;Go to ./RolePolicy-main/test  
&emsp;```cd ./RolePolicy-main/test```  
&emsp;Run test with command:  
&emsp;```python3 -m unittest ./RolePolicy_test.py```

### On Windows

&emsp;Download ZIP code  
&emsp;Unzip downloaded code  

&ensp;Usage:

&emsp;Open folder RolePolicy-main  
&emsp;Open terminal in this folder   
&emsp; Run code with command:  
&emsp; ```python3 .\main.py {names of files}```

&ensp;Running unittest

&emsp;Go to RolePolicy-main\test  
&emsp;Open terminal in this folder  
&emsp;Run test with command:  
&emsp;```python3 -m unittest .\RolePolicy_test.py```


