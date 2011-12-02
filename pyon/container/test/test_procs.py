#!/usr/bin/env python

__author__ = 'Michael Meisinger'

from unittest import SkipTest

from pyon.container.procs import ProcManager
from pyon.service.service import BaseService
from pyon.util.int_test import IonIntegrationTestCase

class FakeContainer(object):
    def __init__(self):
        self.id = "containerid"
        self.node = None

class SampleProcess(BaseService):
    name = 'sample'
    dependencies = []

class TestProcManager(IonIntegrationTestCase):

    def test_procmanager_iso(self):
        fakecc = FakeContainer()
        pm = ProcManager(fakecc)
        self.assertTrue(hasattr(fakecc, "spawn_process"))
        pm.start()
        pm.stop()

    def test_procmanager(self):
        with self.container() as cc:
            pm = cc.proc_manager

            self._spawnproc(pm, 'service')

            self._spawnproc(pm, 'stream_process')

            self._spawnproc(pm, 'agent')

            self._spawnproc(pm, 'simple')

            self._spawnproc(pm, 'immediate')

            success = pm.spawn_process('sample1', 'pyon.container.test.test_procs', 'SampleProcess', None, 'BAMM')
            self.assertTrue(not success)

    def _spawnproc(self, pm, ptype):
        success = pm.spawn_process('sample1', 'pyon.container.test.test_procs', 'SampleProcess', None, ptype)
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()