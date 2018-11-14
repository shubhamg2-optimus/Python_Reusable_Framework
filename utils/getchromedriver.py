import requests
import urllib
import os
from zipfile import ZipFile


class getchromedriver():
    script_dir = os.path.dirname(__file__)

    def __init__(self, logger):
        self.saveto = logger



    def getLatestVersionFromGoogle(self):
        version = requests.get('http://chromedriver.storage.googleapis.com/LATEST_RELEASE').text
        self.saveto.logger.info("Latest version from google : %s" % (version))
        return version.strip()


    def updateVersion(self, version):
        with open(self.script_dir+"/version.txt", 'w') as file:
            file.write(version)


    def getCurrentVersion(self):
        version = 0
        fullfilename = os.path.join(self.script_dir+"/", "version.txt")
        if (os.path.exists(fullfilename)):
            file = open(fullfilename, 'r')
            version = file.read().strip()

        if(version != 0):
            self.saveto.logger.info("Current version stored %s" % (version))

        return version


    def removeFiles(self):
        self.removefile(os.path.join(self.script_dir+"/", "version.txt"))
        self.removefile(os.path.join(self.script_dir+"/", "file.zip"))
        self.removefile(os.path.join(self.script_dir+"/", "chromedriver"))


    def removefile(self, filename):
        if os.path.exists(filename):
            try:
                os.remove(filename)
                self.saveto.logger.info("Removed file %s" % filename)
            except OSError:
                self.saveto.logger.info("Unable to delete the file %s" % filename)


    def downloadDriver(self, latestVersion, fileName):
        fullfilename = os.path.join(self.script_dir, "file.zip")
        url = "http://chromedriver.storage.googleapis.com/%s/%s.zip" % (latestVersion, fileName)
        urllib.request.urlretrieve(url, fullfilename)
        zip = ZipFile(fullfilename, 'r')
        zip.extractall(self.script_dir)
        zip.close()

    def make_executable(self, path):
        mode=0o775
        os.chmod(path, mode)


    def download(self, filename):
        latestVersion = self.getLatestVersionFromGoogle()
        currentVersion = self.getCurrentVersion()

        if (float(latestVersion) > float(currentVersion)):
            self.saveto.logger.info("Downloading from google. url: http://chromedriver.storage.googleapis.com/LATEST_RELEASE")
            self.removeFiles()
            self.downloadDriver(latestVersion,filename)
            self.updateVersion(latestVersion)
            self.make_executable(self.script_dir+'/chromedriver')
        else:
            self.saveto.logger.info("Version is latest. No downloading will occur.")
