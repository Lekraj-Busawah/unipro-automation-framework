import subprocess
import os
import sys

def run_tests():
    # 1. Define the command
    # This runs behave, uses the Allure formatter, and outputs to 'allure-results'
    command = "behave -f allure_behave.formatter:AllureFormatter -o allure-results"
    
    # 2. Add any extra arguments passed to this script (like tags)
    # Example usage: python run.py --tags=@mobile
    if len(sys.argv) > 1:
        command += " " + " ".join(sys.argv[1:])

    print(f"Running command: {command}")
    
    # 3. Execute
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Tests failed (Check report)")
    
    # 4. Optional: Ask to serve report immediately
    choice = input("\nGenerate and serve Allure report? (y/n): ")
    if choice.lower() == 'y':
        subprocess.run("allure serve allure-results", shell=True)

if __name__ == "__main__":
    run_tests()