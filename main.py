import sys
import controller as ct

if len(sys.argv) != 3:
    print("Type: python main.py /dir/example.csv /dest/your_file.xlsx")
    sys.exit(1)

args = sys.argv[1:]

data = ct.extractCSV(args[0])
if data['status']:
    excellRes = ct.intoExcel(data['data'], args[1])
    print(excellRes)
else:
    print(data['message'])