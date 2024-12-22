from dotenv import load_dotenv
load_dotenv()
import os

#!/usr/bin/env python3

print("Fuck Bioengineering!")

# Get the value of the environment variable
env_var = os.environ.get("MY_VAR")

# Print the environment variable
if env_var:
    print(f"The value of MY_VARIABLE is: {env_var}")
else:
    print("MY_VARIABLE is not set.")

