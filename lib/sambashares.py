##
## samba-shares.py
## Author : <shashi@inf.in>
## Started on  Tue Dec  2 11:29:05 2008 Shashishekhar S
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

from configobj import ConfigObj, SimpleVal

class SambaShares:

    def __init__(self):
        pass

    def addshare(self, name, comment, path, group):
        _smb = '/var/tmp/smb.conf'
        self.cfg = ConfigObj(_smb)
        cfg = self.cfg
        section = {
            'comment': comment,
            'path': '/store/'+path,
            'writable': 'yes',
            'browseable': 'yes',
            'create mask': '0765',
            'valid users': '@'+group,
            'public': 'yes'
            }
        cfg[name] = section
        cfg.write()
        return True

    def listshares(self):
        _smb = '/var/tmp/smb.conf'
        self.cfg = ConfigObj(_smb)

        cfg = self.cfg
        shares = []
        for k in cfg.keys():
            if (k != 'global'):
                try:
                    shares.append({'name': k, 'group': cfg[k]['valid users'].replace('@',''), 'path': cfg[k]['path'].replace('/store/','').replace('/','')})
                except KeyError:
                    pass
        return shares

    def remshare(self, name):
        _smb = '/var/tmp/smb.conf'
        self.cfg = ConfigObj(_smb)

        cfg = self.cfg
        cfg.pop(name)
        cfg.write()
        return True

    def modshare(self, name, comment, path, group):
        _smb = '/var/tmp/smb.conf'
        self.cfg = ConfigObj(_smb)

        cfg = self.cfg
        cfg[name]['comment'] = comment
        cfg[name]['path'] = '/store/'+path
        cfg[name]['valid users'] = '@'+group
        cfg.write()
        return True

    def getshare(self, name):
        _smb = '/var/tmp/smb.conf'
        self.cfg = ConfigObj(_smb)
        r = {}
        if self.cfg.has_key(name):
            r['name'] = name
            r['comment'] = self.cfg[name]['comment']
            r['path'] = self.cfg[name]['path'].replace('/store/','').replace('/','')
            r['group'] = self.cfg[name]['valid users'].replace('@','')
        return r


if __name__ == "__main__":
    c = SambaShares()
    s = c.addshare('SHARE-ONE', 'Example Share', 'one', 'office')
    print c.listshares()
    s = c.remshare('SHARE-ONE')
    print c.listshares()
#    t = c.modshare('Backup', 'For Backup', 'backup', 'bigbucks')
    print c.listshares()
    
