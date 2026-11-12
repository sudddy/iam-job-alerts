import re

IAM = re.compile(
    r"identity|\bIAM\b|\bIdP\b|\bSSO\b|OAuth|OIDC|SAML|SCIM|CIAM|\bPAM\b|authentication"
    r"|access management|verifiable credential|OpenID4VC|digital identity",
    re.I,
)
CANADA = re.compile(
    r"canada|toronto|vancouver|montreal|montréal|ottawa|calgary|waterloo|edmonton|winnipeg"
    r"|halifax|quebec|québec|ontario|british columbia|alberta|manitoba|nova scotia"
    r"|\b(ON|BC|AB|QC)\b",
)
REMOTE_OK = re.compile(r"remote.*(north america|americas|anywhere)|(north america|americas|anywhere).*remote", re.I)


def matches(job):
    loc = job["location"]
    return bool(IAM.search(job["title"] + " " + job["text"]) and (CANADA.search(loc) or REMOTE_OK.search(loc)))
