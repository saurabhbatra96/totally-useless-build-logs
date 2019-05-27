import time
import random
import re
from datetime import datetime

TIME_PATTERN = r"\[[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\]"

class Printer:
    @staticmethod
    def fastPrint(text):
        Printer.__customPrint(text.splitlines(), 0.05, 0.1)
    
    @staticmethod
    def medPrint(text):
        Printer.__customPrint(text.splitlines(), 0.5, 1)
    
    @staticmethod
    def slowPrint(text):
        Printer.__customPrint(text.splitlines(), 5, 10)
    
    @staticmethod
    def reallySlowPrint(text):
        Printer.__customPrint(text.splitlines(), 60, 120)

    @staticmethod
    def instaPrint(text):
        text = re.sub(TIME_PATTERN, datetime.now().strftime('[%H:%M:%S]'), text)
        print text
    
    @staticmethod
    def __customPrint(textArray, delayMin, delayMax):
        time.sleep(delayMin)
        for t in textArray:
            t = re.sub(TIME_PATTERN, datetime.now().strftime('[%H:%M:%S]'), t)
            print t
            delay = random.random()*(delayMax-delayMin)+delayMin
            # delay = 3
            time.sleep(delay)

# start message  
text = """Started '"""+datetime.now().strftime("%a %b %d %H:%M:%S UTC %Y")+"""' on 'N-WEB05' by 'Git'
Finished '"""+datetime.now().strftime("%a %b %d %H:%M:%S UTC %Y")+"""' with status 'NORMAL Success'
Target URL https://build/viewLog.html?buildId=477326&userId=8790871389002
Target server version is 9.1.5 (build 37377)"""
Printer.fastPrint(text)
while True:
    # chapter 1
    text = """[23:54:03]i: Target server version is 9.1.5 (build 37377)
[23:54:03]W: bt4 (2m:17s)
[23:54:03] : projectId:project55 projectExternalId:NetworkDev buildTypeId:bt4 buildTypeExternalId:NetworkDev
[23:54:03] : Collecting changes in 2 VCS roots (1s)
[23:54:03] :	 [Collecting changes in 2 VCS roots] VCS Root details
[23:54:03] :		 [VCS Root details] "Github - Target Build Configs" {instance id=968, parent internal id=158, parent id=GithubTargetBuildConfigs, description: "git@git:shared/Target-build-configs.git#refs/heads/master"}
[23:54:03] :		 [VCS Root details] "Github - Network" {instance id=939, parent internal id=99, parent id=GithubNetwork, description: "git@git:core/so.git#refs/heads/master"}
[23:54:04]i:	 [Collecting changes in 2 VCS roots] Waiting for completion of current operations for the VCS root 'Github - Target Build Configs'
[23:54:04]i:	 [Collecting changes in 2 VCS roots] Waiting for completion of current operations for the VCS root 'Github - Network'
[23:54:04]i:	 [Collecting changes in 2 VCS roots] Detecting changes in VCS root 'Github - Network' (used in 'Release', 'SENetwork - Dev' and 36 other configurations)
[23:54:04]i:	 [Collecting changes in 2 VCS roots] Will collect changes for 'Github - Network' starting from revision 52173e6ad55dd55da435aaf7dd3343894afb3f1a
[23:54:04]i:	 [Collecting changes in 2 VCS roots] Detecting changes in VCS root 'Github - Target Build Configs' (used in 'ADTools - Dev', 'ADTools - Dev' and 257 other configurations)
[23:54:04]i:	 [Collecting changes in 2 VCS roots] Will collect changes for 'Github - Target Build Configs' starting from revision 35ddc3e78bcae9b7bbb71638dad519abd7d12249
[23:54:04]i: Waiting for the agent to start the build
[23:54:04]i: Agent time zone: UTC
[23:54:04]i: Agent is running under JRE: 1.7.0_72-b14
[23:54:05]W: Swabra (2s)
[23:54:05] :	 [Swabra] Scanning directory /buildAgent/work/6daa56c20f8558cf for newly created, modified and deleted files comparing with snapshot 62e917d.snapshot, paths to monitor are /buildAgent/work/6daa56c20f8558cf, -:/buildAgent/work/6daa56c20f8558cf/**/.git and 7 more paths
[23:54:07]W:	 [Swabra] Detected 18509 unchanged, 1434 newly created (1434 of them deleted), 70 modified, 0 deleted files and directories
[23:54:07] :	 [Swabra] Checkout directory contains modified files or some files were deleted. Need a clean checkout directory snapshot - forcing clean checkout
[23:54:07] : Clearing temporary directory: /buildAgent/temp/buildTmp
[23:54:07] : Publishing internal artifacts (1s)
[23:54:08] :	 [Publishing internal artifacts] Publishing 1 file using [ArtifactsCachePublisher]
[23:54:08] :	 [Publishing internal artifacts] Publishing 1 file using [WebPublisher]
[23:54:07] : Checkout directory: /buildAgent/work/6daa56c20f8558cf
[23:54:07] : Updating sources: agent side checkout (13s)
[23:54:07] :	 [Updating sources] Will perform clean checkout. Reason: Checkout directory is empty or doesn't exist (running for 2m:14s)
[23:54:07] :	 [Updating sources] Cleaning /buildAgent/work/6daa56c20f8558cf
[23:54:09] :	 [Updating sources] Using vcs information from server. Reason: no revision information for build configuration "SENetwork - Dev" and checkout directory /buildAgent/work/6daa56c20f8558cf on agent
[23:54:09] :	 [Updating sources] VCS Root: Github - Network (11s)
[23:54:09] :		 [VCS Root: Github - Network] revision: 52173e6ad55dd55da435aaf7dd3343894afb3f1a
[23:54:09] :		 [VCS Root: Github - Network] [/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" show-ref
[23:54:09] :		 [VCS Root: Github - Network] [/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" ls-remote origin
[23:54:10] :		 [VCS Root: Github - Network] [/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" show-ref refs/heads/master
[23:54:10] :		 [VCS Root: Github - Network] [/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" show-ref refs/heads/master
[23:54:10] :		 [VCS Root: Github - Network] [/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master (1s)
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] remote: Counting objects: 6, done. [K
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] remote: Compressing objects:  16% (1/6)    [K
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] remote: Compressing objects:  33% (2/6)    [K
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] remote: Compressing objects:  50% (3/6)    [K
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] remote: Compressing objects:  66% (4/6)    [K
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] remote: Compressing objects:  83% (5/6)    [K
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] remote: Compressing objects: 100% (6/6)    [K
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] remote: Compressing objects: 100% (6/6), done. [K
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] remote: Total 6 (delta 5), reused 0 (delta 0) [K
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master] From git:core/so
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master]    e4385c6..52173e6  master     -> master
[23:54:12] :			 [[/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" fetch --progress origin +refs/heads/master:refs/heads/master]    e4385c6..52173e6  master     -> origin/master
[23:54:12] :		 [VCS Root: Github - Network] [/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" log -n1 --pretty=format:%H%x20%s 52173e6ad55dd55da435aaf7dd3343894afb3f1a --
[23:54:12] :		 [VCS Root: Github - Network] Cleaning /buildAgent/work/6daa56c20f8558cf
[23:54:12] :		 [VCS Root: Github - Network] The .git directory is missing in '/buildAgent/work/6daa56c20f8558cf'. Running 'git init'...
[23:54:12] :		 [VCS Root: Github - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" init
[23:54:12] :		 [VCS Root: Github - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" remote add origin git@git:core/so.git
[23:54:12] :		 [VCS Root: Github - Network] [/buildAgent/system/git/git-899F01F4.git]: "(x86)/Git/bin/git" pack-refs --all
[23:54:12] :		 [VCS Root: Github - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" config core.sparseCheckout false
[23:54:12] :		 [VCS Root: Github - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" show-ref
[23:54:12] :		 [VCS Root: Github - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" ls-remote origin
[23:54:14] :		 [VCS Root: Github - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" show-ref refs/remotes/origin/master
[23:54:14] :		 [VCS Root: Github - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" log -n1 --pretty=format:%H%x20%s 52173e6ad55dd55da435aaf7dd3343894afb3f1a --
[23:54:14] :		 [VCS Root: Github - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" branch
[23:54:14] :		 [VCS Root: Github - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" reset --hard 52173e6ad55dd55da435aaf7dd3343894afb3f1a"""
    Printer.medPrint(text)
    # chapter 1 finished

    # chapter 2
    text = """[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  15% (2512/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  16% (2559/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  17% (2718/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  18% (2878/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  19% (3038/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  20% (3198/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  21% (3358/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  22% (3518/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  23% (3678/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  24% (3838/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  25% (3997/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  26% (4157/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  27% (4317/15988)   
[23:54:15] :		 [VCS Root: Github - Network] Checking out files:  28% (4477/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  29% (4637/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  30% (4797/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  31% (4957/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  32% (5117/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  32% (5173/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  33% (5277/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  34% (5436/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  35% (5596/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  36% (5756/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  37% (5916/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  38% (6076/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  39% (6236/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  40% (6396/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  41% (6556/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  42% (6715/15988)   
[23:54:16] :		 [VCS Root: Github - Network] Checking out files:  43% (6875/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  44% (7035/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  45% (7195/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  46% (7355/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  47% (7515/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  48% (7675/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  49% (7835/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  50% (7994/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  51% (8154/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  52% (8314/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  52% (8428/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  53% (8474/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  54% (8634/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  55% (8794/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  56% (8954/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  57% (9114/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  58% (9274/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  59% (9433/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  60% (9593/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  61% (9753/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  62% (9913/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  63% (10073/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  64% (10233/15988)   
[23:54:17] :		 [VCS Root: Github - Network] Checking out files:  65% (10393/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  66% (10553/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  67% (10712/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  68% (10872/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  69% (11032/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  70% (11192/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  70% (11256/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  71% (11352/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  72% (11512/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  73% (11672/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  74% (11832/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  75% (11991/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  76% (12151/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  77% (12311/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  78% (12471/15988)   
[23:54:18] :		 [VCS Root: Github - Network] Checking out files:  79% (12631/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  80% (12791/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  81% (12951/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  82% (13111/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  83% (13271/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  84% (13430/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  85% (13590/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  86% (13750/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  87% (13910/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  87% (14033/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  88% (14070/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  89% (14230/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  90% (14390/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  91% (14550/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  92% (14709/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  93% (14869/15988)   
[23:54:19] :		 [VCS Root: Github - Network] Checking out files:  94% (15029/15988)   
[23:54:20] :		 [VCS Root: Github - Network] Checking out files:  95% (15189/15988)   
[23:54:20] :		 [VCS Root: Github - Network] Checking out files:  96% (15349/15988)   
[23:54:20] :		 [VCS Root: Github - Network] Checking out files:  96% (15412/15988)   
[23:54:20] :		 [VCS Root: Github - Network] Checking out files:  97% (15509/15988)   
[23:54:20] :		 [VCS Root: Github - Network] Checking out files:  98% (15669/15988)   
[23:54:20] :		 [VCS Root: Github - Network] Checking out files:  99% (15829/15988)   
[23:54:20] :		 [VCS Root: Github - Network] Checking out files: 100% (15988/15988)   
[23:54:20] :		 [VCS Root: Github - Network] Checking out files: 100% (15988/15988)"""
    Printer.fastPrint(text)

    text = """, done.
[23:54:20] :		 [VCS Root: Gitub - Network] [/buildAgent/work/6daa56c20f8558cf]: "(x86)/Git/bin/git" branch --set-upstream-to=refs/remotes/origin/master
[23:54:21] : Swabra (6s)
[23:54:22] :	 [Swabra] Saving /buildAgent/work/6daa56c20f8558cf directory state to snapshot file 62e917d.snapshot
[23:54:23]W: Update assembly versions: Scanning checkout directory for assembly information related files to update version to 2016.04.27.21007"""
    Printer.slowPrint(text)

    text = """[23:54:22] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/SocketServer/Properties/AssemblyInfo.cs
[23:54:22] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/StackAuth/Properties/AssemblyInfo.cs
[23:54:22] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/.Website/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/so/Properties/AssemblyInfo.cs
[23:54:23]W:	 [Update assembly versions] Assembly file version was specified, but couldn't be patched in file /buildAgent/work/6daa56c20f8558cf/so/Properties/AssemblyInfo.cs. Is necessary attribute missing?
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/so.Api.V2/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/so.Localization/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/so.Mobile/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/so.Tests/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/StackServer/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/StackSnippets/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/Utilities/BackFillExternalLinks/BackFillExternalLinks/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/Utilities/ExportDataSE/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/Utilities/LinkValidator/Crawler/Properties/AssemblyInfo.cs
[23:54:23] :	 [Update assembly versions] Updating assembly version in /buildAgent/work/6daa56c20f8558cf/Utilities/SyncPrivilegeWikis/Properties/AssemblyInfo.cs"""
    Printer.medPrint(text)

    text = """[23:54:23]i: ##teamcity[buildStatisticValue key='buildStageDuration:sourcesUpdate' value='15908.0']
[23:54:23] : Build preparation done"""
    Printer.slowPrint(text)
    # chapter 2 finished

    # chapter 3
    text = """[23:54:23] : Step 1/9: Migrate Network Databases (Command Line) (10s)
[23:54:23]i:	 [Step 1/9] ##teamcity[buildStatisticValue key='buildStageDuration:firstStepPreparation' value='47.0']
[23:54:23]i:	 [Step 1/9] ##teamcity[buildStatisticValue key='buildStageDuration:buildStepRUNNER_5' value='0.0']
[23:54:23] :	 [Step 1/9] Starting: /buildAgent/work/6daa56c20f8558cf/Build/Migrator-Fast --tier=Dev --sites=Server=DEVSQL01;Database=Dev.Sites;Uid=Dev.Sites;Pwd=******** --migrationPath="/buildAgent/work/6daa56c20f8558cf/Target.Migrations" --force --connectionReplacements=""
[23:54:23] :	 [Step 1/9] in directory: /buildAgent/work/6daa56c20f8558cf
[23:54:23] :	 [Step 1/9] Found 8 sites to update on tier Dev"""
    Printer.fastPrint(text)

    text = """[23:54:23] :	 [Step 1/9] Web Apps Dev
[23:54:23] :		 [Web Apps Dev] Connecting to database: Web Apps Dev
[23:54:23] :		 [Web Apps Dev] Running migrations
[23:54:23] :		 [Web Apps Dev] Found 714 previous migations in the Web Apps Dev database (last: 725 - Add SearchStatus and LastSearchStatusChagedDate to UserJobPreferences.sql)."""
    Printer.medPrint(text)

    text = """[23:54:23] :		 [Web Apps Dev] Attempted 124 migrations.
[23:54:23] :		 [Web Apps Dev]   Skipped: 100, Ran: 24"""
    Printer.slowPrint(text)

    text = """[23:54:23] :		 [Web Apps Dev] Web Apps Dev is up to date
[23:54:23] :	 [Step 1/9] Super User Dev
[23:54:23] :		 [Super User Dev] Connecting to database: Super User Dev
[23:54:23] :		 [Super User Dev] Running migrations
[23:54:23] :		 [Super User Dev] Found 714 previous migations in the Super User Dev database (last: 725 - Add SearchStatus and LastSearchStatusChagedDate to UserJobPreferences.sql).
[23:54:23] :		 [Super User Dev] Attempted 124 migrations.
[23:54:23] :		 [Super User Dev]   Skipped: 124, Ran: 0
[23:54:23] :		 [Super User Dev] Super User Dev is up to date
[23:54:23] :	 [Step 1/9] Area 51 Discussions Dev
[23:54:23] :		 [Area 51 Discussions Dev] Connecting to database: Area 51 Discussions Dev
[23:54:23] :		 [Area 51 Discussions Dev] Running migrations
[23:54:23] :		 [Area 51 Discussions Dev] Found 711 previous migations in the Area 51 Discussions Dev database (last: 725 - Add SearchStatus and LastSearchStatusChagedDate to UserJobPreferences.sql/).
[23:54:23] :		 [Area 51 Discussions Dev] Attempted 124 migrations.
[23:54:23] :		 [Area 51 Discussions Dev]   Skipped: 124, Ran: 0
[23:54:23] :		 [Area 51 Discussions Dev] Area 51 Discussions Dev is up to date
[23:54:23] :	 [Step 1/9] Web Apps Meta Dev
[23:54:23] :		 [Web Apps Meta Dev] Connecting to database: Web Apps Meta Dev
[23:54:23] :		 [Web Apps Meta Dev] Running migrations
[23:54:23] :		 [Web Apps Meta Dev] Found 714 previous migations in the Web Apps Meta Dev database (last: 725 - Add SearchStatus and LastSearchStatusChagedDate to UserJobPreferences.sql/).
[23:54:23] :		 [Web Apps Meta Dev] Attempted 124 migrations.
[23:54:23] :		 [Web Apps Meta Dev]   Skipped: 124, Ran: 0
[23:54:23] :		 [Web Apps Meta Dev] Web Apps Meta Dev is up to date
[23:54:23] :	 [Step 1/9] Meta Super User Dev
[23:54:23] :		 [Meta Super User Dev] Connecting to database: Meta Super User Dev
[23:54:23] :		 [Meta Super User Dev] Running migrations
[23:54:23] :		 [Meta Super User Dev] Found 714 previous migations in the Meta Super User Dev database (last: 725 - Add SearchStatus and LastSearchStatusChagedDate to UserJobPreferences.sql/)."""
    Printer.medPrint(text)

    text = """[23:54:23] :		 [Meta Super User Dev] Attempted 124 migrations.
[23:54:23] :		 [Meta Super User Dev]   Skipped: 120, Ran: 4
[23:54:23] :		 [Meta Super User Dev] Meta Super User Dev is up to date"""
    Printer.slowPrint(text)

    text = """[23:54:23] :	 [Step 1/9] Meta  Dev
[23:54:23] :		 [Meta  Dev] Connecting to database: Meta  Dev
[23:54:23] :		 [Meta  Dev] Running migrations
[23:54:23] :		 [Meta  Dev] Found 567 previous migations in the Meta  Dev database (last: 725 - Add SearchStatus and LastSearchStatusChagedDate to UserJobPreferences.sql on 2016-04-26 11:45:24Z).
[23:54:23] :		 [Meta  Dev] Attempted 124 migrations.
[23:54:23] :		 [Meta  Dev]   Skipped: 124, Ran: 0
[23:54:23] :		 [Meta  Dev] Meta  Dev is up to date
[23:54:23] :	 [Step 1/9] Meta Dev
[23:54:23] :		 [Meta Dev] Connecting to database: Meta Dev
[23:54:23] :		 [Meta Dev] Running migrations
[23:54:23] :		 [Meta Dev] Found 714 previous migations in the Meta Dev database (last: 725 - Add SearchStatus and LastSearchStatusChagedDate to UserJobPreferences.sql on 2016-04-26 11:45:24Z).
[23:54:23] :		 [Meta Dev] Attempted 124 migrations.
[23:54:23] :		 [Meta Dev]   Skipped: 124, Ran: 0
[23:54:23] :		 [Meta Dev] Meta Dev is up to date
[23:54:23] :	 [Step 1/9]  Dev
[23:54:23] :		 [ Dev] Connecting to database:  Dev
[23:54:23] :		 [ Dev] Running migrations
[23:54:23] :		 [ Dev] Found 714 previous migations in the  Dev database (last: 725 - Add SearchStatus and LastSearchStatusChagedDate to UserJobPreferences.sql on 2016-04-26 11:45:24Z).
[23:54:23] :		 [ Dev] Attempted 124 migrations.
[23:54:23] :		 [ Dev]   Skipped: 124, Ran: 0
[23:54:23] :		 [ Dev]  Dev is up to date
[23:54:23] :	 [Step 1/9] 
[23:54:23] :	 [Step 1/9] Total Time: 214ms
[23:54:25] :	 [Step 1/9] Process exited with code 0
[23:54:25]i:	 [Step 1/9] ##teamcity[buildStatisticValue key='buildStageDuration:buildStepRUNNER_5' value='1849.0']"""
    Printer.fastPrint(text)

    # chapter 3 end

    # chapter 4
    text = """[23:54:25]i:	 [Step 2/9] ##teamcity[buildStatisticValue key='buildStageDuration:buildStepRUNNER_6' value='0.0']
[23:54:25] :	 [Step 2/9] Starting: /buildAgent/work/6daa56c20f8558cf/Build/Migrator-Fast --sitesonly=true --tier=Dev --sites=Server=NY-DEVSQL01;Database=Dev.Sites;Uid=Dev.Sites;Pwd=******** --migrationPath="/buildAgent/work/6daa56c20f8558cf/Sites.Migrations" --force
[23:54:25] :	 [Step 2/9] in directory: /buildAgent/work/6daa56c20f8558cf
[23:54:25] :	 [Step 2/9] 
[23:54:25] :		 [] Connecting to database: 
[23:54:25] :		 [] Running migrations
[23:54:25] :		 [] Found 154 previous migations in the  database (last: 200 - Drop Sessions.sql on 2016-04-18 14:03:40Z).
[23:54:25] :		 [] Attempted 146 migrations.
[23:54:25] :		 []   Skipped: 146, Ran: 0
[23:54:25] :		 []  is up to date
[23:54:25] :	 [Step 2/9] 
[23:54:25] :	 [Step 2/9] 
[23:54:25] :	 [Step 2/9] Total Time: 124ms
[23:54:25] :	 [Step 2/9] Process exited with code 0
[23:54:25]i:	 [Step 2/9] ##teamcity[buildStatisticValue key='buildStageDuration:buildStepRUNNER_6' value='308.0']
[23:54:25] : Step 3/9: Find MoonSpeak Tools (Powershell) (1s)
[23:54:25]i:	 [Step 3/9] ##teamcity[buildStatisticValue key='buildStageDuration:buildStepRUNNER_145' value='0.0']
[23:54:25] :	 [Step 3/9] PowerShell Executable: SysWOW64/WindowsPowerShell/v1.0/powershell
[23:54:25] :	 [Step 3/9] Working directory: /buildAgent/work/6daa56c20f8558cf
[23:54:25] :	 [Step 3/9] PowerShell command:  SysWOW64/WindowsPowerShell/v1.0/powershell -NonInteractive -ExecutionPolicy ByPass -Command - < /buildAgent/temp/buildTmp/powershell5615721444225225625.ps1
[23:54:25] :	 [Step 3/9] Executable wrapper: System32/cmd
[23:54:25] :	 [Step 3/9] Wrapper arguments: [/c, /buildAgent/temp/buildTmp/powershell2591189389456020678.bat]
[23:54:26] :	 [Step 3/9] ##teamcity[setParameter name='system.moonspeaktools' value='/buildAgent/work/6daa56c20f8558cf/packages/Target.MoonSpeak.2.3.0/tools']
[23:54:26] :	 [Step 3/9] Process exited with code 0
[23:54:26]i:	 [Step 3/9] ##teamcity[buildStatisticValue key='buildStageDuration:buildStepRUNNER_145' value='1351.0']
[23:54:26] : Step 4/9: Translation Dump JS (Command Line) (1s)
[23:54:26]i:	 [Step 4/9] ##teamcity[buildStatisticValue key='buildStageDuration:buildStepRUNNER_96' value='0.0']
[23:54:26] :	 [Step 4/9] Starting: /buildAgent/temp/agentTmp/custom_script7520893337348765978.cmd
[23:54:26] :	 [Step 4/9] in directory: /buildAgent/work/6daa56c20f8558cf
[23:54:27] :	 [Step 4/9] Process exited with code 0
[23:54:27]i:	 [Step 4/9] ##teamcity[buildStatisticValue key='buildStageDuration:buildStepRUNNER_96' value='1039.0']
[23:54:27]W: Step 5/9: Compile Compress and Minify (MSBuild) (1m:06s)
[23:54:27]i:	 [Step 5/9] ##teamcity[buildStatisticValue key='buildStageDuration:buildStepRUNNER_7' value='0.0']
[23:54:27] :	 [Step 5/9] Starting: /buildAgent/plugins/dotnetPlugin/bin/JetBrains.BuildServer.MsBuildBootstrap /workdir:/buildAgent/work/6daa56c20f8558cf "/msbuildPath:(x86)/MSBuild/14.0/bin/amd64/MSBuild"
[23:54:27] :	 [Step 5/9] in directory: /buildAgent/work/6daa56c20f8558cf
[23:54:29]W:	 [Step 5/9] Build/tc.website.ny.msbuild.teamcity: Build target: PrepareStaticContent (1m:04s)
[23:54:29] :		 [Build/tc.website.ny.msbuild.teamcity] CompileWeb
[23:54:29] :			 [CompileWeb] MSBuild
[23:54:29] :				 [MSBuild] Target.Localization/Target.Localization.csproj: Build target: Build
[23:54:29] :					 [Target.Localization/Target.Localization.csproj] PrepareForBuild
[23:54:29] :						 [PrepareForBuild] MakeDir
[23:54:29] :							 [MakeDir] Creating directory "bin/Debug/".
[23:54:29] :							 [MakeDir] Creating directory "obj/Debug/".
[23:54:29] :					 [Target.Localization/Target.Localization.csproj] CoreCompile
[23:54:29] :						 [CoreCompile] Csc
[23:54:29] :							 [Csc] (x86)/MSBuild/14.0/bin/amd64/csc /noconfig /nowarn:1701,1702 /nostdlib+ /errorreport:prompt /warn:4 /define:DEBUG;TRACE /highentropyva+ /debug+ /debug:full /filealign:512 /optimize- /out:obj/Debug/Target.Localization.dll /subsystemversion:6.00 /target:library /utf8output /analyzer:../packages/Microsoft.CodeAnalysis.Analyzers.1.1.0/analyzers/dotnet/cs/Microsoft.CodeAnalysis.Analyzers.dll /analyzer:../packages/Microsoft.CodeAnalysis.Analyzers.1.1.0/analyzers/dotnet/cs/Microsoft.CodeAnalysis.CSharp.Analyzers.dll JsonHelper.cs Stubs.cs CultureProviderHelper.cs DataSource.cs Properties/AssemblyInfo.cs Strings.cs TranslationString.cs "/buildAgent/temp/buildTmp/.NETFramework,Version=v4.6.AssemblyAttributes.cs"
[23:54:30] :					 [Target.Localization/Target.Localization.csproj] _CopyFilesMarkedCopyLocal
[23:54:30] :						 [_CopyFilesMarkedCopyLocal] Copy
[23:54:30] :							 [Copy] Copying file from "/buildAgent/work/6daa56c20f8558cf/packages/Dapper.1.50.0-beta9/lib/net451/Dapper.dll" to "bin/Debug/Dapper.dll".
[23:54:30] :					 [Target.Localization/Target.Localization.csproj] _CopyAppConfigFile
[23:54:30] :						 [_CopyAppConfigFile] Copy
[23:54:30] :							 [Copy] Copying file from "app.config" to "bin/Debug/Target.Localization.dll.config".
[23:54:30] :					 [Target.Localization/Target.Localization.csproj] CopyFilesToOutputDirectory
[23:54:30] :						 [CopyFilesToOutputDirectory] Copy
[23:54:30] :							 [Copy] Copying file from "obj/Debug/Target.Localization.dll" to "bin/Debug/Target.Localization.dll".
[23:54:30] :						 [CopyFilesToOutputDirectory] Target.Localization -> /buildAgent/work/6daa56c20f8558cf/Target.Localization/bin/Debug/Target.Localization.dll
[23:54:30] :						 [CopyFilesToOutputDirectory] Copy
[23:54:30] :							 [Copy] Copying file from "obj/Debug/Target.Localization.pdb" to "bin/Debug/Target.Localization.pdb".
[23:54:30] :			 [CompileWeb] CompileWeb complete
[23:54:30] :		 [Build/tc.website.ny.msbuild.teamcity] ReplaceConfigs
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/connectionStrings.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/Web.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/Web.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/Web.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/Web.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/Web.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/appSettings.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/appSettings.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/appSettings.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/appSettings.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/appSettings.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/Web.config".
[23:54:30] :			 [ReplaceConfigs] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Target/appSettings.config".
[23:54:30] :			 [ReplaceConfigs] Copy
[23:54:30] :				 [Copy] Copying file from "/buildAgent/work/6daa56c20f8558cf/Build/Jerome.config" to "/buildAgent/work/6daa56c20f8558cf/packages/Target.MoonSpeak.2.3.0/tools/Jerome.config".
[23:54:30] :			 [ReplaceConfigs] Copy
[23:54:30] :				 [Copy] Copying file from "/buildAgent/work/6daa56c20f8558cf/Build/MoonSpeak.Importer.config" to "/buildAgent/work/6daa56c20f8558cf/packages/Target.MoonSpeak.2.3.0/tools/MoonSpeak.Importer.config".
[23:54:30] :			 [ReplaceConfigs] ReplaceConfigs complete
[23:54:30]W:		 [Build/tc.website.ny.msbuild.teamcity] PrepareStaticContent (1m:03s)
[23:54:30] :			 [PrepareStaticContent] Creating fan out call projects
[23:54:30] :			 [PrepareStaticContent] Copy
[23:54:30] :				 [Copy] Copying file from "/buildAgent/work/6daa56c20f8558cf/Build/tc.website.ny.msbuild" to "/buildAgent/work/6daa56c20f8558cf/Build/tc.website.ny.BuildViews.call".
[23:54:30] :				 [Copy] Copying file from "/buildAgent/work/6daa56c20f8558cf/Build/tc.website.ny.msbuild" to "/buildAgent/work/6daa56c20f8558cf/Build/tc.website.ny.CompileNode.call".
[23:54:30] :			 [PrepareStaticContent] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Build/tc.website.ny.BuildViews.call".
[23:54:30] :			 [PrepareStaticContent] FileUpdate
[23:54:30] :				 [FileUpdate] Updating File "/buildAgent/work/6daa56c20f8558cf/Build/tc.website.ny.CompileNode.call".
[23:54:30] :	 [Step 5/9] The target "MvcBuildViews" listed in a BeforeTargets attribute at "Build/Targets/Microsoft/VisualStudio/v14.0/Web/Microsoft.Web.Publishing.targets (843,131)" does not exist in the project, and will be ignored.
[23:54:30]W:			 [PrepareStaticContent] MSBuild (1m:03s)
[23:54:30]W:				 [MSBuild] Build/tc.website.ny.BuildViews.call: Build default targets (57s)
[23:54:30]W:					 [Build/tc.website.ny.BuildViews.call] BuildViews (57s)
[23:54:30]W:						 [BuildViews] MSBuild (57s)
[23:54:30]W:							 [MSBuild] Target/Target.csproj: Build target: BuildViews (57s)
[23:54:30] :								 [Target/Target.csproj] PrepareForBuild
[23:54:30] :									 [PrepareForBuild] MakeDir
[23:54:30] :										 [MakeDir] Creating directory "bin/".
[23:54:30] :										 [MakeDir] Creating directory "obj/Debug/".
[23:54:30] :								 [Target/Target.csproj] ResolveProjectReferences
[23:54:30] :				 [MSBuild] Build/tc.website.ny.CompileNode.call: Build default targets (1m:03s)
[23:54:30] :					 [Build/tc.website.ny.CompileNode.call] BundleJavaScript
[23:54:30] :						 [BundleJavaScript] BundleJavaScript completed
[23:54:30] :					 [Build/tc.website.ny.CompileNode.call] TranslateJSContent (11s)
[23:54:30] :						 [TranslateJSContent] MakeDir
[23:54:30] :							 [MakeDir] Creating directory "/buildAgent/work/6daa56c20f8558cf/Target.Localization/bin/App_Data".
[23:54:30] :						 [TranslateJSContent] Exec (11s)
[23:54:30] :							 [Exec]"""
    Printer.medPrint(text)

    text = """/buildAgent/work/6daa56c20f8558cf/packages/Target.MoonSpeak.2.3.0/tools/Jerome.exe rewrite /buildAgent/work/6daa56c20f8558cf/Target.Localization/bin/Debug/Target.Localization.dll "/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/about.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/answer-loader.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/auth.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/bounty.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/chess.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/citation.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/developer.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/discuss.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/docs.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/election.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/error-cats.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/errors.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/events.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/explore-qlist.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/external-editor.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/full-anon.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/full.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/funnel-autocomplete.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/go.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/help.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/image-upload.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/inline-tag-editing.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/keyboard-shortcuts.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/less.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/local.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/mathjax-editing.beta.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/mathjax-editing.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/mobile.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/mod-community-events.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/mod-user-activity.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/mod-voting-ringleader.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/moderator.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/openid-confirm.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/poker.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/post-validation.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/prettify-full.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/realtime-se.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/realtime.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/review-dashboard.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/review.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/revisions.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/site-analytics.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/snippet-javascript-codemirror.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/snippet-javascript.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/stub.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/tageditor.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/tageditornew.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/tagsuggestions.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/teams.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/test-globalauth.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/user.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/virtual-keyboard.js;/buildAgent/work/6daa56c20f8558cf/Target/Content/Js/wmd.js" > "/buildAgent/work/6daa56c20f8558cf/JeromeStdOut.log" 2>&1"""
    time.sleep(5)
    Printer.instaPrint(text)

    text = """[23:54:30] :									 [ResolveProjectReferences] MSBuild
[23:54:30] :										 [MSBuild] Target.Localization/Target.Localization.csproj: Build default targets
[23:54:30] :											 [Target.Localization/Target.Localization.csproj] GenerateTargetFrameworkMonikerAttribute
[23:54:30] :												 [GenerateTargetFrameworkMonikerAttribute] Skipping target "GenerateTargetFrameworkMonikerAttribute" because all output files are up-to-date with respect to the input files.
[23:54:30] :											 [Target.Localization/Target.Localization.csproj] CoreCompile
[23:54:30] :												 [CoreCompile] Skipping target "CoreCompile" because all output files are up-to-date with respect to the input files.
[23:54:30] :											 [Target.Localization/Target.Localization.csproj] _CopyAppConfigFile
[23:54:30] :												 [_CopyAppConfigFile] Skipping target "_CopyAppConfigFile" because all output files are up-to-date with respect to the input files.
[23:54:30] :											 [Target.Localization/Target.Localization.csproj] CopyFilesToOutputDirectory
[23:54:30] :												 [CopyFilesToOutputDirectory] Target.Localization -> /buildAgent/work/6daa56c20f8558cf/Target.Localization/bin/Debug/Target.Localization.dll
[23:54:31] :								 [Target/Target.csproj] GenerateTargetFrameworkMonikerAttribute
[23:54:31] :									 [GenerateTargetFrameworkMonikerAttribute] Skipping target "GenerateTargetFrameworkMonikerAttribute" because all output files are up-to-date with respect to the input files.
[23:54:31]W:								 [Target/Target.csproj] ResolveCodeAnalysisRuleSet
[23:54:31]W:									 [ResolveCodeAnalysisRuleSet] ResolveCodeAnalysisRuleSet
[23:54:31]W:										 [ResolveCodeAnalysisRuleSet] C:/Program Files (x86)/MSBuild/14.0/bin/amd64/Microsoft.CSharp.CurrentVersion.targets(133, 9): warning MSB3884: Could not find rule set file "AllRules.ruleset"."""
    Printer.medPrint(text)

    text = """[23:54:31]W:								 [Target/Target.csproj] CoreCompile (56s)
[23:54:31]W:									 [CoreCompile] Csc (56s)
[23:54:31] :										 [Csc] """
    Printer.reallySlowPrint(text)
    # chapter 4 end - the end