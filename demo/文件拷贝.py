import os  
import os.path  
import shutil
import time
def copytree(src, dst, symlinks=False):  
    names = os.listdir(src)  
    if not os.path.isdir(dst):  
        os.makedirs(dst)  
          
    errors = []  
    for name in names:  
        srcname = os.path.join(src, name)  
        dstname = os.path.join(dst, name)  
        try:  
            if symlinks and os.path.islink(srcname):  
                linkto = os.readlink(srcname)  
                os.symlink(linkto, dstname)  
            elif os.path.isdir(srcname):  
                copytree(srcname, dstname, symlinks)  
            else:              
                # if os.path.isdir(dstname):  
                #     os.rmdir(dstname)  
                # elif os.path.isfile(dstname):  
                #     os.remove(dstname)  
                shutil.copy2(srcname, dstname)  
        except (IOError, os.error) as why:  
            errors.append((srcname, dstname, str(why)))  
        except OSError as err:  
            errors.extend(err.args[0])  
    try:  
        shutil.copystat(src, dst)  
    except WindowsError:  
        # can't copy file access times on Windows  
        pass  
    except OSError as why:  
        errors.extend((src, dst, str(why)))  
    if errors:  
        raise Error(errors)  


print("拷贝任务已启动")
copytree('D:/Code/ea_iboome_copy/iBoome.Portal/Controllers','D:/Code/ea_iboome/iBoome.Portal/Controllers')
print("拷贝Controller")
copytree('D:/Code/ea_iboome_copy/iBoome.Portal/Views','D:/Code/ea_iboome/iBoome.Portal/Views')
print("拷贝View")
copytree('D:/Code/ea_iboome_copy/iBoome.Portal/Models','D:/Code/ea_iboome/iBoome.Portal/Models')
print("拷贝Model")
copytree('D:/Code/ea_iboome_copy/iBoome.Portal/App_Start','D:/Code/ea_iboome/iBoome.Portal/App_Start')
copytree('D:/Code/ea_iboome_copy/iBoome.Portal/App_Start','D:/Code/ea_iboome/iBoome.Portal/App_Start')
copytree('D:/Code/ea_iboome_copy/iBoome.Portal/Assets/js','D:/Code/ea_iboome/iBoome.Portal/Assets/js')
copytree('D:/Code/ea_iboome_copy/iBoome.Portal/Assets/css','D:/Code/ea_iboome/iBoome.Portal/Assets/css')
copytree('D:/Code/ea_iboome_copy/iBoome.Portal/Com','D:/Code/ea_iboome/iBoome.Portal/Com')
copytree('D:/Code/ea_iboome_copy/iBoome.Portal/Filters','D:/Code/ea_iboome/iBoome.Portal/Filters')
print("拷贝其他类")
copytree('D:/Code/ea_iboome_copy/iBoome.Data/BLL','D:/Code/ea_iboome/iBoome.Data/BLL')
copytree('D:/Code/ea_iboome_copy/iBoome.Data/Entities','D:/Code/ea_iboome/iBoome.Data/Entities')
copytree('D:/Code/ea_iboome_copy/iBoome.Data/Model','D:/Code/ea_iboome/iBoome.Data/Model')
print("拷贝Data层")
copytree('D:/Code/ea_iboome_copy/iBoome.Extension/Com','D:/Code/ea_iboome/iBoome.Extension/Com')
copytree('D:/Code/ea_iboome_copy/iBoome.Extension/Entity','D:/Code/ea_iboome/iBoome.Extension/Entity')
print("拷贝Extension层")
print("ok")
time.sleep(10)
