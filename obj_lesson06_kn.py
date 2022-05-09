import pandas as pd


def cal_基本給(w):
    return w['基本給']


def cal_役職手当(w):
    return w['役職手当']


def cal_残業代(w):
    return w['基本給']/160*1.25//10*10*w['残業時間']


def cal_時間給(w):
    return w['時間単価']*w['勤務時間']


def cal_社会保険料(w):
    return round((w['基本給']+w['役職手当']+cal_残業代(w))*0.17, -1)


def cal_所得税(w):
    return ((w['基本給']+w['役職手当']+cal_残業代(w)-cal_社会保険料(w)) + (cal_時間給(w)))*0.1


if __name__ == '__main__':
    cal_inf = {'管理職': [['基本給', '役職手当'], ['社会保険料', '所得税']],
               '一般社員': [['基本給', '残業代'], ['社会保険料', '所得税']],
               'アルバイト': [['時間給'], ['所得税']]}

    workers_inf = [{'名前': '寺尾哲雄', '種別': '管理職', '基本給': 350000, '役職手当': 80000},
                   {'名前': '若林仁継', '種別': '管理職', '基本給': 375000, '役職手当': 40000},
                   {'名前': '寺田帆香', '種別': '一般社員', '基本給': 320000, '残業時間': 30},
                   {'名前': '広田康博', '種別': '一般社員', '基本給': 295000, '残業時間': 20},
                   {'名前': '菅沼洋一郎', '種別': '一般社員', '基本給': 220000, '残業時間': 35},
                   {'名前': '菊地章 ', '種別': 'アルバイト', '時間単価': 1200, '勤務時間': 90},
                   {'名前': '山岸柑奈', '種別': 'アルバイト', '時間単価': 1000, '勤務時間': 120},
                   {'名前': '浜口知実', '種別': '管理職', '基本給': 360000, '役職手当': 40000},
                   {'名前': '安達道彦', '種別': '一般社員', '基本給': 310000, '残業時間': 20}
                   ]
    df_workers = pd.DataFrame()
    for w in workers_inf:
        df_workers = df_workers.append(pd.Series(w), ignore_index=True)
    df_workers = df_workers.fillna(0)
    # print(df_workers)

    for _, w in df_workers.iterrows():
        salary = 0
        for s in cal_inf[w['種別']][0]:
            #print(s, globals()['cal_'+s](w))
            salary += globals()['cal_'+s](w)
        for s in cal_inf[w['種別']][1]:
            #print(s, globals()['cal_'+s](w))
            salary -= globals()['cal_'+s](w)
        print(f"{w['名前']}の給与振込額は{int(salary)}。")
