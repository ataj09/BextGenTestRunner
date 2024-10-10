import subprocess
import os
import glob


def check_file_integrity():
    """Check if programA is in the same directory as programB"""
    current_dir = os.getcwd()
    files = glob.glob(os.path.join(current_dir, 'programA.py'))

    if files:
        return files[0]
    else:
        return None

def send_command(process, command):
    """Sends command to the process (programA)"""
    process.stdin.write(command + "\n")
    process.stdin.flush()
    return process.stdout.readline().strip()

def main():

    programA_path = check_file_integrity()
    if not programA_path:
        print('Program A is missing')
        return

    #starts program A as new process
    process = subprocess.Popen(
        ["python", programA_path],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True
    )

    hi_test = send_command(process, "Hi")

    if hi_test == "Hi":
        print("Program A seems to be working correctly")
    else:
        print(f"Something went wrong, program A responded: {hi_test}")

    numbers = []
    for _ in range(100):
        numbers.append(int(send_command(process, "GetRandom")))

    send_command(process, "Shutdown")
    process.wait()

    numbers.sort()
    for i, val in enumerate(numbers):
        print(f"element {i + 1}: {val}")

    print(f"Median: {(numbers[49] + numbers[50])/2}")
    print(f"Average: {sum(numbers) / 100}")

if __name__ == '__main__':
    main()