import platform
import subprocess

def print_system_uptime():
    system = platform.system()
    if system == "Windows":
        output = subprocess.check_output("net stats srv", shell=True, text=True)
        for line in output.splitlines():
            if "Statistics since" in line:
                print(f"System uptime info: {line}")
                break
    elif system in ["Linux", "Darwin"]:
        output = subprocess.check_output("uptime -p", shell=True, text=True)
        print(f"System uptime: {output.strip()}")
    else:
        print("Unsupported OS")

if __name__ == "__main__":
    print_system_uptime()
