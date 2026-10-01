import os,subprocess,platform
def run_approved(command,timeout=30):
    sh="powershell" if platform.system().lower()=="windows" else "/bin/bash"; args=[sh,"-NoProfile","-Command",command] if sh=="powershell" else [sh,"-lc",command]
    p=subprocess.run(args,capture_output=True,text=True,timeout=timeout,cwd=os.getcwd()); return {"returncode":p.returncode,"stdout":p.stdout[-10000:],"stderr":p.stderr[-10000:]}
