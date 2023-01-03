import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st. set_page_config(layout="wide")

def line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy):
    fig=px.line(data, x, y,log_y=logy)

    fig.update_layout(title=tit,title_font_size=16,#title_xanchor="center",#title_pad_l=30,
                      xaxis_title= xtit, xaxis_title_font_size=16,
                      yaxis_title= ytit, yaxis_title_font_size=16,
                      width=w, height= h, plot_bgcolor="white",
                      showlegend= False, legend_bordercolor="#080808",legend_borderwidth=0.5,
                      legend_font_size=12,legend_title_font_size=14,legend_title_text="",
                      
                      )
    
    a.plotly_chart(fig)
    return

def scatter_plot(data,x,y,a,tit,xtit,ytit,w,h,logy):
    fig=px.scatter(data, x, y, log_y = logy)

    fig.update_layout(title=tit,title_font_size=16,#title_xanchor="center",#title_pad_l=30,
                      xaxis_title= xtit, xaxis_title_font_size=16,
                      yaxis_title= ytit, yaxis_title_font_size=16,
                      width=w, height= h, plot_bgcolor="white",
                      showlegend= False, legend_bordercolor="#080808",legend_borderwidth=0.5,
                      legend_font_size=12,legend_title_font_size=14,legend_title_text="",
                      
                      )
    
    a.plotly_chart(fig)
    return

def bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode):
    fig=px.bar(data, x, y,color, log_y=logy, barmode=barmode)
    
    fig.update_layout(title=tit,title_font_size=16,#title_xanchor="center",#title_pad_l=30,
                      xaxis_title= xtit, xaxis_title_font_size=16,
                      yaxis_title= ytit, yaxis_title_font_size=16,
                      width=w, height= h, plot_bgcolor="white",
                      showlegend= True,
                      legend_font_size=12,legend_title_font_size=14,legend_title_text="",
                      
                      )
    a.plotly_chart(fig)
    return

def pie_plot(transaction_data,values,names):#,a,tit,txtpo,txtinf,hole=0.5):
    fig=px.pie(transaction_data, values, names,title='Distribution of wallets by transactions')#, title=tit)
    
    # fig.update_traces(textposition= txtpo,
    #                   textinfo= txtinf)
                   
    st.plotly_chart(fig)
    return

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()
interactive=st.container()

st.sidebar.image("data:image/jpeg;base64,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", width=250)
st.sidebar.header("Terra Megadashboard")
introduction = st.sidebar.button('Introduction')
transactions = st.sidebar.button('Transactions')
wallets = st.sidebar.button('Wallets')
development = st.sidebar.button('Development')
supply = st.sidebar.button('Supply')
about = st.sidebar.button('About')

primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="serif"

if introduction:
    st.title('Introduction')

    i1 = st.container()
    i2 = st.container()

    col1, col2 = st.columns(2)
    
    st.info('##### Please select the wide mode from the settings to have a better appearance of the charts in this dashboard.')

    with i1:
         st.write("""
    ##### This Megadashboard offers a holistic view of the Terra ecosystem, including activity, supply, staking, and development using the following metrics:
    """)
   
   
    with i2:
        col1.write("""
    ##### Transactions
     * ###### Average Transaction Fee per transaction per week
     * ###### Total Transaction Fees per week
     * ###### Total number of transactions per week
     * ###### Average TPS per week
     * ###### Avg block time per week
     ##### Wallets
     * ###### Total number of new wallets per week
     * ###### Total number of active wallets per week
     * ###### Cumulative number of wallets over time
     """)
   
        col2.write("""
     ##### Development
     * ###### New contracts deployed each week
     * ###### Total contracts deployed each week
     ##### Supply
     * ###### Total Supply
     * ###### Circulating Supply
     * ###### Vesting Schedule
     * ###### # and % LUNA IBC-ed out
     * ###### Richlist (Top 100)
     * ###### # of LUNA staked
     * ###### % of LUNA staked
     * ###### Staking rewards distributed in USD trend 
    """)
     
    st.info('##### This dashboard updates daily')

 
if transactions:
    t1 = st.container()
    t2 = st.container()
    t3 = st.container()
    t4 = st.container()
    t5 = st.container()
    t6 = st.container()
    
    
    #col1.header("header col1")
    
    with t1:
        st.title('Transactions')
        st.write('Statistics')
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/13c2231f-6e5c-48af-a8e4-e8a2ae37fda0/data/latest"
        total_data= pd.read_json(total_url)
        st.write(total_data)
    
    with t2:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/266cc6f0-59ce-4226-9a0f-61a3df72183a/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig=px.line(transaction_data, x='DATE', y=['TXS','CUMULATIVE_TXS'])#, labels={'x':'Date','y':'Transactions'})
        
        data= transaction_data; x='DATE'; y=['TXS','CUMULATIVE_TXS']; a=col1; tit= 'Weekly Number of LUNA Transactions'
        xtit='Date'; ytit = 'Transactions' ; w=600; h=450 ; logy = False 
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
   
        data= transaction_data; x='DATE'; y=['LUNA_VOLUME','CUMULATIVE_VOLUME']; 
        a=col2; tit= 'Weekly Volume of LUNA Transactions'; xtit='Date'; ytit = 'Volume' ; w=600; h=450 ; logy = False       
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        # fig2=px.line(transaction_data, x='DATE', y=['LUNA_VOLUME','CUMULATIVE_VOLUME'])#, labels={'x':'Date','y':'Transactions'})
        # fig2.update_layout(title='Weekly Users', xaxis_title='Date',yaxis_title='Volume')
        # st.plotly_chart(fig2)
       
        # fig.update_layout(title='Weekly Transactions', xaxis_title='Date',yaxis_title='Transactions')
        # #col1.write('simple graph')
        # st.plotly_chart(fig)
    
    with t4:
        data= transaction_data; x='DATE'; y=['FEES','TPS']; a=st; 
        tit= 'Weekly Luna Fees'; xtit='Date'; ytit = 'FEES & TPS' ; w=700; h=450 ; logy = True 

        fig=scatter_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        # fig3=px.scatter(transaction_data, x='DATE', y=['FEES','TPS'])
        # fig3.update_layout(title='Weekly Luna Fees', xaxis_title='Date',yaxis_title='FEES & TPS')
        # st.plotly_chart(fig3)

    with t5:
        st.write('Block Data')
        block_url="https://node-api.flipsidecrypto.com/api/v2/queries/b80b5a8b-935b-46af-9b1d-c9c53c3b8e58/data/latest"
        block_data= pd.read_json(block_url)
        st.write(block_data)
    
    with t6:
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/26ca6058-eea3-4bc1-beb0-1f291c10a016/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='DATE'; y=['Average Time Between Blocks','Median Time Between Blocks','Average Transactions Per Block','Median Transactions Per Block']; 
        a=st; tit= 'Blocks';xtit='Date'; ytit = 'Time Between Blocks' ; w=700; h=450 ; logy = False       
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        # fig5=px.line(time_data, x='DATE', y=['Average Time Between Blocks','Median Time Between Blocks','Average Transactions Per Block','Median Transactions Per Block'])
        # fig5.update_layout(title='Blocks', xaxis_title='Date',yaxis_title='Time Between Blocks')
        # st.plotly_chart(fig5)
    

    

    # fig6=px.line(time_data, x='DATE', y=['Average Transactions Per Block','Median Time Between Blocks'])
    # fig6.update_layout(title='Blocks', xaxis_title='Date',yaxis_title='Time Between Blocks')
    # st.plotly_chart(fig6)


   


if wallets:
    st.title('Wallets')

    w1 = st.container()
    w2 = st.container()
    w3 = st.container()
    w4 = st.container()
    
    with w1:
        st.write('Statistics')
        average_url="https://node-api.flipsidecrypto.com/api/v2/queries/6264a0f5-5e25-4cc6-9b19-9076dcc5040f/data/latest"
        average_data= pd.read_json(average_url)
        st.write(average_data)
    
    with w2:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/266cc6f0-59ce-4226-9a0f-61a3df72183a/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y=['SENDERS','CUMULATIVE_USERS']; 
        a=col1; tit= 'Weekly Users'; xtit='Date'; ytit = 'Users' ; w=700; h=450 ; logy = False       
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        # fig1=px.line(transaction_data, x='DATE', y=['SENDERS','CUMULATIVE_USERS'])#, labels={'x':'Date','y':'Transactions'})
        # fig1.update_layout(title='Weekly Users', xaxis_title='Date',yaxis_title='Users')
        # st.plotly_chart(fig1)
        
        users_url="https://node-api.flipsidecrypto.com/api/v2/queries/49bae95f-ce8d-401a-8f3a-d3081e9b4c81/data/latest"
        users_data= pd.read_json(users_url)
        data= users_data; x='MINDATE'; y=['NEW_USERS','TOTAL_USERS']; 
        a=col2; tit= 'Weekly New Users'; xtit='Date'; ytit = 'New Users' ; w=700; h=450 ; logy = False       
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        # fig4=px.line(users_data, x='MINDATE', y=['NEW_USERS','TOTAL_USERS'])
        # fig4.update_layout(title='Weekly New Users', xaxis_title='Date',yaxis_title='New Users')
        # st.plotly_chart(fig4)
   
    with w3:
        col1, col2 = st.columns(2)
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/6c01d601-9f5d-42b5-809a-777635bf0751/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='USERS'; y='TXS'; 
        a=col1; tit= 'Top 10 Users by Transactions'; xtit='Users'; ytit = 'Transactions' ; w=700; h=450 ; logy = False  ; color=None ;barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        # fig6=px.bar(time_data, x='USERS', y='TXS')
        # fig6.update_layout(title='Top 10 Users by Transactions', xaxis_title='Users',yaxis_title='Transactions')
        # st.plotly_chart(fig6)
   
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/b6960eef-5f52-4ecd-b5c2-22d01b9028c7/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='USERS'; y='FEES'; 
        a=col2; tit= 'Top 10 Users by Paid Fees'; xtit='Users'; ytit = 'FEES' ; w=700; h=450 ; logy = False; color=None ;barmode='relative'  
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        # fig7=px.bar(time_data, x='USERS', y='FEES')
        # fig7.update_layout(title='Top 10 Users by Paid Fees', xaxis_title='Users',yaxis_title='FEES')
        # st.plotly_chart(fig7)
   
    with w4:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/d09f8673-ff5e-481c-b4f1-c4da8319a0c1/data/latest"
        transaction_data= pd.read_json(transaction_url)
        
        # data= transaction_data; values='USER';  names='TYPE'; #color=None
        # a=st; tit= 'Distribution of wallets by transactions'; txtpo='inside'; txtinf='percent+label' ; w=700; h=450      
        # pie_plot(transaction_data,values,names)#,a,tit,txtpo,txtinf,hole=0.5)
        
        fig8=px.pie(transaction_data, values='USER', names='TYPE' , title='Distribution of wallets by transactions')
        fig8.update_traces(textposition='inside', textinfo='percent+label')
        col1.plotly_chart(fig8)
    
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/1cc93643-819d-48be-93a4-cdc9b21c0e5c/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig8=px.pie(transaction_data, values='USER', names='TYPE' , title='Distribution of wallets by fees' , hole=0.25)
        fig8.update_traces(textposition='inside', textinfo='percent+label')
        col2.plotly_chart(fig8)


   

if development:
    st.title('Development')

    d1 = st.container()
    d2 = st.container()
    d3 = st.container()
    d4 = st.container()
    d5 = st.container()
    d6 = st.container()
    d7 = st.container()
    d8 = st.container()
    d9 = st.container()
    d10 = st.container()
    d11 = st.container()

    
    with d1:    
        st.write('Statistics')
        average_url="https://node-api.flipsidecrypto.com/api/v2/queries/ab1bd0cf-792c-4807-b3cb-12393e5ee7a9/data/latest"
        average_data= pd.read_json(average_url)
        st.write(average_data)
    
    with d2:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/b8161b28-c258-4b79-8e8d-120a39cb2003/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y=['new contracts','Cum Contracts']; 
        a=col1; tit= 'Weekly Deployed New Contracts'; xtit='Date'; ytit = 'Contracts' ; w=700; h=450 ; logy = False       
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        # fig1=px.line(transaction_data, x='DATE', y=['new contracts','Cum Contracts'])#, labels={'x':'Date','y':'Transactions'})
        # fig1.update_layout(title='Weekly Deployed New Contracts', xaxis_title='Date',yaxis_title='Contracts')
        # st.plotly_chart(fig1)
    
        transfer_url="https://node-api.flipsidecrypto.com/api/v2/queries/69e6c13b-64e8-4ff6-8445-d28c7e58e47b/data/latest"
        transfer_data= pd.read_json(transfer_url)
        data= transfer_data; x='DATE'; y='TXS';color="PROJECT_NAME" ;barmode='relative'
        a=col2; tit= 'Weekly Top 10 Most Interacted Contracts by Name'; xtit='Date'; ytit = 'Transactions' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        # fig2=px.bar(transfer_data, x='DATE', y='TXS',color="PROJECT_NAME")
        # fig2.update_layout(title='Weekly Top 10 Most Interacted Contracts by Name', xaxis_title='Date',yaxis_title='Transactions')
        # st.plotly_chart(fig2)
    
    with d3:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/d4bc6ea6-ee05-4b47-bbde-3ce7a003e3c5/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig3=px.pie(transaction_data, values='TXS', names='PROJECT_NAME' , title='Top 10 Most Interacted Contracts by Name')
        fig3.update_traces(textposition='inside', textinfo='percent+label')
        col1.plotly_chart(fig3)
     
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/1edb966f-0932-4201-99da-c1b10758c205/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig4=px.pie(transaction_data, values='TOTAL_TXS', names='TYPE' , title='Distribution of Contracts by Number of Transactions')
        fig4.update_traces(textposition='inside', textinfo='percent+label')
        col2.plotly_chart(fig4)
    
    with d4:
        col1, col2 = st.columns(2)
        transfer_url="https://node-api.flipsidecrypto.com/api/v2/queries/14458aec-c222-4a0c-84cd-4883b658923f/data/latest"
        transfer_data= pd.read_json(transfer_url)
        data= transfer_data; x='DATE'; y='TXS';color="STABLECOIN" ;barmode='relative'
        a=col1; tit= 'Weekly Stablecoins Transfers by Transactions'; xtit='Date'; ytit = 'Transactions' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        # fig5=px.bar(transfer_data, x='DATE', y='TXS',color="STABLECOIN")
        # fig5.update_layout(title='Weekly Stablecoins Transfers by Transactions', xaxis_title='Date',yaxis_title='Transcations')
        # st.plotly_chart(fig5)
    
        transfer_url="https://node-api.flipsidecrypto.com/api/v2/queries/14458aec-c222-4a0c-84cd-4883b658923f/data/latest"
        transfer_data= pd.read_json(transfer_url)
        data= transfer_data; x='DATE'; y='USERS';color="STABLECOIN" ;barmode='relative'
        a=col2; tit= 'Weekly Stablecoins Transfers by Users'; xtit='Date'; ytit = 'Users' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        # fig6=px.bar(transfer_data, x='DATE', y='USERS',color="STABLECOIN")
        # fig6.update_layout(title='Weekly Stablecoins Transfers by Users', xaxis_title='Date',yaxis_title='Users')
        # st.plotly_chart(fig6)
    
    with d5:
        col1, col2 = st.columns(2)
        transfer_url="https://node-api.flipsidecrypto.com/api/v2/queries/14458aec-c222-4a0c-84cd-4883b658923f/data/latest"
        transfer_data= pd.read_json(transfer_url)
        data= transfer_data; x='DATE'; y='VOLUME';color="STABLECOIN" ;barmode='relative'
        a=col1; tit= 'Weekly Stablecoins Transfers by Volume'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        # fig7=px.bar(transfer_data, x='DATE', y='VOLUME',color="STABLECOIN")
        # fig7.update_layout(title='Weekly Stablecoins Transfers by Volume', xaxis_title='Date',yaxis_title='Volume')
        # st.plotly_chart(fig7)

    with d6:
        col1, col2 = st.columns(2)
        transfer_url="https://node-api.flipsidecrypto.com/api/v2/queries/9945e1b3-5f6f-47c9-bb63-e7652eb0dde2/data/latest"
        transfer_data= pd.read_json(transfer_url)
        data= transfer_data; x='STABLECOIN'; y=['TOTAL_TXS','TOTAL_USERS','TOTAL_VOLUME'];color=None; barmode='group'
        a=col1; tit= 'Total Stablecoins Transfer out Activities'; xtit='Stablecoins'; ytit = 'Statistics' ; w=700; h=450 ; logy = True       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        # fig7=px.bar(transfer_data, x='STABLECOIN', y=['TOTAL_TXS','TOTAL_USERS','TOTAL_VOLUME'],log_y=True)
        # fig7.update_layout(title='Total Stablecoins Transfer out Activities', xaxis_title='Stablecoins',yaxis_title='Statistics',barmode='group')
        # st.plotly_chart(fig7)
    
        transfer_url="https://node-api.flipsidecrypto.com/api/v2/queries/9945e1b3-5f6f-47c9-bb63-e7652eb0dde2/data/latest"
        transfer_data= pd.read_json(transfer_url)
        data= transfer_data; x='STABLECOIN'; y=['AVG_TXS','AVG_USERS','AVG_VOLUME'];color=None; barmode='group'
        a=col2; tit= 'Average Stablecoins Transfer out Activities'; xtit='Stablecoins'; ytit = 'Statistics' ; w=700; h=450 ; logy = True       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        # fig8=px.bar(transfer_data, x='STABLECOIN', y=['AVG_TXS','AVG_USERS','AVG_VOLUME'],log_y=True)
        # fig8.update_layout(title='Average Stablecoins Transfer out Activities', xaxis_title='Stablecoins',yaxis_title='Statistics',barmode='group')
        # st.plotly_chart(fig8)
    
    with d7:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/13e291b1-0a9f-4ac0-9987-c39cb96a10c4/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATES'; y='NET_VOLUME'; color=None; barmode='relative'
        a=col1; tit= 'Weekly Stablecoins Transfers Netflow Volume'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
       
        # fig9=px.bar(transaction_data, x='DATES', y='NET_VOLUME')
        # fig9.update_layout(title='Weekly Stablecoins Transfers Netflow Volume', xaxis_title='Date',yaxis_title='Volume')
        # st.plotly_chart(fig9)

        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/13e291b1-0a9f-4ac0-9987-c39cb96a10c4/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATES'; y='CUM_NET_VOLUME'; 
        a=col2; tit= 'Cumulative Stablecoins Transfers Netflow Volume'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = False       
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        
        # fig10=px.line(transaction_data, x='DATES', y='CUM_NET_VOLUME')
        # fig10.update_layout(title='Cumulative Stablecoins Transfers Netflow Volume', xaxis_title='Date',yaxis_title='Volume')
        # st.plotly_chart(fig10)
    
    with d8:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/6fe0880f-32aa-4777-8583-4eee9cd5a306/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y='VOLUME'; color="TRANSFER_TYPE"; barmode='group'
        a=col1; tit= 'Weekly axlUSDC Transfers Volume by Type'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        # fig11=px.bar(transaction_data, x='DATE', y='VOLUME',color="TRANSFER_TYPE")
        # fig11.update_layout(title='Weekly axlUSDC Transfers Volume by Type', xaxis_title='Date',yaxis_title='Volume',barmode='group')
        # st.plotly_chart(fig11)
    
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/3e7cd40b-c6ef-48b7-b601-3be5240d2601/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y='VOLUME'; color="TRANSFER_TYPE"; barmode='group'
        a=col2; tit= 'Weekly axlUSDT Transfers Volume by Type'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        # fig12=px.bar(transaction_data, x='DATE', y='VOLUME',color="TRANSFER_TYPE")
        # fig12.update_layout(title='Weekly axlUSDT Transfers Volume by Type', xaxis_title='Date',yaxis_title='Volume',barmode='group')
        # st.plotly_chart(fig12)
    
    with d9:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/0dc9b033-b396-4e20-aabc-bc05c4990ce8/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig13=px.pie(transaction_data, values='VOLUME', names='TRANSFER_TYPE' , title='Total axlUSDC Transfers Volume by Type')
        fig13.update_traces(textposition='inside', textinfo='percent+label')
        col1.plotly_chart(fig13)
    
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/0067bd89-22d6-40c2-b9ce-cea909c35732/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig14=px.pie(transaction_data, values='VOLUME', names='TRANSFER_TYPE' , title='Total axlUSDT Transfers Volume by Type')
        fig14.update_traces(textposition='inside', textinfo='percent+label')
        col2.plotly_chart(fig14)
    
    with d10:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/cab5d3e8-93bf-4d70-a248-c5cfde69dfb4/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y='VOLUME'; color="CURRENCY"; barmode='relative'
        a=col1; tit= 'Weekly axlUSDT LP Volume per Pool'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = True       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        # fig15=px.bar(transaction_data, x='DATE', y='VOLUME',color="CURRENCY",log_y=True)
        # fig15.update_layout(title='Weekly axlUSDT LP Volume per Pool', xaxis_title='Date',yaxis_title='Volume')
        # st.plotly_chart(fig15)
    
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/d7d25ddf-8e41-4f89-88a5-ba7fb6b654bd/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y='VOLUME'; color="CURRENCY"; barmode='relative'
        a=col2; tit= 'Weekly axlUSDC LP Volume per Pool'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = True       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        # fig16=px.bar(transaction_data, x='DATE', y='VOLUME',color="CURRENCY",log_y=True)
        # fig16.update_layout(title='Weekly axlUSDC LP Volume per Pool', xaxis_title='Date',yaxis_title='Volume')
        # st.plotly_chart(fig16)

    with d11: 
        col1, col2 = st.columns(2)  
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/a081abd4-e625-49db-9b5a-61cab23e5f33/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig17=px.pie(transaction_data, values='VOLUME', names='CURRENCY' , title='Total axlUSDC LP Volume per Pool')
        fig17.update_traces(textposition='inside', textinfo='percent+label')
        col1.plotly_chart(fig17)
    
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/4277ad86-1f86-4d89-8c4a-ef54fea653df/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig18=px.pie(transaction_data, values='VOLUME', names='CURRENCY' , title='Total axlUSDT LP Volume per Pool')
        fig18.update_traces(textposition='inside', textinfo='percent+label')
        col2.plotly_chart(fig18)


if supply:
    st.title('Supply')

    s1 = st.container()
    s2 = st.container()
    s3 = st.container()
    s4 = st.container()
    s5 = st.container()
    s6 = st.container()
    s7 = st.container()
    s8 = st.container()
    s9 = st.container()
    s10 = st.container()
    s11 = st.container()
    s12 = st.container()
    s13 = st.container()
    s14 = st.container()
    s15 = st.container()
    s16 = st.container()
    s17 = st.container()
    
    with s1:  
        col1, col2, col3 = st.columns(3)
        st.write('Statistics')
        
    with s2:
        col1, col2, col3 = st.columns(3)
        average_url="https://node-api.flipsidecrypto.com/api/v2/queries/b330963e-cbf7-4087-9695-2771870658d1/data/latest"
        average_data= pd.read_json(average_url)
        col1.write(average_data)

    with s3:
        average_url="https://node-api.flipsidecrypto.com/api/v2/queries/94bd53f1-5786-41c3-966b-c15b92c1560e/data/latest"
        average_data= pd.read_json(average_url)
        col1.write(average_data)
    with s4:       
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/59611d2e-07da-43be-86a7-6a75fbbffdbf/data/latest"
        total_data= pd.read_json(total_url)
        st.write(total_data)
        
    with s5:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/be1bcbd4-426e-4269-95b9-453d5e2a54fe/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y='TXS'; color="ACTION"; barmode='relative'
        a=col1; tit= 'Weekly Staking Transactions'; xtit='Date'; ytit = 'Transactions' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
       
        # fig1=px.bar(transaction_data, x='DATE', y='TXS',color="ACTION")
        # fig1.update_layout(title='Weekly Staking Transactions', xaxis_title='Date',yaxis_title='Transactions')
        # st.plotly_chart(fig1)

        data= transaction_data; x='DATE'; y='VOLUME'; color="ACTION"; barmode='relative'
        a=col2; tit= 'Weekly Staking Volume'; xtit='Date'; ytit = 'Weekly Staking Volume' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        # fig2=px.bar(transaction_data, x='DATE', y='VOLUME',color="ACTION")
        # fig2.update_layout(title='Weekly Staking Volume', xaxis_title='Date',yaxis_title='Weekly Staking Volume')
        # st.plotly_chart(fig2)
    
    with s6:
        col1, col2 = st.columns(2)
        fig3=px.pie(transaction_data, values='TXS', names='ACTION' , title='Total Staking Transactions')
        fig3.update_traces(textposition='inside', textinfo='percent+label')
        col1.plotly_chart(fig3)
    
        fig4=px.pie(transaction_data, values='VOLUME', names='ACTION' , title='Weekly Staking Volume')
        fig4.update_traces(textposition='inside', textinfo='percent+label')
        col2.plotly_chart(fig4)
   
    with s7:
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/b908b173-30ae-44c1-92d6-a2c3008d0d03/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATES'; y=['Staking Reward USD','Cumulative Staking Reward']; 
        a=st; tit= 'Staking Rewards (USD)'; xtit='Date'; ytit = 'Staking Reward USD' ; w=700; h=450 ; logy = False       
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        
        # fig5=px.line(transaction_data, x='DATE', y=['Staking Reward USD','Cumulative Staking Reward'])
        # fig5.update_layout(title='Staking Rewards (USD)', xaxis_title='Date',yaxis_title='Staking Reward USD')
        # st.plotly_chart(fig5)
    
    with s8:
        st.write('Staking Reward Statistics')
        average_url="https://node-api.flipsidecrypto.com/api/v2/queries/350dcc79-6ead-46ee-85c8-0972fbddbd42/data/latest"
        average_data= pd.read_json(average_url)
        st.write(average_data)
    
    with s9:
        average_url="https://node-api.flipsidecrypto.com/api/v2/queries/413fc733-3fc2-4b16-9c9e-05b7796c3c1b/data/latest"
        average_data= pd.read_json(average_url)
        st.write(average_data)

    
    with s10:
        st.write('Rich list (Top 100)')
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/42fe217e-bd3f-4592-91af-3386ec993665/data/latest"
        transaction_data= pd.read_json(transaction_url)
        # fig6=px.bar(transaction_data, x='USER', y='BALANCE')
        # fig6.update_layout(title='Rich list (Top 100)', xaxis_title='Users',yaxis_title='BALANCE')
        # st.plotly_chart(fig6)
        st.write(transaction_data)
        
    with s11:        
        st.write('IBC Transfers Statistics')
        average_url="https://node-api.flipsidecrypto.com/api/v2/queries/fddbe242-3aaf-4965-a969-435644424912/data/latest"
        average_data= pd.read_json(average_url)
        st.write(average_data)
    

   
    with s12:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/f99e26f5-6c81-41ca-b82d-f8ad115ee617/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y='TXS'; color="BLOCKCHAIN"; barmode='relative'
        a=col1; tit= 'Weekly IBC Transfers Transactions by Blockchain'; xtit='Date'; ytit = 'Transactions' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        # fig7=px.bar(transaction_data, x='DATE', y='TXS',color="BLOCKCHAIN")
        # fig7.update_layout(title='Weekly IBC Transfers Transactions by Blockchain', xaxis_title='Date',yaxis_title='Transactions')
        # st.plotly_chart(fig7)
    
        data= transaction_data; x='DATE'; y='USERS'; color="BLOCKCHAIN"; barmode='relative'
        a=col2; tit= 'Weekly IBC Transfers Users by Blockchain'; xtit='Date'; ytit = 'Users' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        # fig8=px.bar(transaction_data, x='DATE', y='USERS',color="BLOCKCHAIN")
        # fig8.update_layout(title='Weekly IBC Transfers Users by Blockchain', xaxis_title='Date',yaxis_title='Users')
        # st.plotly_chart(fig8)
   
    with s13:
        data= transaction_data; x='DATE'; y='VOLUME'; color="BLOCKCHAIN"; barmode='relative'
        a=st; tit= 'Weekly IBC Transfers Volume by Blockchain'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = False       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        # fig9=px.bar(transaction_data, x='DATE', y='VOLUME',color="BLOCKCHAIN")
        # fig9.update_layout(title='Weekly IBC Transfers Volume by Blockchain', xaxis_title='Date',yaxis_title='Volume')
        # st.plotly_chart(fig9)
    
    with s14:
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/2673fc4e-87f2-4f77-95d4-27b1e57a46f5/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='BLOCKCHAIN'; y='TXS'; color="BLOCKCHAIN"; barmode='relative'
        a=col1; tit= 'Total IBC Transfers Transactions by Blockchain'; xtit='Date'; ytit = 'Transactions' ; w=700; h=450 ; logy = True       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
       
        # fig10=px.bar(transaction_data, x='BLOCKCHAIN', y='TXS',color="BLOCKCHAIN",log_y=True)
        # fig10.update_layout(title='Total IBC Transfers Transactions by Blockchain', xaxis_title='Date',yaxis_title='Transactions')
        # st.plotly_chart(fig10)
    
        data= transaction_data; x='BLOCKCHAIN'; y='USERS'; color="BLOCKCHAIN"; barmode='relative'
        a=col2; tit= 'Total IBC Transfers Users by Blockchain'; xtit='Date'; ytit = 'Users' ; w=700; h=450 ; logy = True       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
       
        
        # fig11=px.bar(transaction_data, x='BLOCKCHAIN', y='USERS',color="BLOCKCHAIN",log_y=True)
        # fig11.update_layout(title='Total IBC Transfers Users by Blockchain', xaxis_title='Date',yaxis_title='Users')
        # st.plotly_chart(fig11)
   
    with s15:
        data= transaction_data; x='BLOCKCHAIN'; y='VOLUME'; color="BLOCKCHAIN"; barmode='relative'
        a=st; tit= 'Total IBC Transfers Volume by Blockchain'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = True       
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        # fig12=px.bar(transaction_data, x='BLOCKCHAIN', y='VOLUME',color="BLOCKCHAIN",log_y=True)
        # fig12.update_layout(title='Total IBC Transfers Volume by Blockchain', xaxis_title='Date',yaxis_title='Volume')
        # st.plotly_chart(fig12)
    

if about:
    st.title('About')

    a1 = st.container()
    a2 = st.container()
    a3 = st.container()
    a4 = st.container()

    with a1: 
        col1, col2, col3, col4= st.columns(4) 
        col2.image("https://pbs.twimg.com/profile_images/1453392380250443782/UC8erEKz_400x400.png",width=250)
        col3.image("https://cryptocurrencyjobs.co/startups/assets/logos/flipside-crypto.jpg",width=250)

    with a2: 
        col1, col2= st.columns(2) 
        st.write(""" #### This dashboard was created using the Flipsidecrypto database for the "Terra - 5. Terradash, Part 4: Bringing It All Together" bounty by Memtricsdao.""")

    with a3:
         st.write("""
        #### If you have any questions about this dashboard, please feel free to contact us via discord: 
        #### @farhad#5364
        #### @mamad#8731
        """)  
                
               
   
   

























  



