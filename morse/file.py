class file:
    """Class for file handling"""
    import os.path

    def __init__(self):
        pass

    def exists(self, file_name):
        """Function checks if given file exists."""
        return self.os.path.isfile(file_name)

    def read(self, src_file):
        """Function reads given file and returns it's content."""
        with open(src_file, 'r') as f_input:
            input_content = f_input.read()
            f_input.close()
        return input_content

    def write(self, target_file, output_content):
        """Function reads string and writes it to given file."""
        with open(target_file, 'w+') as f_output:
            f_output.write(output_content)
            f_output.close()