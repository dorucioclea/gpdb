"""
Copyright (c) 2004-Present Pivotal Software, Inc.

This program and the accompanying materials are made available under
the terms of the under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import tinctest

from mpp.models import SQLConcurrencyTestCase
from mpp.gpdb.tests.storage.lib import Database

os.environ['PGDATABASE'] = os.environ["USER"]

class Setup(SQLConcurrencyTestCase):

    @classmethod
    def setUpClass(cls):
        tinctest.logger.info('Running setup...')
        db = Database()
        db.setupDatabase()
            