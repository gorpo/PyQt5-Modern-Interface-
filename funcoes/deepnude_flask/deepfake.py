# coding=utf-8
import cv2
import os
import sys
import subprocess
from run import process
import argparse



def main(inputpath,out):
	nome = out.strip('.jpg')
	outputpath = f'funcoes/deepnude_flask/images/{nome}_renderizada.jpg'
	if isinstance(inputpath, list):
		for item in inputpath:
			watermark = deep_nude_process(item)
			cv2.imwrite("output_"+item, watermark)
	else:
		watermark = deep_nude_process(inputpath)
		cv2.imwrite(outputpath, watermark)



def deep_nude_process(item):
    #print('Processing {}'.format(item))
    dress = cv2.imread(item)
    h = dress.shape[0]
    w = dress.shape[1]
    dress = cv2.resize(dress, (512,512), interpolation=cv2.INTER_CUBIC)
    watermark = process(dress)
    watermark = cv2.resize(watermark, (w,h), interpolation=cv2.INTER_CUBIC)
    return watermark



if __name__ == '__main__':
	#parser = argparse.ArgumentParser(description="simple deep nude script tool")
	#parser.add_argument("-i", "--input", action="store", nargs="*", default="input.png",					help="Use to enter input one or more files's name")
	#parser.add_argument("-o", "--output", action="store", default="output.png",						help="Use to enter output file name")
	#inputpath, outputpath= parser.parse_args().input, parser.parse_args().output
	#main(inputpath, outputpath)

	inputpath = 'images/file.jpg'
	outputpath = 'images/renderizada.jpg'
	out = ''
	main(inputpath,out)
