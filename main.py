import Reader as reader
import Clicker as clicker
import Crawler as crawler

reader.read()
doneNames=crawler.getDoneNames()
fileData = reader.get_data()
fileNames = reader.get_titles()
fileNames.sort()
clicker.listen()
for name in fileNames:
    if name not in doneNames:
        data=fileData[name]
        clicker.selectMenu()
        clicker.singleData(data)
        clicker.singleTitle(name)
        clicker.clickBuild()
        clicker.clickBack()