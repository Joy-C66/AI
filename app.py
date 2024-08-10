import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
plt.rc("font", family = "Microsoft JhengHei")

st.set_page_config(
    page_title='台灣信用卡分析資料',
    page_icon = 'random',
    layout='centered')

st.title('台灣信用卡資料分析')
st.markdown('''
     :rainbow[信用卡資料分析]''')
# st.markdown(" &mdash;\
#             #:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")  

st.button("Reset",type="primary")
if (st.button("參考資料")):
    # st.write("聯合信用卡處理中心"),
    st.link_button("聯合信用卡處理中心,GO", "https://www.nccc.com.tw/wps/wcm/connect/zh/home/KnowledgeSharing/CardQA?category=qrytyp1")



st.divider()


Female= pd.read_csv('C:\\Users\\user\\Downloads\\Female_csv.csv',encoding='Big5')
fig4 = plt.figure(figsize=(6,9))    
labels = Female["產業別"]     
size = Female["信用卡交易金額[新台幣]"]      
plt.pie(size,                          
        labels = labels,                
        autopct = "%1.1f%%",            
        pctdistance = 0.6,             
        textprops = {"fontsize" : 14},
        wedgeprops={'linewidth':3,'edgecolor':'w','width':1},
        colors={'mediumseagreen','darkkhaki','darkorange','indianred','royalblue','c',
        'mediumorchid'},
        radius=1.5
        ) 
plt.title("女性不同產業別信用卡消費金額", {"fontsize" : 22})
plt.axis('equal')   
plt.legend(loc = "best")


Male= pd.read_csv('C:\\Users\\user\\Downloads\\Male_csv.csv',encoding='Big5')
fig5 = plt.figure(figsize=(6,9))    
labels = Male["產業別"]     
size = Male["信用卡交易金額[新台幣]"]      
plt.pie(size,                          
        labels = labels,                
        autopct = "%1.1f%%",            
        pctdistance = 0.6,             
        textprops = {"fontsize" : 14},
        wedgeprops={'linewidth':3,'edgecolor':'w','width':1},
        colors={'mediumseagreen','darkkhaki','darkorange','indianred','royalblue','c',
        'mediumorchid'},
        radius=1.5
        ) 
plt.title("男性不同產業別信用卡消費金額", {"fontsize" : 22})
plt.axis('equal')   
plt.legend(loc = "best")


# col1, col2 = st.columns(2)

# with col1:
#    st.pyplot(fig4)

# with col2:
#    st.pyplot(fig5)


ages_total = pd.read_csv('C:\\Users\\user\\Downloads\\ages_total_csv.csv', encoding='Big5')
ages_total = ages_total.groupby(['年齡層'], sort=True)['信用卡交易金額[新台幣]'].sum().reset_index()
ages_total.sort_values(by='年齡層')
fig6 = plt.figure() 
plt.scatter(ages_total['年齡層'],ages_total['信用卡交易金額[新台幣]'],color='royalblue')
plt.ylabel('消費總金額[TWD]',fontsize=10)
plt.xlabel('年齡層', fontsize=10)
plt.title('年齡層區間分散圖',fontsize=16)
plt.xticks(rotation=25,fontsize=8)
ax = plt.subplot()
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# st.pyplot(fig6)


pro= pd.read_csv('C:\\Users\\user\\Downloads\\pro_total_csv.csv',encoding='Big5')
fig1 = plt.figure() 
ax  = fig1.add_subplot(1,1,1)
ax.bar(pro['職業類別'], pro['信用卡交易金額[新台幣]'], color='steelBlue')
ax.set_xlabel("職業類別",fontsize=10)
ax.set_ylabel("信用卡交易金額[TWD]",fontsize=10)
ax.set_title('不同職業類別消費金額',fontsize=16)
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.xticks(rotation=25,fontsize=10)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# st.pyplot(fig1)

edu_total = pd.read_csv('C:\\Users\\user\\Downloads\\edu_total_csv.csv', encoding='Big5')
fig2 = plt.figure() 
ax  = fig2.add_subplot(1,1,1)
ax.bar(edu_total['教育程度類別'], edu_total['信用卡交易金額[新台幣]'], color='lightskyBlue')
ax.set_xlabel("教育程度類別",fontsize=10)
ax.set_ylabel("信用卡交易金額[TWD]",fontsize=10)
ax.set_title('不同教育程度消費金額',fontsize=16)
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# st.pyplot(fig2)


income_total= pd.read_csv('C:\\Users\\user\\Downloads\\income_total_csv.csv',encoding='Big5')
fig3 = plt.figure() 
plt.bar(income_total['年收入'],income_total['信用卡交易金額[新台幣]'],color='skyBlue')
plt.ylabel('信用卡交易金額[TWD]',fontsize=10)
plt.xlabel('年收入[TWD]', fontsize=10)
plt.title('年收入區間分布圖',fontsize=16)
plt.xticks(rotation=25)
ax = plt.subplot()
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# st.pyplot(fig3)


tab1, tab2, tab3, tab4, tab5 = st.tabs(["性別","年齡層", "職業", "教育程度","年收入"])

# with tab1:
#    st.header("性別")
#    st.pyplot(fig4)

with tab1:
    st.header("🔆性別")
    col1, col2 = st.columns(2)
    st.markdown("""<center> 🐾男性與女性在不同產業別消費情況不同,在食.衣.住.行消費分布比例不同🐾</center>""", unsafe_allow_html=True)
    # st.markdown(  "🐾男性與女性在不同產業別消費情況不同,在食.衣.住.行消費分布比例不同🐾" )
    
with col1:
    st.pyplot(fig4)

with col2:
    st.pyplot(fig5)


    
with tab2:
    st.header("🔆年齡層")
    st.pyplot(fig6)
    st.markdown("""<center> 🐾不同年齡層信用卡消費金額分布,隨著年齡增加,消費金額也增加,到40-45歲區間的消費者有最高的消費金額,其後則遞減🐾</center>""", unsafe_allow_html=True)
    
    # st.markdown("🐾不同年齡層信用卡消費金額分布,隨著年齡增加,消費金額也增加,到40-45歲區間的消費者有最高的消費金額,其後則遞減🐾")

with tab3:
    st.header("🔆職業")
    st.pyplot(fig1)
    st.markdown("""<center> 🐾不同職業別信用卡消費金額以工商服務類最高,軍警最低🐾</center>""", unsafe_allow_html=True)
    # st.markdown("🐾不同職業別信用卡消費金額以工商服務類最高,軍警最低🐾")

with tab4:
    st.header("🔆教育程度")
    st.pyplot(fig2)
    st.markdown("""<<center> 🐾教育程度在大學畢業的消費者使用信用卡消費的金額最高,博士畢業最低🐾</center>""",unsafe_allow_html=True)

with tab5:
    st.header("🔆年收入")
    st.pyplot(fig3)
    st.markdown("""<center> 🐾年收入區間最低為未滿50萬的消費者使用信用卡消費金額反而最高🐾</center>""", unsafe_allow_html=True)
    # st.markdown("🐾年收入區間最低為未滿50萬的消費者使用信用卡消費金額反而最高🐾")
    
st.divider()



