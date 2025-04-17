import streamlit as st
import pandas as pd

st.title("📊 Excel Data Analyzer")
st.write("آپلود فایل اکسل و دیدن داده‌ها")

uploaded_file = st.file_uploader("یک فایل Excel انتخاب کن", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.subheader("📋 پیش‌نمایش داده‌ها:")
    st.dataframe(df)

    st.subheader("📈 اطلاعات آماری کلی:")
    st.write(df.describe())

    st.subheader("🔍 انتخاب ستون برای تحلیل:")
    column = st.selectbox("ستونی که می‌خوای تحلیل کنی رو انتخاب کن:", df.columns)

    if pd.api.types.is_numeric_dtype(df[column]):
        st.line_chart(df[column])
    else:
        st.bar_chart(df[column].value_counts())
else:
    st.warning("لطفاً یک فایل Excel آپلود کن.")
