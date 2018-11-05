class file:
    import os.path

    def __init__(self):
        pass

    def exists(self, file_name):
        return self.os.path.isfile(file_name)

    def read(self, src_file):
        with open(src_file, 'r') as f_input:
            input_content = f_input.read()
            f_input.close()
        return input_content

    def write(self, target_file, output_content):
        with open(target_file, 'w+') as f_output:
            f_output.write(output_content)
            f_output.close()