#!/usr/bin/env python
""" PyCal
This creates a daily, task driven, today based calendar.
The output is text to represent a calendar, with important events in the calendar.

Representations of the next few days, and a record of what was done can be obtained.

This will require the ability to add items, tasks, meetings, etc.
Importance, severity, date due, etc. can be represented and tracked.

"""

import optparse

import sqlite3
conn = sqlite3.connect('pyCal.db')

optparser = optparse.OptionParser( usage="%prog [options]", version="$prog @VERSION@" )
optparser.add_option( "-n", "--new", action="store_true", dest="newItem", default=False,
		help="make a new entry" )
optparser.add_option( "-2", "--todo", action="store_true", dest="toDo", default=False,
		help="todo flag" )
optparser.add_option( "-b", "--birthday", action="store_true", dest="birthday", default=False,
		help="birthday flag" )


(options, args) = optparser.parse_args()
