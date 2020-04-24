import json
import xmltodict
 
def convertToJSON(xml_file, xml_attribs=True):
    jsonFileName = xml_file.split(".")[0] + ".json"
    jsonFile = open(jsonFileName, "w")
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, force_list = {"children": True})
        writeOut = json.dumps(d, indent=0)
        jsonFile.write(writeOut)
        jsonFile.close()

    f = open(jsonFileName)
    lines = f.readlines()
    f.close()
    
    lineLength = len(lines)       

    f = open(jsonFileName, "w")
    counter = 1
    for line in lines:
        if counter == 2 or counter == lineLength - 1:
            pass
        else:
            f.write((line).replace("\n",""))


        counter += 1
