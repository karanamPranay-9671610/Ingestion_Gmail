import os
import img2pdf
try:
    def convert_tiff_folder_to_pdf(input_folder, output_folder):
        """
        :param input_folder: the folder which contains the tif files
        :param output_folder: the folder where we can push the converted tif - pdf file.
        """
        tiff_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".tif")]

        for tiff_file in tiff_files:
            input_tiff_path = os.path.join(input_folder, tiff_file)
            output_pdf_path = os.path.join(output_folder, os.path.splitext(tiff_file)[0] + ".pdf")

            with open(input_tiff_path, "rb") as tif_file:  # Convert TIFF data to PDF data
                pdf_data = img2pdf.convert(tif_file)

            with open(output_pdf_path, "wb") as pdf_file:  # Write the PDF data to the output PDF file
                pdf_file.write(pdf_data)

            os.remove(input_tiff_path)
except Exception as e:
    print("The Conversion of .TIF to PDF is Failed in Conversion Module")

