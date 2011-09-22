##
## smb-pyro.py
## Author : <shashi@inf.in>
## Started on  Tue Dec  2 13:30:02 2008 Shashishekhar S
## $Id$
## 
## Copyright (C) 2008 INFORMEDIA
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##

import Pyro.core
import Pyro.naming
from Pyro.errors import NamingError
from lib.sambashares import SambaShares

class SambaShares(Pyro.core.ObjBase, SambaShares):
    def __init__(self):
        Pyro.core.ObjBase.__init__(self)

Pyro.core.initServer()

ns=Pyro.naming.NameServerLocator().getNS()

daemon=Pyro.core.Daemon()
daemon.useNameServer(ns)

try:
    ns.createGroup(":smbshare")
except NamingError:
    pass
uri=daemon.connect(SambaShares(),":smbshare.op")

print "SMB Share Server started ..."
try:
    daemon.requestLoop()
finally:
    daemon.shutdown(True)

