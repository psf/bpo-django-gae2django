# Fake taskqueue API to make Rietveld happy.
# It should only use task queues for patch upload,
# which shouldn't ever happen in bugs.python.org

def add(*args, **kw):
    raise NotImplementedError("task queues")
