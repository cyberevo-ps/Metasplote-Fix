import sys,time
import os
os.system("clear")
text = """
███╗   ███╗███████╗███████╗    ███████╗██╗██╗  ██╗
███║   ███║██╔════╝██╔════╝    ██╔════╝██║╚██╗██╔╝
██╔████╔██║███████╗█████╗      █████╗  ██║ ╚███╔╝
██║╚██╔╝██║╚════██║██╔══╝      ██╔══╝  ██║ ██╔██╗
██║ ╚═╝ ██║███████║██║         ██║     ██║██╔╝ ██╗
╚═╝     ╚═╝╚══════╝╚═╝         ╚═╝     ╚═╝╚═╝  ╚═╝"""
os.system(f'echo "{text}" | lolcat -t')

s3 = """
    \033[1;31m╭───────────────────────────────────────╮
    \033[1;31m│\033[1;34m             By Bo Haydar ✓       \033[1;31m     │
    \033[1;31m╰───────────────────────────────────────╯
\033[1;32m[\033[1;31m+\033[1;32m]\033[1m\033[97m \033[1;32mInstall Metasplite In Termux
\033[1;32m[\033[1;31m+\033[1;32m]\033[1m\033[97m The Tool By Bo Haydar \033[1;32m•
\033[1;32m[\033[1;31m+\033[1;32m]\033[1m\033[97m Gitub :\033[1;32mhttps://github.com/bohaydar
\033[1;32m[\033[1;31m+\033[1;32m]\033[1m\033[97m No Root \033[1;32m✓
\033[1;32m[\033[1;31m+\033[1;32m]\033[1m\033[97m Old Android Update \033[1;32m✓
\033[1;31m[\033[1;32m!\033[1;32m\033[1;31m] \033[1m\033[1;32mMeta Size 956 MB / 1 GB \033[1;31m !
\033[1;31m[\033[1;32m!\033[1;32m\033[1;31m] \033[1m\033[1;32mInstall 350 MB \033[1;31m !
\033[1;31m[\033[1;32m!\033[1;32m\033[1;31m] \033[1m\033[1;32mPlease Don't Off Internet \033[1;31m !!!"""
for i in s3 :
     time.sleep(0.01)
     sys.stdout.write(i)
     sys.stdout.flush()
vvvv = input('''
\033[1;31m[\033[1;32m?\033[1;32m\033[1;31m] \033[1;34mDo You Install Metasploite \033[1;37my/n\033[1;36m ?  ''')
if vvvv =='n' :
   os.system("exit")
elif vvvv =='y' :
     print ("\033[1;32mInstall \033[1;31mUpdate & Upgrade\033[0;30m")
     os.system("pkg update && pkg upgrade -y")
     print ("\033[1;32mInstall \033[1;31m Git\033[0;30m")
     os.system("pkg install git")
     print ("\033[1;32mInstall \033[1;31m Curl\033[0;30m")
     os.system("pkg install curl")
     print ("\033[1;32mInstall \033[1;31m Ruby\033[0;30m")
     os.system("pkg install ruby")
     print ("\033[1;32mInstall \033[1;31m ncurses-utils\033[0;30m")
     os.system("apt install ncurses-utils")
     print ("\033[1;32mInstall \033[1;31minstall & wget & curl & openssh\033[0;30m")
     os.system("pkg install wget curl openssh git -y")
     print ("\033[1;32mStarting  \033[1;31m Fix.sh\033[0;30m")
     os.system("chmod +x Fix.sh && ./Fix.sh")
     print ("\033[1;32mInstall Starting \033[1;31m Metasploite V6 In Termux\033[1;36m")
