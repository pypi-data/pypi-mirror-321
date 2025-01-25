from CrystalDecisions.CrystalReports.Engine import ReportDocument
from crystalpy_barno.helpers.database_helper import DatabaseHelper
from crystalpy_barno.helpers.report_parameter_helper import ReportParameterHelper

class BaseReport:
    def __init__(self, filename, output_path):
        self.report = ReportDocument()
        self.report.Load(filename)
        self.output_path = output_path

    def set_parameters(self, parameters):
        for name, value in parameters.items():
            ReportParameterHelper.set_parameter(self.report, name, value)

    def set_formula_fields(self, formulas):
        for name, value in formulas.items():
            ReportParameterHelper.set_formula_field(self.report, name, value)

    def apply_database_connection(self):
        DatabaseHelper.apply_connection(self.report)

    def export(self, format_type):
        self.report.ExportToDisk(format_type, self.output_path)
