"""
Reddit
"""
from models import SavedSource
from . import convert, NBSP, BUTTONS

LABEL = 'reddit'
MARK_CLICK = 'https://click.redditmail.com/'
MARK_POSTED = 'Posted by'


def start(subj, body):
    """
    parse Reddit message
    """
    SavedSource(label=LABEL, subject=subj, body=body).put()

    text = convert(body, extract_link=True).replace(NBSP, ' ')
    border = text.index(MARK_CLICK)

    head = text[:border]
    tail = text[border:]

    head = ' '.join(head[head.index(MARK_POSTED) + len(MARK_POSTED):].strip().split()[1:])
    link = "[Read]({})".format(tail.split()[0])

    return 'Reddit: ' + head + '\n' + BUTTONS + '\n' + link
