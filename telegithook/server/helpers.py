import html


def to_html(text, url):
    return (
        "<a href='" +
        url +
        "'>" +
        html.escape(text) +
        "</a>"
    )
