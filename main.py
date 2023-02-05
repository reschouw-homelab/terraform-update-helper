import sys
import terraform

# Check terraform executable is available and print version
if terraform.is_available():
    version = terraform.get_version()
    print("Using " + version)
else:
    print("Terraform executable not found. Check your $PATH and try again!")
    sys.exit(1)
