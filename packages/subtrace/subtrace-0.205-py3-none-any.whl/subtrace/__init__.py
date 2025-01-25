import os

print("found:", os.listdir(os.path.dirname(os.path.realpath(__file__))))

import truststore
truststore.inject_into_ssl()
