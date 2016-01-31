# Back In Time
# Copyright (C) 2016 Taylor Raack
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public Licensealong
# with this program; if not, write to the Free Software Foundation,Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
import sys
import tempfile
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import config
import logger
import mount

def doOrWarn(exe):
    if os.environ.get('TRAVIS', 'None').lower() == 'true':
        exe()
    else:
        logger.warning("Not executing ssh tests")
            
class TestSSH(unittest.TestCase):
    # running this test requires that user has public / private key pair created and ssh server running

    def setUp(self):
        logger.DEBUG = '-v' in sys.argv
        self.config = config.Config()
        self.config.set_snapshots_mode('ssh')
        self.config.set_ssh_host('localhost')
        self.config.set_ssh_private_key_file(os.path.expanduser(os.path.join("~",".ssh","id_rsa")))
        self.mount_kwargs = {}

    def test_can_mount_ssh_rw(self):
        doOrWarn(lambda: self.internal_test(read_only = False, implicit_read_only = False))
        
    def test_can_mount_ssh_ro_implicitly(self):
        doOrWarn(lambda: self.internal_test(read_only = True, implicit_read_only = True))
    
    def test_can_mount_ssh_ro_explicitly(self):
        doOrWarn(lambda: self.internal_test(read_only = True, implicit_read_only = False))
        
    def internal_test(self, read_only, implicit_read_only):
        with tempfile.TemporaryDirectory() as dirpath:
            self.config.set_snapshots_path_ssh(dirpath)

            if implicit_read_only:
                mnt = mount.Mount(cfg = self.config, tmp_mount = True)
            else:
                mnt = mount.Mount(cfg = self.config, tmp_mount = True, read_only = read_only)
            mnt.pre_mount_check(mode = 'ssh', first_run = True, **self.mount_kwargs)

            try:
                hash_id = mnt.mount(mode = 'ssh', check = False, **self.mount_kwargs)
                full_path = os.path.expanduser(os.path.join("~",".local","share","backintime","mnt",hash_id,"mountpoint"))

                self.assertEquals(not read_only, os.access(full_path, os.W_OK))
            finally:
                mnt.umount(hash_id = hash_id)
