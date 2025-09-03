# first line

import time

def log_event(ip, mail, status, reason, logfile="logs/server.log"):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"{now} - {ip} - {mail} - {status} - {reason}\n"
    print(line.strip())
    with open(logfile, "a") as f:
        f.write(line)

# last line