import re

import pandas as pd

if __name__ == "__main__":

    data = pd.read_csv("Named Entity.csv")
    entityTag = data["NE Code"].tolist()

    df = pd.read_csv("all_data/all_entity_dataset.csv")
    entitySentences = df["Question"].tolist()

    myDict = {}
    reee = len([1 for x in entityTag])
    print(reee)
    for x in entityTag:
        count = 0
        for j in entitySentences:
            sentence = j.split()
            for c in range(len(sentence)):
                # Matches /B-Word until space
                if re.search(r"/B-{}\w*".format(x), sentence[c]):
                    count += 1
                    split = sentence[c].rsplit("/", maxsplit=1)[1]
                    myDict.update({split : count})

    print(myDict)
