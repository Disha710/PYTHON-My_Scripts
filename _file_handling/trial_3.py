import os
from pathlib import Path

print(Path('user','project','file','_1.txt'))

file = ['one.txt','two.txt','three.csv']
for f in file:
	print(Path(r'D:/NEXT',f))

print(Path(('ADDING')/Path('blackslhes','overiding')))

dir = Path.cwd()
print(dir)
os.chdir('D:\\')
print(Path.cwd())
print(Path.home())
os.chdir(dir)
print(Path.cwd())


os.makedirs(r'D:/NEXT/new/dir',exist_ok=True)
Path(r'D:/NEXT2/new2/dir2').mkdir(exist_ok=True,parents=True)

print(Path.cwd().is_absolute())
print(Path('project','name').is_absolute())


path1 = Path('main/attemt.csv')
full_path = Path.cwd()/path1
print(full_path)

print(full_path.anchor)
print(full_path.name)
print(full_path.stem)
print(full_path.suffix)
print(full_path.parent)
print(full_path.drive)


print(full_path.parts)
print(full_path.parts[3])
print(full_path.parts[:4])


print(full_path.parents[0])
print(full_path.parents[1])
print(Path.cwd().parents[3])

files = list(Path.cwd().iterdir())
print(files)
for name in Path('D:/NEXT/pthon_learning/disha_python_practice') .glob('*'):
  print(name)


print(full_path.exists())
print(full_path.is_file())
print(full_path.is_dir())


file = Path('trail_3.txt')
file.write_text('My is Disha')
print(file.read_text())

with open('data_3.txt','w',encoding='UTF-8') as f:
	f.write('I am practcing python')

with open('data_3.txt','r',encoding='UTF-8') as f:
	data = f.read()

print(data)