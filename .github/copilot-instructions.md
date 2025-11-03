## Purpose

This file gives an AI coding agent the minimal, actionable context to be productive in this repository.

## Repository snapshot (what I found)
- Single present file: `README.md` (root). It describes this repo as a Django project template and shows Windows/venv usage:
  - Virtualenv activation shown as: `env\Scripts\activate`
  - Commands: `django-admin startproject project name .` and `python manage.py startapp appname`
  - Reminder to add apps to `INSTALLED_APPS` (README mentions `restframework` and `appname`).

## Quick, concrete facts for AI agents
- Platform: Windows (user default shell: PowerShell). Workspace root: `d:\Water`.
- Branch: `main` (current). There are no source directories, requirements, or test files detected.
- There is no existing `.github/copilot-instructions.md` or other agent docs in the repo — this file was created to capture the above facts.

## What the agent should assume and check before changing code
- Confirm Python and Django versions with the repo owner before scaffolding or installing packages.
- Confirm whether the virtual environment name `env` (used in README) is authoritative; do not assume other env names.
- The README's `restframework` string is likely shorthand; confirm whether the project expects `rest_framework` (the package name) or a custom app called `restframework`.

## Typical tasks & how to perform them here (explicit, repo-specific)
- To reproduce the README steps on Windows PowerShell:
  - Activate venv: `env\Scripts\activate` (matching README).
  - Start project: `django-admin startproject <project_name> .`
  - Create app: `python manage.py startapp <appname>`
  - Register apps: edit the generated `settings.py` and add the app(s) to `INSTALLED_APPS`.

## Patterns / conventions to follow in this repo
- Because the repo is currently a Django template, prefer the conventional Django layout when adding code: a top-level `manage.py`, a project package with `settings.py`, and per-app folders.
- Keep Windows-safe paths and activation instructions in README updates (the user works on Windows by default).

## Integration points & missing pieces (what to ask the user)
- No requirements file (e.g., `requirements.txt` or `pyproject.toml`) was found — ask which dependency manager and lockfile to use.
- No tests or CI/CD found — ask whether the user wants GitHub Actions, pytest, or Django test runner wired up.
- Confirm desired package names and exact INSTALLED_APPS entries.

## When committing changes
- Use small, focused commits. Mention in the PR title that changes are scaffolded from the README (e.g., "Add django project scaffold and requirements").

## Example prompts the agent can run automatically (only after asking the user)
- "I will create a Python virtualenv named `env`, add `Django` and `djangorestframework` to `requirements.txt`, run `django-admin startproject` and commit the scaffold — proceed?"

## Notes & limitations
- This file documents only what is discoverable in the repository. The README indicates a Django template but the repo currently lacks source files, dependency manifests, tests, and CI.
- Ask for the missing pieces before performing destructive or large-scoped edits.

---
If any of these points are unclear or you'd like the agent to scaffold a specific Django version, dependency file format, or CI workflow, tell me which and I will update this file and proceed.
