# git

## functionality

### adding new changes

* `git add`: add changes from existing files or adds new files to be committed. **step one** of adding changes
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

### checking status

* `git log`: shows log of all commits, also tells where remote is 
* `git status`: tells which changes are pending. useful when you mess up lol

## todo

* merge, checkout, rebase, deleting remote branch (basically whole section about branching)
* add section about gh cli. mainly creating repo from command line and maybe some other uses of gh cli 
