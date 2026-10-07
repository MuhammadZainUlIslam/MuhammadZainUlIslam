# Add your monthly contribution chart

This is an add-on to your current profile. Keep your existing README, headers, daily graph, streak.svg, and streak workflow.

## 1. Add the two files

In MuhammadZainUlIslam/MuhammadZainUlIslam, add these exact paths on the default branch:

- scripts/monthly_contributions.py
- .github/workflows/monthly-contributions.yml

You can use GitHub's Add file → Create new file for each path, pasting the file's full contents. This also avoids the hidden .github folder being missed when uploading from Finder. Do not replace an existing workflow: this has its own filename.

Commit with: feat(profile): add monthly contribution chart automation

## 2. Run it once

Open Actions → Update monthly contributions → Run workflow. Choose the default branch, then click Run workflow. When the run turns green, the bot commit should add:

- profile/monthly-contributions-light.svg
- profile/monthly-contributions-dark.svg

Only then add the README section, so your profile never references missing images.

## 3. Add the README section

Copy the contents of README-SECTION.md into your actual README.md, between the existing Contribution Activity graph and Streak Stats. Commit the README update. Do not overwrite your README with README-SECTION.md; it is only a snippet.

The workflow runs daily at approximately 02:23 UTC / 07:23 Pakistan time. GitHub may delay scheduled runs. You can also run it manually at any time.

## What the chart counts

It queries GitHub's contribution calendar monthly totals, rather than counting only commits. It shows the current month plus the previous 11 calendar months, including zero-activity months. In October 2026, that means November 2025–October 2026. The current month is marked with an asterisk because it is incomplete. Date boundaries use UTC. The older months are fetched too; you do not need to wait a year to build history.

The default workflow uses its built-in GITHUB_TOKEN. That token is restricted to this repository, so do not assume it includes activity from your other private repositories. Start with this setup; no personal token is required for public activity.

If you want authenticated owner-visible contribution counts, add your own personal access token as a repository Actions secret named MONTHLY_STATS_TOKEN (Settings → Secrets and variables → Actions → New repository secret), then rerun. Use a token with only the read access needed for the repositories whose contributions you want included; organization policies and token access can affect results. Never paste a token into the README, script, or workflow. The optional token is used only to read statistics; pushing uses GITHUB_TOKEN.

If the calendar exposes private activity counts to the token, those aggregate counts will become public in the generated chart. Repository names and private code are not queried or displayed. Compare the chart against your profile using equivalent visibility settings.

## If a run fails

- HTTP 401: check whether MONTHLY_STATS_TOKEN has expired, if you added one.
- HTTP 403 / GraphQL access error: check the Actions log and token permissions or organization restrictions.
- Push rejected: ensure repository policy allows this workflow to write to the default branch. Branch protections may require a different publishing approach.
- File not found: confirm both exact paths in step 1, including the leading dot in .github.
- Scheduled runs stop: GitHub can disable schedules in inactive public repositories; re-enable the workflow from Actions.

The package includes no invented contribution values. Actual charts are created by the first successful run. The Python script uses only the standard library; no pip installation is needed.
