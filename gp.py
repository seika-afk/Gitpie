import subprocess
def gitpush (url):
    subprocess.run(["git","add","."])
    print("")
    print("> added everything")
    #can set to ask for message
    msg=input("> Commit Message: ")
    subprocess.run(["git","commit","-m",msg])
    print("> commited.")
    subprocess.run(["git","branch","-M","main"])
    subprocess.run(["git","remote","add","origin",url])
    print("> pushing now.")
    
    subprocess.run(["git","push","-u","origin","main"])
