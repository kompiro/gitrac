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
