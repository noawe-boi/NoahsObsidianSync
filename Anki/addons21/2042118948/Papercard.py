#!/usr/bin/env python3

# Copyright: Tobias Haupenthal
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
###############################################################################
"""
This plugin exports all flashcards to pdf.
It adds a

Configuration
----------
This a plugin, which can export anki vocabulary cards to an HTML or PDF page.
You can use it to print them on paper.
"""

import base64
import logging
import re
import shutil
import subprocess
import sys
import time
from os import environ
from pathlib import Path
from string import Template
from urllib.request import urlopen

# noinspection PyUnresolvedReferences
from aqt.qt import QStandardPaths

# from .types import AnkiUtils, Config, Cards

###############################################################################
# Configuration
#


###############################################################################
# Main Program
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class IntendedException(Exception):
    pass


class Papercard(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Papercard, cls).__new__(cls)
        return cls._instance

    def __init__(self, ankiutils, addonmanager, mediapath: Path, debugmode=False):
        self.ankiutils = ankiutils
        self.addonmanager = addonmanager
        self.mediapath = mediapath
        self.config = None
        self.htmlout = None
        self.pdfout = None
        self.logger = self.init_logger(debugmode)

    @staticmethod
    def init_logger(debugmode):
        logger = logging.getLogger(__name__)
        if debugmode:
            logger.setLevel(logging.DEBUG)
            fh = logging.FileHandler('/tmp/papercards.log')
            fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            logger.addHandler(fh)
            logger.debug('logger started')
        return logger

    def get_outputdir(self) -> Path:
        path = self.config['output']['path']
        if path == 'download':
            return Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation))

        return self.get_homepath(path)

    @staticmethod
    def get_homepath(path: str) -> Path:
        path = Path(path)
        if not path.is_absolute():
            return Path.home() / path.as_posix()

        return path.absolute()

    def build_question_card(self, q: str) -> str:
        # logging.debug("build question")
        q = re.sub('<style>[^<]*</style>', '', q)
        q = re.sub('(<img.*? src=")(.*?)(".*?>)', self.replace_image_source, q)
        html = '<div class="cardA">{}</div>\n'.format(q)
        return html

    def build_answer_card(self, a: str) -> str:
        # logging.debug("build answer")
        if self.config['card']['skipQuestionOnBack']:
            a = a.split('<hr id=answer>')[-1].strip()
        a = re.sub('<style>[^<]*</style>', '', a)
        a = re.sub('(<img.*? src=")(.*?)(".*?>)', self.replace_image_source, a)
        html = '<div class="cardB">{}</div>\n'.format(a)
        return html

    def replace_image_source(self, match) -> str:
        filepath = match.group(2)
        imagefile = Path(match.group(2))
        ext = imagefile.suffix[1:]
        if re.match(r'https?://', filepath):
            img = base64.b64encode(urlopen(filepath).read())
        else:
            if not imagefile.is_absolute():
                imagefile = self.mediapath / imagefile
            if imagefile.exists():
                img = base64.b64encode(imagefile.read_bytes())
            else:
                return match.group(0)
        img_binary = '{}data:image/{};base64,{}{}' \
            .format(match.group(1), ext, img.decode('ascii'), match.group(3))
        return img_binary

    def prepare_html(self, content: str) -> str:
        settings = {
            'papersize': self.config['paper']['format'],
            'orientation': self.config['paper']['orientation'],
            'cardWidth': str(100 / self.config['paper']['cardsPerRow']) + '%',
            'cardHeight': str(100 / self.config['paper']['cardsPerCol']) + '%',
            'fontSize': str(self.config['card']['fontSize']),
            'cardPadding': str(self.config['card']['padding']),
            'borderWidth': '1' if self.config['card']['showBorder'] else 0,
            'flexDirection': 'row-reverse' if self.config['card']['reverseOrderOnBack'] else 'row',
        }
        css_style = (Path(__file__).parent / 'tpl/style.css').read_text()
        style = Template(css_style).substitute(settings)
        html_template = (Path(__file__).parent / 'tpl/page.html').read_text()
        html = Template(html_template).substitute({'style': style, 'content': content})
        return html

    def arrange_cards(self, cards) -> str:
        questions, answers = cards
        cards_per_page = self.config['paper']['cardsPerRow'] * self.config['paper']['cardsPerCol']
        html = ''
        i = j = 0
        while True:
            html += '<div class="pageA">\n'
            while i < len(questions):
                html += self.build_question_card(questions[i])
                i += 1
                if i % cards_per_page == 0:
                    break
            html += '</div><div class="pageB">\n'
            while j < len(answers):
                html += self.build_answer_card(answers[j])
                j += 1
                if j % cards_per_page == 0:
                    break
            html += '</div>'
            if j == len(answers):
                break
        return html

    def save_html(self, deck: str, content: str) -> Path:
        deck = deck.replace(':', '^')
        filetpl = self.config['output']['filename']
        filename = time.strftime(filetpl)
        filename = filename.replace('{deck}', deck)
        file = self.get_outputdir() / (filename + '.html')
        try:
            file.write_text(content, encoding='utf8')
        except (OSError, IOError) as e:
            error = 'HTML file saving failed: {}.\n Does the path "{}" really exists?'.format(e, file)
            logging.error(error)
            raise IntendedException(error)
        return file

    def generate_pdf(self, htmlfile: Path):
        if not self.config['output']['createPdf']:
            return
        if htmlfile is None or not htmlfile.exists():
            error = 'HTML file has not been generated. It is required for the pdf generation step.'
            logging.error(error)
            raise IntendedException(error)

        # generate pdf
        pdffile = htmlfile.parent / (htmlfile.stem + '.pdf')
        cmdrun = self.find_browser()
        cmd = [cmdrun] + ['--headless', '--no-pdf-header-footer', f'--print-to-pdf={pdffile}', f'{htmlfile}']
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf8')
            print(result)
        except Exception as e:
            error = 'PDF generation failed with an error: {}'.format(e)
            self.logger.error(error)
            raise IntendedException(error)

        return pdffile

    def find_browser(self):
        if sys.platform == 'win32':
            runcmd = self.find_win_browser()
        elif sys.platform == 'darwin':
            runcmd = self.find_mac_browser()
        else:
            runcmd = self.find_linux_browser()
        if not runcmd:
            error = ('To generate a PDF you need the browser Chrome.<br/>\n'
                     'Please install Google Chrome or disable pdf-generation in settings.')
            raise IntendedException(error)
        return runcmd

    @staticmethod
    def find_win_browser():
        browsers = [r'Google\Application\chrome.exe', r'Microsoft\Edge\Application\msedge.exe']
        for browserpath in browsers:
            for programdata in ['ProgramW6432', 'ProgramFiles(x86)']:
                if programdata not in environ:
                    continue
                path = Path(environ[programdata]) / browserpath
                if path.exists():
                    return str(path.absolute())

    @staticmethod
    def find_mac_browser():
        browsers = ['Google Chrome', 'Microsoft Edge']
        for browser in browsers:
            for apppath in [Path('/Applications'), Path.home() / 'Applications']:
                path = apppath / f'{browser}.app/Contents/MacOS/{browser}'
                if path.exists():
                    return str(path.absolute())

    @staticmethod
    def find_linux_browser():
        browsers = ['google-chrome', 'chrome', 'chromium', 'chromium-browser']
        for browser in browsers:
            result = shutil.which(browser)
            if result:
                return result

    def generate_paper(self, deckname, cards):
        if not deckname:
            self.ankiutils.show_info('Please select a deck')
            return
        content = self.arrange_cards(cards)
        html = self.prepare_html(content)
        htmlfile = self.save_html(deckname, html)
        pdffile = self.generate_pdf(htmlfile)
        if not self.config['output']['createHtml'] and htmlfile.exists():
            htmlfile.unlink()
            htmlfile = None
        return htmlfile, pdffile

    @staticmethod
    def link(path: Path, name=None) -> str:
        href = path.absolute().as_uri()
        linktext = name if name else path.name
        return '<a href="{}">{}</a>'.format(href, linktext)

    def retrieve_config(self):
        default_conf = self.addonmanager.addonConfigDefaults(self.addonmanager.addonFromModule(__name__))
        conf = self.addonmanager.getConfig(__name__)
        for i in default_conf:
            if i not in conf:
                conf[i] = default_conf[i]
            for j in default_conf[i]:
                if j not in conf[i]:
                    conf[i][j] = default_conf[i][j]
        return conf

    def export_paper(self, deckname: str, cards) -> None:
        self.config = self.retrieve_config()
        htmlfile, pdffile = self.generate_paper(deckname, cards)
        outputdir = htmlfile.parent

        infotext = 'File saved to directory:<br/>\n'
        infotext += 'Dir: ' + self.link(outputdir, outputdir) + '<br/>\n' if outputdir is not None else ''
        pdflink = 'Pdf: ' + self.link(pdffile) + '<br/>\n' if pdffile is not None else ''
        htmllink = 'Html: ' + self.link(htmlfile) + '<br/>\n' if htmlfile is not None else ''

        self.ankiutils.showInfo(infotext + pdflink + htmllink, textFormat='rich')
