import subprocess
import platform

if platform.system() == "Windows":

    cmd = "ipconfig/all"

    B = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = B.communicate()
    print('out:Hardware Device and Ethernet Address in Windows {0}'.format(out))

    if B.returncode == 0:
        print('Result : Passed')
    else:
        print("Result : Failed")
        print("err:couldn't find{0}".format(err))

elif platform.system() == "Darwin":

    cmd = "networksetup -listallhardwareports"

    B = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = B.communicate()
    print('out:Hardware,Device and Ethernet Address in MAC {0}'.format(out))

    if B.returncode == 0:
        print('Result : Passed')
    else:
        print("Result : Failed")
        print("err:couldn't find{0}".format(err))

elif platform.system() == "Linux":

    cmd = "hwinfo"

    B = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = B.communicate()
    print('out:Hardware Device and Ethernet Address in Linux {0}'.format(out))

    if B.returncode == 0:
        print('Result : Passed')
    else:
        print("Result : Failed")
        print("err:couldn't find{0}".format(err))




