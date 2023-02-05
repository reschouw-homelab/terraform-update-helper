import subprocess

def is_available():
    results = subprocess.run(["terraform", "version"], capture_output=True)
    return results.returncode == 0

def get_version():
    results = subprocess.run(["terraform", "version"], capture_output=True, text=True)
    return results.stdout.split('\n', 1)[0]

#def plan():
#    output = subprocess.run("echo terraform plan")