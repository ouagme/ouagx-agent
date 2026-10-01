from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from .config import Config
from .ai import AIClient
from .agent import Agent
from .security import PermissionEngine
from .audit import AuditLog
from .memory import Memory
console=Console()
def main():
    c=Config(); audit=AuditLog(c.db_path); memory=Memory(c.db_path); agent=Agent(AIClient(c),PermissionEngine(c.confirm_write,c.confirm_privileged,c.confirm_dangerous),audit,memory)
    console.print(Panel.fit('[bold cyan]OUAGx Agent[/bold cyan]\nTerminal Computer & Network Assistant\nType help or exit.'))
    while True:
        try: text=console.input('[bold green]ouagx>[/bold green] ').strip()
        except (EOFError,KeyboardInterrupt): print(); break
        if not text: continue
        if text.lower() in {'exit','quit'}: break
        if text.lower()=='help': console.print('Commands: help, system, network, logs, exit. Other text goes to the AI.'); continue
        if text.lower()=='system': from .tools.system import system_info; console.print(system_info()); continue
        if text.lower()=='network': from .tools.system import network_info; console.print(network_info()); continue
        if text.lower()=='logs':
            t=Table('Time','Action','Permission','Status'); [t.add_row(*[str(x) for x in row[:4]]) for row in audit.recent()]; console.print(t); continue
        try: console.print(agent.handle(text))
        except Exception as e: console.print(f'[red]Error:[/red] {e}')
