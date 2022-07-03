# git

## functionality

### adding new changes

* `git add`: add changes from existing files or adds new files to be committed. **step one** of adding changes
	* `git commit -am` also stages all changes and commits in one step. basically combines `git add .` and `git commit -m` into one step. useful if you want to add all changes.
* `git commit`: commit changes to current branch. **step two** of adding changes. use `-m` to specify a message with commit
* `git push`: pushes commits to repo. specify `origin main` to push to github repo where project was originally cloned from
* `git pull`: updates local repo to match github repo.
* `git tag <tagname>`: tags current commit with a short name, specified with tagname. useful if you may have to rollback to certain commit and do not want to use entire hash to specify the commit

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
* `git branch -d <branch_name>`: deletes branch (locally)
* **note:** `git checkout` changes working directory to match whatever branch or commit was specified

### gh cli

* (add useful gh commands) 

## todo

* merge, checkout, rebase, deleting remote branch (basically whole section about branching)
* add section about gh cli. mainly creating repo from command line and maybe some other uses of gh cli 
