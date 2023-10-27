from pptx2md.outputter import md_outputter


class heysam_outputter(md_outputter):
    def __init__(self, file_path):
        super().__init__(file_path)

    def put_table(self, table):
        def gen_table_row(row):
            return "| " + " | ".join([c.replace("\n", " ") for c in row]) + " |"

        self.ofile.write(gen_table_row(table[0]) + "\n")
        if len(table) == 1:
            return
        self.ofile.write(gen_table_row(["---" for _ in table[0]]) + "\n")
        self.ofile.write("\n".join([gen_table_row(row) for row in table[1:]]) + "\n\n")

    def get_strong(self, text):
        return text
