import falcon

from falconpy import OAuth2
from falconpy import CloudConnectAWS
from falconpy import Detects




# You may also use Credential Authentication to
# create the instance of the authentication object
auth = OAuth2(client_id=CLIENT_ID,
              client_secret=CLIENT_SECRET
              )

# The auth object is then passed when instantiating
# subsequent Service Class objects
falcon_aws = CloudConnectAWS(auth_object=auth)
falcon_detects = Detects(auth_object=auth)

# You can use PEP8 or Operation ID syntax for these calls
print(falcon_aws.query_aws_accounts())
print(falcon_detects.query_detects())