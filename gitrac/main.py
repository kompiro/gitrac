#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,os.path
import sys
import sqlite3
import xmlrpclib
import ConfigParser

home = os.environ['PWD'];
local_trac_dir = home+'/.trac';

def parse_opt():
  if len(sys.argv) == 1:
    help();
    return;
  opt = sys.argv[1]
  if opt == "init":
    url = sys.argv[2]
    create_ticket_repository(url);
    return;

  init_ticket_db();
  if opt == "list":
    ticket_list();
    return;
  if opt == "add":
    summary = sys.argv[2]
    ticket_add(summary);
    return;
  if opt == "push":
    ticket_push();
    return;
  if opt == "help":
    help();
    return;

def create_ticket_repository(url):
  """ init [url] - initialized repository setting """
  config = ConfigParser.RawConfigParser();
  if os.path.exists(local_trac_dir) == False:
    os.mkdir(local_trac_dir);
  path = __get_config_path__()
  config.add_section("REPOSITORY")
  config.set("REPOSITORY","URL",url);
  config.write(open(path,"w"));
  init_ticket_db();

def init_ticket_db():
  global db;
  db = sqlite3.connect(local_trac_dir + '/ticket.db',isolation_level=None);
  create_local_ticket()
  #if not_exists_local_ticket():
  return db;

def not_exists_local_ticket():
  sql = """
    SELECT count(*) FROM sqlite_master WHERE
    type='table' AND name='local_ticket';
  """;
  for count in db.execute(sql):
    return count[0] == 0;

def create_local_ticket():
  sql = u"""CREATE TABLE IF NOT EXISTS local_ticket (
    id integer primary key autoincrement,
    ticket_id integer,
    summary TEXT,
    close)
  """;
  db.execute(sql);

def ticket_list():
  """ list - show local ticket list """
  for id,ticket_id,summary,close in db.execute('select * from local_ticket'):
    resistered = ticket_id != None
    if resistered:
      show = ticket_id
    else:
      show = "unregistered"
    print id,show,summary,close == 1

def ticket_add(summary):
  """ add [summary] - create ticket to local ticket """
  sql = u"""
  insert into local_ticket values(null,?,?,?)
  """;
  db.execute(sql,(None,summary.decode('utf-8'),False));  

def ticket_push():
  """ push - push tickets to Trac repository """
  config = ConfigParser.RawConfigParser();
  path = __get_config_path__()
  config.read(path);
  url = config.get("REPOSITORY","URL")
  server = xmlrpclib.ServerProxy(url);
  for id,ticket_id,summary,close in db.execute('select * from local_ticket'):
    resistered = ticket_id != None
    if resistered == False:
      registered_id = server.ticket.create(summary,"",{'type':'defect'})
      print "created", registered_id,summary;
      db.execute("update local_ticket set ticket_id=? where id = ?",(registered_id,id))

def help():
  """ help - showing message """
  usage_message = """Usage: gitrac [command] 
  command:
    %s
    %s
    %s
    %s
    %s""" % (
    create_ticket_repository.__doc__,
    ticket_add.__doc__,
    ticket_list.__doc__,
    ticket_push.__doc__,
    help.__doc__
    );
  print usage_message;

def __get_config_path__():
  return local_trac_dir + '/settings.conf';

def main():
  parse_opt();

if __name__=='__main__':
  main();

