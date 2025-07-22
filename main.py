#!/home/sei/work_zone/uploadgit/env/bin/python

from github import Github
from github import Auth
import pyfiglet
import pyperclip
from InquirerPy import inquirer
from termcolor import colored
import subprocess

from gp import gitpush

class git_user:
    def __init__(self,token):
        auth=Auth.Token(token)
        g=Github(auth=auth)
        self.user=g.get_user()
        self.show_intro()
    #shows intro
    def show_intro(self):
        f=pyfiglet.figlet_format("GitPie",font="starwars")
        f=colored(f,color="cyan")
        print("")
        print(f)
        print("---------------------------------------------------------")
    
    def doinquire(self):
        x = inquirer.select(
            message="Visibility : ",
            choices=["> Public ", "> Private"]
        ).execute()

        if x == "> Public ":
            y = False
        else:
            y = True

        return y
        

        return y
    
    def copy_it(self,url):
        pyperclip.copy(url)

    def create_repo(self):
        repo_name=input("> Enter Your Repo Name : \n >")
        description_=input("> Enter Description : \n >")
#inquirer here
        setPrivate=self.doinquire()
        repo= self.user.create_repo(f"{repo_name}",description=description_,private=setPrivate)
        print("---")
        print(f"Repositery created : {repo_name}")
        self.copy_it(repo.ssh_url)
        print(f"Clone URL(ssh url) has been Copied :>.")
        self.moveon(repo.ssh_url)
    def moveon(self,url):
        option =inquirer.select(
                message=">> What next? ",
                choices=["> push cd","> exit"]
                ).execute()
        if option=="> exit":
            quit()
        else:
            gitpush(url)
        

token=""



user=git_user(token)
user.create_repo()

