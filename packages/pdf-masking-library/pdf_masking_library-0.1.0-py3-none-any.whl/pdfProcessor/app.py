from flask import Flask, request, jsonify
import time
import base64
from io import BytesIO
from pdf2image import convert_from_bytes
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from pdfrw import PdfReader, PdfWriter, PageMerge
import logging
from concurrent.futures import ThreadPoolExecutor

from .logger_config import setup_logger
from .pdf_processing import process_page

logger = setup_logger(log_file="masking_app.log", log_level=logging.DEBUG)

def create_app(custom_pattern=None):
    app = Flask(__name__)
    # custom_pattern = [r"\b\d{2}\b"]
    
    @app.route('/process_pdf', methods=['POST'])
    def process_pdf():
        start_time = time.time()

        try:
            data = request.get_json()
            if 'Base64' not in data:
                return jsonify({"error": "No file provided"}), 400

            base64_pdf_old = data['Base64']
            pdf_bytes_old = base64.b64decode(base64_pdf_old)
            images = convert_from_bytes(pdf_bytes_old, fmt='jpeg', dpi=100)

            pdf_buffer = BytesIO()
            pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)

            for img in images:
                img_buffer = BytesIO()
                img.save(img_buffer, format="JPEG")
                img_buffer.seek(0)

                img_reader = ImageReader(img_buffer)

                pdf_canvas.drawImage(img_reader, 0, 0, width=letter[0], height=letter[1])
                pdf_canvas.showPage()

            pdf_canvas.save()
            pdf_buffer.seek(0)

            new_pdf_bytes = pdf_buffer.read()
            base64_pdf = base64.b64encode(new_pdf_bytes).decode('utf-8')
            pdf_bytes = base64.b64decode(base64_pdf)

            try:
                pdf_reader = PdfReader(BytesIO(pdf_bytes))
            except Exception as e:
                logger.error(f"Error reading original PDF: {e}")
                return jsonify({"error": f"Error reading original PDF: {e}"}), 500
            
            num_pages = len(pdf_reader.pages)

            writer = PdfWriter()

            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(process_page, i + 1, pdf_bytes, pdf_reader, custom_pattern=custom_pattern) for i in range(num_pages)]
                for future in futures:
                    page_num, new_page = future.result()
                    original_page = pdf_reader.pages[page_num - 1]
                    if new_page:
                        PageMerge(original_page).add(new_page).render()
                    writer.addpage(original_page)

            # output_pdf_path = "static/masked_output.pdf"
            # with open(output_pdf_path, "wb") as output_pdf:
            #     writer.write(output_pdf)
                
            # with open(output_pdf_path, "rb") as output_pdf:
            #     encode_bytes = output_pdf.read()
            
            output_buffer = BytesIO()
            writer.write(output_buffer)
            output_buffer.seek(0)
            encode_bytes = output_buffer.read()

            encode_pdf_bytes = base64.b64encode(encode_bytes).decode('utf-8')
            execution_time = time.time() - start_time
            logger.info(f"Total execution time: {execution_time:.2f} seconds")
            

            return jsonify({'pdfBase64': encode_pdf_bytes}), 200

        except Exception as e:
            logger.error(f"Error in main function: {e}")
            return jsonify({"error": f"Error in main function: {e}"}), 500
        
    return app

# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True)