# Form implementation generated from reading ui file 'MaxImporterBVH.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
# 3dsMax 2015,2016,2017
import sys
from PySide import QtCore#, QtGui
from os import path

from PySide.QtCore import Qt,QSize
from PySide.QtGui import QApplication,QLineEdit,QSpinBox,QDialog,QVBoxLayout,QPushButton,QLabel,QHBoxLayout,QFileDialog

import MaxPlus

temp_path = r'D:\Git_NDTools_self\Dev_Channel\bvh-python'
if not temp_path in sys.path:
	sys.path.append(temp_path)

from bvh import Bvh

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s
try:
	_encoding = QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QApplication.translate(context, text, disambig)

class SuperQLineEdit(QLineEdit):
	def focusInEvent(self, event):
		MaxPlus.CUI.DisableAccelerators()
		super(SuperQLineEdit, self).focusInEvent(event)

	def focusOutEvent(self, event):
		MaxPlus.CUI.EnableAccelerators()
		super(SuperQLineEdit, self).focusOutEvent(event)

class SuperQSpinBox(QSpinBox):
	def focusInEvent(self, event):
		MaxPlus.CUI.DisableAccelerators()
		super(SuperQSpinBox, self).focusInEvent(event)

	def focusOutEvent(self, event):
		MaxPlus.CUI.EnableAccelerators()
		super(SuperQSpinBox, self).focusOutEvent(event)

class UI_import_bvh(QDialog):

	def __init__(self, parent=None):
		QDialog.__init__(self)
		#self.resize(400, 300)
		self.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.WindowCloseButtonHint)

		self.bvh_file = None
		self.mocap = None
		self.file_path = None
		self.setupUi()

	def setupUi(self):

		self.resize(300, 180)

		self.verticalLayout = QVBoxLayout(self)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

		self.lineEdit = SuperQLineEdit(self)
		#self.lineEdit = QtGui.QLineEdit(self)

		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.horizontalLayout.addWidget(self.lineEdit)
		self._open_file = QPushButton(self)
		self._open_file.setMaximumSize(QSize(50, 16777215))
		self._open_file.setObjectName(_fromUtf8("_open_file"))
		self.horizontalLayout.addWidget(self._open_file)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

		#时间偏移
		self.label = QLabel(self)
		self.label.setMaximumSize(QSize(60, 16777215))
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout_2.addWidget(self.label)

		#self._time_offest = QtGui.QSpinBox(self)
		self._time_offest = SuperQSpinBox(self)
		self._time_offest.setRange(-9999,99999)
		self._time_offest.setMinimumSize(QSize(100, 0))
		self._time_offest.setObjectName(_fromUtf8("_time_offest"))
		self.horizontalLayout_2.addWidget(self._time_offest)

		self.label_001 = QLabel(self)
		self.label.setObjectName(_fromUtf8("label_001"))
		self.label_001.setMaximumSize(QSize(60, 16777215))
		self.horizontalLayout_2.addWidget(self.label_001)

		self._scale_ = SuperQSpinBox(self)
		self._scale_.setRange(1,99999)
		self._scale_.setValue(100)
		self._scale_.setMinimumSize(QSize(100, 0))
		self._scale_.setObjectName(_fromUtf8("_scale_"))
		self.horizontalLayout_2.addWidget(self._scale_)


		self.verticalLayout.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_3 = QHBoxLayout()
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.label_2 = QLabel(self)
		self.label_2.setMaximumSize(QSize(35, 16777215))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.horizontalLayout_3.addWidget(self.label_2)

		#self._time_start = QtGui.QSpinBox(self)
		self._time_start = SuperQSpinBox(self)
		self._time_start.setRange(0,99999)


		self._time_start.setMinimumSize(QSize(80, 0))
		self._time_start.setObjectName(_fromUtf8("_time_start"))
		self.horizontalLayout_3.addWidget(self._time_start)
		self.label_3 = QLabel(self)
		self.label_3.setMaximumSize(QSize(35, 16777215))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.horizontalLayout_3.addWidget(self.label_3)

		#self._time_end = QtGui.QSpinBox(self)
		self._time_end = SuperQSpinBox(self)
		self._time_end.setRange(0,99999)


		self._time_end.setMinimumSize(QSize(80, 0))
		self._time_end.setObjectName(_fromUtf8("_time_end"))
		self.horizontalLayout_3.addWidget(self._time_end)
		self.verticalLayout.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_6 = QHBoxLayout()
		self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
		self.label_7 = QLabel(self)
		self.label_7.setMaximumSize(QSize(35, 16777215))
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.horizontalLayout_6.addWidget(self.label_7)
		self._label_frameFPS = QLabel(self)
		self._label_frameFPS.setObjectName(_fromUtf8("_label_frameFPS"))
		self.horizontalLayout_6.addWidget(self._label_frameFPS)
		self.label_6 = QLabel(self)

		self.label_6.setObjectName(_fromUtf8("label_6"))
		self.horizontalLayout_6.addWidget(self.label_6)
		self._label_frameCount = QLabel(self)
		self._label_frameCount.setObjectName(_fromUtf8("_label_frameCount"))
		self.horizontalLayout_6.addWidget(self._label_frameCount)
		self.verticalLayout.addLayout(self.horizontalLayout_6)
		self.horizontalLayout_4 = QHBoxLayout()
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.label_4 = QLabel(self)

		self.label_4.setMaximumSize(QSize(60, 16777215))
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.horizontalLayout_4.addWidget(self.label_4)

		#self._namespace = QtGui.QLineEdit(self)
		self._namespace = SuperQLineEdit(self)


		self._namespace.setObjectName(_fromUtf8("_namespace"))
		self.horizontalLayout_4.addWidget(self._namespace)
		self.verticalLayout.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_5 = QHBoxLayout()
		self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
		self.do_creat_SK = QPushButton(self)
		self.do_creat_SK.setObjectName(_fromUtf8("do_creat_SK"))
		self.horizontalLayout_5.addWidget(self.do_creat_SK)
		self.label_5 = QLabel(self)
		self.label_5.setMinimumSize(QSize(35, 0))
		self.label_5.setMaximumSize(QSize(45, 16777215))
		self.label_5.setAlignment(Qt.AlignCenter)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.horizontalLayout_5.addWidget(self.label_5)
		self.do___import_anim = QPushButton(self)
		self.do___import_anim.setObjectName(_fromUtf8("do___import_anim"))
		self.horizontalLayout_5.addWidget(self.do___import_anim)
		self.verticalLayout.addLayout(self.horizontalLayout_5)

		self.setLayout(self.verticalLayout)
		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self):
		self.setWindowTitle(_translate("Form", "Form", None))

		self.setWindowTitle(_translate("Dialog","导入BVH 1.0", None))

		self._open_file.setText(_translate("Form", ".BVH", None))
		self._open_file.clicked.connect(self.__get_bvh_file)

		self.label.setText(_translate("Form", "时间偏移:", None))
		self.label_001.setText(_translate("Form","缩放因子:",None))

		self.label_2.setText(_translate("Form", "起始:", None))
		self.label_3.setText(_translate("Form", "结束", None))
		self.label_7.setText(_translate("Form", "帧率：", None))
		self._label_frameFPS.setText(_translate("Form", "0", None))
		self.label_6.setText(_translate("Form", "动画帧数:", None))
		self._label_frameCount.setText(_translate("Form", "0", None))
		self.label_4.setText(_translate("Form", "命名空间：", None))

		self.do_creat_SK.setText(_translate("Form", "创建骨架", None))
		self.do_creat_SK.clicked.connect(self.__create_new_skeleton)

		#self.label_5.setText(_translate("Form", "Help", None))
		
		self.label_5.setText(u"<a href = 'http://101.34.112.80/pages/b5c64f/'>Help</a>")
		
		self.label_5.setOpenExternalLinks(True)

		self.do___import_anim.setText(_translate("Form", "导入动画", None))
		self.do___import_anim.clicked.connect(self.__import_anim)

		self._namespace.setText("BvH")

	def __get_bvh_file(self):
		thefile = QFileDialog.getOpenFileName(self,u"打开 bvh 文件",self.file_path,"*.bvh")

		if thefile :
			if len(thefile[0]) > 1:
				self.lineEdit.setText(thefile[0])
				self.bvh_file = thefile[0]
				print(thefile[0])

				self.file_path = path.split(thefile[0])
				self.file_path = self.file_path[0]

				fps,frame_count = self.__read_bvh_frame_count(self.bvh_file)

				if fps > 0 :
					self.mocap = None
					self._label_frameFPS.setText(str(fps))
				else:
					self.bvh_file = None
					self._label_frameFPS.setText("")

				if frame_count > 0 :
					self.mocap = None
					self._label_frameCount.setText(str(frame_count))
					self._time_end.setValue(frame_count)
				else:
					self.bvh_file = None
					self.mocap = None
					self._label_frameCount.setText("")

	def __open_bvh_file(self):
		if self.bvh_file:
			try:
				with open(self.bvh_file) as f:
					self.mocap = Bvh(f.read())

			except BaseException:
				self.mocap = None

	def __create_new_skeleton(self):
		if not self.mocap :
			self.__open_bvh_file()

			self.__creat_BVH_skeleton(self.mocap,self._namespace.text())
			#print(self._namespace.text())
		else:
			self.__creat_BVH_skeleton(self.mocap,self._namespace.text())
			#print("self.mocap")
	def __import_anim(self):
		if not self.mocap :
			self.__open_bvh_file()
			self.__add_skeletion_anim(self.mocap,self._namespace.text(),self._time_start.value(),self._time_end.value(),self._time_offest.value())
		else:
			self.__add_skeletion_anim(self.mocap,self._namespace.text(),self._time_start.value(),self._time_end.value(),self._time_offest.value())

	#@staticmethod
	#@classmethod
	def __read_bvh_frame_count(self,file_name):
		#动画帧数
		nframes = None
		#动画帧率
		frame_time = -2
		#https://www.jianshu.com/p/fbda66b5f102?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
		#读取文件换行符问题
		with open(file_name,'rU') as f:
			# Check to see if the file is valid (sort of)
			if not f.next().startswith("HIERARCHY"):
				print("No valid .bvh file selected.")
				return -1,-1
			for line in f:
				line = line.replace("	"," ") # force spaces

				if "Frames" in line:
					data = line.split(" ")
					if len(data) > 0:
						try:
							frame_time = float(data[-1].rstrip())
							frame_time = int(frame_time)

						except BaseException:
							frame_time = -2

				if "Frame Time" in line:
					data = line.split(" ")
					if len(data) > 0:
						try:
							#print(data[-1].rstrip())
							nframes = float(data[-1].rstrip())
							nframes *= 100
							nframes = int(nframes) * 10
							return nframes,frame_time

						except BaseException:
							return -3,-1
					else:
						return -4,-1

		return -5,-1				
	def try_max_namespace_root(self,namespace):
		pass

	def __creat_BVH_skeleton(self,mocap,namespace):
		#场景root
		scene_root_text = "scene_root = point name:\"{}\"".format(namespace)
		scene_root_text += ";scene_root.rotation.controller.X_Rotation = 90"
		MaxPlus.Core.EvalMAXScript(scene_root_text)

		for i in mocap.get_joints():
			text = "joins_ = point name:\"{}:{}\" \n".format(namespace,i.name)
			MaxPlus.Core.EvalMAXScript(text)
			#print("{}-- {}".format(i.parent , len(i.parent)))
			if len(i.parent) > 0 :
				try:
					valeu = mocap.joint_offset(i.name)
					x =valeu[0] * (self._scale_.value() * 0.01) 
					y =valeu[1] *(self._scale_.value() * 0.01) 
					z =valeu[2] * (self._scale_.value() * 0.01) 
					#print("{} -> {} * {}".format(i.name, valeu,(valeu[0]*self._scale_.value() * 0.01)))
					text = "joins_.parent = getnodebyname \"{}:{}\"".format(namespace,i.parent.name)
					MaxPlus.Core.EvalMAXScript(text)
					#xyz
					text = "joins_.position.controller.value = [{},{},{}] \n".format(x,y,z)
					text += "addNewKey joins_.transform.controller 0"
					MaxPlus.Core.EvalMAXScript(text)

				except BaseException :
					pass 
			else:
				valeu = mocap.joint_offset(i.name)
				print("{} -> {}".format(i.name, valeu))
				x =valeu[0] * (self._scale_.value() * 0.01) 
				y =valeu[1] *(self._scale_.value() * 0.01) 
				z =valeu[2] * (self._scale_.value() * 0.01) 
				
				text = "joins_.parent = getnodebyname \"{}\";".format(namespace)
				text += "joins_.position.controller.value = [{},{},{}] ;".format(x,y,z)
				text += "addNewKey joins_.transform.controller 0"
				MaxPlus.Core.EvalMAXScript(text)

	def __add_skeletion_anim(self,mocap,namespace,frame_start=1,frame_end=None,time_offset=0):
		#设置根骨骼的位移动画
		root = mocap.get_joints_names()[0]

		if frame_end > mocap.nframes :
			frame_end = mocap.nframes

		if not frame_end :
			frame_end = mocap.nframes

		print("root {} == frame_start {} --> frame_end {}".format(root,frame_start,frame_end))
		for o in range(frame_start,frame_end):
			x = mocap.frame_joint_channel(o, root, 'Xposition')
			y = mocap.frame_joint_channel(o, root, 'Yposition')
			z = mocap.frame_joint_channel(o, root, 'Zposition')

			x *= (self._scale_.value() * 0.01) 
			y *= (self._scale_.value() * 0.01) 
			z *= (self._scale_.value() * 0.01) 

			text = "animate true(at time {}(joins_ = getNodeByName \"{}:{}\";".format((o+time_offset),namespace,root )

			text += "if isValidNode joins_ do (joins_.position.controller.X_Position = {};".format(x)
			text += "joins_.position.controller.Y_Position = {};".format(y)
			text += "joins_.position.controller.Z_Position = {};".format(z)

			text += ")))"
			MaxPlus.Core.EvalMAXScript(text)



		#设置 旋转动画
		for i in mocap.get_joints():
			for o in range(frame_start,frame_end):
				x = mocap.frame_joint_channel(o, i.name, 'Zrotation')
				y = mocap.frame_joint_channel(o, i.name, 'Yrotation')
				z = mocap.frame_joint_channel(o, i.name, 'Xrotation')

				text = "animate true(at time {}(joins_ = getNodeByName \"{}:{}\";".format((o+time_offset),namespace,i.name )

				text += "if isValidNode joins_ do (joins_.rotation.controller.X_Rotation = {};".format(z)

				text += "joins_.rotation.controller.Y_Rotation = {};".format(y)

				text += "joins_.rotation.controller.Z_Rotation = {};".format(x)

				text += ")))"
				MaxPlus.Core.EvalMAXScript(text)





if __name__ == "__main__":
	app = QApplication.instance()
	uiapp = UI_import_bvh()
	uiapp.show()
	#a = r"D:\Git_NDTools_self\Dev_Channel\bvh-python\tests\archery.bvh"
	#print(UI_import_bvh.__read_bvh_frame_count(a))


