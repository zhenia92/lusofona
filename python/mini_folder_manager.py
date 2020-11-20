#coding=utf-8

import os
import sys

def create(name):
    os.mkdir(name)

def rename(old_name,new_name):
    os.rename(old_name,new_name)

def list_dir():
    print("*"*30)
    for f in os.listdir():
        print("- "+str(f))
    print("*"*30)
def rm_dir(name):
    os.rmdir(name)

def pwd_dir():
    return os.getcwd()

def ch_dir(dir_add):
    os.chdir(dir_add)

def main():
    
    try:
        print("="*30)
        print("Avalible Options to do with Folders:")
        print("1.List")
        print("2.Create")
        print("3.Rename")
        print("4.Delete")
        print("5.Print current directory path")
        print("6.Change directory")
        print("="*30)
        print("Please choose action: ")
        while True:

            decision = input(">")
            decision = decision.strip()
            
            if decision == "1":
                list_dir()

            elif decision == "2":
                name = input("Please enter name: ")
                name = name.strip().lower()
                create(name)

            elif decision == "3":
                old_name = input("Please old name: ")
                new_name = input("Please new name: ")
                rename(old_name,new_name)

            elif decision == "4":
                name = input("Please enter name: ")
                rm_dir(name)
            elif decision == "5":
                print(pwd_dir())

            elif decision == "6":
                print("Current dir is -> "+str(pwd_dir()))
                dir_add = input("Please enter full path to go: ")
                ch_dir(dir_add)


    except KeyboardInterrupt:
        sys.exit()
    except FileNotFoundError:
        print("please select correct folder name!!!")
if __name__ == "__main__":
    main()