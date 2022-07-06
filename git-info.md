# git

## functionality

### adding new changes

* `git add`: add changes from existing files or adds new files to be committed. **step one** of adding changes
	* `git commit -am` also stages all changes and commits in one step. basically combines `git add .` and `git commit -m` into one step. useful if you want to add all changes.
* `git commit`: commit changes to current branch. **step two** of adding changes. use `-m` to specify a message with commit
* `git push`: pushes commits to repo. specify `origin main` to push to github repo where project was originally cloned from
* `git pull`: updates local repo to match github repo.
* `git tag <tagname>`: tags current commit with a short name, specified with tagname. useful if you may have to rollback to certain commit and do not want to use entire hash to specify the commit
* `git stash`: temporarily saving changes. for example, making changes and saving them with stash so you do not have to add or commit changes before switching branches
	* `git stash push "message"`: stash current changes
	* `git stash apply <stashid>` or `git stash pop`: `apply` adds changes from stash back into working directory, and the stash is preserved. `pop` adds the most recent stash's changes to the working directory, and the stash is removed
	* `git stash drop <stashid>`: remove specified stash from list of stashes
	* `git stash list`: list all current stashes
	* `git stash clear`: remove all stashes

### version rollback

* `git reset`: moves branch pointer back to specified commit.
	* use case: wanting to reset to specific commit in local repo, NOT remote
	* how to use
		* `git reset <commit hash/tag>` where commit hash or tag is the commit you are resetting to
		* `git checkout <commit hash/tag> -- <filename to reset>` again, hash/tag is commit you are resetting to. also, filename is the specific file you want to reset in your working directory
* `git revert`: adds new commit with specified version
	* use case: pushed changes that are wrong to remote. want to fix remote essentially.
	* how to use
		* `git revert <commit hash/tag>` where commit hash/tag is the commit you want to undo. doing this will add a new commit that has the state before the commit being reverted
		* `git push origin main` this pushes new commit with change undone to remote so change is undone in remote as well

### remote commands

* `git remote add origin <url>`: adds remote origin for local repository
* `git remote -v`: verifies remote url of repo
* `git push -d origin <branch_name>`: deletes branch (remotely)

### checking status

* `git log`: shows log of all commits, also tells where remote is 
* `git status`: tells which changes are pending. useful when you mess up lol

### branching

* `git branch`: lists all branches in repo
* creating new branch
	* `git branch <branch_name>`: creates new branch
	* `git checkout <branch>`: switches to specified branch
	* `git checkout -b <new_branch_name>`: creates and switches to specified branch
* `git merge <branch>`: merges changes from specified branch into current branch you are on
* `git branch -d <branch_name>`: deletes branch (locally). or specify -D option instead to delete an unmerged branch
* `git rebase`: useful if a branch is opened but another branch is still being worked on. for example, feature branch is created but master is then given another commit. to keep feature updated with main workflow, use `git rebase main` when on feature to add the newest commit of main onto the feature branch. then, to keep all commits separated and linear, switch back to main and use `git rebase feature` to make the git log show all commits linearly.
* `git merge` **vs** `git rebase`: same overall functionality, but rebase is better because it adds all the feature branch commits on top of main. merge just combines all the changes of feature and puts it on top of main in one single commit. downside of git rebase is that it gets weird when using a remote repo and collaborators.
* **note:** `git checkout` changes working directory to match whatever branch or commit was specified
* **another note:** the branch is only pushed to the remote repo if it is unmerged when a push is done. if the branch is created and merged before a push, it is never shown on the remote repo. however, the branch still exists locally.

### gh cli

* (add useful gh commands) 

## todo

* merge, checkout, rebase, deleting remote branch (basically whole section about branching)
* add section about gh cli. mainly creating repo from command line and maybe some other uses of gh cli 
