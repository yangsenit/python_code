import os
import cv2
pppath=os.getcwd()
print  pppath
count=0
wp='../image/'

ppath=os.listdir(pppath)
for path in ppath:
        path=pppath+'/'+path
        if os.path.isdir(path):
                filelist=os.listdir(path)
                for filename in filelist:
                        filename=path+'/'+filename
                        img=cv2.imread(filename,0)
                        count=count+1
                        des=wp+str(count)+'.jpg'
                        cv2.imwrite(des,img)
