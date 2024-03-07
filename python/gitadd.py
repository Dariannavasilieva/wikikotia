import os

def addCSVtoGit(filename):
    token = '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'
    os.chdir("git init")
    os.system('git init')
    print('1')
    os.system('git add --all')
    print('2')
    os.system('git commit -m "обновление файлов"')
    print('3')
    os.system('git branch -M main')
    print('4')
    os.system('git remote set-url origin https://Dariannavasilieva:'+ token +'@github.com/Dariannavasilieva/wikikotia.git')
    print('5')
    os.system('git push -f origin main')
    print('done')
              



    

addCSVtoGit('test.csv')

