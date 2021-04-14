import html


def to_html(text, url):
    return f"<a href='{url}'>{html.escape(text)}</a>"
