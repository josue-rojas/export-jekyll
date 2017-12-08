# Todo
# add ability to also copy _config file (for jekyll sake)
# add ability to change project_root folder
# add ability to change render_sites
# might need to do same for css (some may have local files)
# clean comments/ remove useless ones
#
# profile page export
# python export.py -i '/Users/josuerojas/GitHub/Modulos-Design/pages/examples/simple-theme.html' -o '/Users/josuerojas/GitHub/josuerojasrojas.github.io' -l '/'
# python export.py -i '/Users/josuerojas/GitHub/Modulos-Design/pages/main/home.html' -o '/Users/josuerojas/Desktop/temp' -l '/'
# python export.py -i '/Users/josuerojas/GitHub/Modulos-Design/pages/examples/scrollexample.html' -o '/Users/josuerojas/Desktop/temp' -p
import re, os, sys, getopt, errno
from shutil import copyfile


# this file needs to be in _scripts folder or in a folder inside jekyll project
# or change project root
# might add option to change
project_root = '/'.join(os.getcwd().split('/')[:-1])
render_sites = project_root + '/_site'


# get the render page path
def getRenderedPage(route):
    with open(route, 'r') as before_render:
        for line in before_render.readlines():
            match = re.search(r'permalink: \/.*', line)
            if match:
                link = match.group()[11:]
                permalink_file = link if link != '/' else '/index'
                # returns route location file and permalink
                return [render_sites + permalink_file + '.html', link]
    print 'No permalink found!'
    exit()

# gets all local file paths from the rendere html
def getLocalPaths(render_page):
    local_files = []
    with open(render_page, 'r') as rendered_page:
        for line in rendered_page.readlines():
            match = re.findall(r'(\'\/[^\' ]*\'|\"\/[^\" ]*\")', line)
            if match:
                # while adding all the match also removes the quotes
                local_files += [local_file[1:(len(local_file)-1)] for local_file in match]
    return local_files

# copy the local files into the output folder
def copyLocalFiles(local_files, output):
    for local_file in local_files:
        src = project_root + '/_site' + local_file
        directory = '/'.join(local_file.split('/')[:-1])
        if not os.path.exists(output + directory):
            os.makedirs(output + directory)
        dst = output + local_file
        if os.path.isfile(src):
            copyfile(src, dst)

# add permalink to the beginning of the exported html (use for jekyll)
def addPermalink(permalink_route, export_html, new_permalink):
    with open(export_html, 'r+') as newHTML:
        original = newHTML.readline()
        permalink_route = permalink_route if new_permalink == '' else new_permalink
        permalink_text = '---\npermalink: '+ permalink_route + '\n---\n'
        newHTML.seek(0, 0)
        newHTML.write(permalink_text + original)

def usage():
    print 'Usage:\n-i --input:  path of page to be exported\n-o --output: path for exports\n-p --permalink: flag that tells to use and keep permalink\n-l --link: new permalink to use ie "/thislink", note: this overrides -p\n-h --help: print this text'

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:o:pl:', ['help', 'input=', 'output=', 'permalink', 'link='])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)
    route = ''
    output = ''
    permalink = False
    new_permalink = ''
    if len(opts) == 0:
        usage()
        exit()
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            exit()
        elif o in ('-i', '--input'):
            route = a
        elif o in ('-o', '--output'):
            output = a
        elif o in ('-p', '--permalink'):
            permalink = True
        elif o in ('-l', '--link'):
            new_permalink = a
        else:
            print 'unhandled option'

    # output defaults to route folder if no output
    output = output if output!='' else '/'.join(route.split('/')[:-1])

    # actual copying stuff
    render_page, permalink_route = getRenderedPage(route)
    local_files = getLocalPaths(render_page)
    copyfile(render_page, output + '/' + render_page.split('/')[-1])
    if permalink or new_permalink != '':
        addPermalink(permalink_route, output + '/' + render_page.split('/')[-1], new_permalink)
    copyLocalFiles(local_files, output)

if __name__ == "__main__":
    main()
