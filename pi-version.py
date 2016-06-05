import subprocess
import re

class PiModel:
	def __init__(self, revision, release_date, model, pcb_revision, memory):
		self.regex = '\A0*' + revision + '\Z'
		self.revision = revision
		self.release_date = release_date
		self.model = model
		self.pcb_revision = pcb_revision
		self.memory = memory

pi_models = [
	PiModel('Beta', "Q1 2012", "B (Beta)", " ?", "256 MB"),
	PiModel('2', "Q1 2012", "B", "1.0", "256 MB"),
	PiModel('3', "Q3 2012", "B (ECN0001)", "1.0", "256 MB"),
	PiModel('4', "Q3 2012", "B", "2.0", "256 MB"),
	PiModel('5', "Q4 2012", "B", "2.0", "256 MB"),
	PiModel('6', "Q4 2012", "B", "2.0", "256 MB"),
	PiModel('7', "Q1 2013", "A", "2.0", "256 MB"),
	PiModel('8', "Q1 2013", "A", "2.0", "256 MB"),
	PiModel('9', "Q1 2013", "A", "2.0", "256 MB"),
	PiModel('d', "Q4 2012", "B", "2.0", "512 MB"),
	PiModel('e', "Q4 2012", "B", "2.0", "512 MB"),
	PiModel('f', "Q4 2012", "B", "2.0", "512 MB"),
	PiModel('10', "Q3 2014", "B+", "1.0", "512 MB"),
	PiModel('11', "Q2 2014", "Compute Module", "1.0", "512 MB"),
	PiModel('12', "Q4 2014", "A+", "1.1", "256 MB"),
	PiModel('13', "Q1 2015", "B+", "1.2", "512 MB"),
	PiModel('14', "Q2 2014", "Compute Module", "1.0", "512 MB"),
	PiModel('15', " ?", "A+", "1.1", "256 MB"),
	PiModel('a01041', "Q1 2015", "2 Model B", "1.1", "1 GB"),
	PiModel('a21041', "Q1 2015", "2 Model B", "1.1", "1 GB"),
	PiModel('900092', "Q4 2015", "Zero", "1.2", "512 MB"),
	PiModel('900093', "Q2 2016", "Zero", "1.3", "512 MB"),
	PiModel('a02082', "Q1 2016", "3 Model B", "1.2", "1024 MB"),
	PiModel('a22082', "Q1 2016", "3 Model B", "1.2", "1024 MB"),
]

revision = subprocess.check_output("cat /proc/cpuinfo | grep 'Revision' | awk '{print $3}' | sed 's/^1000//'", stdin=subprocess.PIPE, shell=True ).strip()
model_found = False

for pi_model in pi_models:
	if (re.search(pi_model.regex, revision)):
		model_found = True
		print "You have a Raspberry Pi " + pi_model.model + ", released " + pi_model.release_date + " with " + pi_model.memory + " memory."
		
if not model_found:
	print "Your Raspberry Pi is revision " + revision + ", not really sure what that is. Most recent known version is Q1 2016."


	

