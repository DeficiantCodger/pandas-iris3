import os
import subprocess 

# os.system("pip install -r src/requirements.txt")
# os.system("pip install kedro")
# os.system(" pip install great-expectations")
# os.system(" pip install pytest")
# os.system(" pip install pytest-cov")
# os.system(" pip install sphinx")
# os.system("kedro run")

print(subprocess.check_output("kedro -help",shell = True))


