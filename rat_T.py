from subprocess import run

from time import sleep

sudo='sudo'
packages=['bs4', 'requests','fake-useragent','selenium','PyVirtualDisplay','fake_usrag_bor']

for pkg in packages:
	run('python3.7 -m pip install '+pkg,shell=True)
	
print('All packages were installed')

ubun_pkgs=['wget','unzip','xvfb']
run(sudo+' apt-get -y update',shell=True)

for pkg in ubun_pkgs:
	run(sudo+' apt-get -y install '+pkg,shell=True)

print('ubuntu packages installed')

#get google chrome
print('......get chrome.....'*20)
run(sudo+' apt-get -y install fonts-liberation xdg-utils libxss1 libappindicator1 libindicator7',shell=True)
run('wget -c https://docs.google.com/uc?id=1L1N_Bx77plgiWzfnQ-wGhW0W29fYS7pn -O chrome64_61.deb',shell=True)

####################
######## needed####
run(sudo+' dpkg -i chrome64_61.deb',shell=True)

run(sudo+' apt-get -y install -f',shell=True)

run(sudo+' dpkg -i chrome64_61.deb',shell=True)
###################

#download chromedriver
print('chromedriver.............')
run('wget -c https://docs.google.com/uc?id=1LiN7rc6ngA4CSuqVnqr4GVXuSx4gquOT -O chromedriver',shell=True)

#change directory and permission
print('permission......   ...........')
run(sudo+' cp chromedriver /usr/bin/',shell=True)

run(sudo+' chmod ugo+rx /usr/bin/chromedriver',shell=True)


	
print('#'*60)


print('finished....setup,NOW DOWNLOADING SCRIPT....')

# down minibot link
run('wget -c https://docs.google.com/uc?id=1RZAJDkWDV0NZftjzhBGn5cXudS5z79o5 -O mini_bot.py',shell=True)
print('done.....')

run('python3.7 mini_bot.py',shell=True)
sleep(30)
