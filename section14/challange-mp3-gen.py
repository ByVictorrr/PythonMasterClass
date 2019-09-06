import os
import fnmatch
import id3reader_p3 as id3reader

def file_names(start_dir, exten_str):
	for path, directories, files in os.walk(start_dir):
		for fil in fnmatch.filter(files, "*.{}".format(exten_str)):
			yield fil



for f in file_names("music", "emp3"):
	try:
		id3r = id3reader.Reader(f)
		print("arist: {}, Album: {}, Track: {}, Song: {}".format(
		id3r.get_value("performer"),
		id3r.get_value("album"),
		id3r.get_value("track"),
		id3r.get_value("title")))
	except FileNotFoundError:
		print("File that caused an error is {}".format(f))


