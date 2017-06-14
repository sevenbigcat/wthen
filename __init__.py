from .runner import *

def run_all(file, scope=None):
    runner = RuleRunner()
    return runner.run_file(file, scope = scope)

def run(text, scope=None):
    runner = RuleRunner()
    return runner.run_text(text, scope = scope)
