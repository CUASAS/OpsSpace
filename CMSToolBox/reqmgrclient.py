"""
Uses the `reqmgr2 APIs <https://github.com/dmwm/WMCore/wiki/reqmgr2-apis>`_
to get information about workflows.

:author: Daniel Abercrombie <dabercro@mit.edu>
"""

from .webtools import get_json

def get_workflow_parameters(workflow):
    """
    Get the workflow parameters from ReqMgr2

    :param str workflow: The name of the workflow
    :returns: Parameters for the workflow
    :rtype: dict
    """

    result = get_json('cmsweb.cern.ch',
                      '/reqmgr2/data/request',
                      params={'name': workflow},
                      use_https=True, use_cert=True)

    for params in result['result']:
        for key, item in params.iteritems():
            if key == workflow:
                return item

    return {}