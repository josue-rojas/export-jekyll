# export-jekyll

Script to export a Jekyll page along with its local files (css, images, js, etc)

### Usage:
(Note this uses python 2.7)
- First move export.py to a folder in jekyll project. I just made '\_scripts' folder
- add export.py in the exclude in jekyll config
- read the arguments
  >-i --input:  path of page to be exported

  >-o --output: path for exports

  >-p --permalink: flag that tells to use and keep permalink

  >-l --link: new permalink to use ie "/thislink", note: this
overrides -p

  >-h --help: print this text

- BEFORE running make sure your most recent change is rendered (just run 'jekyll serve')
- cd into the folder and call script in terminal to do your bidding

  ```bash
  python export.py -i /User
  # ALL THESE EXAMPLE EXPORT LOCALFILES THAT ARE REQUESTED BY THE HTML

  # this one exports about.html into exportfolder and adds permalink "/"
  python export.py -i '/Users/josuerojas/GitHub/JekyllProject/pages/about.html' -o '/Users/josuerojas/GitHub/exportfolder' -l '/'

  # this one exports about.html into exportfolder and adds permalink "/about"
  python export.py -i '/Users/josuerojas/GitHub/JekyllProject/pages/about.html' -o '/Users/josuerojas/GitHub/exportfolder' -l '/about'

  # this one exports about.html into exportfolder and adds keeps permalink
  python export.py -i '/Users/josuerojas/GitHub/JekyllProject/pages/about.html' -o '/Users/josuerojas/GitHub/exportfolder' -p

  # this one just exports about.html into exportfolder
  python export.py -i '/Users/josuerojas/GitHub/JekyllProject/pages/about.html' -o '/Users/josuerojas/GitHub/exportfolder'

  # this one just exports about.html into pages folder (no -o means same export to same folder)
  python export.py -i '/Users/josuerojas/GitHub/JekyllProject/pages/about.html'
  ```
