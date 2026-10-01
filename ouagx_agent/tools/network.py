import socket,subprocess,platform
def reachable(host,port=None,timeout=2):
    if port is not None:
        try:
            with socket.create_connection((host,int(port)),timeout=timeout): return {"host":host,"port":port,"reachable":True}
        except OSError as e: return {"host":host,"port":port,"reachable":False,"error":str(e)}
    try: socket.gethostbyname(host); return {"host":host,"reachable":True}
    except OSError as e: return {"host":host,"reachable":False,"error":str(e)}
def ping(host):
    flag="-n" if platform.system().lower()=="windows" else "-c"; p=subprocess.run(["ping",flag,"1",host],capture_output=True,text=True,timeout=5); return {"returncode":p.returncode,"output":p.stdout[-4000:] or p.stderr[-4000:]}
