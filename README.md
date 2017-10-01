# chumbawumbas
public repo for cs 326 projects

tips for using git:

-make sure you are editing code/generally working in the dev branch
->how to check what branch you’re working in: git branch
switch branches: git checkout <branch name>
git  status: useful to check what branch you’re in, if you have unsaved changes etc.

When you first get started:
1. navigate to your directory using cd
2. make sure you’re in the dev branch
3. git pull (this sees any changes that may have happened when you weren’t working)
~~edit code locally on your machine using whatever text editor you have (I personally like Sublime Text or Atom)~~
4. when you’re ready to upload your changes, git add . (this adds all the files again) or you can also just do git add <name of file you were working on>
5. git commit -m “<short message about what changes you made, this just makes it for other people to see what you’ve worked on>”
6. git push
