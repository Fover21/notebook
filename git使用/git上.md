## 建立本地版本库
## 本地版本库与远程关联
## 修改文件并提交
## 创建分支,修改文件合并至master


1. git的由来
    linux系统是很多开发者贡献代码不断完善的,linux的创始人linus起初管理贡献者的代码,是通过手工的方式,但随着代码的增多,很难通过手工方式去管理,于是找了一个商业的版本控制系统BitKeeper管理代码.
    开发Samba的Andrew试图破解BitKeeper的协议（这么干的其实也不只他一个），被BitMover公司发现了（监控工作做得不错！），于是BitMover公司怒了，要收回Linux社区的免费使用权。
    Linus可以向BitMover公司道个歉，保证以后严格管教弟兄们，嗯，这是不可能的。实际情况是这样的：
    Linus花了两周时间自己用C写了一个分布式版本控制系统，这就是Git！一个月之内，Linux系统的源码已经由Git管理了！

2. 集中式与分布式区别
    - 集中式： cvs, svn
    版本库集中放在中央服务器上,所有人干活时,都要先从中央服务器获取最新版本到本地,然后在本地修改,干完活后,将修改推送到中央服务器.
    **必须联网**才能工作.
    - 分布式
    每个人的电脑都是一个版本库,工作的时候 **不需要联网**,直接在本地修改,提交就可以.你和同事同时修改一个文件A,修改完成后互相将自己修改的文件推送给对方即可.
    **安全性高**, 每个人的本地都有一个完整的版本库,某个人的电脑突然崩溃,从其他人那直接copy一份就可以了.
    但集中式版本控制系统,一旦中央服务器垮掉,版本库信息就都丢失了.

3. 创建版本库,添加文件
命令:
    - 创建版本库
        mkdir studyGit
        git init
    - 添加文件
        vim readme.txt
        git add readme.txt
        git commit -m "注释说明,方便自己或他人查看"

4. 修改文件并提交
命令:
    - vim  编辑修改文件内容
    - git status  查看当前仓库状态
    - git diff filename  查看文件具体改动内容
    - 提交:
        git add filename
        git commit -m "本次提交注释说明"

5. 版本回退
Git的版本回退速度非常快，因为Git在内部有个指向当前版本的HEAD指针，当你回退版本的时候，Git仅仅是把HEAD指向至你切换的版本.
命令:
    - 回退到上一个版本
        git reset --hard HEAD^
    - 回退到上上版本
        git reset --hard HEAD^^
    - 回退到指定版本
        git log  查看你要切换版本的commit id
        或 git log --pretty=oneline
        git reset --hard target_commit_id
    - 回退之后后悔了,想切换到回退前的版本
        1) 通过git log是找不到回退前那次提交的日志的,没办法指定commit id回退切换
        2) 通过git reflog查看, git reflog是记录我们的历史命令的,找到你那次提交历史命令前的commit id,即可切换回去

6. 工作区和暂存区
    工作区: 电脑上直接看到的,你管理的文件夹(使用git init创建的),就是工作区
    暂存区: 在工作区下,隐藏的.git文件夹,其中有很多文件,有几个重要的要理解:
            - 暂存区: stage
            - 版本信息(master分支)
            - HEAD指针,指向具体分支
    提交工作区的文件修改或新增文件:
        1) git add files  -> 实际将这些修改先推送到本地暂存区(暂存区中存放了所有待提交的文件)
        2) git commit -m "说明"  -> 提交暂存区中的所有文件至master或分支版本

7. 管理修改
    工作区中readme.txt文件
    1) 第一次修改, 增加一行内容, git add readme.txt
    2) 第二次修改, 又增加了一行内容, 但未执行 git add readme.txt
    3) git commit -m "注释"; 那么此次提交的只是第一次修改的内容
    git diff HEAD -- readme.txt  查看工作区中与版本库中的不同之处

8. 撤销修改
    1) 工作区修改,改乱了,还没有提交至暂存区; 可以通过 git checkout -- filename 恢复至与版本库一致的状态
    2) 工作区修改,改乱了,但之前已提交至暂存区,撤销修改:
        git reset HEAD filename  把暂存区的修改撤销掉(unstage)
        git checkout -- filename  恢复工作区与版本库一致

9. 删除文件
    git rm filename
    git commit -m "delete file filename"

10. 远程仓库关联
    1) 创建ssh key:
    ssh-keygen -t rsa -C "youremail@example.com"  # 一路回车即可
    在用户主目录里会生成一个.ssh文件夹,里面有id_rsa和id_rsa.pub, id_rsa是私钥, id_rsa.pub是公钥;
    登录github,进入个人账户settings页面,选择ssh key -> add new; 添加, 将id_rsa.pub复制到页面中,完成.
    2) 添加远程仓库
        - 在github网站新增仓库,与本地要关联的仓库同名
        - 进入本地仓库所在的目录, git remote add origin <新增的远程仓库地址>
        - git push -u origin master  # 将本地仓库的master分支推送到远程服务器上,后续提交可以省略参数-u(远程初始仓库为空,所以加-u)
        - 本地修改文件,提交; 推送至远程

11. 克隆远程仓库
    进入你想保存仓库的路径,然后执行:
    git clone <远程仓库地址>

12. 创建与合并分支
查看分支：git branch

创建分支：git branch <name>

切换分支：git checkout <name>

创建+切换分支：git checkout -b <name>

合并某分支到当前分支：git merge <name>

删除分支：git branch -d <name>

13. 解决冲突
    1) 在分支上修改了文件,并commit
    2) 在mster上修改了文件,并commit
    3) git merge <ranchname>; 报错, 无法实现快速合并, 需先解决冲突, 把冲突文件改成自己想要的内容,
    然后 git add filename, git commit -m "注释".        




