# © 2019 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import odoo.tests


@odoo.tests.tagged('post_install', '-at_install')
@odoo.tests.common.at_install(False)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_01_test_tour(self):
        self.phantom_js(
            "/web#action=test_new_api.action_discussions",
            "odoo.__DEBUG__.services['web_tour.tour'].run('advitus_Partners Hierarchy', 100)",
            "odoo.__DEBUG__.services['web_tour.tour'].tours['advitus_Partners Hierarchy'].ready",
            login="admin",
            timeout=120,
        )
