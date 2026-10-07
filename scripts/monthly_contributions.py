#!/usr/bin/env python3
"""Generate two static SVGs from GitHub monthly contribution totals (stdlib only)."""
import argparse
import calendar
from datetime import datetime, timedelta, timezone
from html import escape
import json
import math
import os
from pathlib import Path
import urllib.error
import urllib.request

QUERY = '''query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar { totalContributions }
    }
  }
}'''


def month_start(year, month, offset=0):
    index = year * 12 + month - 1 + offset
    return datetime(index // 12, index % 12 + 1, 1, tzinfo=timezone.utc)


def periods(now):
    for offset in range(-11, 1):
        start = month_start(now.year, now.month, offset)
        end = min(month_start(start.year, start.month, 1) - timedelta(seconds=1), now)
        yield start, end


def fetch_total(login, token, start, end):
    payload = json.dumps({'query': QUERY, 'variables': {
        'login': login, 'from': start.isoformat(), 'to': end.isoformat()}}).encode()
    req = urllib.request.Request('https://api.github.com/graphql', data=payload,
        headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json',
                 'User-Agent': 'monthly-contributions-chart'})
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f'GitHub API returned HTTP {exc.code}. Check token permissions.') from None
    except urllib.error.URLError:
        raise RuntimeError('Could not reach the GitHub API.') from None
    if result.get('errors'):
        raise RuntimeError('GitHub GraphQL rejected the query: ' +
                           '; '.join(str(e.get('message', 'Unknown error')) for e in result['errors']))
    user = result.get('data', {}).get('user')
    if not user:
        raise RuntimeError('GitHub username not found.')
    count = user['contributionsCollection']['contributionCalendar']['totalContributions']
    if not isinstance(count, int) or count < 0:
        raise RuntimeError('GitHub returned an invalid contribution count.')
    return count


def render(rows, login, now, dark):
    bg, fg, muted, grid, accent = (('#0D1117','#E6EDF3','#A8B5C6','#24344B','#7AA2F7')
                                  if dark else ('#F6F8FA','#172B4D','#52647A','#DCE5EF','#2458A6'))
    maximum = max(count for _, count in rows)
    step = max(1, math.ceil(maximum / 4))
    top = step * 4
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="380" viewBox="0 0 960 380" role="img" aria-labelledby="title desc">',
           '<title id="title">Monthly GitHub contributions — last 12 months</title>',
           '<desc id="desc">' + escape('; '.join(f'{d:%B %Y}: {n} contributions' for d,n in rows)) + '. Current month is incomplete.</desc>',
           f'<rect x="1" y="1" width="958" height="378" rx="16" fill="{bg}" stroke="{grid}"/>',
           f'<g font-family="Segoe UI,Arial,sans-serif" fill="{fg}">',
           '<text x="32" y="40" font-size="22" font-weight="700">Monthly Contributions</text>',
           f'<text x="32" y="65" font-size="13" fill="{muted}">{escape(login)} · Last 12 calendar months · Updated {now:%d %b %Y} (UTC)</text>']
    for i in range(5):
        y = 280 - i * 45
        out += [f'<path d="M66 {y}H930" stroke="{grid}"/>',
                f'<text x="55" y="{y+4}" text-anchor="end" font-size="12" fill="{muted}">{i*step}</text>']
    for i,(date,count) in enumerate(rows):
        x = 77 + i * 71
        h = count / top * 180
        out += [f'<rect x="{x}" y="{280-h:.2f}" width="44" height="{h:.2f}" rx="4" fill="{accent}" opacity="{0.65 if i==11 else 1}"><title>{date:%B %Y}: {count} contributions</title></rect>',
                f'<text x="{x+22}" y="{max(88, 271-h):.2f}" text-anchor="middle" font-size="12">{count}</text>',
                f'<text x="{x+22}" y="303" text-anchor="middle" font-size="12" fill="{muted}">{calendar.month_abbr[date.month]}{"*" if i==11 else ""}</text>',
                f'<text x="{x+22}" y="321" text-anchor="middle" font-size="11" fill="{muted}">{date.year}</text>']
    out += [f'<text x="32" y="354" font-size="12" fill="{muted}">* Current month is incomplete · GitHub contributions, not only commits</text>', '</g></svg>']
    return '\n'.join(out) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--username', default=os.getenv('PROFILE_USERNAME', 'MuhammadZainUlIslam'))
    parser.add_argument('--output', default='profile')
    args = parser.parse_args()
    token = os.getenv('GH_TOKEN')
    if not token:
        parser.error('GH_TOKEN is required; supply it through a GitHub Actions secret.')
    now = datetime.now(timezone.utc).replace(microsecond=0)
    # Fetch every month before writing, so API failures preserve existing charts.
    rows = [(start, fetch_total(args.username, token, start, end)) for start,end in periods(now)]
    directory = Path(args.output)
    directory.mkdir(parents=True, exist_ok=True)
    for theme in ('light', 'dark'):
        path = directory / f'monthly-contributions-{theme}.svg'
        temp = path.with_suffix('.tmp')
        temp.write_text(render(rows, args.username, now, theme=='dark'), encoding='utf-8')
        temp.replace(path)
    print('Updated both monthly contribution charts.')


if __name__ == '__main__':
    try:
        main()
    except RuntimeError as exc:
        raise SystemExit(str(exc))
