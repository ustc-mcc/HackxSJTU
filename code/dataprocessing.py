# By USTC-MCC Group

import cv2
import os

def video2frame(videolist):
	if not os.path.exist(videolist):
		print "Videolist file does not exist!"
		eixt()
	with open(videolist) as f_vl:
		for line in f_vl:
			sline = line.split(' ')

def video2frame_single(filename, srcroot, dstroot):
	if not os.path.exist(filename):
		print "Error. Video file does not exist!"
		exit()
	vc = cv2.VideoCapture(os.path.join(srcroot, filename))
	if not vc.isOpened():
		print "Can not open this video named" + filename
		exit()
	notEnd = True
	frmIdx = 0
	dstroot_filename = os.path.join(dstroot, filename)
	if not os.path.exits(dstroot_filename:
		os.mkdir(dstroot_filename)

	wihle notEnd:
		notEnd, frame = cv.read()
		frmName = os.path.join(dstroot_filename, "%06d.jpg" % frmIdx)
		cv.imwrite(frmName, frame)
		frmIdx += 1
	vc.release

