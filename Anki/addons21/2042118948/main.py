#!/usr/bin/env python3

# Copyright: Tobias Haupenthal
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
###############################################################################

import sys
from pathlib import Path

# noinspection PyUnresolvedReferences
import aqt.utils as ankiutils
# noinspection PyUnresolvedReferences
from aqt import mw, utils, QAction

from .Papercard import IntendedException, Papercard


def get_cards(deck: str):
    ids = mw.col.find_cards('deck:"' + str(deck) + '"')
    questions = []
    answers = []
    for i in ids:
        card = mw.col.get_card(i)
        questions.append(card.question())
        answers.append(card.answer())
    return questions, answers


def export_papercards():
    debugmode = False
    version = (Path(__file__).parent / 'VERSION').read_text()
    deck = mw.col.decks.current()['name']
    cards = get_cards(deck)
    try:
        papercard = Papercard(utils, mw.addonManager, Path(mw.col.media.dir()), debugmode)
        papercard.export_paper(deck, cards)
    except IntendedException as e1:
        ankiutils.showCritical('<b>Papercards Plugin Exception (V:{})</b><br/>\n {}'.format(version, e1),
                               textFormat='rich')
    # noinspection PyBroadException
    except Exception as e2:
        msg = 'Papercards Plugin Exception (V:{})\n'.format(version)
        msg += '<class \'{}\'>: {}'.format(type(e2).__name__, e2)
        # noinspection PyTypeChecker
        raise Exception(msg).with_traceback(sys.exc_info()[2])


action = QAction("Export to Papercards", mw)
# noinspection PyUnresolvedReferences
action.triggered.connect(export_papercards)
mw.form.menuTools.addAction(action)
