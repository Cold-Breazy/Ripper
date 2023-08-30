
import subprocess

try:
    # Check if Googlesearch package is installed
    subprocess.check_output(['pip', 'show', 'google'])
    print("      [#] GOOGLE IS ALREADY INSTALLED")
except subprocess.CalledProcessError:
    print("      [!] GOOGLE IS NOT INSTALLED")

    # Silent installation using bash command
    subprocess.run(['pip', 'install', 'google', '--quiet'])

    # Verify installation
    try:
        subprocess.check_output(['pip', 'show', 'google'])
        print("      [#] GOOGLE INSTALLED SUCCESSFUL")
    except subprocess.CalledProcessError:
        print("      [!] FAILED TO INSTALL REQUIRED PACKAGE.")
