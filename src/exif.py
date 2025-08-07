import exifread

class ExifData():
    def extract_exif_data(filename):
        with open(filename, "rb") as file_handle:
            return exifread.process_file(file_handle)
