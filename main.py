import sys
import controller as ct

args = sys.argv

data = ct.extractCSV(args[1])

excellRes = ct.intoExcel(data, args[2])

