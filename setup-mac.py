from setuptools import setup

APP = ["TimelapsePhotoOrganiser.py"]
APP_NAME = "TimelapsePhotoOrganiser"
DATA_FILES = []

OPTIONS = {
    "argv_emulation": True,
    'iconfile': 'app.icns',
    'includes': ["sip", "PyQt4._qt"],
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Timelapse Photo Organiser",
        'CFBundleIdentifier': "com.kuntat.osx.timelapsephotoorganiser",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"GNU General Public License (GPL)"
    }

}

setup(
    name=APP_NAME,
    app=APP,
    options={"py2app":OPTIONS},
  setup_requires=["py2app"],
) 
