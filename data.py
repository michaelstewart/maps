import json

def csv_to_json(file_name):
	f_in = open(file_name + '.csv');
	data = []
	for line in f_in.readlines():
		line = line.strip()
		line_list = line.split(',')
		if len(line_list) == 4:
			reading = {}
			reading['time'] = line_list[0]
			reading['latitude'] = float(line_list[1])
			reading['longitude'] = float(line_list[2])
			reading['temperature'] = float(line_list[3])
		data.append(reading)
	f_in.close()

	f_out = open(file_name + '.json', 'w')
	f_out.write(json.dumps(data))
	f_out.close()


if __name__ == '__main__':
	csv_to_json('data')