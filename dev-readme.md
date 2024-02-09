
## Site URLs
The dev site is hosted at: https://incharge.github.io/thedissenter/

## Site structure
The website uses the Astro web frameowrk. See https://astro.build/
Astro is built on Vite (https://vitejs.dev/), which is built on Node.js (https://nodejs.org/en)
Astro is a static website generator (like the better known Jekyll and Hugo), so no server-side processing is required to host the website (Unlike a wordpress websites that requires PHP and MySql)

The site is made up of three git repositories
thedissenter
    https://github.com/incharge/thedissenter
    Contains podcast data in /yaml and podcast web pages in /md
    Github workflows in .github/workflows
Astro website & Astrowind theme
    https://github.com/incharge/astrowind
    Contains the website structure
        Website pages in src/pages
        Menu in src/navigation.js
        Site configuration in src/config.yaml
        When the site is built, it is stored in dist
    This is a customised version of the Astrowind theme. The original version is here:
        https://astro.build/themes/details/astrowind/
        https://github.com/onwidget/astrowind
    A third-party module is used for blog pagination
        See node_modules/@philnash/astro-pagination
        https://philna.sh/blog/2023/07/13/easy-and-accessible-pagination-links-for-your-astro-collections/
        https://github.com/philnash/astro-components
    PageFind is used for site search
        Pagefind official docs https://pagefind.app/docs/ui-usage/
        astro-pagefind GitHub https://github.com/shishkin/astro-pagefind
        Astro/PageFind Tutorial https://blog.otterlord.dev/posts/astro-search/
    Astro component for embedding YouTube videos:
        https://www.npmjs.com/package/@astro-community/astro-embed-youtube
        https://github.com/delucis/astro-embed/tree/main/packages/astro-embed-youtube
        astro-embed-youtube is an astro wrapper for lite-youtube-embed:
        https://www.npmjs.com/package/lite-youtube-embed

inCharge podcaster
    https://github.com/incharge/incharge-podcaster
    Contains scripts that import a podcast into a website

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
Delete all layers except the background (bottom layer)
Scale the image width to 1600, maintaining aspect ratio
Resize the canvass to 500 x 65
Crop the background using the Crop tool & check the box marked Current layer only
Change foreground colour to: d0b0b0
Add a background layer & fill with foreground colour, move it to the bottom layer
Reset the foreground colour to black
Add layer mask with an invisible gradient, so the background colour shows on the right
    https://daviesmediadesign.com/how-to-create-a-transparent-gradient-in-gimp/
Export to header.png, omitting colour profile
Optimise the iamge e.g. https://tinypng.com/
