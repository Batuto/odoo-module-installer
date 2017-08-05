# -*- coding: utf-8 -*-
import xmlrpclib

db = "script"
pwd = "admin"
usr = "admin"

conn = xmlrpclib.ServerProxy('http://127.0.0.1:8069/xmlrpc/2/common')
uid = conn.authenticate(db, usr, pwd, {})
print uid, "UserID"
uninstall = xmlrpclib.ServerProxy('http://127.0.0.1:8069/xmlrpc/2/object')
res_id = uninstall.execute(db, uid, pwd, 'ir.module.module', 'search', [('name', '=', 'calendar')])
print res_id
t = uninstall.execute(db, uid, pwd, 'ir.module.module', 'button_immediate_uninstall', res_id)
print t


