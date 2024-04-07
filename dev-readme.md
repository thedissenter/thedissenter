# Website development guide
This document contains information to help web developers maintain this website's code.  If you are not a web developer or you just want to edit the website content, see [readme.md](dev-readme.md)

## Site structure
- The website uses the Astro web frameowrk. See https://astro.build/.
- Astro is built on Vite (https://vitejs.dev/), which is built on Node.js (https://nodejs.org/en).
Astro is a static website generator (like the better known Jekyll and Hugo), so no server-side processing is required to host the website (Unlike a wordpress websites that requires PHP and MySql).
- astrowind and incharge-podcaster are submodules of incharge-podcaster.

### thedissenter
Github workflows are in .github/workflows

### astrowind
https://github.com/incharge/astrowind
- Website pages are in src/pages
- Menu in src/navigation.js
- Site configuration in src/config.yaml
- When the site is built, it is stored in dist, but this is not committed to git
- This is a customised version of the Astrowind theme. The original version is here:
    https://astro.build/themes/details/astrowind/
    https://github.com/onwidget/astrowind
- Files ending in **.astro ** are an in JSX format, https://react.dev/learn#writing-markup-with-jsx

#### Third party modules
- Blog pagination
    See node_modules/@philnash/astro-pagination
    https://philna.sh/blog/2023/07/13/easy-and-accessible-pagination-links-for-your-astro-collections/
    https://github.com/philnash/astro-components
- PageFind is used for site search
    Pagefind official docs https://pagefind.app/docs/ui-usage/
    astro-pagefind GitHub https://github.com/shishkin/astro-pagefind
    Astro/PageFind Tutorial https://blog.otterlord.dev/posts/astro-search/
- lite-youtube-embed YouTube video player:
    https://www.npmjs.com/package/lite-youtube-embed
    https://github.com/paulirish/lite-youtube-embed
    This is a wrapper for the YouTube IFrame Player API
    https://developers.google.com/youtube/iframe_api_reference
    Demo with skip https://paulirish.github.io/lite-youtube-embed/variants/js-api.html
- VideoJs player, which is used to play audio
    https://github.com/videojs/video.js
    https://www.npmjs.com/package/video.js/v/7.0.3
    https://docs.videojs.com/
    https://videojs.com/guides
    https://docs.videojs.com/control-bar_skip-buttons_skip-forward.js.html
    https://videojs.com/guides/player-workflows/#showing-and-hiding-a-player
    https://videojs.com/guides/player-workflows/#using-playback-information-functions
    Note: VideoJs can play YouTube, but this is not used
    https://github.com/videojs/videojs-youtube
- Vanilla Cookie Consent
	https://cookieconsent.orestbida.com/
	https://github.com/orestbida/cookieconsent
    https://playground.cookieconsent.orestbida.com/
- Astro
    https://docs.astro.build/en/getting-started/
- Vite
    https://vitejs.dev/config
    https://vitejs.dev/guide/build.html
    https://vitejs.dev/guide/env-and-mode#node-env-and-modes
- Rollup
    https://rollupjs.org/migration/
- Tailwind
    https://tailwindcss.com/docs/installation
- HTML
    https://developer.mozilla.org/en-US/docs/Web/HTML/Element
    https://html.spec.whatwg.org/
    New features https://wicg.io/ and https://github.com/WICG
- Bash
    Bash cheat sheet https://devhints.io/bash
    Man https://www.man7.org/linux/man-pages/
- Python
    https://docs.python.org/3/library/
- AWS ClI
    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws
- VS Code
    https://dax.tips/2020/10/21/use-visual-studio-code-to-autoformat-json/

### Start a bash shell
```
# Use Windows explorer or Start/Run to run...
admin\shell.bat
```

### Upgrade vscode
Download the latest portable vscode for windows https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-archive
or browse to https://code.visualstudio.com/download and click the x64 zip option
Save to ~/installer
Replace the contents of ~/bin/vscode with the contents of the zip

### Start vscode
```
# In a bash shell, run...
bin/vscode/code.exe
```

### Start a local dev server
```
# From within a vscode shell...
~/thedissenter/incharge-podcaster/dev.sh
```
Browse to the link shown on the screen e.g. http://localhost:4321/thedissenter/

### Build a distributable release
```
# From within a vscode shell...
~/thedissenter/incharge-podcaster/build.sh
```
Exports the site to ~/thedissenter/astrowind/dist

### Preview the distributable release
```
# From within a vscode shell...
~/thedissenter/incharge-podcaster/preview.sh
```
Browse to the link shown on the screen e.g. http://localhost:4321/thedissenter/

### Create header.png from YOUTUBE.psd
- Delete all layers except the background (bottom layer)
- Scale the image width to 1600, maintaining aspect ratio
- Resize the canvass to 500 x 100
- Crop the background using the Crop tool & check the box marked Current layer only
- Change foreground colour to: d0b0b0
- Add a background layer & fill with foreground colour, move it to the bottom layer
- Reset the foreground colour to black
- Add layer mask with an invisible gradient, so the background colour shows on the right (See  https://daviesmediadesign.com/how-to-create-a-transparent-gradient-in-gimp/)
- Export to header.png, omitting colour profile
- Optimise the iamge e.g. https://tinypng.com/

