import subprocess
import psutil
import time

def is_process_running(script_name, arg):
    for proc in psutil.process_iter(['pid', 'cmdline']):
        try:
            cmdline = proc.info['cmdline']
            if cmdline and script_name in cmdline and arg in cmdline:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def run_script():
    print("Starting api.py...")
    return subprocess.Popen(["python3", "api.py", "1"])

if __name__ == "__main__":
    process = None

    while True:
        if not is_process_running("api.py", "1"):
            if process:
                print("Stopping api.py...")
                process.terminate()  # Terminate the previous process if it's still running
            process = run_script()  # Start the new process

        time.sleep(1)  # Check every 1 second if the script is running

