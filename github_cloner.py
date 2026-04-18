import os
import subprocess

def clone_repo(github_url: str):
    """
    Clones a GitHub repository using the provided URL.

    Parameters:
    github_url (str): The URL of the GitHub repository to clone.

    Returns:
    None
    """
    if not github_url:
        raise ValueError("The GitHub URL must be provided.")

    # Command to clone the repo
    command = ['git', 'clone', github_url]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f'Repository cloned successfully: {github_url}')
    except subprocess.CalledProcessError:
        print(f'Error while cloning the repository: {github_url}')
        raise

if __name__ == '__main__':
    url = input('Enter the GitHub repository URL to clone: ')
    clone_repo(url)