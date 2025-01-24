import os
import shutil
from functools import reduce

from simple_xlsx_writer import writer


class TestXlsxWriter:
    def test_always_passes(self):
        assert True


    @staticmethod
    def reduce_text_list(txt_as_list: [str]) -> str:
        return reduce(lambda txt, l: txt + l.strip(), txt_as_list, "")


    @staticmethod
    def reduce_text(multiline: str) -> str:
        return TestXlsxWriter.reduce_text_list(multiline.splitlines())


    @staticmethod
    def read_contents(file_path: str) -> str:
        with open(file_path, 'r') as f:
            sheet1_raw_data = f.readlines()
            return TestXlsxWriter.reduce_text_list(sheet1_raw_data)


    def test_generated_xlsx_file(self):
        # NOTE: we cannot simply test if the resulting file is a valid xlsx file so instead we test internal file contents
        # given
        base_path = "simple_xlsx_writer_test_files01"
        shutil.rmtree(base_path, ignore_errors=True)
        os.mkdir(base_path)
        data = [['A', 'B'],[1.1, 'TEST1'],[1.2, 'TEST2'],[1.3, 'TEST1']]
        # when
        writer.write_raw_data(base_path, 'test01', data, debug=True)
        # then file resulting exists as well as internal files (when debug=True files are not deleted)
        assert os.path.isfile(os.path.join(base_path, 'test01.xlsx'))
        assert os.path.isfile(os.path.join(base_path, 'test01', '[Content_Types].xml'))
        assert os.path.isfile(os.path.join(base_path, 'test01', '_rels', '.rels'))
        assert os.path.isfile(os.path.join(base_path, 'test01', 'xl', 'workbook.xml'))
        assert os.path.isfile(os.path.join(base_path, 'test01', 'xl', 'sharedStrings.xml'))
        assert os.path.isfile(os.path.join(base_path, 'test01', 'xl', '_rels', 'workbook.xml.rels'))
        assert os.path.isfile(os.path.join(base_path, 'test01', 'xl', 'worksheets', 'sheet1.xml'))

        # and sheet1.xml has expected contents
        sheet1_txt = self.read_contents(os.path.join(base_path, 'test01', 'xl', 'worksheets', 'sheet1.xml'))
        expected_sh1 = self.reduce_text(writer.__prepare_sheet1_xml__("""
            <row><c t="s"><v>1</v></c><c t="s"><v>2</v></c></row>
            <row><c t="n"><v>1.1</v></c><c t="s"><v>0</v></c></row>
            <row><c t="n"><v>1.2</v></c><c t="s"><v>3</v></c></row>
            <row><c t="n"><v>1.3</v></c><c t="s"><v>0</v></c></row>"""))
        assert sheet1_txt == expected_sh1
        # and sharedStrings.xml has expected contents
        shared_strings_txt = self.read_contents(os.path.join(base_path, 'test01', 'xl', 'sharedStrings.xml'))
        # NOTE: TEST1 is repeated twice so it appears at the top of the list
        expected_ss = self.reduce_text(writer.__prepare_shared_strings__(5,4,"""
            <si><t>TEST1</t></si>
            <si><t>A</t></si>
            <si><t>B</t></si>
            <si><t>TEST2</t></si>"""))
        assert shared_strings_txt == expected_ss

