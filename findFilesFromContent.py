import os
import sys
import threading

class Gf():
	def getFiles(self, path, text, ext=''):
		findedFiles = []
		#All files in directory and nested
		files = list(os.walk(path))
		#cp866 decode text
		word = text.encode('utf-8').decode('cp866')

		for i in files:
			for j in i[2]:
				filePath = i[0].replace('\\', '/') + '/' + j

				try:
					if sys.argv[0].replace('\\', '/') != filePath:
						if j.endswith(ext):
							if not word in filePath:
								if not j.startswith('.'):
									#Open file to read
									with open(filePath, 'r', encoding='cp866') as fileText:
										if word.lower() in fileText.read().lower():
											findedFiles.append(filePath)
				
							else:
								#if in file name there is finded text
								findedFiles.append(filePath)
				except:
					pass

		return findedFiles