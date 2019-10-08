<https://git-fork.com/> Fork: UI for Git

<https://bitbucket.org/BitPusher16/dotfiles/raw/49a01d929dcaebcca68bbb1859b4ac1aea93b073/refs/git/git_examples.sh>

<https://news.ycombinator.com/item?id=21189256>

```
    git add/rm/commit/status/push
    git branch/checkout/merge/rebase
    git tag/push --tag
```    

When I want to get back to a pristine state, I prefer
$ git reset --hard origin/master

over the suggested

$ git reset --hard HEAD

If you use git and don't know the difference, read this: 
<https://stackoverflow.com/questions/8196544/what-are-the-git-concepts-of-head-master-origin>

*HEAD: the current commit your repo is on. Most of the time HEAD points to the latest commit in your current branch, but that doesn't have to be the case. HEAD really just means "what is my repo currently pointing at".

In the event that the commit HEAD refers to is not the tip of any branch, this is called a "detached head".

*master: the name of the default branch that git creates for you when first creating a repo. In most cases, "master" means "the main branch". Most shops have everyone pushing to master, and master is considered the definitive view of the repo. But it's also common for release branches to be made off of master for releasing. Your local repo has its own master branch, that almost always follows the master of a remote repo.

*origin: the default name that git gives to your main remote repo. Your box has its own repo, and you most likely push out to some remote repo that you and all your coworkers push to. That remote repo is almost always called origin, but it doesn't have to be.

HEAD is an official notion in git. HEAD always has a well-defined meaning. master and origin are common names usually used in git, but they don't have to be.


- Always pull w/ rebase for the current branch.

- Always merge other branches into your current branch, eg master -> feature.

- Always stage individual chunks of code one at a time to make sure I'm committing the right stuff.

- Always squash feature branches into a single commit when merging back.

- Stash changes if needed when switching branches.

- Cherry-pick one-off commits if needed.

- Append a previous commit that I haven't pushed yet if I happened to forget something.

- For complicated merge conflicts I switch to Visual Studio Code which also has a great GUI.

I constantly use
    git commit --fixup 6138D3A
    git rebase --autosquash --interactive origin/master
to keep a clean history of cohesive commits. Rarely do I change _everything_ required for an objective in one go, I still like to commit as I work, I just like the finished product to _seem_ like I did it in one go, for future maintainers' sake.
And I rebase to catch up with upstream, I can't stand having intermediate merge commits in my history and rebasing lets you resolve conflicts as they're introduced, instead of an all-at-once at the end.


When I merge my feature back to origin/master I do `git merge --squash myFeatureBranch` which automatically rebases everything and keeps a clean history.

 If I'm working on a feature that I haven't pushed up yet I might squash my commits together for a cleaner history (it also helps with rebasing). 
 
 If you ever mess up a rebase and finish it before you're able to abort you can use `git reflog` to get a reference back to the previous commit. It's come super handy a few times.
