### 1. Git 的基本配置

- 系统配置（对所有用户`--system`）：`%Git%/etc/gitconfig`
- 用户配置（对当前用户`--global`）：`~/.gitconfig`
- 仓库配置（对当前项目`--local`）：当前仓库的`.git/config`

每一个级别的配置会覆盖上层的相同配置。

#### (1). 配置个人身份

```apl
$ git config --[] user.name "你的名字"
$ git config --global user.email "你的邮箱@example.com"
```

#### (2). 服务器认证配置

##### a. http / https

* 添加 HTTPS 证书信任：

```apl
$ git config http.sslverify false
```

##### b. ssh

###### ①配置 SSH 密钥路径：

```apl
$ git config --global core.sshCommand "ssh -i ~/.ssh/id_rsa"
```

###### ②与服务器的认证配置过程：

1. 生成公钥

```apl
$ ssh-keygen -t rsa -C 12345678910@qq.com
```

2. 添加公钥到代码平台

* 登录代码平台  ”Profile Settings“  ”SSH Keys“  ”Add SSH Key“，将生成的公钥内容复制到 "Public Key"栏即可。

### 2. Git 基本命令

#### (1). 基础知识

##### a. 三种工程区域：

1. **版本库（Respository）**
2. **工作区（Working Directory）**
3. **暂存区（Stage）**

##### b. 三种文件状态：

1. **已修改（modified）**
2. **已暂存（staged）**
3. **已提交（committed）**

#### (2). 操作

##### a. 工程准备：

```
$ git init # 工程初始化
$ git clone # 工程克隆
```

##### b. 查看工作区：

```
$ git diff # 查看工作区文件修改内容
$ git status # 查看工作区文件状态
```

![git-查看工作区](http://113.45.142.235:9001/laffrex/pictures/2024/10/13/202410131429067.png)

##### c. 文件修改：

```
$ git add # 新增文件到暂存区
$ git rm # 删除文件到暂存区
$ git mv # 移动文件到暂存区
```

##### d, 文件提交：

```
$ git commit
```

##### e. 文件推送：

```
$ git push
```

##### f. 查看日志：

```
$ git log
```

![git-查看日志](C:/Users/26254/AppData/Roaming/Typora/typora-user-images/image-20241013143123532.png)

##### g. 分支管理：

```
git branch # 列出本地分支
git branch / git checkout -b # 新建分支
git branch -d # 删除分支
git checkout # 切换分支
git pull # 更新分支
git merge # 合并分支
git rebase # 变基分支
```