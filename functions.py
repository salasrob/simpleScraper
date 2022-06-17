import os
import sys


# contains all functions

def create_directory(directory_name):
	if not os.path.exists(directory_name):
		os.makedirs(directory_name)



def create_new_file(path):
	file = open(path,'w')
	file.write("")
	file.close()


def write_to_file(path,data):
	with open(path, 'a') as file:
		file.write(data + '\n')


def clear_file(path):
	file = open(path, 'w')
	file.close()


def does_file_exist(path):
	return os.path.isfile(path)


def read_data(path):
	with open(path, 'rt') as file:
		for line in file:
			print(line.replace("\n",""))

def read_lines(path,lines):
	with open(path, 'rt') as file:
		current_line = 0
		for line in file:
			if current_line == lines:
				break
			current_line = current_line + 1
			print(line.replace("\n",""))