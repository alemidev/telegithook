actions = {
    "forkee": (
        "{html(r['sender']['login'], r['sender']['html_url'])}"
        " forked"
        " {html(r['repository']['name'], r['repository']['html_url'])}."
        " Total forks now: {r['repository']['forks']}."
    )
}
