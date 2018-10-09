
-----------

1. 分支管理策略
    1）master分支
    非常稳定的，只用来发布新版本，平时不在上面干活
    2）dev分支
    不稳定的，主要在上面干活，每个人都有自己的分支，时不时的往dev分支上合并

    通常，合并分支时，如果可能，Git会用`Fast forward`模式，但这种模式下，删除分支后，会丢掉分支信息。
    如果要强制禁用Fast forward模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。
    > git log --graph --pretty=oneline --abbrev-commit

2. Bug分支
    你目前在dev分支上工作，工作到一半，但突然有一个紧急的bug需要修复，可以先保存你的工作现场，修复完bug后，在切回来。
    步骤：
    当前在dev分支上：
        git stash  # 把当前工作现场“储藏”起来
    切换到要修复bug的分支（假定master）：
        git checkout master
        git checkout -b issue-101
        .... 修复问题
        git add filename
        git commit filename
    把修改合并到修复的分支：
        git checkout master
        git merge --no-ff -m "merge fix 101 modification" issue-101
        git branch -D issue-101
    切换回工作现场：
        git checkout dev
        git stash list  # 查看之前保存了哪些工作现场
        git stash drop
        两种恢复方式：
        1）git stash apply恢复，但是恢复后，stash内容并不删除，你需要用git stash drop来删除
            git stash apply stash@{0}
            git stash drop stash@{0}
        2）git stash pop，恢复的同时把stash内容也删了

3. Feature分支
    与bug分支类似
    两条命令：
    1）git branch -d dev_name  # 已经合并完的分支可以使用此命令删除
    2）git branch -d dev_name  # 强制删除分支（未合并的也可以）

4. 多人协作
    多个人在同一分支上工作，如何正确的合并文件？
    两种情况：
    **1）你和他人同时修改同一个文件，他人修改完成，提前推送到远程，如何提交你的修改**
    详细步骤：
        1）试图用git push origin <branch-name>推送自己的修改；
        2）如果推送失败，则因为远程分支比你的本地更新，需要先用git pull拉取远程最新的版本；
        3）如果合并有冲突，则解决冲突，并在本地提交；
        4）没有冲突或者解决掉冲突后，再用git push origin <branch-name>推送
    **2）你和他人操作的不是同一个文件
    详细步骤：
        1）试图用git push origin <branch-name>推送自己的修改；
        2）如果推送失败，先用git pull拉取远程最新的版本；
        3）git add .  # 添加本地的全部修改到暂存区
        4）git commit -m "说明信息"  # 提交更改至本地
        5）git push origin <branch-name>推送本地分支至远程
    提交更改前，都要先git pull拉取远程最新版本  

    当从远程克隆时，Git自动把本地的master分支与远程的master分支对应起来，远程仓库的默认名称是origin。
    查看远程库信息：
        git remote -v
    推送分支：
        git push origin master  把本地的mater分支推送到远程对应的master分支上
        git push origin dev     把本地的dev分支推送到远程对应的dev分支（远程没有dev分支会自动创建一个dev分支）
    创建远程origin的dev分支到本地
        git checkout -b dev origin/dev
    指定本地dev分支与远程origin/dev分支的链接
        git branch --set-upstream-to origin/dev dev
        或
        git branch --track origin/dev dev

5. 标签
    tag是一个容易记住的有意义的名字，它跟某个commit绑定在一起。
    打标签：
        git tag tag_name  # 默认打在最新提交的commit上,当前HEAD的指向
        git tag  # 查看标签
        git show tag_name  # 查看标签详细信息
    在指定的commit上打标签：
        git log --pretty=oneline  # 查看commit id
        git log -a tag_name -m "explain content" commit_id
    推送标签：
        git push origin tag_name    # 推送一个指定的标签
        git push origin --tags      # 推送全部尚未推送到远程的本地标签
    删除标签：
        1) 标签尚未推送到远程
        git tag -d tag_name
        2）标签已推送到远程
        git tag -d tag_name
        git push origin :refs/tags/tag_name

6. Rebase
    解决查看log分支多，混乱的问题；遗留
    



