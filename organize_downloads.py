"""
MIT License

Copyright (c) 2020 Yannick E.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Imports:
import os
import shutil


def createfolders(directories, directory_path): # This creates the folders in <directory_path>, where the files will be moved to.
    for key in directories:
        if key not in os.listdir(directory_path):
            os.mkdir(directory_path + '/'+key)
        if "OTHER" not in os.listdir(directory_path):
            os.mkdir(directory_path + '/'+"OTHER")

def organizefolders(directories, directory_path): #This organizes the different files into the specified folder
    for file in os.listdir(directory_path):
        if os.path.isfile(directory_path + '/'+file):
            srcpath = directory_path + '/'+file
            for key in directories:
                extension = directories[key]
                if file.endswith(extension):
                    destination = os.path.join(directory_path, key, file)
                    shutil.move(srcpath, destination)
                    break


def organize_remainings(directory_path): # This assigns files that don't have a corresponding folder into the <OTHER> directory.
    for file in os.listdir(directory_path):
        if os.path.isfile(directory_path + '/'+file):
            source = directory_path + '/' + file
            dest = os.path.join(directory_path, "OTHER", file)
            shutil.move(source, dest)


def organize_remaining_folders(directories, directory_path): # This assigns folders within the specified directory to the <FOLDER> dir.
    list_dir = os.listdir(directory_path)
    organized_folder = []
    for folder in directories:
        organized_folder.append(folder)
    organized_folder = tuple(organized_folder)
    for folder in list_dir:
        if folder not in organized_folder:
            source = directory_path + '/' + folder
            dest = os.path.join(directory_path, "FOLDERS", folder)
            shutil.move(source, dest)

if __name__ == '__main__':

    directory_path = input("Please enter the whole download directory location. E.G. C:/Users/yanni/Downloads. : ")
    directories = {
        "HTML": (".html5", ".html", ".htm", ".xhtml"),
        "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg","JPG",
                   ".heif", ".psd"),
        "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      "pptx"),
        "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PLAINTEXT": (".txt", ".in", ".out"),
        "PDF": ".pdf",
        "ROBLOX": (".rbxm", ".rbxl", ".rbxmx", ".rbxlx"),
        "OPENIV": ".oiv",
        "OPENVPN_CONFIGS": ".ovpn",
        "PYTHON": ".py",
        "INSTALLERS": (".exe", ".msi"),
        "OTHER": "",
        "FOLDERS": ""   
    }
    createfolders(directories, directory_path)
    organizefolders(directories, directory_path)
    organize_remainings(directory_path)
    organize_remaining_folders(directories, directory_path)
