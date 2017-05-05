# By USTC-MCC Group

import cv2
import os
import sys

def video2frame(videolist):
	if not os.path.exist(videolist):
		print "Videolist file does not exist!"
		eixt()
	with open(videolist) as f_vl:
		for line in f_vl:
			sline = line.split(' ')

def video2frame_single(filename, srcroot, dstroot):
	srcroot_filename = os.path.join(srcroot, filename)
	if not os.path.exists(srcroot_filename):
		print "Error. Video file does not exist!"
		sys.exit()
	vc = cv2.VideoCapture(srcroot_filename)
	if not vc.isOpened():
		print "Can not open this video named " + srcroot_filename
		sys.exit()
	notEnd = True
	frmIdx = 0
	dstroot_filename = os.path.join(dstroot, filename)
	if not os.path.exists(dstroot_filename):
		os.mkdir(dstroot_filename)

	while notEnd:
		notEnd, frame = cv.read()
		frmName = os.path.join(dstroot_filename, "%06d.jpg" % frmIdx)
		cv.imwrite(frmName, frame)
		frmIdx += 1
	vc.release


if __name__ == '__main__':
    video2frame_single('sr_video_data/1-low.mp4', '../data', '../data')
