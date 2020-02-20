
# coding: utf-8

# 1. Import all libraries
# 

# In[1]:


import pandas as pd


# Load dataset using pandas dataframe

# In[2]:


form5500 = pd.DataFrame.from_csv('f_5500_2017_latest.csv', index_col=None)
sf5500 = pd.DataFrame.from_csv('f_5500_sf_2017_latest.csv', index_col=None)


# Print column name

# In[4]:


print(form5500.columns.values)


# In[7]:


print(sf5500.columns.values)


# In[8]:


sf5500.describe()


# In[9]:


form5500.describe()


# In[10]:


form5500.head()


# In[11]:


sf5500.head()


# In[12]:


sf5500.isnull().any()


# In[13]:


sf5500.info()


# In[14]:


sf5500.describe(include=['O'])


# In[71]:


criteria_row_indices = form5500[form5500['SPONS_DFE_MAIL_US_STATE']=='IA'].index


# In[72]:


new_iowa = form5500.loc[criteria_row_indices, :]


# In[73]:


new_iowa.describe()


# In[3]:


iowa=form5500[form5500['SPONS_DFE_MAIL_US_STATE']=='IA']


# In[4]:


iowa.head()


# In[5]:


iowa.describe()


# In[6]:


sf_iowa=sf5500[sf5500['SF_SPONS_US_STATE']=='IA']


# In[7]:


sf_iowa.describe()


# In[8]:


sf_iowa.to_csv('sf_iowa.csv')


# In[9]:


iowa.to_csv('iowa.csv')


# In[10]:


formA = pd.DataFrame.from_csv('F_SCH_A_2017_latest.csv', index_col=None)


# In[13]:


merge=pd.merge(iowa,formA,on='ACK_ID',how='inner')


# In[14]:


merge.describe()


# In[15]:


merge[merge['ACK_ID']=='20180226093757P040073013165001']


# In[16]:


merge.head()


# In[18]:


iowa_FormA_attach=iowa[iowa['SCH_A_ATTACHED_IND']==1]


# In[19]:


iowa_FormA_attach.describe()


# In[20]:


iowa_FormA = pd.merge(iowa_FormA_attach,formA,on='ACK_ID',how='inner')


# In[21]:


iowa_FormA.describe()


# In[22]:


iowa_FormA.to_csv('iowa_FormA.csv')


# In[23]:


iowa_FormA_attach_Life_under_200=iowa_FormA_attach[iowa_FormA_attach['TOT_PARTCP_BOY_CNT']<=200]


# In[24]:


iowa_FormA_attach_Life_under_200.describe()


# In[25]:


iowa_FormA = pd.merge(iowa_FormA_attach_Life_under_200,formA,on='ACK_ID',how='inner')


# In[26]:


iowa_FormA.describe()


# In[27]:


iowa_FormA.to_csv('iowa_FormA.csv')


# In[77]:


criteria_row_indices = new_iowa[new_iowa['TYPE_WELFARE_BNFT_CODE'].notnull()].index


# In[78]:


new_iowa_Welfare_Benefit = new_iowa.loc[criteria_row_indices, :]


# In[79]:


new_iowa_Welfare_Benefit.describe()


# In[113]:


criteria_row_indices = new_iowa_Welfare_Benefit[new_iowa_Welfare_Benefit['TOT_PARTCP_BOY_CNT']<=200].index


# In[114]:


new_iowa_Welfare_Benefit_Life_under_200 = new_iowa_Welfare_Benefit.loc[criteria_row_indices, :]


# In[115]:


new_iowa_Welfare_Benefit_Life_under_200.describe()


# In[29]:


iowa_Welfare_Benefit = iowa[iowa['TYPE_WELFARE_BNFT_CODE'].notnull()]


# In[30]:


iowa_Welfare_Benefit.describe()


# In[31]:


iowa_Welfare_Benefit_Life_under_200=iowa_Welfare_Benefit[iowa_Welfare_Benefit['TOT_PARTCP_BOY_CNT']<=200]


# In[32]:


iowa_Welfare_Benefit_Life_under_200.describe()


# In[33]:


iowa_Welfare_Benefit_Life_under_200_FormA = pd.merge(iowa_Welfare_Benefit_Life_under_200,formA,on='ACK_ID',how='inner')


# In[34]:


iowa_Welfare_Benefit_Life_under_200_FormA.describe()


# In[36]:


iowa_Welfare_Benefit_Life_under_200_FormA.to_csv('iowa_Welfare_Benefit_Life_under_200_FormA.csv')


# In[38]:


iowa_Welfare_Benefit_Life_under_200_FormA.groupby(['ACK_ID'])


# In[42]:


iowa_Welfare_Benefit_Life_under_200_FormA_Columns=iowa_Welfare_Benefit_Life_under_200_FormA[['ACK_ID','FORM_PLAN_YEAR_BEGIN_DATE','FORM_TAX_PRD','PLAN_EFF_DATE','SPONSOR_DFE_NAME','SPONS_DFE_MAIL_US_ADDRESS1','SPONS_DFE_MAIL_US_CITY','SPONS_DFE_MAIL_US_STATE','SPONS_DFE_MAIL_US_ZIP','SPONS_DFE_EIN','SPONS_DFE_PHONE_NUM','BUSINESS_CODE','ADMIN_SIGNED_NAME','TOT_PARTCP_BOY_CNT','TYPE_WELFARE_BNFT_CODE','INS_CARRIER_NAME','INS_CARRIER_EIN','INS_CARRIER_NAIC_CODE','INS_CONTRACT_NUM','INS_PRSN_COVERED_EOY_CNT','INS_BROKER_COMM_TOT_AMT','INS_BROKER_FEES_TOT_AMT','WLFR_BNFT_DENTAL_IND','WLFR_BNFT_VISION_IND','WLFR_BNFT_LIFE_INSUR_IND','WLFR_BNFT_TEMP_DISAB_IND','WLFR_BNFT_LONG_TERM_DISAB_IND','WLFR_TYPE_BNFT_OTH_TEXT','WLFR_TOT_CHARGES_PAID_AMT']]


# In[43]:


iowa_Welfare_Benefit_Life_under_200_FormA_Columns.to_csv('iowa_Welfare_Benefit_Life_under_200_FormA_Columns.csv')


# In[123]:



new_iowa_Welfare_Benefit_Life_under_200.loc[:,'Life']='YES'
new_iowa_Welfare_Benefit_Life_under_200.loc[:,'Dental']='YES'
new_iowa_Welfare_Benefit_Life_under_200.loc[:,'Vision']='YES'
new_iowa_Welfare_Benefit_Life_under_200.loc[:,'Temporary disability']='YES'
new_iowa_Welfare_Benefit_Life_under_200.loc[:,'Long-term disability']='YES'

for idx,obj in enumerate(new_iowa_Welfare_Benefit_Life_under_200['TYPE_WELFARE_BNFT_CODE']):
    #print(idx,obj)
    characters=list(obj)
    i=0
    #print(new_iowa_Welfare_Benefit_Life_under_200.index)
    principal_list=['Life','Dental','Vision','Temporary disability','Long-term disability']

    while i<len(characters):
        x=characters[i]+characters[i+1]
        i=i+2
        #print(x,product[x])
        try:
            if(product[x] in principal_list):
                new_iowa_Welfare_Benefit_Life_under_200.loc[idx:,product[x]]='NO'
        except:
            print('error')
            
        
    #print(principal_product_prob)
    #benefit=pd.DataFrame.from_dict(principal_product_prob,orient='index')
    #iowa_Welfare_Benefit_Life_under_200.append(principal_product_prob,ignore_index=True)
    #print (benefit)


# In[47]:


product={}
product['4A']='Health'
product['4B']='Life'
product['4C']='Supplemental'
product['4D']='Dental'
product['4E']='Vision'
product['4F']='Temporary disability'
product['4G']='Prepaid legal'
product['4H']='Long-term disability'
product['4I']='Severance pay'
product['4J']='Apprenticeship and training'
product['4K']='Scholarship (funded)'
product['4L']='Death benefits'
product['4P']='Taft-Hartley Financial Assistance'
product['4Q']='Other'
product['4R']='Unfunded'
product['4S']='Unfunded'
product['4T']='10 or more employer plan'
product['4U']='Collectively-bargained welfare benefit arrangement'


# In[118]:


new_iowa_Welfare_Benefit_Life_under_200.to_csv('new_iowa_Welfare_Benefit_Life_under_200.csv')


# In[ ]:




