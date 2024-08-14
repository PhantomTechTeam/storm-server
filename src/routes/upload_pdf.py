import uuid
from os import environ, makedirs, path
import markdown
from xhtml2pdf import pisa
from io import BytesIO
import shutil


def create_pdf_file_locally(content: str, filepath: str):
    with open(f"{filepath}.md", "w+", encoding="utf8") as file:
        file.writelines(content)
    html_content = markdown.markdownFromFile(
        input=f"{filepath}.md", output=f"{filepath}.html"
    )
    with open(f"{filepath}.html", "r", encoding="utf-8") as file:
        # Read the content of the file and store it as a string
        html_content = file.read()

    # Create a BytesIO object to store the PDF output
    pdf_output = BytesIO()
    # Convert the HTML content to a PDF document
    pisa.CreatePDF(html_content, dest=pdf_output, encoding="utf-8")
    with open(f"{filepath}.pdf", "wb") as pdf_file:
        # Write the PDF content to the file
        pdf_file.write(pdf_output.getvalue())


def upload_pdf(content: str, user_id: str, topic: str):
    topic_updated = topic.replace(" ", "_").replace("-", "_").lower()
    folder_path = f'{environ.get("PDF_STORAGE")}/{topic_updated}'
    if path.isdir(folder_path):
        shutil.rmtree(folder_path)
        makedirs(str(folder_path))

    makedirs(str(folder_path))
    random_uuid = uuid.uuid4()

    pdf_name = f"{topic_updated}_{random_uuid}.pdf"
    pdf_filepath = f"{environ.get('PDF_STORAGE')}/{topic_updated}_{random_uuid}"
    # Using the markdown content, create a pdf file locally that will be uploaded to the cloud
    create_pdf_file_locally(content, pdf_filepath)

    if environ.get("PDF_STORAGE_SERVICE") == "supabase":
        from configs.supabase import Supabase

        supabase = Supabase()
        public_url = supabase.create_pdf(pdf_filepath, user_id, pdf_name, folder_path)

        data = {"public_url": public_url}
        return data
