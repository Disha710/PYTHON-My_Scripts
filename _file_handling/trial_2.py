import os
from pathlib import Path

print(Path('parent','subdir','dir'))

my_files = ['first.txt','second.csv','third.py']
for name in my_files:
  print(Path(r'D:/NEXT/Python',name))
  
  
print('---working with / ---')

print(Path(('spam')/Path('bacon','eggs')))

current_dir = Path.cwd()
print(current_dir)
os.chdir('D:\\NEXT')
print(Path.cwd())
print(Path.home())
os.chdir(current_dir)
print(Path.cwd())

print('---new dir---')
os.makedirs('D:\\NEXT\\python_learning\\new', exist_ok =True)
Path(r'D:/NEXT/python_learning/new2').mkdir(exist_ok=True)

print('---absolute path---')
print(Path.cwd().is_absolute())
print(Path('spam','bacon','eggs').is_absolute())

P1 = Path('disha/disha.txt')
p2 = Path.cwd()/P1
print(p2)


  
print('--- parts ---')
p3 = Path('D:/NEXT/python_learning/invite.docx')
print(p3.anchor)
print(p3.parent)
print(p3.name)
print(p3.stem)
print(p3.suffix)
print(p3.drive)

print('--- split path---')
print(p3.parts)
print(p3.parts[0])
print(p3.parts[2:])

print('--- parent---')
print(p3.parents[0])
print(p3.parents[1])
print(Path.cwd())
print(Path.cwd().parents[3])


print('--- stat_result---')

p4 = Path(r'D:\NEXT\pthon_learning\disha_python_practice\_file_handling\trial.txt')
calc_file = p4
print(calc_file.stat())

print('----glob pattern--')
files = list(Path.cwd().iterdir())
print(files)
for name in Path('D:/NEXT/pthon_learning/disha_python_practice') .glob('*'):
  print(f"name is: {name}")


print(p4.exists())
print(p4.is_file())
print(p4.is_dir())


#file handling

file = Path('trail_2.txt')
file.write_text("This is a sencond attempt")
print(file.read_text())

with open('data_1.txt','w',encoding='UTF-8') as f:
  f.write('This is me !!')

with open('data_1.txt',encoding='UTF-8') as f:
  content = f.read()

print(content)


import shelve
shelf_file = shelve.open('mydata2')
shelf_file['nam'] = ['xx','yy','zz']
shelf_file.close()
