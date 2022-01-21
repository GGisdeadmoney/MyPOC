import os

def DirectoryFilter(path):
    return os.path.isdir(path)

TARGET_PATH = os.getcwd()
os.system("echo test")
targets = os.listdir(path=TARGET_PATH)
for i, tar in enumerate(targets):
    targets[i] = os.path.join(TARGET_PATH,tar)

targets = list(filter(DirectoryFilter, targets))
for tar in targets:
    print("demo")
    print(tar)

print(targets)
print(len(targets))
for tar in targets:
    print (123)
    os.system(f'explorer.exe {tar}')

#os.system(r'explorer.exe "D:\Mypython\20220121_explorer_poc\open_UTF_path_explorer\テスト"')