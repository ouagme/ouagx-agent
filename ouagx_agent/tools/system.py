import os,platform,socket,psutil,time
def system_info():
    return {"os":platform.platform(),"hostname":socket.gethostname(),"python":platform.python_version(),"cpu_percent":psutil.cpu_percent(interval=.3),"ram_percent":psutil.virtual_memory().percent,"disk_percent":psutil.disk_usage(os.path.abspath(os.sep)).percent,"uptime_seconds":int(time.time()-psutil.boot_time())}
def network_info():
    return {n:[{"family":str(a.family),"address":a.address,"netmask":a.netmask} for a in ads] for n,ads in psutil.net_if_addrs().items()}
