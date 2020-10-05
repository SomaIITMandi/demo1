### GIT commands

// to clone a git repository
>> git clone http://.....clone_address.git


// After cloning, go to that directory, and then you can check git status
// to see the status
>> git status

// to add file <add file to staging area>
>> git add <file_name>

>> git add .      // shortcut to add all files


// now staging area to local commit
>> git commit -m 'your message'

// log of all your commit history
>> git log

// push your code to git hub
>> git push

// diff between the previous code and current code
>> git difftool HEAD

// before commit it asks to introduce yourself
>> git config --global user.email "you@example.com"

>> git checkout master
>> git pull



git config --global user.email "you@example.com"
  
git config --global user.name "Your Name"


### To create git branch
>> git branch <branch_name>      // then checkout the branch_name

>> git checkout -b <branch_name>   // branch created and checkout at same time

>> git branch -a     // to show all the branches

>> git checkout <branch_name>     // to change from master branch to new branch

>> git branch -d <branch_name>    // to delete the branch, if it's already merged with master

>> git branch -D <branch_name>    // to delete the branch, if it's not merged with master

>> git merge <branch_name>    // do it from master
