import csv

inputFilename = "OtwartyWroclaw_rozklad_jazdy_GTFS/routes.txt"
outputFilname = "routes-wroclaw.csv"

with open(inputFilename) as f_in, open(outputFilname, 'w') as f_out:
    header = f_in.readline()
    f_out.write("route_id,route_short_name,route-desc\n")

    for line in f_in:
        splitted = line.split(',')
        print(splitted)
        f_out.write(splitted[0]+','+splitted[2]+','+splitted[4]+'\n')

