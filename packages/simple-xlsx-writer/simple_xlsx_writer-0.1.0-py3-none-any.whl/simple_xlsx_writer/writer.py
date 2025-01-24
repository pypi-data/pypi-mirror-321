import os
import datetime
import shutil

def __ensure_path__(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)

def __save_template__(path: str, template: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(template)

__CONTENT_TYPES_XML__ = \
"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default ContentType="application/vnd.openxmlformats-package.relationships+xml" Extension="rels"/>
<Default ContentType="application/xml" Extension="xml"/>
<Override ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml" PartName="/xl/sharedStrings.xml"/>
<Override ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml" PartName="/xl/workbook.xml"/>
<Override ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml" PartName="/xl/worksheets/sheet1.xml"/>
</Types>"""

__RELS__ = \
"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Target="xl/workbook.xml" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"/>
</Relationships>"""

__XL_WORKBOOK_XML__ = \
"""<?xml version="1.0" encoding="UTF-8"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
<workbookPr date1904="false"/><bookViews><workbookView activeTab="0"/></bookViews>
<sheets>
<sheet name="{{ SHEET_NAME }}" r:id="rId2" sheetId="1"/>
</sheets>
</workbook>"""

__XL_RELS_WORKBOOK_XML__ = \
"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Target="sharedStrings.xml" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings"/>
<Relationship Id="rId2" Target="worksheets/sheet1.xml" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"/>
</Relationships>"""

__SHEET1_XML__ = \
"""<?xml version="1.0" encoding="UTF-8"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<sheetData>
{{ ROWS }}
</sheetData>
</worksheet>"""

def __prepare_sheet1_xml__(rows: str) -> str:
    return __SHEET1_XML__.replace("{{ ROWS }}", rows)

__SHARED_STRINGS_XML__ = \
"""<?xml version="1.0" encoding="UTF-8"?>
<sst count="{{ TOTAL_COUNT }}" uniqueCount="{{ UNIQUE_COUNT }}" xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
{{ STRINGS }}
</sst>"""

def __prepare_shared_strings__(count: int, unique: int, strings: str) -> str:
    return (__SHARED_STRINGS_XML__
            .replace("{{ TOTAL_COUNT }}", str(count))
            .replace("{{ UNIQUE_COUNT }}", str(unique))
            .replace("{{ STRINGS }}", str(strings)))

def prepare_blank_xlsx(base_path: str, target_name: str, sheet_name: str = "data") -> None:
    __ensure_path__(base_path)
    target_path = os.path.join(base_path, target_name)
    __ensure_path__(target_path)
    rels_path = os.path.join(os.path.join(target_path, "_rels"))
    __ensure_path__(rels_path)
    xl_path = os.path.join(target_path, "xl")
    __ensure_path__(xl_path)
    xl_rels_path = os.path.join(os.path.join(xl_path, "_rels"))
    __ensure_path__(xl_rels_path)
    wks_path = os.path.join(xl_path, "worksheets")
    __ensure_path__(wks_path)

    __save_template__(os.path.join(target_path, "[Content_Types].xml"), __CONTENT_TYPES_XML__)
    __save_template__(os.path.join(rels_path, ".rels"), __RELS__)
    __save_template__(os.path.join(xl_path, "workbook.xml"),
                      __XL_WORKBOOK_XML__.replace("{{ SHEET_NAME }}", sheet_name))
    __save_template__(os.path.join(xl_rels_path, "workbook.xml.rels"), __XL_RELS_WORKBOOK_XML__)


def __group_by_and_count_data__(data: []) -> {}:
    shared_str_dict = {}
    for row in data:
        for cell in row:
            if type(cell) is str and cell != "":
                try:
                    existing_cnt = shared_str_dict[cell]
                except KeyError:
                    existing_cnt = 0

                shared_str_dict[cell] = existing_cnt+1

    return shared_str_dict


def __get_repeated_by_count__(str_dict: {}) -> {}:
    # take only repeated items, ignore the rest
    shared_dict_repetitions = dict(filter(lambda i: i[1] > 1, str_dict.items()))
    # sort repetitions by number of occurrences (this is not super slow)
    shared_str_dict_sorted = dict(sorted(shared_dict_repetitions.items(), key=lambda x: x[1], reverse=True))
    return shared_str_dict_sorted


def __write_sheet1_file__(base_path: str, target_name: str) -> None:
    with open(os.path.join(base_path, f".{target_name}_rows.tmp"), "r") as f:
        rows_txt=f.read()

    # now read contents of temporary files and save it to templates
    sheet1_xml = __prepare_sheet1_xml__(rows_txt)
    __save_template__(os.path.join(base_path, target_name, 'xl', 'worksheets', "sheet1.xml"), sheet1_xml)


def __write_shared_strings_file__(base_path: str, target_name: str, total_cnt: int, unique_cnt: int) -> None:
    with open(os.path.join(base_path, f".{target_name}_shared_str.tmp"), "r") as f:
        shared_str_txt=f.read()

    shared_strings_xml = __prepare_shared_strings__(total_cnt, unique_cnt, shared_str_txt)

    # finally save files to proper place...
    __save_template__(os.path.join(base_path, target_name, 'xl', "sharedStrings.xml"), shared_strings_xml)


def write_raw_data(base_path: str, target_file_name: str, data: [], debug: bool = False) -> None:
    # remove redundant file extension
    target_name = target_file_name if not target_file_name.endswith(".xlsx") else target_file_name[:-3]

    prepare_blank_xlsx(base_path, target_name)

    # assuming that most of the strings is actually unique, let's find all repeated strings and ignore the rest
    shared_str_dict = __group_by_and_count_data__(data)
    shared_str_dict_sorted = __get_repeated_by_count__(shared_str_dict)
    if debug:
        for i, item in enumerate(shared_str_dict_sorted.items()):
            print(f"{i}: {item[0]} {item[1]}")
            if i>10: break

    # open temporary files to write data on the fly (do NOT manipulate large strings in memory, this is super slow!)
    shared_str_file = open(os.path.join(base_path, f".{target_name}_shared_str.tmp"), "w")
    rows_file = open(os.path.join(base_path, f".{target_name}_rows.tmp"), "w")

    # add index that will be necessary when writing worksheet data
    # start preparing sharedStrings file, begin with repeated items
    # this is done at the same time to ensure that order of items is the same
    shared_dict_repetitions_indexed = {}
    for i,item in enumerate(shared_str_dict_sorted.items()):
        shared_dict_repetitions_indexed[item[0]] = (item[1], i)
        shared_str_file.write("<si><t>" + item[0] + "</t></si>\n")

    # loop over all cells and prepare temporary files with row data and shared strings (that appear only once)
    # using temporary files instead of arrays or strings *significantly* improves performance
    # as these operations are expensive in Python
    total_cnt = 0 # this is required for sharedStrings (total number of string occurrences)
    row_cnt = 0
    str_index_counter = len(shared_dict_repetitions_indexed) # this is required for sharedStrings (unique string references)
    for row in data:
        if row_cnt % 10000 == 0 and debug:
            print(f"{row_cnt} / {total_cnt} / {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        row_txt_one = "<row>"
        for cell in row:
            if type(cell) is int or type(cell) is float or (type(cell) is str and cell==""):
                # write numeric or empty cell
                row_txt_one += '<c t="n"><v>' + str(cell) + '</v></c>'
            elif type(cell) is str:
                total_cnt += 1
                try: # repeated string, already stored in sharedStrings
                    str_index = shared_dict_repetitions_indexed[cell][1]
                except KeyError: # one-off string, append it to sharedStrings and increment counter (item index)
                    shared_str_file.write("<si><t>" + cell + "</t></si>\n")
                    str_index = str_index_counter
                    str_index_counter += 1

                # write textual cell data with reference to shared string
                # leave it to Excel to figure out format (e.g. date)
                row_txt_one += '<c t="s"><v>' + str(str_index) + '</v></c>'
            else:
                raise TypeError("Unsupported type, ensure that input data is: int, float or str")

        row_txt_one += "</row>\n"
        rows_file.write(row_txt_one)
        row_cnt += 1

    shared_str_file.close()
    rows_file.close()

    # rewrite sheet1.xml file using temporary file already prepared
    __write_sheet1_file__(base_path, target_name)
    # rewrite sharedStrings.xml file temporary file already prepared
    __write_shared_strings_file__(base_path, target_name, total_cnt, str_index_counter)

    # ... and zip the whole directory as Excel file
    shutil.make_archive(os.path.join(base_path, target_name+".xlsx"), 'zip', os.path.join(base_path, target_name))
    shutil.move(os.path.join(base_path, target_name+".xlsx.zip"), os.path.join(base_path, target_name+".xlsx"))
    # cleanup
    os.remove(os.path.join(base_path, f".{target_name}_rows.tmp"))
    os.remove(os.path.join(base_path, f".{target_name}_shared_str.tmp"))
    if not debug:
        shutil.rmtree(os.path.join(base_path, target_name), ignore_errors=True)


def write_dummy(base_path: str, target_name: str) -> None:
    data = [["A", "B", "C"], ["TEST", 1.23, "2024-10-01 12:34:56"], ["TEST", 200, "2024-10-01 12:34:56"]]
    write_raw_data(base_path, target_name, data)
