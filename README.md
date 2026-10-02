# Week 3 booking repository

For **IA 3.1 and IA 3.2**. This is a new teaching repository built from the Week 2 booking model, split across a few files so that you can practise selecting context and inspecting changes. Keep it separate from your Week 1 and Week 2 folders.

The starter implements booking creation and conflict checks. `move_booking` is a function in `service.py`. Its declaration exists, but its body raises `NotImplementedError` until you implement it. Cancellation remains a lecture example from Week 2; this repository has no cancellation operation. Existing records may already have cancelled status.

## 1. Open the correct folder

Download `ICCS471_Week3_Booking_Starter.zip`, extract it, then open the extracted `booking_week3` folder in VS Code. Its Explorer should show `models.py`, `rules.py`, `service.py`, `SPEC.md` and the tests directly. All commands below run in this folder.

Python 3.12 is the teaching version. There are no third-party packages, server, database or API keys. Use your existing Python/uv setup.

## 2. Run the known baseline

In a VS Code PowerShell terminal, enter each command separately:

```powershell
Get-Location   # pwd on unix
Get-ChildItem  # ls on unix
uv run --python 3.12 python -m unittest -v test_baseline
```

Expected: **6 tests, OK**. This checks existing creation behaviour only.

Then inspect the unfinished feature:

```powershell
uv run --python 3.12 python -m unittest -v test_move_smoke
```

Expected in a fresh starter: **3 tests, 3 errors**, each caused by `NotImplementedError`. These are expected because the function is unfinished. They are different from import errors, a missing Python installation or a failure in the six baseline tests.

If `uv` is unavailable but Python 3.12 is installed, use `py -3.12 -m unittest -v test_baseline` on Windows, or `python3 -m unittest -v test_baseline` on Mac/Linux. Use the corresponding prefix for the other test commands. Otherwise report the setup problem and seek help. After five minutes, continue code inspection so setup does not consume the class.

## 3. Keep an untouched copy and a Git checkpoint

Before edits, keep a second extracted copy outside your working folder named `booking_week3_original`. Never edit that copy. Work in `booking_week3`.

For IA 3.2, use your own separate repository. Initialise Git in the working folder and commit the unchanged starter:

```powershell
git init
git add .
git commit -m "Week 3 starter baseline"
git rev-parse --short HEAD
git status --short
```

If Git asks for author identity, set your own name and email **for this repository** using `git config user.name "Your Name"` and `git config user.email "your-email"`, then repeat the commit. A clean baseline produces no output from `git status --short`. IA 3.2 requires your own GitHub repository and a pushed final commit.

After completing IA 3.1's `AGENTS.md`, you may make a second checkpoint before implementation. Write down which commit you will compare your implementation against. Git tracks saved files, so save before inspecting.

## 4. Inspect changes

Before staging or committing implementation changes:

```powershell
git status --short
git diff --stat HEAD
git diff HEAD -- service.py rules.py test_student.py
```

In the diff, lines beginning with `-` were removed and lines beginning with `+` were added; `---` and `+++` identify the compared files. `git diff --stat HEAD` is a file-level summary, not the detailed code review.

`git diff HEAD` includes staged and unstaged changes to tracked files since the current commit. It does **not** show the contents of new untracked files. Open files marked `??` by `git status` and read them too. If you already committed your implementation, compare with your recorded baseline commit instead of `HEAD`.

If Git setup is blocked, use VS Code's file comparison between the original and working copies. Record both versions, the files compared and the relevant before/after lines. This comparison fallback can earn full review credit; report it honestly and resolve repository access before submission.

## 5. Run the checks after implementation

```powershell
uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student
```

With exactly two new student test methods, this runs **11 tests**. The count alone is not evidence of adequate coverage. Read the assertions and relate them to SPEC.md. If you add extra methods, report the actual count.

## 6. If an edit goes wrong

Stop the agent. Save the questionable version separately before changing it. Use file comparison to understand the edit, then repair just the relevant lines or recover the affected file from the untouched copy. Do not overwrite useful work with a whole-folder reset. Re-run the relevant checks after the repair.

## 7. Prepare the submission

IA 3.1 requires one short PDF. IA 3.2 requires your own GitHub repository URL and final commit hash in Classroom, with a short `REVIEW.md` in the repository. No IA 3.2 PDF or code ZIP is required. See the assignment for the four REVIEW.md headings.

Keep these files at the repository root: `models.py`, `rules.py`, `service.py`, `test_baseline.py`, `test_move_smoke.py`, `test_student.py`, `SPEC.md`, `README.md`, `AGENTS.md` and `REVIEW.md`. Retain the template/fallback if useful. Exclude virtual environments, caches, credentials and unrelated files.

Create an empty repository in your GitHub account. Use GitHub's “push an existing repository” commands with your actual URL. Commit and push final work. Run `git rev-parse HEAD` for the submitted commit hash. Confirm the instructor can access it (grant access if private) and check a fresh clone runs with the documented command. No branches or pull requests are required.

If you began without a baseline commit, preserve the actual history and explain your untouched-copy comparison. Do not invent a baseline history.

If execution is still blocked at submission, include your exact command/error and source-based review. This can earn review and process credit, but cannot establish runtime behaviour or earn points that require observed passing checks. The supplied-candidate route solves AI access problems; it does not invent test results.
