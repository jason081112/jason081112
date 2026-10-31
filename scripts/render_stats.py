#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 jason081112
# SPDX-License-Identifier: MIT
"""Generate GitHub stats SVGs for the profile README.

Why this exists: `github-readme-stats.vercel.app` is unreachable from many
networks (verified: connection times out, http=000), so the two cards in the
README rendered as broken images. This script produces the same information as
static SVG committed into the repo, so the README depends on nothing but
GitHub itself.

Usage:
    GITHUB_TOKEN=<token> python3 scripts/render_stats.py
    # locally, `gh auth token` is used when GITHUB_TOKEN is absent
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

LOGIN = os.getenv("PROFILE_LOGIN", "jason081112")
OUT_DIR = Path(__file__).resolve().parents[1] / "resources"
API = "https://api.github.com/graphql"

BG = "#0d1117"
BORDER = "#30363d"
TITLE = "#c9d1d9"
SUBTLE = "#8b949e"
ACCENT = "#58a6ff"
BAR = ["#3572A5", "#f1e05a", "#e34c26", "#563d7c", "#89e051", "#b07219"]

QUERY = """
query($login: String!) {
  user(login: $login) {
    name
    login
    followers { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10) { edges { size node { name color } } }
      }
    }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
    }
  }
}
"""


def _token() -> str:
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if token:
        return token
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception as exc:  # noqa: BLE001
        raise SystemExit(f"没有 GITHUB_TOKEN，也拿不到 gh token：{exc}") from exc


def fetch(login: str) -> dict:
    payload = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    request = urllib.request.Request(
        API, data=payload,
        headers={
            "Authorization": f"bearer {_token()}",
            "Content-Type": "application/json",
            "User-Agent": "profile-stats-renderer",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.loads(response.read().decode())
    if "errors" in data:
        raise SystemExit(f"GraphQL 报错：{data['errors']}")
    return data["data"]["user"]


def summarize(user: dict) -> dict:
    repos = user["repositories"]["nodes"]
    stars = sum(node["stargazerCount"] for node in repos)

    sizes: dict[str, int] = defaultdict(int)
    colors: dict[str, str] = {}
    for node in repos:
        for edge in node["languages"]["edges"]:
            name = edge["node"]["name"]
            sizes[name] += edge["size"]
            colors[name] = edge["node"]["color"] or "#8b949e"

    total = sum(sizes.values()) or 1
    langs = sorted(sizes.items(), key=lambda item: -item[1])[:6]

    contrib = user["contributionsCollection"]
    commits = contrib["totalCommitContributions"]
    pulls = contrib["totalPullRequestContributions"]
    issues = contrib["totalIssueContributions"]

    return {
        "login": user["login"],
        "stars": stars,
        "repos": user["repositories"]["totalCount"],
        "followers": user["followers"]["totalCount"],
        "commits": commits,
        "pulls": pulls,
        "issues": issues,
        "langs": [(name, size, colors[name], size / total) for name, size in langs],
    }


def _esc(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def stats_svg(stat: dict, *, width: int = 420, height: int = 150) -> str:
    cells = [
        (str(stat["stars"]), "Total Stars"),
        (str(stat["commits"]), "Commits"),
        (str(stat["repos"]), "Public Repos"),
        (str(stat["followers"]), "Followers"),
    ]
    col_w = (width - 40) / 2
    rows = []
    for index, (value, label) in enumerate(cells):
        col, row = index % 2, index // 2
        x = 20 + col * col_w
        y = 62 + row * 44
        rows.append(
            f'<text x="{x:.0f}" y="{y}" fill="{ACCENT}" font-size="20" font-weight="600">'
            f"{value}</text>"
            f'<text x="{x:.0f}" y="{y + 18}" fill="{SUBTLE}" font-size="12">{label}</text>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" \
viewBox="0 0 {width} {height}" role="img" aria-label="GitHub stats">
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" fill="{BG}" \
stroke="{BORDER}"/>
  <text x="20" y="30" fill="{TITLE}" font-size="14" font-weight="600">\
{_esc(stat['login'])} · GitHub Stats</text>
  {''.join(rows)}
</svg>
"""


def langs_svg(stat: dict, *, width: int = 420, height: int = 170) -> str:
    langs = stat["langs"]
    bar_x, bar_w = 20, width - 40
    segments = []
    cursor = bar_x
    for index, (_, _, color, ratio) in enumerate(langs):
        seg_w = bar_w * ratio
        segments.append(
            f'<rect x="{cursor:.2f}" y="46" width="{max(seg_w, 0):.2f}" height="8" rx="4" '
            f'fill="{color or BAR[index % len(BAR)]}"/>'
        )
        cursor += seg_w

    legend = []
    for index, (name, _, color, ratio) in enumerate(langs):
        col, row = index % 2, index // 2
        x = bar_x + col * (bar_w / 2)
        y = 82 + row * 24
        legend.append(
            f'<circle cx="{x + 5:.0f}" cy="{y - 4}" r="5" fill="{color or BAR[index % len(BAR)]}"/>'
            f'<text x="{x + 16:.0f}" y="{y}" fill="{TITLE}" font-size="12">'
            f"{_esc(name)}</text>"
            f'<text x="{x + 16:.0f}" y="{y + 14}" fill="{SUBTLE}" font-size="11">'
            f"{ratio * 100:.1f}%</text>"
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" \
viewBox="0 0 {width} {height}" role="img" aria-label="Top languages">
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" fill="{BG}" \
stroke="{BORDER}"/>
  <text x="20" y="30" fill="{TITLE}" font-size="14" font-weight="600">Top Languages</text>
  {''.join(segments)}
  {''.join(legend)}
</svg>
"""


def main() -> int:
    user = fetch(LOGIN)
    stat = summarize(user)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "stats.svg").write_text(stats_svg(stat), encoding="utf-8")
    (OUT_DIR / "top-langs.svg").write_text(langs_svg(stat), encoding="utf-8")
    print(f"[stats] stars={stat['stars']} commits={stat['commits']} repos={stat['repos']} "
          f"followers={stat['followers']}")
    print(f"[stats] languages={[name for name, *_ in stat['langs']]}")
    print(f"[stats] 写入 {OUT_DIR}/stats.svg 与 top-langs.svg")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
