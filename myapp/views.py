import subprocess
from django.http import FileResponse
from django.conf import settings
import os

def generate_jasper_report(request):
    # Replace 'path/to/your/report.jrxml' with the actual path to your JasperReports file
    # Use absolute path instead of relative path
    report_path = os.path.join(settings.BASE_DIR, 'jasper', 'purchase order report_1_PO_305.jrxml')

    # Replace 'output_file.pdf' with the desired output file name
    output_file = 'output_file.pdf'
    output_file_path = os.path.join(settings.BASE_DIR, output_file)

    # Specify the correct full path to jasperstarter executable
    jasperstarter_path = '/usr/local/bin/jasperstarter/jasperstarter'
    
    # Run JasperReports command using subprocess
    subprocess.run([jasperstarter_path, 'process', report_path, '-o', output_file_path])

    # Return the generated PDF file as a response
    with open(output_file_path, 'rb') as f:
        response = FileResponse(f, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{output_file}"'
        return response
