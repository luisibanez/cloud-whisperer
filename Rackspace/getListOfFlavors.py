#!/usr/bin/python
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
# Retrieves the list of available flavors from the Cloud service.
#
# This script expects to find the token.json file in the 'Session' directory.
# That file should have been created during the authentication stage.
#
# The response is put in the file:
#
#                    Session/latestListOfFlavors.json.
#
# For details, please see:
# http://docs.rackspace.com/servers/api/v2/cs-devguide/content/List_Flavors-d1e4188.html
#
#---------------------------------------------------------------------------

import requests
import json

tokenFile=open('Session/token.json','r')
token=json.load(tokenFile)
tokenFile.close()

host='https://dfw.servers.api.rackspacecloud.com/v2/'
account=token['tenant']['id']
uri='/flavors'

url=host+account+uri

headers={'X-Auth-Token':token['id']}

response = requests.get(url,headers=headers)

tokenFile=open('Session/latestListOfFlavors.json','w')
tokenFile.write(json.dumps(response.json))
tokenFile.close()

