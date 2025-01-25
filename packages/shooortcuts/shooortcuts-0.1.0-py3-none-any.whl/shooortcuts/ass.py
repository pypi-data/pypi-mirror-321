from .common import get_repo, get_version_from_last_commit, print_git_log


def ass_command():
    repo = get_repo()

    # Check if there are any changes
    if not repo.is_dirty(untracked_files=True):
        print("No changes to commit")
        return

    version = get_version_from_last_commit()

    # Add all changes
    repo.git.add(".")

    # Commit with version
    message = f"gitCMD: auto temp commit for {version}"
    repo.index.commit(message)
    print(f"Created temporary commit with version: {version}")
    print_git_log()
