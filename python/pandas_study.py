#!/usr/bin/python
#-*- encoding: utf-8 -*-

import pandas as pd
import pprint
import sys

if sys.version_info.major < 3:
    print( 'Upgrade to Python 3' )
    exit(1)

pp = pprint.PrettyPrinter(indent=2)

if __name__ == "__main__":

    #case 01
    #fruits = pd.DataFrame( [[30, 21]], columns=['Apples', 'Bananas'] )
    #pp.pprint( fruits )


    #case 02
    contents = pd.read_csv('./winemag-data-130k-v2-cut50.csv', index_col=0)
    #pp.pprint( contents.head() )

    #temp = contents.loc[ [1,2,3,5,8] ]
    #pp.pprint( temp )

    #temp = contents.loc[ [0,1,10], ['country', 'province', 'region_1', 'region_2'] ]
    #pp.pprint( temp )

    #temp1 = contents.loc[:10]
    #temp2 = contents.iloc[:10]
    #print( "loc[:10]  count = %s" % len(temp1) )
    #print( "iloc[:10] count = %s" % len(temp2) )

    #temp = contents[ contents.country == 'Italy' ]
    #pp.pprint( temp )

    temp = contents.loc[ (contents.country.isin(['Italy', 'New Zealand'])) & (contents.points >= 87) ]
    pp.pprint( temp )



    exit(0)
