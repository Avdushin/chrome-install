echo -e "\e[0;92minstalling google-chrome-stable"
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/getsolus/3rd-party/master/network/web/browser/google-chrome-stable/pspec.xml -y
sudo eopkg it google-chrome-*.eopkg;sudo rm google-chrome-*.eopkg -y
echo -e "\e[0;92mDone"