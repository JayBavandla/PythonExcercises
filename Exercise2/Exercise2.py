import json


def removeJsonElement(givenElement):

    with open('test_payload.json') as inputfile:
        inputdata = json.load(inputfile)
        print(inputdata.items())

        for key, value in inputdata.items():
            print(key, value)

            if (givenElement == key) :
                inputdata.pop(key, 'None')
                break
            else :
                #print(value)
                value_str = str(value).replace("'", "\"")
                try:
                    json2 = json.loads(value_str)
                    #print(json2.items())

                    for keyInner, valueInner in json2.items():
                        #print(keyInner, valueInner)
                        if (givenElement == keyInner):
                            inputdata[key].pop(keyInner, 'None')
                            break

                except:
                    print("String could not be converted to JSON")

        # Save the updated file into new_payload.json file.
        with open('new_payload.json', 'w') as outfile:
            json.dump(inputdata, outfile)



#Method calling with two INT values.
removeJsonElement('outParams');
