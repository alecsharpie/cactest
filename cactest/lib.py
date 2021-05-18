from termcolor import colored

def try_me():
    print(colored("           *-*,\n\
       ,*\/|`| \ \n\
       \   | |'| *,\n\
        \ `| | |/ )\n\
         | |'| , /\n\
         |'| |, /", 'green'))
    print("       ",colored("__","red"),colored("|","green"),colored("_","red"),colored("|","green"),colored("_","red"),colored("|","green"),colored("_","red"),colored("|","green"),colored("__","red"), sep='')
    print(colored("      [___________]\n\
       |         |\n\
       |         |\n\
       |         |\n\
       |_________|\n\
       ", 'red'))

if __name__ == "__main__":
  try_me()
