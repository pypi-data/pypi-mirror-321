from crystalpy_barno.reports.report_factory import ReportFactory
from crystalpy_barno.enums import FileTypes

def generate_report(report_type, filename, output_path, parameters, formulas, sp_name, file_type=FileTypes.PDF):
    report = ReportFactory.create_report(report_type, filename, output_path, parameters, formulas, sp_name)
    export_format = ReportFactory.get_export_format(file_type)
    report.export(export_format)
    print(f"Report exported to {output_path} in {file_type.upper()} format.")
