import os

fileContent = {}
fileList = []
def read():
    for i in os.listdir('./blast_easy_swiss_input'):
        if i.endswith('.fasta'):
            spt=i.split(".")
            fileList.append(spt[0])

    for filename in fileList:
        with open('./blast_easy_swiss_input/'+filename+".fasta", "r") as file:
            fileContent[filename] = file.read()

    # for filename, text in fileContent.items():
        # print(filename)
        # print("=" * 80)
        # print(text)

def get_data():
    return fileContent

def get_titles():
    return fileList
