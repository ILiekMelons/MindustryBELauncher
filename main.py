import requests
import os
import wget
import subprocess


def update_mindustry():
    global response
    global be_wrapper
    global current_build

    download_url = "https://github.com/Anuken/MindustryBuilds/releases/download/" + str(current_build)
    download_url = download_url + "/Mindustry-BE-Desktop-" + str(current_build) + ".jar"

    os.system("rm -f " + os.path.join(be_wrapper, "Mindustry.jar"))
    wget.download(download_url, os.path.join(be_wrapper, "Mindustry.jar"))
    bfile = open(be_wrapper + "/last.txt", "w")
    bfile.write(str(current_build))
    print()


def run_mindustry():
    global be_wrapper
    global current_build
    if not os.path.exists(os.path.join(be_wrapper, "Mindustry.jar")):
        print("The Mindustry jar file does not exist. Download it now?")
        if input("Update now? (Y/N):").lower() == "y":
            update_mindustry()
        else:
            print("Exiting")
            exit(0)
    os.system("java -jar " + be_wrapper + "/Mindustry.jar")


try:
    subprocess.check_call("java -version", shell=True)
except subprocess.CalledProcessError as x:
    if not x.returncode == 127:
        raise

response = requests.get("https://api.github.com/repos/Anuken/MindustryBuilds/releases/latest").json()
current_build = int(response['tag_name'])

home = os.path.expanduser("~")
be_wrapper = os.path.join(home, "BEWrapper")

if not os.path.exists(be_wrapper):
    os.mkdir(be_wrapper)

try:
    build_file = open(be_wrapper + "/last.txt", "r")
    saved_build = int(build_file.read())
    build_file.close()
except FileNotFoundError:
    saved_build = 0
except ValueError:
    saved_build = 0

if saved_build < current_build:
    print("Your Mindustry build seems to be out of date by " + str(current_build - saved_build) + " releases.")
    if input("Update now? (Y/N):").lower() == "y":
        update_mindustry()

print("Mindustry appears to be up to date!")
print("Running Mindustry")
run_mindustry()
