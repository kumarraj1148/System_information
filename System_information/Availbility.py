import psutil


class Phyiscal_Memory_status:

    def __init__(self):
        print("Checking the physical memory status")
        self.status=psutil.virtual_memory()


obj=Phyiscal_Memory_status()


print("Total RAM status:",obj.status[0])
print("Used RAM status:",obj.status[3])
print("Free of RAM:",obj.status[4])
print("Percent of RAM:",obj.status[2])