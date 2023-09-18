#Research Task

- ###Version Control
  it is using to manage the process of the software and maintain the source code.
  How does it work?
  Let's say we are making a software and has nine functions is distributed in 3 milestones. so when we finish each milestone we call the software with new version I.E v1.0 v1.1 v2 and so on. It helps the team and the manager to know where the software is and what is the upcoming steps to do. And it is very helpful in maintaining the software and add more features and improve continuously one of the popular Version control systems in Git And we will talk about it in the next section
- ###Git
  As we mentioned before git is a version control system it handles projects whether they is small or large.Its performance is fast and handling the commit to the source and getting from it smoothly
- ###Why GitHub works only with git?
  Because Git is a version control system and GitHub is a website the built based on git we use GitHub to enhance our experience but when we use GitHub we actually using git functionalities like push , commit , making branches , making pull requests and so on
- ###add git to the project
  We talked about the benefits of using git in any project even you is making it alone or with a team now we will talk about how to add it to your project using CMD or powerShell (you have to install git on your pc you can use this command `winget install --id Git.Git -e --source winget` ) 
  You go to the directory that contains your project files and type `git init`  and then type `git add` and finally type `git commit` to connect your project to GitHub type `git remote add origin git@github.com:username/new_repo` and then type `git push -u origin master`
- ###Main vs. Branches
  The main directory (branch) is the deployed and working source, and it is a branch.
  a branch has all files in the master but in separate way which means when you change the branch the master doesn't change.
  It is important that when you have a released project, no to play with the master branch because any change you do will be deployed, and if it is wrong, the whole software will not be working.
  Now, in brief, the main (master) is the actually working software but any branch is the software but is isolated from the master and any changes won't affect the master branches is using when we are adding a new feature to the software or maintaining it
