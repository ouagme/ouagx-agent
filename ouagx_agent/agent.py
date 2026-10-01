from .security import Permission
from .tools import filesystem,system,network,shell
class Agent:
    def __init__(self,ai,permissions,audit,memory): self.ai,self.permissions,self.audit,self.memory=ai,permissions,audit,memory
    def execute_tool(self,tool,args,permission,reason):
        p=Permission(permission)
        if not self.permissions.authorize(p,reason): self.audit.log(tool,permission,"denied",reason); return {"error":"Operation cancelled by user."}
        try:
            f={"system.info":system.system_info,"network.info":system.network_info,"network.reachable":network.reachable,"network.ping":network.ping,"filesystem.list":filesystem.list_files,"filesystem.read":filesystem.read_text,"filesystem.mkdir":filesystem.create_directory,"filesystem.write":filesystem.create_text_file,"filesystem.copy":filesystem.copy_path,"filesystem.zip":filesystem.zip_directory,"shell.run":shell.run_approved}[tool]; result=f(**args); self.audit.log(tool,permission,"success",str(result)[:2000]); return result
        except Exception as e: self.audit.log(tool,permission,"error",str(e)); return {"error":str(e)}
    def handle(self,text):
        r=self.ai.chat(text)
        if r.get("type")=="message": return r.get("content","")
        if r.get("type")=="tool": return f"Tool result:\n{self.execute_tool(r['tool'],r.get('arguments',{}),r.get('permission','READ'),r.get('reason','AI requested an operation'))}"
        return str(r)
