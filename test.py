import base64
import pickle

from django.contrib.sessions.models import Session
from django.utils.encoding import force_unicode



def decode_session_data(session_key):
    """Decode the data in a session object stored under ``session_key``.
    :param session_key: e.g. ``'1180b5ed42c2a3a5f217e35b755865da'`` 
    :return: decoded session data
    :rtype: :class:`dict`
    """
    session_obj = Session.objects.get(pk=session_key)
    session_data = force_unicode(session_obj.session_data)
    encoded_data = base64.decodestring(session_data)
    hash, pickled = encoded_data.split(':', 1)
    
    return pickle.loads(pickled)
session_key='6qdiwgzs6f5lj5qyi3chue3wvvqylem8'
decode_session_data(session_key)

