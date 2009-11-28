#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3;
import os

home = os.environ['PWD'];
local_trac_dir = home+'/.trac';

class ListCommand:

  def execute(self):
    self.init_ticket_db()
    self.ticket_list()

  def init_ticket_db(self):
    self.db = sqlite3.connect(local_trac_dir + '/ticket.db',isolation_level=None);
    self.create_local_ticket()

  def create_local_ticket(self):
    sql = u"""CREATE TABLE IF NOT EXISTS local_ticket (
      id integer primary key autoincrement,
      ticket_id integer,
      summary TEXT,
      close)
    """;
    self.db.execute(sql);

  def ticket_list(self):
    """ list - show local ticket list """
    for id,ticket_id,summary,close in self.db.execute('select * from local_ticket'):
      resistered = ticket_id != None
      if resistered:
        show = ticket_id
      else:
        show = "unregistered"
      print id,show,summary,close == 1


if __name__=='__main__':
  command = ListCommand()
  command.execute()
