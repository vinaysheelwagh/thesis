import shutil, os

dirList = []
for root, dir, file in os.walk('E:\\NCI\Thesis\\Dataset\\test\\xBD-test'):
	print(dir)
	dirList.append(dir)
print(dirList[0])	

for disaster in dirList[0]:
	for r, d, f in os.walk('E:\\NCI\Thesis\\Dataset\\test\\xBD-test\\'+disaster+'\\masks'):
		print(f)
		for file in f:
			shutil.copy('E:\\NCI\Thesis\\Dataset\\test\\xBD-test\\'+disaster+'\\masks\\'+file,'E:\\NCI\Thesis\\Dataset\\test\\xBD-test\\spacenet_gt_test\\labels')
			shutil.copy('E:\\NCI\Thesis\\Dataset\\test\\xBD-test\\'+disaster+'\\images\\'+file,'E:\\NCI\Thesis\\Dataset\\test\\xBD-test\\spacenet_gt_test\\images')

file1 = open("E:\\NCI\Thesis\\Dataset\\test\\xBD-test\\spacenet_gt_test\\dataset\\test.txt","a") 
for r, d, f in os.walk('E:\\NCI\Thesis\\Dataset\\test\\xBD-test\\spacenet_gt_test\\images'):
	for file in f:
		file1.writelines(file+"\n")
file1.close()