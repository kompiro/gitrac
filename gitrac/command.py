#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3;
import os

home = os.environ['PWD'];
local_trac_dir = home+'/.trac';

class DbCommand:
    def __init__(self):
        self.init_ticket_db()

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

class ListCommand(DbCommand):

    def execute(self):
        result = self.ticket_list()
        for ticket in command.ticket_list():
            print ticket

    def ticket_list(self):
        """ list - show local ticket list """
        tickets = self.db.execute("select * from local_ticket");
        results = []
        for id,ticket_id,summary,close in tickets:
            resistered = ticket_id != None
            if resistered:
                show = ticket_id
            else:
                show = "x"
            results.append(ListedTicket(id,show,summary.encode('utf-8'),close == 1))
        return results


class ListedTicket():
    def __init__(self,id,remote_id,summary,closed):
        self.id = id;
        self.remote_id = remote_id;
        self.summary = summary;
        self.closed = closed;
    def __str__(self):
        return "%d\t%s\t'%10s'\t%s" % (self.id,self.remote_id,self.summary,self.closed)

if __name__=='__main__':
    command = ListCommand()
    for ticket in command.ticket_list():
        print ticket
