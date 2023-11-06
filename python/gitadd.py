import os

def addCSVtoGit(filename):
    #os.system('cd /D D:\MyProject')
    os.chdir("D:\MyProject")
    os.system('git init')
    print('1')
    os.system('git add --all')
    print('2')
    os.system('git commit -m "обновление файлов"')
    print('3')
    os.system('git branch -M main')
    print('4')
    #os.system('git remote add origin https://github.com/Dariannavasilieva/wikikotia.git')
    os.system('git remote set-url origin https://Dariannavasilieva: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@github.com/Dariannavasilieva/wikikotia.git')
    print('5')
    os.system('git push -f origin main')
    print('done')
              



    

addCSVtoGit('test.csv')

'''
    file_list = [
    'C:\\Users\jesse\Dropbox\Swell-Forecast\git-test\index.html',
    'C:\\Users\jesse\Dropbox\Swell-Forecast\git-test\margin_table.html'
    ]
    file_names = [
        'index.html',
        'margin_table.html'
    ]
    commit_message = 'python commit'
    master_ref = repo.get_git_ref('heads/master')
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)

    element_list = list()
    for i, entry in enumerate(file_list):
        with open(entry) as input_file:
            data = input_file.read()
        if entry.endswith('.png'): # images must be encoded
            data = base64.b64encode(data)
        element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
        element_list.append(element)

    tree = repo.create_git_tree(element_list, base_tree)
    parent = repo.get_git_commit(master_sha)
    commit = repo.create_git_commit(commit_message, tree, [parent])
    master_ref.edit(commit.sha)
'''