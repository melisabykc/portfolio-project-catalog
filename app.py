import argparse, json, sqlite3
from pathlib import Path
DB=Path(__file__).with_name('projects.sqlite3')
def connect(path=DB):
 c=sqlite3.connect(path); c.row_factory=sqlite3.Row; c.execute('CREATE TABLE IF NOT EXISTS projects(id INTEGER PRIMARY KEY, name TEXT NOT NULL, technology TEXT NOT NULL, url TEXT, status TEXT NOT NULL DEFAULT \'planned\')'); return c
def add(name,technology,url,status,path=DB):
 if not name.strip() or not technology.strip(): raise ValueError('name and technology are required')
 if status not in ('planned','in_progress','completed'): raise ValueError('invalid status')
 with connect(path) as c:
  cur=c.execute('INSERT INTO projects(name,technology,url,status) VALUES(?,?,?,?)',(name,technology,url,status)); return cur.lastrowid
def main():
 p=argparse.ArgumentParser(description='Portfolio project catalog'); s=p.add_subparsers(dest='cmd',required=True); a=s.add_parser('add'); a.add_argument('--name',required=True); a.add_argument('--technology',required=True); a.add_argument('--url',default=''); a.add_argument('--status',choices=['planned','in_progress','completed'],default='planned'); s.add_parser('list'); x=p.parse_args()
 if x.cmd=='add': print(json.dumps({'id':add(x.name,x.technology,x.url,x.status)}))
 else:
  with connect() as c: print(json.dumps([dict(r) for r in c.execute('SELECT * FROM projects ORDER BY id DESC')],indent=2))
if __name__=='__main__': main()
