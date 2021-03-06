#!/usr/bin/env python
#---------------------------------------------------------------------------
# Copyright 2011 The Open Source Electronic Health Record Agent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#---------------------------------------------------------------------------
#
# Authenticates your connection to the Rackspace Open Cloud.
#
# This script expects to find your account credentials in a JSON file in the
# directory 'LocalConfiguration'. The file is expected to be called
# accountCredentials.json.
#
# The output of the authentication will be placed in the 'Session' directory
# under the file name token.json. If this authentication is successful, the
# token file contains a hashed token that is valied for a limited period of
# time (the period is indicated as part of the token).
#
# Other scripts will look for this token.json file and will expect the token
# to be in its period of validity.
#
# For details, please see:
# http://docs.rackspace.com/servers/api/v2/cs-devguide/content/auth.html
#
#---------------------------------------------------------------------------

import requests
import json

jsonFile=open('LocalConfiguration/accountCredentials.json')
accountCredentials=json.load(jsonFile)
jsonFile.close()

username=accountCredentials['username']
accountId=accountCredentials['accountId']
apiKey=accountCredentials['apiKey']

apiKeyCredentials={'username':username, 'apiKey':apiKey}
authorization={'RAX-KSKEY:apiKeyCredentials':apiKeyCredentials}
payload={'auth':authorization}

url="https://identity.api.rackspacecloud.com/v2.0/tokens"
headers={'Content-Type': 'application/json','Accept':'application/json'}

r = requests.post(url,data=json.dumps(payload),headers=headers)

token=r.json["access"]["token"]

tokenFile=open('Session/token.json','w')
tokenFile.write(json.dumps(token))
tokenFile.close()

