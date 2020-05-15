#!/usr/bin/env python
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020

import cv2
#Import Neural Network Model
from funcoes.gan import DataLoader, DeepModel, tensor2im
#OpenCv Transform:
from funcoes.opencv_transform.mask_to_maskref import create_maskref
from funcoes.opencv_transform.maskdet_to_maskfin import create_maskfin
from funcoes.opencv_transform.dress_to_correct import create_correct
from funcoes.opencv_transform.nude_to_watermark import create_watermark

"""
run.py

This script manage the entire transormation.

Transformation happens in 6 phases:
	0: dress -> correct [opencv] dress_to_correct
	1: correct -> mask:  [GAN] correct_to_mask
	2: mask -> maskref [opencv] mask_to_maskref
	3: maskref -> maskdet [GAN] maskref_to_maskdet
	4: maskdet -> maskfin [opencv] maskdet_to_maskfin
	5: maskfin -> nude [GAN] maskfin_to_nude
	6: nude -> watermark [opencv] nude_to_watermark

"""

phases = ["dress_to_correct", "correct_to_mask", "mask_to_maskref", "maskref_to_maskdet", "maskdet_to_maskfin", "maskfin_to_nude", "nude_to_watermark"]

class Options():

	#Init options with default values
	def __init__(self):
	
		# experiment specifics
		self.norm = 'batch' #instance normalization or batch normalization
		self.use_dropout = False #use dropout for the generator
		self.data_type = 32 #Supported data type i.e. 8, 16, 32 bit

		# input/output sizes       
		self.batchSize = 1 #input batch size
		self.input_nc = 3 # of input image channels
		self.output_nc = 3 # of output image channels

		# for setting inputs
		self.serial_batches = True #if true, takes images in order to make batches, otherwise takes them randomly
		self.nThreads = 1 ## threads for loading data (???)
		self.max_dataset_size = 1 #Maximum number of samples allowed per dataset. If the dataset directory contains more than max_dataset_size, only a subset is loaded.
		
		# for generator
		self.netG = 'global' #selects model to use for netG
		self.ngf = 64 ## of gen filters in first conv layer
		self.n_downsample_global = 4 #number of downsampling layers in netG
		self.n_blocks_global = 9 #number of residual blocks in the global generator network
		self.n_blocks_local = 0 #number of residual blocks in the local enhancer network
		self.n_local_enhancers = 0 #number of local enhancers to use
		self.niter_fix_global = 0 #number of epochs that we only train the outmost local enhancer

		#Phase specific options
		self.checkpoints_dir = ""
		self.dataroot = ""

	#Changes options accordlying to actual phase
	def updateOptions(self, phase):

		if phase == "correct_to_mask":
			self.checkpoints_dir = "funcoes/checkpoints/cm.lib"

		elif phase == "maskref_to_maskdet":
			self.checkpoints_dir = "funcoes/checkpoints/mm.lib"

		elif phase == "maskfin_to_nude":
			self.checkpoints_dir = "funcoes/checkpoints/mn.lib"

# process(cv_img, mode)
# return:
# 	watermark image
def process(cv_img):

	#InMemory cv2 images:
	dress = cv_img
	correct = None
	mask = None
	maskref = None
	maskfin = None
	maskdet = None
	nude = None
	watermark = None

	for index, phase in enumerate(phases):


		print("Executing phase: " + phase) 
			
		#GAN phases:
		if (phase == "correct_to_mask") or (phase == "maskref_to_maskdet") or (phase == "maskfin_to_nude"):

			#Load global option
			opt = Options()

			#Load custom phase options:
			opt.updateOptions(phase)

			#Load Data
			if (phase == "correct_to_mask"):
				data_loader = DataLoader(opt, correct)
			elif (phase == "maskref_to_maskdet"):
				data_loader = DataLoader(opt, maskref)
			elif (phase == "maskfin_to_nude"):
				data_loader = DataLoader(opt, maskfin)
			
			dataset = data_loader.load_data()
			
			#Create Model
			model = DeepModel()
			model.initialize(opt)

			#Run for every image:
			for i, data in enumerate(dataset):

				generated = model.inference(data['label'], data['inst'])

				im = tensor2im(generated.data[0])

				#Save Data
				if (phase == "correct_to_mask"):
					mask = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)

				elif (phase == "maskref_to_maskdet"):
					maskdet = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)

				elif (phase == "maskfin_to_nude"):
					nude = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)

		#Correcting:
		elif (phase == 'dress_to_correct'):
			correct = create_correct(dress)

		#mask_ref phase (opencv)
		elif (phase == "mask_to_maskref"):
			maskref = create_maskref(mask, correct)

		#mask_fin phase (opencv)
		elif (phase == "maskdet_to_maskfin"):
			maskfin = create_maskfin(maskref, maskdet)

		#nude_to_watermark phase (opencv)
		elif (phase == "nude_to_watermark"):
			watermark = create_watermark(nude)

	return watermark