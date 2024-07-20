import uuid
from os import environ, mkdir, path
import markdown
from xhtml2pdf import pisa
from io import BytesIO
import shutil
def create_pdf(content: str, filepath: str):
    with open(f"{filepath}.md", "w+", encoding="utf8") as file:
        file.writelines(content)
    html_content = markdown.markdownFromFile(input=f"{filepath}.md", output=f"{filepath}.html")
    with open(f"{filepath}.html", "r", encoding="utf-8") as file:
        # Read the content of the file and store it as a string
        html_content = file.read()

    # Create a BytesIO object to store the PDF output
    pdf_output = BytesIO()

    # Convert the HTML content to a PDF document
    pisa.CreatePDF(html_content, dest=pdf_output, encoding='utf-8')
    with open(f"{filepath}.pdf", "wb") as pdf_file:
        # Write the PDF content to the file
        pdf_file.write(pdf_output.getvalue())

def upload_pdf(content: str, user_id: str, topic: str):
    folder_path = f'{environ.get("PDF_STORAGE")}/{topic}'
    if(path.isdir(folder_path)):
        shutil.rmtree(folder_path)
        mkdir(str(folder_path))
    
    mkdir(str(folder_path))
    random_uuid = uuid.uuid4()
    topic_updated = topic.replace(" ", "_").lower()
    
    pdf_name = f"{topic_updated}_{random_uuid}.pdf"
    pdf_filepath = f"{environ.get('PDF_STORAGE')}/{topic_updated}_{random_uuid}"
    create_pdf(content, pdf_filepath)

    from configs.supabase import supabase_client, supabase_bucket
    with open(f"{pdf_filepath}.pdf", 'rb') as f:
        supabase_client.storage.from_(supabase_bucket).upload(file=f,path=f"{user_id}/{pdf_name}", file_options={"content-type": "application/pdf"})

    shutil.rmtree(folder_path)
    public_url = supabase_client.storage.from_(supabase_bucket).get_public_url(f"{user_id}/{pdf_name}")
    data = {"public_url": public_url}
    return data
