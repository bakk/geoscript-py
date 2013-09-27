"""
The :mod:`workspace.sqlserver` module a workspace implementation based on the contents of a Sql Server database.
"""
from java.lang.System import getProperty as sysprop
from geoscript.workspace import Workspace
from org.geotools.data.sqlserver import SQLServerDataStoreFactory

class Sqlserver(Workspace):
  """
  A subclass of :class:`Workspace <geoscript.workspace.workspace.Workspace>` for a MS Sql Server database. Layers of the workspace correspond to tables in the database.

  *db* is the name of the database.

  *host* is the optional host name. Defaults to 'localhost'.

  *port* is the optional port the database is listening on as an ``int``. Defaults to 1433.

  *schema* is the optional database schema to connect to. If not specified 
  defaults to the same value as *value*

  *user* is the optional username to connect as. Defaults to the current user.

  *passwd* is the optional password to connect with.

  """

  def __init__(self, db, host='localhost', port=1433, schema=None,
               user=sysprop('user.name'), passwd=None, expose_pk=False, native_serialization=False):

    if schema is None:
      schema = user

    params = {'host': host, 'port': port,  'schema': schema, 'database': db,
              'user':user, 'passwd': passwd, 'Expose primary keys': expose_pk, 
              'dbtype': 'sqlserver', 'NATIVE_SERIALIZATION': native_serialization}
    
    Workspace.__init__(self, SQLServerDataStoreFactory(), params)
