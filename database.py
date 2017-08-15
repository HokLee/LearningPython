
import pyodbc
import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import  datetime
from aiohttp import web

print('cat '*20)

def index(request):
    return web.Response(body=b'<h1>啊</h1>'
                             b'Last name:'
                             b'<input type="text" name="lastname">'
                             b'<input type="submit" value="Submit">',content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=GD-XX-M7100Z\MSSQLSERVER2012;DATABASE=精准扶贫;UID=sa;PWD=123456')
#;UID=sa;PWD=123456'
cursor = cnxn.cursor()
#for row in cursor.execute("select * from dbo.非精准扶贫"):
#for row in cursor.execute("select @@VERSION"):
    #print(row)
