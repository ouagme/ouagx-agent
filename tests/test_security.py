from ouagx_agent.security import Permission,PermissionEngine
def test_read_does_not_require_confirmation(): assert PermissionEngine().requires_confirmation(Permission.READ) is False
def test_write_requires_confirmation_by_default(): assert PermissionEngine().requires_confirmation(Permission.WRITE) is True
