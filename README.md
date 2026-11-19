# Decision Ledger

Your AI remembers what you said. It forgets what you said no to.

So every few weeks it suggests the idea you already killed, and you argue the same argument again. Decision Ledger keeps a record of every decision you make and every option you discard, with the reason and what would make you reconsider. Your AI checks it before it suggests anything.

```
You:    We get 11 paid signups a month. How should I grow this?
Claude: I'd usually suggest a free tier, but you discarded that on 2026-03-02:
        free users never upgraded in your last product. You said you'd only
        reopen it if paid signups stall below 5 a month for 2 months.
        At 11 a month that hasn't happened, so here's what I'd do instead...
```

Free and open source (MIT). Works with Claude Code, Claude.ai and ChatGPT.

## What it does

1. **Logs decisions with their losers.** When you commit to something, it writes down what you chose, what you rejected, why, and when to look again.
2. **Guards your past self.** Before recommending a price, a tool, a channel or a plan, it checks the ledger. If you already said no, it tells you when and why instead of pitching it as new.
3. **Answers "why did we...?"** with the date and the reason, quoted from your own words.
4. **Keeps the trail.** When you change your mind, the old decision is marked superseded and stays in the ledger. You can see how your thinking moved.

## Install in Claude Code (10 minutes)

1. Copy the skill (run from this folder):
   - macOS / Linux:
     `mkdir -p ~/.claude/skills/decision-ledger && cp skills/decision-ledger/SKILL.md ~/.claude/skills/decision-ledger/`
   - Windows (PowerShell):
     `New-Item -ItemType Directory -Force $HOME\.claude\skills\decision-ledger; Copy-Item skills\decision-ledger\SKILL.md $HOME\.claude\skills\decision-ledger\`
   - Check: the file must end up at `~/.claude/skills/decision-ledger/SKILL.md`. If it sits directly in `skills/`, it will not load.
2. Copy the `ledger/` folder into your project folder. Want one ledger for every project? Put it in your home folder and follow the full path note at the end of `setup/CLAUDE-snippet.md`.
3. Open the CLAUDE.md in your project folder (create an empty one if you have none) and paste the block from `setup/CLAUDE-snippet.md`. This makes the guard run every session, even when you forget to ask.
4. Open a terminal in your project folder, start Claude Code there, and type `/decision-ledger seed`. It interviews you about your last 5 real decisions. That is when it starts paying off.

## Use it in Claude.ai or ChatGPT

No terminal needed. Follow `setup/claude-ai-and-chatgpt.md`: one file in a Project, one block of instructions. The AI gives you each new row and you paste it into the file.

## What a record looks like

See `examples/`: a small business that set a price, raised it 7 weeks later and paused Instagram. Read `examples/2026-03-02-pricing-model.md` first. Each discarded option has a "reopen only if" line. That line is what stops the loop.

## Everyday use

- Just talk. When you say "let's go with B" or "drop that", it logs it.
- "Why did we pick €39?" → answer with date and reason.
- "Did we already try Instagram?" → yes, when, why it lost, what would bring it back.
- "What's due for a revisit?" → decisions whose date has passed.

## Files

| Path | What |
|---|---|
| `skills/decision-ledger/SKILL.md` | The skill Claude Code follows |
| `ledger/DECISIONS.md` | Your empty ledger index |
| `setup/CLAUDE-snippet.md` | Paste into CLAUDE.md so the guard always runs |
| `setup/claude-ai-and-chatgpt.md` | Version for Claude.ai and ChatGPT Projects |
| `examples/` | Three filled records and their index |

Your ledger is plain markdown in your own folder. Nothing leaves your computer except what your AI tool already sees.

Made by Nina Niamh · [ninaneev.github.io](https://ninaneev.github.io) · [TikTok](https://www.tiktok.com/@nina.neev)
