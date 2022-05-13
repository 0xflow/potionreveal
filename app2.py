import streamlit as st
import pandas as pd


def app():
    st.subheader("Find your potion match!   (Beta version test)")

    src = pd.read_csv("refinedpotionp3.csv")

    elfin = []
    finfin = []

    element1 = st.multiselect('Select an Element', list(set(src['Element'])))
    finish1 = st.multiselect('Select a Finish', list(set(src['Finish'])))
    color1 = st.multiselect('Select a Color', list(set(src['Color'])))
    shape1 = st.multiselect('Select a Shape', list(set(src['Shape'])))
    taste1 = st.multiselect('Select a Taste', list(set(src['Taste'])))
    matter1 = st.multiselect('Select a Matter', list(set(src['Matter'])))
    potency1 = st.multiselect('Select a Potency', list(set(src['Potency'])))
    superpower1 = st.multiselect('Select a Superpower', list(set(src['Superpower'])))
    temperature1 = st.multiselect('Select a Temperature', list(set(src['Temperature'])))
    artist1 = st.multiselect('Select an Artist', list(set(src['Artist'])))
    

    test1 = src.loc[(src['Element'].isin(element1)) & src['Finish'].isin(finish1) & src['Shape'].isin(shape1) & src['Color'].isin(color1) & src['Matter'].isin(matter1) & src['Potency'].isin(potency1) & src['Superpower'].isin(superpower1) & src['Temperature'].isin(temperature1) & src['Taste'].isin(taste1) & src['Artist'].isin(artist1)]
    test2 = src.loc[(src['Element'].isin(element1)) | src['Finish'].isin(finish1) | src['Shape'].isin(shape1) | src['Color'].isin(color1) | src['Matter'].isin(matter1) | src['Potency'].isin(potency1) | src['Superpower'].isin(superpower1) | src['Temperature'].isin(temperature1) | src['Taste'].isin(taste1) | src['Artist'].isin(artist1)]

    test3 = src.loc[((src['Element'].isin(element1)) & src['Finish'].isin(finish1) & src['Shape'].isin(shape1) & src['Color'].isin(color1) & src['Matter'].isin(matter1) & src['Potency'].isin(potency1) & src['Superpower'].isin(superpower1) & src['Temperature'].isin(temperature1) & src['Taste'].isin(taste1) & src['Artist'].isin(artist1)) | 
    ((src['Element'].isin(element1)) & src['Finish'].isin(finish1)) | ((src['Element'].isin(element1)) & src['Color'].isin(color1)) | ((src['Element'].isin(element1)) & src['Shape'].isin(shape1)) | ((src['Element'].isin(element1)) & src['Taste'].isin(taste1)) | ((src['Element'].isin(element1)) & src['Matter'].isin(matter1)) | ((src['Element'].isin(element1)) & src['Potency'].isin(potency1)) | ((src['Element'].isin(element1)) & src['Temperature'].isin(temperature1)) | ((src['Element'].isin(element1)) & src['Superpower'].isin(superpower1)) | ((src['Element'].isin(element1)) & src['Artist'].isin(artist1)) | (src['Element'].isin(element1)) |
    ((src['Finish'].isin(finish1)) & src['Color'].isin(color1)) | ((src['Finish'].isin(finish1)) & src['Shape'].isin(shape1)) | ((src['Finish'].isin(finish1)) & src['Taste'].isin(taste1)) | ((src['Finish'].isin(finish1)) & src['Matter'].isin(matter1)) | ((src['Finish'].isin(finish1)) & src['Potency'].isin(potency1)) | ((src['Finish'].isin(finish1)) & src['Temperature'].isin(temperature1)) | ((src['Finish'].isin(finish1)) & src['Superpower'].isin(superpower1)) | ((src['Finish'].isin(finish1)) & src['Artist'].isin(artist1)) | (src['Finish'].isin(finish1)) |
    ((src['Color'].isin(color1)) & src['Shape'].isin(shape1)) | ((src['Color'].isin(color1)) & src['Taste'].isin(taste1)) | ((src['Color'].isin(color1)) & src['Matter'].isin(matter1)) | ((src['Color'].isin(color1)) & src['Potency'].isin(potency1)) | ((src['Color'].isin(color1)) & src['Temperature'].isin(temperature1)) | ((src['Color'].isin(color1)) & src['Superpower'].isin(superpower1)) | ((src['Color'].isin(color1)) & src['Artist'].isin(artist1)) | (src['Color'].isin(color1)) |
    ((src['Shape'].isin(shape1)) & src['Taste'].isin(taste1)) | ((src['Shape'].isin(shape1)) & src['Matter'].isin(matter1)) | ((src['Shape'].isin(shape1)) & src['Potency'].isin(potency1)) | ((src['Shape'].isin(shape1)) & src['Temperature'].isin(temperature1)) | ((src['Shape'].isin(shape1)) & src['Superpower'].isin(superpower1)) | ((src['Shape'].isin(shape1)) & src['Artist'].isin(artist1)) | (src['Shape'].isin(shape1)) |
    ((src['Taste'].isin(taste1)) & src['Matter'].isin(matter1)) | ((src['Taste'].isin(taste1)) & src['Potency'].isin(potency1)) | ((src['Taste'].isin(taste1)) & src['Temperature'].isin(temperature1)) | ((src['Taste'].isin(taste1)) & src['Superpower'].isin(superpower1)) | ((src['Taste'].isin(taste1)) & src['Artist'].isin(artist1)) | (src['Taste'].isin(taste1)) |
    ((src['Matter'].isin(matter1)) & src['Potency'].isin(potency1)) | ((src['Matter'].isin(matter1)) & src['Temperature'].isin(temperature1)) | ((src['Matter'].isin(matter1)) & src['Superpower'].isin(superpower1)) | ((src['Matter'].isin(matter1)) & src['Artist'].isin(artist1)) | (src['Matter'].isin(matter1)) |
    ((src['Potency'].isin(potency1)) & src['Temperature'].isin(temperature1)) | ((src['Potency'].isin(potency1)) & src['Superpower'].isin(superpower1)) | ((src['Potency'].isin(potency1)) & src['Artist'].isin(artist1)) | (src['Potency'].isin(potency1)) |
    ((src['Temperature'].isin(temperature1)) & src['Superpower'].isin(superpower1)) | ((src['Temperature'].isin(temperature1)) & src['Artist'].isin(artist1)) | (src['Temperature'].isin(temperature1)) | 
    ((src['Superpower'].isin(superpower1)) & src['Artist'].isin(artist1)) | (src['Superpower'].isin(superpower1)) | (src['Artist'].isin(artist1))] 



    finans1 = []
    idxelement = []
    element2 = []
    idxfinish = []
    finish2 = []
    idxcolor = []
    color2 = []
    idxshape = []
    shape2 = []
    idxtaste = []
    taste2 = []
    idxmatter = []
    matter2 = []
    idxpotency = []
    potency2 = []
    idxtemperature = []
    temperature2 = []
    idxsuperpower = []
    superpower2 = []
    idxartist = []
    artist2 = []


    test4 = test3

    for i in range(len(element1)):
    	idx = test4[ (test4['Element'] != element1[i])].index
    	idxelement.append(idx)


    element2 = [x for l in idxelement for x in l]


    for i in range(len(finish1)):
    	idx = test4[ (test4['Finish'] != finish1[i])].index
    	idxfinish.append(idx)


    finish2 = [x for l in idxfinish for x in l]


    for i in range(len(color1)):
    	idx = test4[ (test4['Color'] != color1[i])].index
    	idxcolor.append(idx)


    color2 = [x for l in idxcolor for x in l]	


    for i in range(len(shape1)):
    	idx = test4[ (test4['Shape'] != shape1[i])].index
    	idxshape.append(idx)


    shape2 = [x for l in idxshape for x in l]


    for i in range(len(taste1)):
    	idx = test4[ (test4['Taste'] != taste1[i])].index
    	idxtaste.append(idx)


    taste2 = [x for l in idxtaste for x in l]	


    for i in range(len(matter1)):
    	idx = test4[ (test4['Matter'] != matter1[i])].index
    	idxmatter.append(idx)


    matter2 = [x for l in idxmatter for x in l]


    for i in range(len(potency1)):
    	idx = test4[ (test4['Potency'] != potency1[i])].index
    	idxpotency.append(idx)


    potency2 = [x for l in idxpotency for x in l]	


    for i in range(len(temperature1)):
    	idx = test4[ (test4['Temperature'] != temperature1[i])].index
    	idxtemperature.append(idx)


    temperature2 = [x for l in idxtemperature for x in l]


    for i in range(len(superpower1)):
    	idx = test4[ (test4['Superpower'] != superpower1[i])].index
    	idxsuperpower.append(idx)


    superpower2 = [x for l in idxsuperpower for x in l]


    for i in range(len(artist1)):
    	idx = test4[ (test4['Artist'] != artist1[i])].index
    	idxartist.append(idx)


    artist2 = [x for l in idxartist for x in l]


    index_list1 = [element2, finish2, color2, shape2, taste2, matter2, potency2, temperature2, superpower2, artist2]
    index_list = element2 + finish2 + color2 + shape2 + taste2 + matter2 + potency2 + temperature2 + superpower2 + artist2






    finans2 = []
    idxelement3 = []
    element3 = []
    idxfinish3 = []
    finish3 = []
    idxcolor3 = []
    color3 = []
    idxshape3 = []
    shape3 = []
    idxtaste3 = []
    taste3 = []
    idxmatter3 = []
    matter3 = []
    idxpotency3 = []
    potency3 = []
    idxtemperature3 = []
    temperature3 = []
    idxsuperpower3 = []
    superpower3 = []
    idxartist3 = []
    artist3 = []


    for i in range(len(element1)):
    	idx = test4[ (test4['Element'] == element1[i])].index
    	idxelement3.append(idx)


    element3 = [x for l in idxelement3 for x in l]


    for i in range(len(finish1)):
    	idx = test4[ (test4['Finish'] == finish1[i])].index
    	idxfinish3.append(idx)


    finish3 = [x for l in idxfinish3 for x in l]


    for i in range(len(color1)):
    	idx = test4[ (test4['Color'] == color1[i])].index
    	idxcolor3.append(idx)


    color3 = [x for l in idxcolor3 for x in l]	


    for i in range(len(shape1)):
    	idx = test4[ (test4['Shape'] == shape1[i])].index
    	idxshape3.append(idx)


    shape3 = [x for l in idxshape3 for x in l]


    for i in range(len(taste1)):
    	idx = test4[ (test4['Taste'] == taste1[i])].index
    	idxtaste3.append(idx)


    taste3 = [x for l in idxtaste3 for x in l]	


    for i in range(len(matter1)):
    	idx = test4[ (test4['Matter'] == matter1[i])].index
    	idxmatter3.append(idx)


    matter3 = [x for l in idxmatter3 for x in l]


    for i in range(len(potency1)):
    	idx = test4[ (test4['Potency'] == potency1[i])].index
    	idxpotency3.append(idx)


    potency3 = [x for l in idxpotency3 for x in l]	


    for i in range(len(temperature1)):
    	idx = test4[ (test4['Temperature'] == temperature1[i])].index
    	idxtemperature3.append(idx)


    temperature3 = [x for l in idxtemperature3 for x in l]


    for i in range(len(superpower1)):
    	idx = test4[ (test4['Superpower'] == superpower1[i])].index
    	idxsuperpower3.append(idx)


    superpower3 = [x for l in idxsuperpower3 for x in l]


    for i in range(len(artist1)):
    	idx = test4[ (test4['Artist'] == artist1[i])].index
    	idxartist3.append(idx)


    artist3 = [x for l in idxartist3 for x in l]


    index_list3 = [element3, finish3, color3, shape3, taste3, matter3, potency3, temperature3, superpower3, artist3]
    index_list2 = element3 + finish3 + color3 + shape3 + taste3 + matter3 + potency3 + temperature3 + superpower3 + artist3


    el4 = [x for x in element2 if x not in element3]
    fi4 = [x for x in finish2 if x not in finish3]
    co4 = [x for x in color2 if x not in color3]
    sh4 = [x for x in shape2 if x not in shape3]
    ta4 = [x for x in taste2 if x not in taste3]
    ma4 = [x for x in matter2 if x not in matter3]
    po4 = [x for x in potency2 if x not in potency3]
    te4 = [x for x in temperature2 if x not in temperature3]
    su4 = [x for x in superpower2 if x not in superpower3]
    ar4 = [x for x in artist2 if x not in artist3]

    idx4 = el4 + fi4 + co4 + sh4 + ta4 + ma4  + po4 + te4 + su4 + ar4



    index_list4 = [x for x in index_list if x not in index_list2]









    #res = list(set.intersection(*map(set, index_list)))

    test5 = test4.drop(idx4)
    test5 = test5.drop(['tokenid', 'ipfsnew'], axis=1)




																				



    #test4 = test3.loc[test3['Element'].isin(element1) & test3['Finish'].isin(finish1) & test3['Shape'].isin(shape1) & test3['Matter'].isin(matter1) & test3['Taste'].isin(taste1) & test3['Potency'].isin(potency1) & test3['Temperature'].isin(temperature1) & test3['Superpower'].isin(superpower1) & test3['Artist'].isin(artist1) & test3['Color'].isin(color1)]



    #st.write('Potions having all selected traits:', test1)
    #st.write('Potions having either of the selected traits:', test2)
    #st.write(color2)
    #st.write(test4)
    st.write(test5)
    #st.write(idx4)

