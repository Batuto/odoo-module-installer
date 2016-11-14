#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import argparse

URL = "localhost:8069"  # localhost address : odoo port
DB = "script"
USERNAME = "admin"
PASSWORD = "admin"
uid = 1





common = xmlrpclib.ServerProxy("http://{}/xmlrpc/2/object".format(URL))
#uid = common.login(DB, USERNAME, PASSWORD)
#version_mesg = common.version()
mod_id = common.execute(DB, uid, PASSWORD, 'ir.module.module', 'search', [('name', '=', 'calendar')])
common.execute_kw(DB, uid, PASSWORD, "ir.module.module", "button_immediate_install", mod_id)
#print version_mesg
#help = common.__doc__()
#print help
# X.....................DatabaseName - UserID - UserPassword - ModelName          -  MethodName              -  [Parameters]
#install = common.execute_kw(DB,             uid,   PASSWORD,      "ir.module.module", "button_inmediate_install", ["stock"])
#some = common.execute_kw(DB, uid, PASSWORD, "sale.order", "onchange_partner_id", [[], [1]])
#print some
#install = common.execute_kw(DB, uid, ["stock"])
#uid = 1
#print install
