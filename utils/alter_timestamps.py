import json
import datetime
import sys
import re

pattern = re.compile("^(.+)\[.+\](.*)$")

for line in sys.stdin:
    jo = json.loads(line)

    ts = datetime.datetime.utcnow()
    iso_ts = "{}000Z".format(ts.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-6])
    log_ts = "{} +0000".format(ts.strftime('%d/%b/%Y:%H:%M:%S'))

    jo['@timestamp'] = iso_ts

    match = pattern.search(jo["message"])

    jo["message"] = "{}[{}]{}".format(match.group(1), log_ts, match.group(2))
    
    print(json.dumps(jo))
