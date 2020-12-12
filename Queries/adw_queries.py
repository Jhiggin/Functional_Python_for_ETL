factsales_query = '''
SELECT *, YEAR(OrderDate) AS OrderYear, MONTH(OrderDate) AS OrderMonth, DAY(OrderDate) AS OrderDay
  FROM [AdventureWorksDW2017].[dbo].[FactInternetSales] 
'''