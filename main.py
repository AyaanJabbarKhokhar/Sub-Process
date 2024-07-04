import subprocess
import time

cmd_str = "nod main.js"

print("Python Code Started!")
time.sleep(1)
subprocess.call(["node" , "main.js"])

print("File Executed!")