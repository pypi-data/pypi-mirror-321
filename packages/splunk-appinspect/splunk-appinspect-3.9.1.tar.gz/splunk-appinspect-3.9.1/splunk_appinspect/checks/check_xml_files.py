# Copyright 2019 Splunk Inc. All rights reserved.

"""
### XML file standards
"""

import logging
import re
import xml
from pathlib import Path
from typing import TYPE_CHECKING

import bs4
from defusedxml.sax import make_parser

import splunk_appinspect
from splunk_appinspect.constants import Tags

if TYPE_CHECKING:
    from splunk_appinspect import App
    from splunk_appinspect.reporter import Reporter


logger = logging.getLogger(__name__)
report_display_order = 7


@splunk_appinspect.tags(
    Tags.SPLUNK_APPINSPECT,
    Tags.CLOUD,
    Tags.PRIVATE_APP,
    Tags.PRIVATE_VICTORIA,
    Tags.MIGRATION_VICTORIA,
    Tags.PRIVATE_CLASSIC,
)
def check_that_all_xml_files_are_well_formed(app: "App", reporter: "Reporter") -> None:
    """Check that all XML files are well-formed."""

    # From Python cookbook
    # https://www.safaribooksonline.com/library/view/python-cookbook-2nd/0596007973/ch12s02.html
    def parse_xml(filename: Path) -> None:
        parser = make_parser()
        parser.parse(str(filename))

    for relative_filepath, full_filepath in app.get_filepaths_of_files(types=[".xml"]):
        try:
            parse_xml(full_filepath)
        except (xml.sax.SAXException, ValueError):
            reporter.fail(f"Invalid XML file: {relative_filepath}", relative_filepath)


@splunk_appinspect.tags(Tags.SPLUNK_APPINSPECT, Tags.CLOUD, Tags.MANUAL)
def check_for_xml_embedded_javascript(app: "App", reporter: "Reporter") -> None:
    """Check any XML files that embed JavaScript via CDATA for compliance
    with Splunk Cloud security policy.
    """
    for relative_filepath, full_filepath in app.get_filepaths_of_files(types=[".xml"]):
        with open(full_filepath, "rb") as file:
            soup = bs4.BeautifulSoup(file, "html.parser", store_line_numbers=False)
        script_elements = soup.find_all("script")

        cdata_script_elements = [
            e for e in soup(text=True) if isinstance(e, bs4.CData) and re.search(r"<script\b", e) is not None
        ]
        script_elements.extend(cdata_script_elements)

        if script_elements:
            total_lines_of_code_output = 0
            for element in script_elements:
                element_as_string = f"{element}"
                element_content_regex = re.compile(">(.*?)<.*(?:>)", re.DOTALL | re.IGNORECASE | re.MULTILINE)
                content_matches = re.findall(element_content_regex, element_as_string)

                for content_match in content_matches:
                    content_match_split = content_match.splitlines()
                    total_lines_of_code_output += len(content_match_split)

            total_lines_of_code_output += len(cdata_script_elements)
            reporter_output = (
                "Embedded JavaScript has been detected."
                f" Total line(s) of code found: {total_lines_of_code_output}."
                f" File: {relative_filepath}"
            )
            reporter.manual_check(reporter_output, relative_filepath)
