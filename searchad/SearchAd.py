# 일반 검색광고
class CommonSearchAd:

    def __init__(self, account_name):
        self.account_name = account_name


    def keywords_expansion(self, file_path, combinations, max_len=15, if_windows=True):
        self.file_path = file_path
        self.combinations = combinations
        self.max_len = max_len
        self.if_windows = if_windows

        import pandas as pd
        import datetime
        from pytz import timezone

        # 파일 가져오기
        try:
            input_df = pd.read_csv(file_path)
        except:
            input_df = pd.read_csv(file_path, encoding='ms949')

        # 각 columns 리스트화
        groups = []
        for idx, col in enumerate(input_df.columns):
            factor = list(input_df[col].loc[input_df[col].isna()==False])
            if len(factor):
                factor = [each.replace(" ", "") for each in factor]
                groups.append(factor)

        # 결과물 도출
        result = []
        for comb in combinations:
            length = len(comb)
            if length:
                # 1개 (=최소값)
                if length == 1:
                    for a in groups[comb[0]-1]:
                        if len(a) <= max_len:
                            result.append(a)
                # 2개
                elif length == 2:
                    for a in groups[comb[0]-1]:
                        for b in groups[comb[1]-1]:
                            if len(a+b) <= max_len:
                                result.append(a+b)
                # 3개            
                elif length == 3:
                    for a in groups[comb[0]-1]:
                        for b in groups[comb[1]-1]:
                            for c in groups[comb[2]-1]:
                                if len(a+b+c) <= max_len:
                                    result.append(a+b+c)
                # 4개            
                elif length == 4:
                    for a in groups[comb[0]-1]:
                        for b in groups[comb[1]-1]:
                            for c in groups[comb[2]-1]:
                                for d in groups[comb[3]-1]:
                                    if len(a+b+c+d) <= max_len:
                                        result.append(a+b+c+d)
                # 5개            
                elif length == 5:
                    for a in groups[comb[0]-1]:
                        for b in groups[comb[1]-1]:
                            for c in groups[comb[2]-1]:
                                for d in groups[comb[3]-1]:
                                    for e in groups[comb[4]-1]:
                                        if len(a+b+c+d+e) <= max_len:
                                            result.append(a+b+c+d+e)
                # 6개            
                elif length == 6:
                    for a in groups[comb[0]-1]:
                        for b in groups[comb[1]-1]:
                            for c in groups[comb[2]-1]:
                                for d in groups[comb[3]-1]:
                                    for e in groups[comb[4]-1]:
                                        for f in groups[comb[5]-1]:
                                            if len(a+b+c+d+e+f) <= max_len:
                                                result.append(a+b+c+d+e+f)
                # 7개
                elif length == 7:
                    for a in groups[comb[0]-1]:
                        for b in groups[comb[1]-1]:
                            for c in groups[comb[2]-1]:
                                for d in groups[comb[3]-1]:
                                    for e in groups[comb[4]-1]:
                                        for f in groups[comb[5]-1]:
                                            for g in groups[comb[6]-1]:
                                                if len(a+b+c+d+e+f+g) <= max_len:
                                                    result.append(a+b+c+d+e+f+g)

                # 8개
                elif length == 8:
                    for a in groups[comb[0] - 1]:
                        for b in groups[comb[1] - 1]:
                            for c in groups[comb[2] - 1]:
                                for d in groups[comb[3] - 1]:
                                    for e in groups[comb[4] - 1]:
                                        for f in groups[comb[5] - 1]:
                                            for g in groups[comb[6] - 1]:
                                                for h in groups[comb[7] - 1]:
                                                    if len(a + b + c + d + e + f + g + h) <= max_len:
                                                        result.append(a + b + c + d + e + f + g + h)

                # 9개
                elif length == 9:
                    for a in groups[comb[0] - 1]:
                        for b in groups[comb[1] - 1]:
                            for c in groups[comb[2] - 1]:
                                for d in groups[comb[3] - 1]:
                                    for e in groups[comb[4] - 1]:
                                        for f in groups[comb[5] - 1]:
                                            for g in groups[comb[6] - 1]:
                                                for h in groups[comb[7] - 1]:
                                                    for i in groups[comb[8] - 1]:
                                                        if len(a + b + c + d + e + f + g + h + i) <= max_len:
                                                            result.append(a + b + c + d + e + f + g + h + i)

                # 10개
                elif length == 10:
                    for a in groups[comb[0] - 1]:
                        for b in groups[comb[1] - 1]:
                            for c in groups[comb[2] - 1]:
                                for d in groups[comb[3] - 1]:
                                    for e in groups[comb[4] - 1]:
                                        for f in groups[comb[5] - 1]:
                                            for g in groups[comb[6] - 1]:
                                                for h in groups[comb[7] - 1]:
                                                    for i in groups[comb[8] - 1]:
                                                        for j in groups[comb[9] - 1]:
                                                            if len(a + b + c + d + e + f + g + h + i + j) <= max_len:
                                                                result.append(a + b + c + d + e + f + g + h + i + j)

                # 11개
                elif length == 11:
                    for a in groups[comb[0] - 1]:
                        for b in groups[comb[1] - 1]:
                            for c in groups[comb[2] - 1]:
                                for d in groups[comb[3] - 1]:
                                    for e in groups[comb[4] - 1]:
                                        for f in groups[comb[5] - 1]:
                                            for g in groups[comb[6] - 1]:
                                                for h in groups[comb[7] - 1]:
                                                    for i in groups[comb[8] - 1]:
                                                        for j in groups[comb[9] - 1]:
                                                            for k in groups[comb[10] - 1]:
                                                                if len(a + b + c + d + e + f + g + h + i + j + k) <= max_len:
                                                                    result.append(a + b + c + d + e + f + g + h + i + j + k)

                # 12개 (최대값)
                else:
                    for a in groups[comb[0] - 1]:
                        for b in groups[comb[1] - 1]:
                            for c in groups[comb[2] - 1]:
                                for d in groups[comb[3] - 1]:
                                    for e in groups[comb[4] - 1]:
                                        for f in groups[comb[5] - 1]:
                                            for g in groups[comb[6] - 1]:
                                                for h in groups[comb[7] - 1]:
                                                    for i in groups[comb[8] - 1]:
                                                        for j in groups[comb[9] - 1]:
                                                            for k in groups[comb[10] - 1]:
                                                                for l in groups[comb[11] - 1]:
                                                                    if len(a + b + c + d + e + f + g + h + i + j + k + l) <= max_len:
                                                                        result.append(a + b + c + d + e + f + g + h + i + j + k + l)

        # 대문자화 (키워드도구에서 쓸 때 대문자 자동변환됨)
        result = [each.upper() for each in result]
        
        # output csv로 내보내기
        output_df = pd.DataFrame(result, columns=["col1"])
        output_df = output_df.drop_duplicates(['col1'])
        realtime = str(datetime.datetime.now(timezone('Asia/Seoul'))).replace("-","").replace(":", "").replace(" ", "").split(".")[0]

        if self.if_windows:
            output_df.to_csv(f"./output/{self.account_name}/{self.account_name}_expanded_keywords_{realtime}.csv",
                             sep=',', index=False, encoding='ms949')
        else:
            output_df.to_csv(f"./output/{self.account_name}/{self.account_name}_expanded_keywords_{realtime}.csv",
                             sep=',', index=False, encoding='utf-8-sig')
        return output_df
        print("작업 완료!")



# 네이버 검색광고
class NaverSearchAd:

    def __init__(self, account_name, base_url='https://api.naver.com'):
        from searchadapi import signaturehelper, keyinfo

        self.account_name = account_name
        self.API_KEY = keyinfo.API_KEY
        self.SECRET_KEY = keyinfo.SECRET_KEY
        self.CUSTOMER_ID = keyinfo.CUSTOMER_ID
        self.account_name = account_name
        self.BASE_URL = base_url


    def get_header(self, method, uri):
        import time
        from searchadapi import signaturehelper, keyinfo

        self.method = method
        self.uri = uri
        timestamp = str(round(time.time() * 1000))
        signature = signaturehelper.Signature.generate(timestamp, method, uri, self.SECRET_KEY)
        return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': self.API_KEY,
                'X-Customer': str(self.CUSTOMER_ID), 'X-Signature': signature}


    def keywords_tool(self, file_path, uri='/keywordstool', method='GET', if_windows=True):
        self.file_path = file_path
        self.uri = uri
        self.method = method
        self.if_windows = if_windows

        import requests
        import pandas as pd
        import datetime
        import time
        from pytz import timezone

        # 파일 가져오기
        try:
            kw_list = pd.read_csv(file_path).iloc[:, 0]
        except:
            kw_list = pd.read_csv(file_path, encoding='ms949').iloc[:, 0]
        tic = time.time()
        cnt = 0

        # 키워드 도구 통해 데이터 가져오기
        print("-------------------- 데이터 가져오기 시작! --------------------")
        for i in range(len(kw_list) // 5 + 1):
            req = requests.get(self.BASE_URL + self.uri,
                               params={"hintKeywords": list(kw_list[5 * i: 5 * (i + 1)]),
                                       "showDetail": "1"
                                       },
                               headers=self.get_header(self.method, self.uri),
                               )
            if cnt == 0:
                output_df = pd.DataFrame(req.json()['keywordList'])
                cnt += len(list(kw_list[5 * i: 5 * (i + 1)]))
                print(f"{cnt}번째 행 완료!")
                time.sleep(0.3)
            else:
                tmp_result = pd.DataFrame(req.json()['keywordList'])
                output_df = pd.concat([output_df, tmp_result])
                cnt += len(list(kw_list[5 * i: 5 * (i + 1)]))
                print(f"{cnt}번째 행 완료!")
                time.sleep(0.3)
        print("-------------------- 데이터 가져오기 완료! --------------------")
        print("데이터 가져오는 데 걸린 시간:", str(round(time.time() - tic, 1)), "초")

        # 열이름 수정 및 인덱스 리셋
        output_df = output_df.rename({
            'relKeyword': '연관키워드',
            'monthlyPcQcCnt': '월간검색수_PC',
            'monthlyMobileQcCnt': '월간검색수_모바일',
            'monthlyAvePcClkCnt': '월평균클릭수_PC',
            'monthlyAveMobileClkCnt': '월평균클릭수_모바일',
            'monthlyAvePcCtr': '월평균클릭률_PC',
            'monthlyAveMobileCtr': '월평균클릭률_모바일',
            'plAvgDepth': '월평균노출광고수',
            'compIdx': '경쟁정도',
        },
            axis=1)
        output_df = output_df.reset_index(drop=True)

        # 데이터 후처리
        print("-------------------- 데이터 후처리 시작! --------------------")
        ## 중복제거
        print("중복제거 전 키워드 갯수:", len(output_df))
        output_df = output_df.drop_duplicates(["연관키워드"])
        print("중복제거 후 키워드 갯수:", len(output_df))
        # 10 미만의 것들은 내림차순 정렬을 위해 편의상 3으로 통일
        output_df.replace("< 10", int(3), inplace=True)
        print("<10은 3으로 수정 완료")
        # 월간검색수_모바일 기준 내림차순 정렬
        output_df.sort_values(by='월간검색수_모바일', axis=0, ascending=False).reset_index(drop=True)
        print("월간검색수_모바일 기준 내림차순 정렬 완료!")
        print("-------------------- 데이터 후처리 완료! --------------------")

        # output 파일 내보내기
        realtime = \
        str(datetime.datetime.now(timezone('Asia/Seoul'))).replace("-", "").replace(":", "").replace(" ", "").split(
            ".")[0]
        ## 확장키워드와 연관키워드 구분해서 내보내기
        output_df_extended = output_df.loc[output_df["연관키워드"].isin(kw_list) == True].reset_index(drop=True)
        output_df_related = output_df.loc[output_df["연관키워드"].isin(kw_list) == False].reset_index(drop=True)

        ## 내림차순 정렬
        output_df_extended = output_df_extended.sort_values(by='월간검색수_모바일', axis=0, ascending=False).reset_index(
            drop=True)
        output_df_related = output_df_related.sort_values(by='월간검색수_모바일', axis=0, ascending=False).reset_index(
            drop=True)

        ## csv로 내보내기
        if self.if_windows:
            output_df_extended.to_csv(
                f"./output/{self.account_name}/{self.account_name}_extended_kwtools_metric_{realtime}.csv", sep=',',
                index=False, encoding='ms949')
            output_df_related.to_csv(
                f"./output/{self.account_name}/{self.account_name}_related_kwtools_metric_{realtime}.csv", sep=',',
                index=False, encoding='ms949')
        else:
            output_df_extended.to_csv(
                f"./output/{self.account_name}/{self.account_name}_extended_kwtools_metric_{realtime}.csv", sep=',',
                index=False, encoding='utf-8-sig')
            output_df_related.to_csv(
                f"./output/{self.account_name}/{self.account_name}_related_kwtools_metric_{realtime}.csv", sep=',',
                index=False, encoding='utf-8-sig')
        print("작업 완료!")


    def brandscrub(self, file_path, if_windows=True):
        self.file_path = file_path
        self.if_windows = if_windows

        import pandas as pd
        import time
        import datetime
        from pytz import timezone
        import requests
        from bs4 import BeautifulSoup as bs

        # 파일 가져오기
        try:
            input_df = pd.read_csv(file_path)
        except:
            input_df = pd.read_csv(file_path, encoding='ms949')
        input_df = input_df[["keyword", "device", "url"]]

        # 데이터 전처리
        ## 공백 제거
        input_df['keyword'] = input_df['keyword'].str.replace(" ", "")
        input_df['device'] = input_df['device'].str.replace(" ", "")
        input_df['url'] = input_df['url'].str.replace(" ", "")

        ## 대소문자 변환 (keyword, device는 대문자, url은 소문자)
        input_df['keyword'] = input_df['keyword'].str.upper()
        input_df['device'] = input_df['device'].str.upper()
        input_df['url'] = input_df['url'].str.lower()

        # 빈 리스트 준비
        kw_list, device_list, url_list = [], [], []
        tic = time.time()

        # input데이터 행 하나씩 가져와서 수행
        for idx, row in input_df.iterrows():
            query = row["keyword"]
            device = row["device"]
            exception_kw = row["url"]
            page_num = 1

            # PC와 MOBILE URL이 다르기 때문에 구분
            while page_num:
                if device == "PC":
                    url = f"https://ad.search.naver.com/search.naver?where=ad&sm=svc_nrs&query={query}&referenceId=&pagingIndex={page_num}"
                elif device == "MOBILE":
                    url = f"https://m.ad.search.naver.com/search.naver?where=m_expd&query={query}&referenceId=hmE6dwp0JWhssEXKQk8ssssssR0-504759&page={page_num}"
                else:
                    print("device name error!")
                    break

                req = requests.get(url)
                if not req:
                    print("request error!")
                    continue

                html = req.text
                # header = req.headers
                # status = req.status_code
                # is_ok = req.ok
                soup = bs(html, 'html.parser')

                # 페이지 수를 증가시켰을 때 검색결과가 있을 때만 실행되고, 0이면 stop
                # PC와 MOBILE CSS_SELECTOR 주소가 다르기 때문에 구분
                if device == "PC":
                    my_urls = soup.select('li > div.inner > div.url_area > a')
                elif device == "MOBILE":
                    my_urls = soup.select('li > div > div.tit_wrap > div > a > div > cite > span.url_link')

                # 검색결과가 없다면 반복문 escape하고 다음 행 데이터에 대해 수행
                if len(my_urls) == 0:
                    break

                # 검색결과가 있다면 제외url 조건에 따라 필터링하며 데이터 적재
                for i in range(len(my_urls)):
                    if not exception_kw in my_urls[i].text:
                        kw_list.append(query)
                        device_list.append(device)
                        url_list.append(my_urls[i].text)

                page_num += 1
                time.sleep(0.2)
            # 중간에 진척상황을 파악하기 위한 알림
            print(f"{idx + 1} 번째 행 완료!")
        print("전체 데이터 처리 완료! 걸린 시간:", str(round(time.time() - tic, 1)), "초")

        # output 파일 생성 후 csv로 내보내기
        output_df = pd.DataFrame({"keyword": kw_list,
                                  "device": device_list,
                                  "url": url_list})
        realtime = \
        str(datetime.datetime.now(timezone('Asia/Seoul'))).replace("-", "").replace(":", "").replace(" ", "").split(
            ".")[0]
        if self.if_windows:
            output_df.to_csv(
                f"./output/{self.account_name}/{self.account_name}_brandscrub_result_{realtime}.csv", sep=',',
                index=False, encoding='ms949')
        else:
            output_df.to_csv(
                f"./output/{self.account_name}/{self.account_name}_brandscrub_result_{realtime}.csv", sep=',',
                index=False, encoding='utf-8-sig')
        print("작업 완료!")


    def estimate_average_position_bid(self, file_path, ad_type, method='POST', if_windows=True):
        self.file_path = file_path
        if ad_type == "npl":
            self.ad_type = ad_type
            self.uri = '/estimate/average-position-bid/keyword'
        elif ad_type == "npc":
            self.ad_type = ad_type
            self.uri = '/npc-estimate/average-position-bid/keyword'
        else:
            sys.exit("No ad_type set")
        self.method = method
        self.if_windows = if_windows

        import requests
        import pandas as pd
        import datetime
        import time
        from pytz import timezone

        # 파일 가져오기
        try:
            input_df = pd.read_csv(file_path)
        except:
            input_df = pd.read_csv(file_path, encoding='ms949')

        # 파일 전처리
        ## device열 대문자
        input_df['device'] = input_df['device'].str.upper()

        # 빈 리스트 및 cnt 변수 생성
        device, bid, keyword, position = [], [], [], []
        cnt = 0

        # PC와 MOBILE로 input_df 둘로 나누기
        input_df_pc = input_df.loc[input_df['device'] == "PC"].reset_index(drop=True)
        input_df_mobile = input_df.loc[input_df['device'] == "MOBILE"].reset_index(drop=True)

        # 기기별로 행 단위 데이터 딕셔너리화 후 리스트로 묶기
        tmp_list_pc, tmp_list_mobile = [], []
        for _, row in input_df_pc.iterrows():
            tmp_dict = {'key': row["keyword"], 'position': row["position"]}
            tmp_list_pc.append(tmp_dict)
        for _, row in input_df_mobile.iterrows():
            tmp_dict = {'key': row["keyword"], 'position': row["position"]}
            tmp_list_mobile.append(tmp_dict)

        # 각 기기별로 200개씩 끊어서 request 보내고 response 받기, 그리고 리스트에 담아놓기
        tic = time.time()

        ## PC
        for i in range(len(tmp_list_pc) // 200 + 1):
            req = requests.post(self.BASE_URL + self.uri,
                                json={"device": "PC",
                                      "items": tmp_list_pc[200*i : 200*(i+1)],
                                      },
                                headers=self.get_header(self.method, self.uri),
                                )
            if req:
                for j in range(len(req.json()['estimate'])):
                    keyword.append(req.json()['estimate'][j]['keyword'])
                    device.append(req.json()['device'])
                    position.append(req.json()['estimate'][j]['position'])
                    bid.append(req.json()['estimate'][j]['bid'])
                cnt += len(req.json()['estimate'])
                print(f"{cnt}번째 행 완료!")
                time.sleep(0.2)
            else:
                print("request error")
                print(f"{cnt}번째 행 완료!")
                time.sleep(0.2)
                continue
        print("PC 데이터 처리 완료!")

        ## MOBILE
        for i in range(len(tmp_list_mobile) // 200 + 1):
            req = requests.post(self.BASE_URL + self.uri,
                                json={"device": "MOBILE",
                                      "items": tmp_list_mobile[200*i : 200*(i+1)],
                                      },
                                headers=self.get_header(self.method, self.uri),
                                )
            if req:
                for j in range(len(req.json()['estimate'])):
                    keyword.append(req.json()['estimate'][j]['keyword'])
                    device.append(req.json()['device'])
                    position.append(req.json()['estimate'][j]['position'])
                    bid.append(req.json()['estimate'][j]['bid'])
                cnt += len(req.json()['estimate'])
                print(f"{cnt}번째 행 완료!")
                time.sleep(0.2)
            else:
                print("request error")
                print(f"{cnt}번째 행 완료!")
                time.sleep(0.2)
                continue
        print("MOBILE 데이터 처리 완료!")
        print("전체 데이터 처리 완료! 걸린 시간:", str(round(time.time() - tic, 1)), "초")

        # output 파일 생성 후 csv로 내보내기
        output_df = pd.DataFrame({"keyword": keyword,
                                  "device": device,
                                  "position": position,
                                  "bid": bid,
                                  })
        realtime = \
            str(datetime.datetime.now(timezone('Asia/Seoul'))).replace("-", "").replace(":", "").replace(" ", "").split(
                ".")[0]
        if self.if_windows:
            output_df.to_csv(
                f"./output/{self.account_name}/{self.account_name}_{self.ad_type}_esimate_bid_position_{realtime}.csv",
                sep=',', index=False, encoding='ms949')
        else:
            output_df.to_csv(
                f"./output/{self.account_name}/{self.account_name}_{self.ad_type}_esimate_bid_position_{realtime}.csv",
                sep=',', index=False, encoding='utf-8-sig')
        print("작업 완료!")
        return output_df


    def get_keywords_info(self, customer_id, method='GET', if_windows=True):
        self.CUSTOMER_ID = str(customer_id)
        self.method = method
        self.if_windows = if_windows

        import time
        import requests
        import pandas as pd
        import datetime
        from pytz import timezone

        # 1. 전체 캠페인 리스트 가져오기 & 캠페인ID-캠페인명 매칭하는 dict 만들기
        print("-------------------- 캠페인 리스트 가져오기 시작! --------------------")
        # request & response
        self.uri = '/ncc/campaigns'
        query = {'campaignType': "WEB_SITE", 'baseSearchId': None, 'recordSize': None,
                 'selector': None}  # WEB_SITE, SHOPPING, POWER_CONTENTS, BRAND_SEARCH. 일단 파워링크 ONLY.
        req = requests.get(self.BASE_URL + self.uri,
                           params=query,
                           headers=self.get_header(self.method, self.uri),
                           )
        nccCampaignId_list = [each['nccCampaignId'] for each in req.json()]
        nccCampaignName_list = [each['name'] for each in req.json()]
        nccCampaignDict = {'nccCampaignId': nccCampaignId_list,
                           'nccCampaignName': nccCampaignName_list}
        print("-------------------- 캠페인 리스트 가져오기 완료! --------------------")

        # 2. 전체 캠페인으로부터 전체 광고그룹 리스트 가져오기 & 광고그룹ID-광고그룹명 매칭하는 dict 만들기
        print("-------------------- 광고그룹 리스트 가져오기 시작! --------------------")
        # request & response
        self.uri = '/ncc/adgroups'
        nccCampaignId_list, nccAdgroupId_list, nccAdgroupName_list = [], [], []
        cnt = 0

        for campaignId in nccCampaignDict["nccCampaignId"]:
            query = {'nccCampaignId': campaignId, 'baseSearchId': None, 'recordSize': None, 'selector': None}
            req = requests.get(self.BASE_URL + self.uri, params=query,
                               headers=self.get_header(self.method, self.uri),
                               )

            for each in req.json():
                nccCampaignId_list.append(each["nccCampaignId"])
                nccAdgroupId_list.append(each["nccAdgroupId"])
                nccAdgroupName_list.append(each["name"])
            print(f"{cnt}번째 캠페인의 광고그룹 리스트 가져오기 완료!")
            cnt += 1
        print("전체 캠페인 완료!")
        nccAdgroupDict = {'nccCampaignId': nccCampaignId_list,
                          'nccAdgroupId': nccAdgroupId_list,
                          'nccAdgroupName': nccAdgroupName_list}
        print("-------------------- 광고그룹 리스트 가져오기 완료! --------------------")

        # 3. 전체 광고그룹으로부터 전체 키워드 리스트 가져오기
        print("-------------------- 키워드 리스트 가져오기 시작! --------------------")
        # request & response
        self.uri = '/ncc/keywords'
        bidAmt_list, customerId_list, nccKeywordName_list, nccCampaignId_list, nccAdgroupId_list, nccKeywordId_list,\
        status_list, status_reason_list = [], [], [], [], [], [], [], []
        cnt = 0

        for adgroupId in nccAdgroupDict["nccAdgroupId"]:
            query = {'nccAdgroupId': adgroupId, 'baseSearchId': None, 'recordSize': None, 'selector': None}
            req = requests.get(self.BASE_URL + self.uri, params=query,
                               headers=self.get_header(self.method, self.uri))

            for each in req.json():
                bidAmt_list.append(each['bidAmt'])
                customerId_list.append(each['customerId'])
                nccKeywordName_list.append(each['keyword'])
                nccCampaignId_list.append(each['nccCampaignId'])
                nccAdgroupId_list.append(each['nccAdgroupId'])
                nccKeywordId_list.append(each['nccKeywordId'])
                status_list.append(each['status'])
                status_reason_list.append(each['statusReason'])
            if cnt % 10 == 0:
                print(f"{cnt}번째 광고그룹의 키워드 리스트 가져오기 완료!")
            cnt += 1
        print("전체 광고그룹 완료!")

        nccKeywordDict = {'CustomerId': customerId_list,
                          'nccCampaignId': nccCampaignId_list,
                          'nccAdgroupId': nccAdgroupId_list,
                          'nccKeywordId': nccKeywordId_list,
                          'nccKeywordName': nccKeywordName_list,
                          'bidAmt': bidAmt_list,
                          'status': status_list,
                          'statusReason': status_reason_list}
        print("-------------------- 키워드 리스트 가져오기 완료! --------------------")

        # 4. 데이터프레임의 결과물과 키워드리스트, 총 두 가지를 만들어서 내보내기 및 return
        ## 1~3의 결과물들을 활용하여 '대량등록'에서 다운로드받는 양식대로 결과물(df) 만들기
        nccCampaignDf = pd.DataFrame(nccCampaignDict)
        nccAdgroupDf = pd.DataFrame(nccAdgroupDict)
        nccKeywordDf = pd.DataFrame(nccKeywordDict)

        ## 캠페인명, 광고그룹명 merge (엑셀의 vlookup 개념)
        nccKeywordDf = pd.merge(nccKeywordDf, nccAdgroupDf[["nccAdgroupId", "nccAdgroupName"]], on='nccAdgroupId',
                                how='left')
        nccKeywordDf = pd.merge(nccKeywordDf, nccCampaignDf[["nccCampaignId", "nccCampaignName"]], on='nccCampaignId',
                                how='left')

        ## 열 순서 재배치
        nccKeywordDf = nccKeywordDf[
            ["CustomerId", "nccCampaignId", "nccCampaignName", "nccAdgroupId", "nccAdgroupName", "nccKeywordId",
             "nccKeywordName", "bidAmt", "status", "statusReason"]
        ]

        ## csv로 내보내기
        realtime = \
        str(datetime.datetime.now(timezone('Asia/Seoul'))).replace("-", "").replace(":", "").replace(" ", "").split(
            ".")[0]
        nccKeywordDf.to_csv(f"./output/{self.account_name}/{self.account_name}_keywords_info_{realtime}.csv", sep=',',
                            index=False, encoding='ms949')

        # 5. 별도 전체 키워드리스트 만들어 위 df과 함께 return. 키워드확장 시 기등록키워드 제거에 활용하기 위함
        kwlist = nccKeywordDf[["nccKeywordName"]].drop_duplicates()

        return nccKeywordDf, kwlist


    # def drop_existing_keywords(self, customer_id, expanded_kw_df, if_windows=True):
    #     self.customer_id = customer_id
    #     self.expanded_kw_df = expanded_kw_df
    #     self.if_windows = if_windows
    #
    #     import pandas as pd
    #     import datetime
    #     from pytz import timezone
    #
    #     _, kwlist = self.get_keywords_info(self, self.customer_id, self.if_windows)
    #     output_df = pd.DataFrame({"result_col": set(expanded_kw_df.iloc[:, 0]) -
    #                               set(kwlist.iloc[:, 0])})
    #     realtime = \
    #     str(datetime.datetime.now(timezone('Asia/Seoul'))).replace("-", "").replace(":", "").replace(" ", "").split(
    #         ".")[0]
    #
    #     if self.if_windows:
    #         output_df.to_csv(f"./output/{self.account_name}/{self.account_name}_filtered_expanded_keywords_{realtime}.csv",
    #                          sep=',', index=False, encoding='ms949')
    #     else:
    #         output_df.to_csv(f"./output/{self.account_name}/{self.account_name}_filtered_expanded_keywords_{realtime}.csv",
    #                          sep=',', index=False, encoding='utf-8-sig')
    #     return output_df
    #     print("작업 완료!")