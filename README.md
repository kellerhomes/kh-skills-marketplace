# KH Skills — shared skill bundle

This is a **plugin marketplace** with one plugin, `kh-skills`, that holds every
skill KH uses in Claude Cowork. Install it once on each device and they all
show the same skill menu. Add a new skill in one place and every device picks
it up on the next update.

## What's in here

```
kh-skills-marketplace/
├── .claude-plugin/
│   └── marketplace.json        ← the catalog (lists the kh-skills plugin)
└── plugins/
    └── kh-skills/
        ├── .claude-plugin/
        │   └── plugin.json     ← plugin metadata
        └── skills/
            ├── llm-council/    ← your existing council skill (already folded in)
            │   └── SKILL.md
            └── _template-skill/← copy this to make a new skill
                └── SKILL.md
```

Each subfolder under `skills/` is one skill. A skill is just a folder with a
`SKILL.md` inside it (plus any extra files it needs).

---

## One-time setup: host it (recommended)

To keep every device in sync automatically, put this folder in a place all your
devices can reach. Best option is a **private Git repo** (GitHub/GitLab). A
shared cloud folder (OneDrive/Dropbox) also works for the marketplace source.

> Note: OneDrive is fine as the *source* you install FROM. It does **not** work
> to just drop loose skills into Claude's app folder on OneDrive — Cowork reads
> skills from installed plugins, not from a synced folder. Installing this
> marketplace is what actually puts the skills on each machine.

If using Git:

```bash
cd kh-skills-marketplace
git init
git add .
git commit -m "Initial KH skills bundle"
# create a private repo, then:
git remote add origin <your-private-repo-url>
git push -u origin main
```

---

## Install on each device (server, PC, laptop)

Do this once per machine. Open Cowork and use the plugin commands:

**From a Git repo:**
```
/plugin marketplace add <your-private-repo-url>
/plugin install kh-skills@kh-marketplace
```

**From a local / OneDrive folder:**
```
/plugin marketplace add /path/to/kh-skills-marketplace
/plugin install kh-skills@kh-marketplace
```

You can also do it from the UI: Cowork → **Customize** → **Browse plugins** →
**Upload custom plugin**, and point it at this folder.

**Phone:** nothing to install. The phone rides on your account and your
desktop's setup.

---

## Add a new skill (the repeatable workflow)

When you find a skill you want — e.g. from a reel/tutorial — add it here once:

1. Copy the `_template-skill` folder inside `plugins/kh-skills/skills/` and
   rename it to your new skill name (kebab-case, e.g. `cold-email-writer`).
2. Open its `SKILL.md`, set the `name:` to match the folder, and write a clear
   `description:` — that's what tells Claude when to use it. Then write the body.
3. Bump the `version` in `plugins/kh-skills/.claude-plugin/plugin.json`
   (e.g. `0.1.0` → `0.2.0`). Optional but keeps updates clean.
4. Save / push:
   - Git: `git add . && git commit -m "Add <skill>" && git push`
   - OneDrive: just save — it syncs.

Then on each device, pull the update:
```
/plugin marketplace update kh-marketplace
```
The new skill appears in the `/` menu, namespaced as
`kh-skills:<skill-name>`.

---

## Quick reference

| Action | Command |
| --- | --- |
| Add this marketplace | `/plugin marketplace add <repo-or-path>` |
| Install the bundle | `/plugin install kh-skills@kh-marketplace` |
| Pull latest skills | `/plugin marketplace update kh-marketplace` |
| Remove the bundle | `/plugin uninstall kh-skills` |

Skills currently in the bundle: **ask-gary, brain, buildertrend, llm-council, resume**
(plus the `_template-skill` starter, which you can ignore or delete).

**buildertrend** runs KH jobs Buildertrend-style — schedules, daily logs,
change orders, selections & allowances, budgets/draws, punch lists, warranty —
as plain files in the vault's `Jobs/` folder, and doubles as a research
briefing on Buildertrend the product (features, pricing, competitors).
