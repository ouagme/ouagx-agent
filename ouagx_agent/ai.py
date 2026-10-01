import json,requests
SYSTEM_PROMPT='''You are OUAGx Agent, a local computer assistant. Use structured JSON tool calls only. Never invent results. Never request unauthorized access. Prefer read-only tools. Write, privileged and dangerous operations require host confirmation. Tools: system.info, network.info, network.reachable, network.ping, filesystem.list, filesystem.read, filesystem.mkdir, filesystem.write, filesystem.copy, filesystem.zip, shell.run. Return {"type":"message","content":"..."} or {"type":"tool","tool":"...","arguments":{},"permission":"READ|WRITE|PRIVILEGED|DANGEROUS","reason":"..."}.'''
class AIClient:
    def __init__(self,config): self.config=config
    def chat(self,user_text):
        if self.config.provider=="ollama":
            r=requests.post(f"{self.config.ollama_url}/api/chat",json={"model":self.config.ollama_model,"messages":[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":user_text}],"stream":False,"format":"json"},timeout=120); r.raise_for_status(); return json.loads(r.json()["message"]["content"])
        r=requests.post(f"{self.config.openai_base_url}/chat/completions",headers={"Authorization":f"Bearer {self.config.api_key}"},json={"model":self.config.openai_model,"messages":[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":user_text}],"response_format":{"type":"json_object"}},timeout=120); r.raise_for_status(); return json.loads(r.json()["choices"][0]["message"]["content"])
