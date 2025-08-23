from github import Github
import os
from datetime import datetime

def main():
    try:
        print("Script started!")
        
        # Initialize GitHub
        g = Github(os.environ['GITHUB_TOKEN'])
        repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
        
        print(f"Connected to repo: {repo.full_name}")
        
        # Create a simple test file to verify the script works
        test_content = f"Last updated by GitHub Actions: {datetime.now()}"
        
        # Try to update a file
        try:
            # Check if file exists
            try:
                contents = repo.get_contents("activity_test.txt")
                # Update existing file
                repo.update_file(
                    contents.path,
                    "Test update from GitHub Actions",
                    test_content,
                    contents.sha
                )
                print("✅ Updated existing test file")
            except:
                # Create new file
                repo.create_file(
                    "activity_test.txt",
                    "Test create from GitHub Actions",
                    test_content
                )
                print("✅ Created new test file")
                
        except Exception as e:
            print(f"❌ Error with file operation: {e}")
            
    except Exception as e:
        print(f"❌ Main error: {e}")
        raise e

if __name__ == "__main__":
    main()
