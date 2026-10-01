from enum import Enum
from dataclasses import dataclass
class Permission(str, Enum):
    READ="READ"
    WRITE="WRITE"
    PRIVILEGED="PRIVILEGED"
    DANGEROUS="DANGEROUS"
@dataclass
class PermissionEngine:
    confirm_write: bool=True
    confirm_privileged: bool=True
    confirm_dangerous: bool=True
    def requires_confirmation(self,p):
        return (p==Permission.WRITE and self.confirm_write) or (p==Permission.PRIVILEGED and self.confirm_privileged) or (p==Permission.DANGEROUS and self.confirm_dangerous)
    def authorize(self,p,description):
        if not self.requires_confirmation(p): return True
        return input(f"\n[OUAGx] {p.value}: {description}\nConfirm? [y/N]: ").strip().lower() in {"y","yes"}
