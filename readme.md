# Website content editing guide
This document contains information to help you manage the **content** of this website.  It is aimed at people who are not web developers.  If you are a web developer planning to work on the code, you can find more technical information in [dev-readme.md](dev-readme.md)

## Site URLs
The dev site is hosted at: https://www.thedissenter.net/    

The website is made up of three git repositories:
- [thedissenter](https://github.com/thedissenter/thedissenter) contains podcast episode data 
- [astrowind](https://github.com/thedissenter/astrowind) contains the rest the website's structure and static pages
- [incharge-podcaster](https://github.com/thedissenter/incharge-podcaster) contains scripts that import podcast data and build the website

## How to edit website pages via the GitHub UI
Web pages are formatted using Markdown syntax.
For a concise list of Markdown formatting codes see https://www.markdownguide.org/cheat-sheet/.
For Markdown training see https://www.markdownguide.org/.
For more information about Markdown, see https://en.wikipedia.org/wiki/Markdown.

Web pages are stored in a git repository: https://github.com/thedissenter/astrowind

The **src/pages** folder contains the static website pages.
Files ending in **.md** are an extended version of Markdown format, so they are quite simple to edit.
Do not change other types of file unless you're a web developer and you're working in a development environment.

Note: Changes are not live (visible to website users) until the Deploy process completes.

- Before you can edit files, you need to log into https://github.com with an account that has write permission.
- Navigate to the [astrowind](https://github.com/thedissenter/astrowind) repository.
- Click through to [src/pages](https://github.com/thedissenter/astrowind/tree/main/src/pages)
- Click the page you want to edit.
- Click the pen icon in to top right. This shows `Edit this file` when the pointer hovers over it.
- Make your changes.
- Click `Preview` (top left) to see a side-by-side comparison of the old and new versions of the file.
- Click `Commit changes...` (top right). The `Commit changes` dialog box is displayed.
- Change the `Commit message` to describe your change.
- Make sure `Commit directly to the main branch` is selected.
- Click `Commit changes`

## How to deploy website changes to the live site

- Go to [thedissenter repository](https://github.com/thedissenter/thedissenter).
- Click [Actions](https://github.com/thedissenter/thedissenter/actions)
- Click [Deploy to GitHub Pages](https://github.com/thedissenter/thedissenter/actions/workflows/deploy.yaml) (on the left). A list is displayed showing the history of when this action has been run in reverse chronological order.
- Click `Run workflow`.  After a few seconds, a new item is added to the top of the list titled `Deploy to GitHub Pages`.  An orange dot on the left shows that the action is running.  A green tick shows that it has completed.  A red cross indicates there was an error.

## thedissenter git repository
The **yaml** folder contains podcast data in yaml format (See https://en.wikipedia.org/wiki/YAML and https://yaml.org/). This data is imported from YouTube and podcast platforms such as Spotify.
The **md** folder contains podcast pages in Markdown format.  These pages are generated from the podcast yaml files.
The **transcript** folder contains episode transcripts in markdown format.

Click the `Commits` link (top right) to see the history of commits (i.e. changes) to the repository. Each commit is shown with a description and date.  Commits titled `Import podcast episodes from rss feeds` are created by the daily import. Click the commit description to see which files were added/changed/removed in the commit.
