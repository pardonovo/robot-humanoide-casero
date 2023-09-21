import struct
import smbus
import sys
import time
import subprocess

subprocess.run(['/usr/local/bin/x750shutdown.sh'], check=True, shell=True)

