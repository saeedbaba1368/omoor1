def load_data_for_year(year):
    import streamlit as st
    import pandas as pd
    month_names = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    tabs = st.tabs(month_names)
    
    for i, tab in enumerate(tabs, start=1):
        with tab:
            try:
                
                df = pd.read_excel(f"data/{year}/{i}.xls", index_col=0, usecols=range(1, 20))
                if df is not None:
                    df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)
                    st.dataframe(df)
            except Exception as e:
                st.write("بزودی منتشر می گردد")