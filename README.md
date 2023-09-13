Problem Statemnt
Price Table
col1 > symbol
col2 and so on > date

Info Table 
col1 > symbol
numbers of share market
market cap(last col of prices)
ratios
summary/text/ABOUT


API
1)Index Genrator(array[stocks])
{
	var sum = get sum of market cap of all the stocks mentioned in this array
	key value pair
	key > stock (symbol)
	value > weight(sybol m cap/sum*100)
	
	return key value pair
	
}
// genrate porfolio
2)Invested_amount_in_index(key value pair index,money to invest)
{
	key value pair porfolio;
	for(i:index)
		porfolio.key = symbol;
		porfolio.no_of_shares = (invest*i.value/100)/stock_cmp;

	return portfolio;
}
@ovelloading
3)plot_chart(sybmol,time )
{
	//chart genrating librabry (need to do lot of R&D)
	return chart from today-time, today
	
}

3)plot_chart(sybmol,d1,d2 )
{
	//chart genrating librabry (need to do lot of R&D)
	return chart from d1, d2
}

4)All time high tell(listofstocks,p%,up)
{
	return listofstocks which are near p% of there maximum price
}
5)high tell(listofstocks,p%,up, timeframe)
{
	return listofstocks which are near p% of there maximum price in today-trimframe,today
}
6)All time high tell(listofstocks,p%,down)
{
	return listofstocks which are near p% of there lowest price
}
7)high tell(listofstocks,p%,up, timeframe)
{
	return listofstocks which are near p% of there lowest price in today-trimframe,today
}
8)get_fno_stocks()
{
	modify db of f&o;
	return listofstocks present in f&o;
}
9)tell market dolidays(today)
{
	return the list of holidays from today
}
10)is_holiday()
{
	return boll holday or not
}
11)recentholiday()
{
	return recent holdiay
}

-----------------------------------------------------------------------------------------------
Lisence fuctions
-----------------------------------------------------------------------------------------
Test a startegy
description of a satergy for testing 
startegy return a list of stocks and a time period
1)check_startergy(listof_stocks,dateofstart,dateend)
{
	for(i:list)
		//handel null pointer exception
		sum += cmp_today/price_dateof_start;

	return sum;
}
2)check_startergy(map_of_stocs_with_money,dateofstart,dateend)
{
	
	for(i:list)
		total_money += i.value
		//handel null pointer exception
		sum += cmp_today/price_dateof_start*i.value;

	return sum/total/money;
}

-----------------------------------------------------------------------------------------------------------------------
Algorithms
Algo_gernic_format(Listofstocsk)
{
	//Busissuess logic
	gives the stocsk to which that logic is applicable
	return list of stocks;
}
----------------------------------------------------------------------------------------------------------------------
Baskets
similar_stocks(stock_name)
{
	return list of stocks that show simialr moment to that stock_name;
}


---------------------------------------------------------------------------------------------------
Web Scrapper


get_concol(symbol)
{
	return last_four
}

get_anual_report(symbol)
{
	return last_four
}

get_news(symbol)
{
	returns the news of that stocks
}

get_news()
{
	return the genral news of what is happening
}

get_results()
{
	
}

get_dividents()
{
	
}

get_ipos()
{
	
}

get_mergers()
{
	
}

get_demerger()
{
	
}

----------------------------------------------------------------------------------------------------
NLP

analaze_anual_report(pdf)
{
	return summary
}

analaze_diff_anual_report(pdf,pdf)
{
	return dif_summary
}

analaze_concol(pdf)
{
	return summary
}


---------------------------------------------------------------------------------------------------------
Charts (web interface)

Plot charts() //drwable chart 



