import streamlit as st
from create_styled_sidebar import create_styled_sidebar
from load_data_for_year import load_data_for_year
import pandas as pd 
from stc_html import stc_html
a=create_styled_sidebar()
def main():
# Main content of the app
    
    if a==1:
        df = pd.read_csv("data/p_havaee.csv")
        st.dataframe(df)
    elif a==2:
        df = pd.read_csv("data/p_zamini.csv")
        st.dataframe(df)
    elif a==1401 or a==1402:
        
        load_data_for_year(a)
    else:
        stc_html()
        st.title('امور یک رشت')
        dfmap=pd.read_csv("data/sample_map.csv")
        st.map(dfmap,zoom=15)
        
if __name__=="__main__" :
    main()