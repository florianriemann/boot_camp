# git collaboration

28/02/2022

## Setup

1) Open repository at github.com
2) Add collaborator to repo
3) `clone` the repo

## Good practice

* When editing files, you have to check in changes each time with `git add` and `git commit`
* With `git pull` you can request the most recent version of the code
* **Always** run `git commit` before `git pull`
* With `git push` you can publish changes, so that others can see them
* **Always** run `git pull` before `git push` --> to make sure if there is an merge conflict or not (because somebody e.g. pushed a new version during your last pull and push!)

## Common merge strategie during pull
enter:
git config pull.rebase false

## Unwanted changes

* `git checkout .`  	- put HEAD back to last `local` commit 

## Merge conflict

* Both users change the same file at the same position

* Look at file and remove conflict manually

* Concret Scenario:
USER A : 
- pull repo
- change line 2
- add, commit, push
--> remote repo updatet

USER B: 
- pull repo silmutaneously with USER A
- change line 2
- add, commit, push --> AFTER USER B
--> push leads to an error message (Remote contains updates your local repo doesnt contain --> change in line of USER A)

--> run "pull" again!! (What Jens mentioned in line 17: always "git pull" before "git push" to get a note about possible merge conflicts!

- nano <file>

    * Remove marks and unwanted line
    * Save file
    * `git add <file>`
    * `git commit`
    * `git push`

    ```{git}
    <<<<<<< HEAD
    <local commit>
    =======
    <remote commit>
    >>>>>>> <remote>
    ```

    

* set a mergetool, e.g. [kdiff3](http://kdiff3.sourceforge.net/) 

  * Show list of available and supported mergetools

  ```{shell}
  git mergetool --tool-help
  ```

  *   Set mergetool

  ```{shell}
  git mergetool --tool=kdiff3
  ```

  * Run `mergetool`

  ```{shell}
  git mergetool

* Mergetool has 4 windows:
    1.   `base`: file content before conflicting commits (A)
    2.   `local`: file content `local` commit (B)
    3.   `remote`: file content `remote` commit (C)
    4.   New resolved file content

## Merge behavior

*   [Possible settings](https://www.atlassian.com/git/tutorials/using-branches/merge-strategy)

## Git Hooks

* [Introduction](https://githooks.com/)
