# Copyright 2015 Futurewei.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Initial Mitaka no-op script.

Revision ID: 48072cb59133
Revises: start_networking_sfc
Create Date: 2015-07-28 22:18:13.330846

"""

from neutron.db.migration import cli


# revision identifiers, used by Alembic.
revision = '48072cb59133'
down_revision = 'start_networking_sfc'
branch_labels = (cli.CONTRACT_BRANCH,)


def upgrade():
    pass
