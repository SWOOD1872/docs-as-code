import os
import markdown as md


def list_files(target_dir):
    """ Returns a list of all files in a given directory """

    file_paths = []
    for dirpath, _, files in os.walk(target_dir):
        for file in files:
            file_paths.append(os.path.join(dirpath, file))
    return file_paths or None


def create_file(target_file):
    pass


def list_dirs(target_dir):
    """ Returns a list of all directories in a given directory """

    dir_paths = []
    for dirpath, dirs, _ in os.walk(target_dir):
        for _dir in dirs:
            dir_paths.append(os.path.join(dirpath, _dir))
    return dir_paths or None


def create_dir(target_dir, postfix=None):
    """ Creates a directory based on the given directory """
    
    if postfix:
        postfix = f"_{postfix}"
        base_name = os.path.dirname(target_dir)
        file_name = os.path.basename(target_dir)
        dir_with_postfix = f"{base_name}{postfix}"
        target_dir = os.path.join(dir_with_postfix, file_name)
    if not postfix:
        postfix = ""
    os.mkdir(target_dir)

    return


def md2html(md_file):
    """ Converts a Markdown file to HTML """

    dir_name = os.path.dirname(md_file)
    file_name = os.path.splitext(os.path.basename(md_file))[0]
    html_file = f"{os.path.join(dir_name,file_name)}.html"
    md.markdownFromFile(input=md_file, output=html_file)
    
    with open(html_file, "r+", encoding="utf-8") as f:
        html_markup = f"<html>\n\t<head>\n\t\t<title>{file_name}</title>\n\t</head>\n\t<body>\n{f.read()}\n\t</body>\n</html>"
        f.seek(0)
        f.write(html_markup)

    return html_file


dirs = list_dirs("C:\\Testing\\md")

ctr = 0
for _dir in dirs:
    if ctr == 0:
        create_dir(_dir, postfix="dac")
    create_dir(_dir)


# Sam@Sam-Wood-PC MINGW64 ~/Documents/Code/DaC/dac
# $ python convert.py
# Traceback (most recent call last):
#   File "convert.py", line 66, in <module>
#     create_dir(_dir, postfix="dac")
#   File "convert.py", line 40, in create_dir
#     os.mkdir(target_dir)
# FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C:\\Testing\\md_dac\\functions'