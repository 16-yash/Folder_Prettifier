# """
# These Program pretify the perticular folder
# by 
# 1) changing first letter of file to capital
# 2) all jpg file in the folder is rename to 1jpg , 2jpg etc

#  """
import  os
def soldier(path,file,format):
    i=1
    os.chdir(path)
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())

        if os.path.splitext(file)[1] ==format:
            os.rename(file,f"{i}{format}")
            i+=1
soldier(r"C:\Users\VARDAYNI INFOTECH\Desktop\testing",r"C:\Users\VARDAYNI INFOTECH\Desktop\testing\book_record.txt",".png")

    






 