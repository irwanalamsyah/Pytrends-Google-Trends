from pytrends.request import TrendReq

pytrends = TrendReq(hl='us-US')

all_keywords = ['Naruto', 'One Piece', 'Dragon Ball', 'Bleach', 'Inuyasa']
keywords = []

timeframes = ['today 5-y', 'today 12-m',
              'today 3-m', 'today 1-m']
cat = '0'
geo = 'US', 'FR', 'ID'
gprop = ''


# Interest by region
def interest_by_region():
    pytrends.build_payload(all_keywords,
                           cat,
                           timeframes[1],
                           geo[2],
                           gprop)

    data = pytrends.interest_by_region(resolution='REGION',
                                       inc_low_vol=True,
                                       inc_geo_code=True)
    for kw in all_keywords:
        print(kw)
        data = data.sort_values(by=kw, ascending=False)
        print(data.head())
        print('')

interest_by_region()