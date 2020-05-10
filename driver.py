import IOUtils
import RepoMiner
import os

projectMap = {}

repository_list = "./repos_small_2.txt"
bug_fixing_commits_dir = "./bug_fixing_commits"
path_to_local_repos = "./repos_to_analyze"

# Delete output folder to re-run buggy commit extraction
if not os.path.exists(bug_fixing_commits_dir):
   RepoMiner.extractBuggyCommits(repository_list,path_to_local_repos,bug_fixing_commits_dir)

# read in buggy commits
IOUtils.readBugMap(projectMap,"./bug_fixing_commits")