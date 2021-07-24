import pandas as pd
import requests
import json
from pandas import json_normalize

class Dataset:
    
    def __init__(self, ae, cm):
        # Getting AE Subject ID's
        self.df_ae = requests.get(ae)
        self.df_ae.json().keys()
        self.df_ae=pd.DataFrame.from_dict(self.df_ae.json()['data'])
        self.df_ae= self.df_ae.set_axis(["subid"], axis=1)
        # Getting CM Subject ID's
        self.df_cm = requests.get(cm)
        self.df_cm.json().keys()
        self.df_cm=pd.DataFrame.from_dict(self.df_cm.json()['data'])
        self.df_cm= self.df_cm.set_axis(["subid"], axis=1)
        #print(df_ae.shape)
        #print(df_cm.shape)
        # Merging two domain subject id's and converting into list for iterlation to get the data set of ae and cm
        df_list = pd.merge(self.df_ae, self.df_cm, on='subid', how='outer')
        #subid_list = df_list['subid'].tolist()
        subid_list = ['76809','130301']
        data_list_am = []
        for i in subid_list:
            ae_subid = 'https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/ae/subject/{}/list'.format(i)
            df_ae_subid = requests.get(ae_subid)
            df_ae_subid=json.loads(df_ae_subid.text)
            df_ae_subid=json_normalize(df_ae_subid,record_path = ['data'])
            data_list_am.append(df_ae_subid)
        dfae = pd.concat((data_list_am), ignore_index=True)
        data_list_cm = []
        for j in subid_list:
            cm_subid = 'https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/cm/subject/{}/list'.format(j)
            df_cm_subid = requests.get(cm_subid)
            df_cm_subid=json.loads(df_cm_subid.text)
            df_cm_subid=json_normalize(df_cm_subid,record_path = ['data'])
            data_list_cm.append(df_cm_subid)
        dfcm = pd.concat((data_list_cm), ignore_index=True)
        dfcm['cmstdat'] = pd.to_datetime(dfcm['cmstdat'], errors='coerce')
        dfcm['cmendat'] = pd.to_datetime(dfcm['cmendat'], errors='coerce')
        dfae['aestdat'] = pd.to_datetime(dfae['aestdat'], errors='coerce')
        dfae['aeendat'] = pd.to_datetime(dfae['aeendat'], errors='coerce')
        self.dfae = dfae
        self.dfcm = dfcm
        print("ae & cm domain shape:",dfae.shape, dfcm.shape)
        #return dfae, dfcm
    def type1(self):
        dfae = self.dfae
        dfcm = self.dfcm
        #print(dfae.shape)
        #print(dfcm.shape)
        df1_cm = []
        df1_ae = []
        for i, r1 in dfae.iterrows():
            for j, r2 in dfcm.iterrows():
                if (r1['subjectid'] == r2['subjectid'] and r1['formidx'] == r2['formidx']):
                    if (r1['aestdat'] > r2['cmstdat']):
                        df1_cm.append(dfcm.iloc[j])
                        df1_ae.append(dfae.iloc[i])
                    else:
                        continue
                else:
                    continue
        df1_ae = pd.DataFrame(df1_ae)
        df1_cm = pd.DataFrame(df1_cm)
        # df1_ae = df1_ae.drop_duplicates(keep='first')
        # df1_cm = df1_cm.drop_duplicates(keep='first')
        # df1_ae.reset_index(inplace=True)
        # df1_cm.reset_index(inplace=True)
        print("Type1:",df1_cm.shape)
    def type2(self):
        dfae = self.dfae
        dfcm = self.dfcm
        df2_cm = []
        df2_ae = []
        for i, r1 in dfae.iterrows():
            for j, r2 in dfcm.iterrows():
                if (r1['subjectid'] == r2['subjectid'] and r1['formidx'] == r2['formidx']):
                    if (r1['aestdat'] < r2['cmstdat']):
                        df2_cm.append(dfcm.iloc[j])
                        df2_ae.append(dfae.iloc[i])
                    else:
                        continue
                else:
                    continue
        df2_cm = pd.DataFrame(df2_cm)
        df2_ae = pd.DataFrame(df2_ae)
        df2_ae.reset_index(inplace=True)
        df2_cm.reset_index(inplace=True)
        return print("Type2:",df2_ae.shape)
    def type3_4(self):
        dfae = self.dfae
        dfcm = self.dfcm
        df3 = dfae[dfae.duplicated(['aestdat', 'aeendat'])]
        df4 = dfcm[dfcm.duplicated(['cmstdat', 'cmendat'])]
        return print("Type 3 & 4: ae duplicate", df3.shape, ", cm duplicate", df4.shape)
    def type5(self):
        dfae = self.dfae
        dfcm = self.dfcm
        df5_cm = []
        df5_ae = []
        for i, r1 in dfae.iterrows():
            for j, r2 in dfcm.iterrows():
                if (r1['subjectid'] == r2['subjectid'] and r1['formidx'] == r2['formidx']):
                    if (r1['aestdat'] > r2['cmstdat']):
                        if (r1['aeendat'] < r2['cmendat']):
                            df5_cm.append(dfcm.iloc[j])
                            df5_ae.append(dfae.iloc[i])
                        else:
                            continue
        df5_cm = pd.DataFrame(df5_cm)
        df5_ae = pd.DataFrame(df5_ae)
        #df6_cm = df1_cm.drop_duplicates(keep='first')
        #df6_ae = df1_ae.drop_duplicates(keep='first')
        df5_ae.reset_index(inplace=True)
        df5_cm.reset_index(inplace=True)
        return print("Type5:",df5_cm.shape, df5_ae.shape)


ae = 'https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/ae/subject/list'
cm = 'https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/cm/subject/list'
data = Dataset(ae, cm)
# data.ae_dataset()
# data.cm_dataset()
data.type1()
# data.type2()
# data.type3_4()
# data.type5()