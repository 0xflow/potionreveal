import streamlit as st
import pandas as pd

def space(num_lines=1):
		for _ in range(num_lines):
			st.write("")

def app():


	
    #st.set_page_config(layout="wide", page_icon="^_^", page_title="Potion Rarity and Ranking")
    st.title("Check Potion Rarity and Ranking")
    st.subheader("Unofficial Webapp*")


    src = pd.read_csv("refinedpotionp3.csv")
    potion_num = src['Potion Number']
    potionnum = st.number_input("Select Potion Number", min_value=1, max_value=3000, value=1, step=1)


    space(1)

    st.write("Current Selection:", potionnum)

    indexval1 = src.index[src['Potion Number'] == potionnum].tolist()
    indexval = indexval1[0]

    url = "https://rarible.com/token/flow/A.667a16294a089ef8.SomePlaceCollectible:"+str(src['tokenid'][indexval])+"?tab=details"
    #st.write('Rarible [link](%s)' % url)
    if st.button(f'Get Rarible link for Potion #{potionnum}'):
    	st.write('[Rarible link](%s)' % url)

    space(2)

    


    st.markdown("----------------------")


    col0, col1, col2 = st.columns(3)

    col0.metric("Ranking", src['Ranking'][indexval])
    col1.metric("Artist", src['Artist'][indexval], src['Artist Rarity'][indexval])
    col2.metric("Element", src['Element'][indexval], src['Element Rarity'][indexval])


    space(2)
    st.markdown("----------------------")


    col3, col4, col5 = st.columns(3)

    col3.metric("Finish", src['Finish'][indexval], src['Finish Rarity'][indexval])
    col4.metric("Color", src['Color'][indexval], src['Color Rarity'][indexval])
    col5.metric("Shape", src['Shape'][indexval], src['Shape Rarity'][indexval])


    space(2)
    st.markdown("----------------------")


    col6, col7, col8 = st.columns(3)

    col6.metric("Taste", src['Taste'][indexval], src['Taste Rarity'][indexval])
    col7.metric("Matter", src['Matter'][indexval], src['Matter Rarity'][indexval])
    col8.metric("Potency", src['Potency'][indexval], src['Potency Rarity'][indexval])


    space(2)
    st.markdown("----------------------")


    col9, col10, col11 = st.columns(3)

    col9.metric("Temperature", src['Temperature'][indexval], src['Temperature Rarity'][indexval])
    col10.metric("Superpower", src['Superpower'][indexval], src['Superpower Rarity'][indexval])

    st.markdown("----------------------")
