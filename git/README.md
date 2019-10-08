<https://bitbucket.org/BitPusher16/dotfiles/raw/49a01d929dcaebcca68bbb1859b4ac1aea93b073/refs/git/git_examples.sh>

<https://news.ycombinator.com/item?id=21189256>

```
    git add/rm/commit/status/push
    git branch/checkout/merge/rebase
    git tag/push --tag
```    

 I do everything from a GUI (Fork for macOS) and very rarely have to deal with any complicated issues that require a terminal.
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
