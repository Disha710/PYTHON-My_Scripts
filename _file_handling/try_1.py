from pathlib import Path
import os


print(Path('spam','bacon','eggs'))
print(str(Path('spam','bacon','eggs')))

my_files = ['accounts.txt','details.csv','invite.docx']
for filename in my_files:
  print(Path(r'D:\Next\python_learning', filename))


  
#pathlib overload(/) division operater and consider it as joining of folder
# #author suggest to use / for both mac and windows
#print(Path('spam'/'bacon'/'eggs')) # will not work cannot work on 2 strings also left to right operation

print(Path('spam')/Path('bacon','eggs'))


#print(Path.cwd())
#os.chdir('D:\\NEXT')
print(Path.cwd())
#print(Path.home())
#os.chdir('D:\\NEXT\\python_learning\\disha_python_practice')

print('---new dir---')
os.makedirs('D:\\NEXT\\python_learning\\new', exist_ok=True)
Path(r'D:\NEXT\python_learning\new\new1').mkdir(exist_ok=True)

print('---absolute path---')
print(Path.cwd().is_absolute())
print((Path('spam') / 'bacon' / 'eggs').is_absolute())

Path('python_learning/invite.docx')
print(Path.cwd()/Path('python_learning/invite.docx'))

#parts
  
print('--- parts ---')
p = Path('D:/NEXT/python_learning/invite.docx')
print(p.anchor)
print(p.parent)  
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)  

print('--- split path ---')
p = Path('D:/NEXT/python_learning/invite.docx')
print(p.parts)
print(p.parts[3])  
print(p.parts[0:1])


print('--- parent---')
print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])


print('--- stat_result---')

calc_file = Path('C:/Windows/System32/calc.exe')
print(calc_file.stat())


print('--- glob pattern---')
# * matches any text, all filenames   ? matches exactly one char 
for name in Path('D:/NEXT/pthon_learning/disha_python_practice').glob('*'):
  print(name)

print('_____Path Validity___')
p = Path('D:/NEXT/pthon_learning/disha_python_practice')
print(p.exists())
print(p.is_file())
print(p.is_dir())


print('_____file hadling___')

file = Path('trial.txt')
file.write_text("Hello world")
print(file.read_text())

print(Path.home())
print(p)

hello_file = open(p/'test.txt',encoding = 'UTF-8')
hello_content = hello_file.read()
print(hello_content)
hello_file.seek(0)
print(hello_file.readlines())


with open('data.txt','w',encoding='UTF-8') as file_obj:
  file_obj.write('Hello world')

with open('data.txt', encoding='UTF-8') as file_obj:
  content = file_obj.read()

print(content)


print('____shelve module___')

import shelve
shelf_file = shelve.open('mydata')
shelf_file['cats'] = ['zophie','pooka','simon']
shelf_file.close()