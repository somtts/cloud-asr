from lib import create_master
import os


master = create_master(os.environ['WORKER_ADDR'], os.environ['FRONTEND_ADDR'])
master.run()
