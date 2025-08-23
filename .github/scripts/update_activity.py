from github import Github
import os
from datetime import datetime

def main():
    print("✅ Activity script is working!")
    # Create a simple file to test
    with open("test_output.txt", "w") as f:
        f.write(f"Script ran at: {datetime.now()}")
    print("✅ Test file created!")

if __name__ == "__main__":
    main()
