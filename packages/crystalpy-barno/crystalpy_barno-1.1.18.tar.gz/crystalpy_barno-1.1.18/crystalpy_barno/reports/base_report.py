from CrystalDecisions.CrystalReports.Engine import ReportDocument
from crystalpy_barno.config.database_config import DatabaseConfig
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

    def set_stored_procedure(self, stored_procedure_name):
        """
        Set the stored procedure for the report.
        :param stored_procedure_name: The name of the stored procedure.
        """
        database_name = DatabaseConfig.get_database_name()
        if database_name:
            # Set the stored procedure as the location for the first table
            self.report.Database.Tables[0].Location = f"{database_name}.dbo.{stored_procedure_name}"
        else:
            raise ValueError("Database name not set. Ensure the connection is properly configured.")

    def export(self, format_type):
        self.report.ExportToDisk(format_type, self.output_path)
