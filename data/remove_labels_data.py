
# import pandas as pd

# # 3 -> no quoting
# movies_data = pd.read_csv("data/movies.txt", delimiter=",", quoting=0)

# # recode rationales so that sentences are (1) or are not (-1)
# # rationales; polarity is implicit
# sent_lbls = movies_data["sentence_lbl"]
# # in the original dataset: positive rationale is 2, the negative 
# #  rationale is 0, and the neutral one is 1. 
# sent_lbls_recoded = sent_lbls.replace(1, -1) 
# # sent_lbls_recoded = sent_lbls_recoded.replace([1,-1], 1) 
# movies_data["sentence_lbl"] = sent_lbls_recoded

# movies_data.to_csv("data/movies.txt", index=False)
    
with open('data/movies_labelled.txt') as infile, open('data/movies_unlabelled.txt', 'w') as outfile:
    for line in infile:
        words = line.rsplit(',', 1)
        # if len(words) > 1:
        #     words[1] = '-1'
        if len(words) > 1:
            outfile.write(words[0] + ",-1\n")
        else:
            outfile.write(words[0] + "\n")
