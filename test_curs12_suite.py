import unittest

import HtmlTestRunner

import test_curs12_formy_project_autocomplete
import test_curs12_formy_project_checkbox
import test_curs12_formy_project_form


class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_curs12_formy_project_checkbox.TestFormyCheckbox),
            unittest.defaultTestLoader.loadTestsFromTestCase(
                test_curs12_formy_project_autocomplete.TestFormyAutocomplete),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_curs12_formy_project_form.TestFormyForm),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='TestReportAutoCurs12',
            report_name='Smoke Test Result Curs12'
        )

        runner.run(teste_de_rulat)
