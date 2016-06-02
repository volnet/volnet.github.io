Git撤销提交
==========

在使用Git进行版本管理的时候，经常会遇到一些错误的提交。

在开始演示之前，我们先建立一个测试的环境。

```
mkdir gittest
cd gittest
git init

echo "a" >> a.md
git add .
git commit -m "add a.md"

echo "b" >> b.md
git add .
git commit -m "add b.md"

echo "c" >> c.md
git add .
git commit -m "add c.md"

rm -rf a.md
git add .
git commit -m "remove a.md"

git remote add origin http://gitserver-url
```

方法一：git revert（推荐）
------------------------

推荐理由：git revert将保留commit历史。假设有a、b、c三次顺序提交，那么假设被回滚到a，则b、c仍然存在，同时会多出d。

```
git log --oneline

931568f remove a.md
f622cef add c.md
2a0c5a9 add b.md
6fbba34 add a.md

＃ 假设要回到2a0c5a9

git revert -n 2a0c5a9..931568f

# ls可以看到工作目录中的文件已经恢复到当时的状态，这个时候查询git status将看到 2a0c5a9 commit前的状态。

# 这时候需要重新提交文件

git commit -m "revert 2a0c5a9..931568f and recommit"

git push

```

方法二：git reset --hard（不推荐）
-----------------------------

不推荐理由：git reset将使历史无法恢复。假设有a、b、c三次顺序提交，那么假设被回滚到a，则b、c将不复存在。

```
git log --oneline 

931568f remove a.md
f622cef add c.md
2a0c5a9 add b.md
6fbba34 add a.md

# 假设我们要恢复到2a0c5a9，则可以

git reset --hard 2a0c5a9

# 此时ls你将看到a.md

git push -f

#这里需要增加-f或者--force命令，原因当前的HEAD指针指向了一个旧版本，而服务器上这个版本不是最新版本。其实服务器并不知道你是使用reset命令得到的旧版本，以为你是一个长期没有获取最新版本的用户，提交了一个错误的版本。因此它会建议你git pull之后再更新。如果你非常明确你要这么做，并且不关心你目标版本之后的版本（可能包含别人的提交），你大可以就此使用-f来强制提交。同时你将获得一个干净的历史，就像什么都没有发生过一样。

```
