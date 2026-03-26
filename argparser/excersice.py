# to print json data in command line
import os
import json
import argparse
data ={
  'name':[
    'ccrs','ccrm','ccb','cprs'
  ],
  'count': 10,
  'recording':"x.rrec",
  'result':{
    'ccrs': 'Pass',
    'ccrm': 'Fail',
    'ccb': 'Pass',
    'cprs': None

  }
}
with open("_data.json",'w',encoding='utf-8') as f :
  json.dump(data,f,indent = 2)

parser = argparse.ArgumentParser(
  prog = "filereader",
  usage = '%(prog)s [options ]<imput_file>',
  description = "A simple scirpt to  manage json reading",
  epilog = 'Thanks for using',
  formatter_class = argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("input_file", help = "Path of json file")
parser.add_argument("-r", "--read", action = 'store_true' ,help ="ready and print the data")
args = parser.parse_args()

if not os.path.exists(args.input_file):
  parser.error(f"File not found")
  
with open(args.input_file, 'r',encoding = 'utf-8') as f:
  json_data = json.load(f)
  
if args.read:
  print(json.dumps(json_data,indent = 2))
else:
  print(json_data)

#run python excersice.py --help 
#python excersice.py _data.json here action will store false
#python excersice.py _data.json -r here true