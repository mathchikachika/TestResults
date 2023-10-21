import os, sys

CURRENT_DIR = os.getcwd().replace("\\", "/").replace("C:", "")
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)