#!/bin/bash
clear
logo(){
echo -e " ${red}
    ███████████████████████████████████
    █▄─▄▄▀█▄─▄█▄─▄▄─█▄─▄▄─█▄─▄▄─█▄─▄▄▀█
    ██─▄─▄██─███─▄▄▄██─▄▄▄██─▄█▀██─▄─▄█
    ▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀
"
}

test(){
if ! command -v python &>/dev/null; then
  echo -e "${yelo}[${red}!${yelo}] ${green}SILENTLY INSTALLING ${red}PYTHON"
  pkg install -y python > /dev/null 2>&1
  echo -e "      ${yelo}[${green}+${yelo}] ${green}PYTHON INSTALLED SUCCESSFUL"
else
  echo -e "      ${yelo}[${red}#${yelo}] ${green}PYTHON IS ALREADY INSTALLED"
fi

python .required.py
}

proc(){
echo
echo -e "${yelo}      [!] ${red} REMOVING UNECESSARY FILES"
echo
rm ripper.png README.md .txt
sleep 1.5
echo -e "${yelo}      [!] ${red} DONE...!"
echo
echo
echo -e "${red} TO START THE TOOL RUN ${yelo}python Rip.py"

# colors
red="\033[1;31m"
green="\033[1;32m"
yelo="\033[1;33m"


logo
test
