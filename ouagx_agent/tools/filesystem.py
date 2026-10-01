from pathlib import Path
import shutil,zipfile
def list_files(path):
    p=Path(path).expanduser().resolve()
    if not p.exists(): raise FileNotFoundError(p)
    return [{"name":x.name,"type":"dir" if x.is_dir() else "file"} for x in p.iterdir()]
def read_text(path,max_chars=20000): return Path(path).expanduser().resolve().read_text(encoding="utf-8",errors="replace")[:max_chars]
def create_directory(path):
    p=Path(path).expanduser().resolve(); p.mkdir(parents=True,exist_ok=True); return str(p)
def create_text_file(path,content):
    p=Path(path).expanduser().resolve(); p.write_text(content,encoding="utf-8"); return str(p)
def copy_path(source,destination):
    s,d=Path(source).expanduser().resolve(),Path(destination).expanduser().resolve()
    shutil.copytree(s,d,dirs_exist_ok=True) if s.is_dir() else shutil.copy2(s,d); return str(d)
def zip_directory(source,destination):
    s,d=Path(source).expanduser().resolve(),Path(destination).expanduser().resolve()
    with zipfile.ZipFile(d,"w",zipfile.ZIP_DEFLATED) as z:
        for f in s.rglob("*"):
            if f.is_file(): z.write(f,f.relative_to(s.parent))
    return str(d)
