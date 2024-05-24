import os

# List of project directories
project_directories = [
    # Add directory of required projects
]

for project_dir in project_directories:
    if os.path.isdir(project_dir):
        print(f"Processing repository: {project_dir}")
        os.chdir(project_dir)

        # Check if there is any uncommitted changes
        git_status = os.popen('git status --porcelain').read().strip()
        if git_status:
            # Save uncommitted changes using stash
            os.system('git stash push -m "Auto-generated stash by script"')
            print(f"Uncommitted changes stashed in repository: {project_dir}")

        # Pull the latest changes from the remote repository
        os.system('git pull')
        print(f"Latest changes pulled in repository: {project_dir}")
        
        # If changes were stashed, apply them back
        git_stash_list = os.popen('git stash list').read().strip()
        if git_stash_list:
            os.system('git stash pop')
            print(f"Uncommitted changes restored in repository: {project_dir}")