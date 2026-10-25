<div align="center">

# Hi there, I'm Jason Wang 👋

<img src="resources/globe.gif" width="96" alt="spinning globe" />

**Student developer · Building a privacy-first companion AI, games, and tools for education**
学生开发者 · 做隐私优先的陪伴型 AI、游戏，以及赋能教育的技术

[![GitHub](https://img.shields.io/badge/GitHub-jason081112-181717?logo=github&logoColor=white)](https://github.com/jason081112)
[![Pre_Alpha](https://img.shields.io/badge/Pre_Alpha-in%20progress-2ea44f?logo=python&logoColor=white)](https://github.com/jason081112/Pre_Alpha)
[![Email](https://img.shields.io/badge/Email-contact-blue)](mailto:58059436+jason081112@users.noreply.github.com)

</div>

---

You could describe me as —

- 🤖 **companion AI builder** — building **Pre_Alpha**, a privacy-first companion AI: distill chat logs into a persona, run the persona engine in the cloud, and expose it through Web/PWA and an OpenAI-compatible API. P1 backend is complete; the distillation pipeline is next.
- 🎓 **edtech builder** — puts technology and AI behind education: a gaokao essay evaluator that auto-detects **应用文 & 读后续写** and scores against the official rubric, plus an agent skill that distills a writer's style and recreates it in new text
- 🎮 **game maker** — built *Nyan Hero*, a browser platformer with difficulty progression, multi-mode obstacles, and four playable characters
- 🌍 **open-source translator** — contributed Simplified & Traditional Chinese to [Sniffnet](https://github.com/GyulyVGC/sniffnet) (41k+ ⭐), merged and added to the official contributors list

---

## 🚧 Currently Building

### 🫧 Pre_Alpha — privacy-first companion AI

Distill chat logs into a persona, then run the persona engine in the cloud. Web/PWA first; raw chat logs are not uploaded or stored.

把聊天记录蒸馏成一个人格，引擎在云端运行；Web/PWA 优先，原始聊天记录不上传、不入库。

**P1 backend complete · P1 后端已跑通**

- Email/password + invite auth, refresh tokens, per-user session isolation
- User/IP rate limits and platform-vs-BYOK quota split
- Multi-provider routing with fallback chains and encrypted BYOK keys
- Externalized agent state with CAS persistence
- OpenAI-compatible `POST /v1/chat/completions` (streaming + non-streaming), tested with the official `openai-python` SDK

[Repo](https://github.com/jason081112/Pre_Alpha) · [Progress board](https://github.com/users/jason081112/projects/1) · [OpenAI compatibility notes](https://github.com/jason081112/Pre_Alpha/blob/main/docs/p1-68-openai-compat.md)

`Python` `FastAPI` `OpenAI-compatible` `WIP`

> **Next:** P2 — chat-log distillation pipeline and persona profile.

---

## 🛠️ Projects

<table>
<tr>
<td width="50%" valign="top">

### 🕹️ Nyan Hero
<img src="resources/pixel-run.gif" width="150" alt="Nyan Hero character" />

Rainbow-hero endless runner. Difficulty ramps up over time, multi-mode pipes, and per-character stats tracking.

彩虹英雄跑酷游戏，难度渐进、多模式管子、分角色统计。

[▶ Play it live](https://jason081112.github.io/nyan.github.io/) · [Repo](https://github.com/jason081112/nyan.github.io)

`JavaScript` `HTML5 Canvas` `CSS`

</td>
<td width="50%" valign="top">

### 📝 高考作文诊断器

Auto-detects **应用文 & 读后续写**, then scores against the official gaokao rubric in three tiers.

自动识别应用文 & 读后续写，按新高考标准三档评分。

[▶ Try it](https://jason081112.github.io/gaokao-writing-evaluator/) · [Repo](https://github.com/jason081112/gaokao-writing-evaluator)

`HTML` `JavaScript`

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 🧬 写作蒸馏器 · Writing Distiller

Agent skill that distills a writer's style and then recreates it in new text.

蒸馏复刻任意写作风格的 agent skill。

`Python` `⚠️ Customized fork`

> Heavily customized fork of
> [larashero3-dotcom/writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill) —
> rewritten docs, rebuilt skill spec, localized content.

</td>
</tr>
</table>

---

## 🌍 Open Source

<img src="resources/coding.gif" width="230" alt="terminal committing translations" />

### [Sniffnet](https://github.com/GyulyVGC/sniffnet) — 41k+ ⭐

Comfortably monitor your network traffic.

| | |
|---|---|
| **Contributed** | Simplified & Traditional Chinese translations for v1.6 |
| **Bug fixed** | Simplified characters had leaked into the `zh_TW` strings (`数据阈值` → `數據閾值`) |
| **Merged** | PR [#1322](https://github.com/GyulyVGC/sniffnet/pull/1322), [#1323](https://github.com/GyulyVGC/sniffnet/pull/1323), [#1326](https://github.com/GyulyVGC/sniffnet/pull/1326) |
| **Recognized** | Added to the official [contributors list](https://github.com/GyulyVGC/sniffnet/blob/main/CONTRIBUTORS.md) — contributor **#119**, type 🌍 Translation |

---

## 📊 GitHub Stats

<div align="center">

![Jason's GitHub stats](https://github-readme-stats.vercel.app/api?username=jason081112&show_icons=true&theme=dark&hide_border=true)

![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=jason081112&layout=compact&theme=dark&hide_border=true)

</div>

---

<div align="center">

📫 **Get in touch** — [GitHub](https://github.com/jason081112) · [✉️ Email](mailto:58059436+jason081112@users.noreply.github.com)

<sub>Built with plain Markdown · Also live as a static site on [jason081112.github.io](https://jason081112.github.io)</sub>

</div>
