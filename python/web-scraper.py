#import urllib.request
from sqlalchemy import create_engine

#url_base = "https://serval.uvm.edu/~rgweb/batch/enrollment/curr_enroll_"

#for i in range(1995, 2021):
#    for j in [1, 6, 9]:
#        url_end = str(i) + "0" + str(j) + ".txt"
#        url = url_base + url_end
#        f = open("../data/" + url_end, 'w')
#        response = urllib.request.urlopen(url)
#        for line in response:
#            f.write(line.decode('utf-8'))
#        f.close()

ssl_args = {'ssl': {'ca': '/etc/pki/tls/certs/webdb-cacert.pem'}}
db_engine = create_engine(
        'mysql://oreckord:74&9d$xVVWz1@webdb.uvm.edu/ORECKORD_HISTORICAL_ENROLLMENT',
        connect_args=ssl_args)
Session = sessionmaker(bind=db_engine)
db = Session()
db.table_names()
