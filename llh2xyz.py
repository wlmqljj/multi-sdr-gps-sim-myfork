import csv
import math

# Earth constant parameters
WGS84_A = 6378137.0
WGS84_F = 1 / 298.257223563
WGS84_E = math.sqrt(2 * WGS84_F - WGS84_F**2)

height = 0

def geodetic_to_ecef(lat, lon, h):
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    sin_lat = math.sin(lat_rad)
    cos_lat = math.cos(lat_rad)
    N = WGS84_A / math.sqrt(1 - WGS84_E * WGS84_E * sin_lat * sin_lat)

    x = (N + h) * cos_lat * math.cos(lon_rad)
    y = (N + h) * cos_lat * math.sin(lon_rad)
    z = (N * (1 - WGS84_E * WGS84_E) + h) * sin_lat

    return x, y, z

input_filename = 'input.csv'
output_filename = 'output.csv'

with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)

    # Optional headers
    # csv_writer.writerow(['time', 'x', 'y', 'z'])

    time = 0.0

    for row in csv_reader:
        # clean headers
        lat_str, lon_str = row[0].lstrip('\ufeff'), row[1]
        lat, lon = map(float, (lat_str, lon_str))

        x, y, z = geodetic_to_ecef(lat, lon, height)

        csv_writer.writerow([f'{time:.1f}', f'{x:.6f}', f'{y:.6f}', f'{z:.6f}'])

        time += 0.1

print("success!")
