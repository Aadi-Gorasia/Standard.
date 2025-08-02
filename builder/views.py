# builder/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.template import Context, Template

# Import Python's built-in libraries for handling files in memory and creating zips
import io
import zipfile

# Import the form we just created
from .forms import WebsiteGenerationForm


@login_required
def dashboard(request):
    """
    Displays the main user dashboard.
    """
    return render(request, 'builder/dashboard.html')


@login_required
def create_website_view(request):
    """
    This view handles both displaying the website creation form (a GET request)
    and processing the submitted form data to generate the website (a POST request).
    """
    
    # If the form is being submitted (POST request)
    if request.method == 'POST':
        form = WebsiteGenerationForm(request.POST)
        
        # Check if the submitted data is valid
        if form.is_valid():
            # Extract the cleaned data from the form
            data = form.cleaned_data
            
            # --- The Magic Happens Here: Generate the Website Files ---
            
            # 1. Define the paths to our raw template files
            template_dir = settings.BASE_DIR / 'builder' / 'site_templates' / 'portfolio'
            html_template_path = template_dir / 'template.html'
            css_template_path = template_dir / 'style.css'

            # 2. Read the raw HTML template content
            with open(html_template_path, 'r') as f:
                html_content = f.read()

            # 3. Use Django's template engine to replace the placeholders
            template = Template(html_content)
            context = Context(data) # The context is a dictionary of our form data
            rendered_html = template.render(context)
            
            # 4. Read the raw CSS content
            with open(css_template_path, 'r') as f:
                rendered_css = f.read()

            # 5. Create a ZIP file in memory (not on the server's disk)
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                # Write the final HTML file into the zip
                zip_file.writestr('index.html', rendered_html)
                # Write the CSS file into the zip
                zip_file.writestr('style.css', rendered_css)
            
            # Move the buffer's pointer to the beginning
            zip_buffer.seek(0)

            # 6. Create an HTTP response to serve the ZIP file as a download
            response = HttpResponse(zip_buffer, content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="your_website.zip"'
            return response

    # If it's a GET request (the user is just visiting the page),
    # create a blank form and display it.
    else:
        form = WebsiteGenerationForm()

    # Pass the form to the template for rendering
    return render(request, 'builder/create.html', {'form': form})