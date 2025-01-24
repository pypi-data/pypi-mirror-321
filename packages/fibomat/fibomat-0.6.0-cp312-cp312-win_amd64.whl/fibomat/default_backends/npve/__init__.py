from fibomat.default_backends.npve.npve_txt import NPVETxt
from fibomat.default_backends.npve.step_and_repeat import StepAndRepeatBackend
from fibomat.default_backends.npve.step_and_repeat.npve_mill import NPVEMill
from fibomat.backend import registry

registry.register(NPVETxt, NPVETxt.name)
registry.register(StepAndRepeatBackend, StepAndRepeatBackend.name)

__all__ = ["NPVETxt", "StepAndRepeatBackend", "NPVEMill"]
