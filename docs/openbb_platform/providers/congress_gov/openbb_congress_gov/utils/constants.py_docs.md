# Documentation: openbb_platform/providers/congress_gov/openbb_congress_gov/utils/constants.py

## File Metadata
- **Path**: `openbb_platform/providers/congress_gov/openbb_congress_gov/utils/constants.py`
- **Size**: 2,850 characters, 73 lines
- **Words**: 399
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""US Congress Constants."""

base_url = "https://api.congress.gov/v3/"

BillTypes: list = ["hr", "s", "hjres", "sjres", "hconres", "sconres", "hres", "sres"]

bill_type_options: list[dict[str, str]] = [
    {"label": "House Bill", "value": "hr"},
    {"label": "Senate Bill", "value": "s"},
    {"label": "House Joint Resolution", "value": "hjres"},
    {"label": "Senate Joint Resolution", "value": "sjres"},
    {"label": "House Concurrent Resolution", "value": "hconres"},
    {"label": "Senate Concurrent Resolution", "value": "sconres"},
    {"label": "House Simple Resolution", "value": "hres"},
    {"label": "Senate Simple Resolution", "value": "sres"},
]

bill_type_docstring = """Bill type (e.g., "hr" for House bills).

Must be one of: hr, s, hjres, sjres, hconres, sconres, hres, sres.

Bills
-----

A bill is the form used for most legislation, whether permanent or temporary, general or special, public or private.

A bill originating in the House of Representatives is designated by the letters “H.R.”,
signifying “House of Representatives”, followed by a number that it retains throughout all its parliamentary stages.

Bills are presented to the President for action when approved in identical form
by both the House of Representatives and the Senate.

Joint Resolutions
-----------------

Joint resolutions may originate either in the House of Representatives or in the Senate.

There is little practical difference between a bill and a joint resolution. Both are subject to the same procedure,
except for a joint resolution proposing an amendment to the Constitution.

On approval of such a resolution by two-thirds of both the House and Senate,
it is sent directly to the Administrator of General Services for submission to the individual states for ratification.

It is not presented to the President for approval.
A joint resolution originating in the House of Representatives is designated “H.J.Res.” followed by its individual number.
Joint resolutions become law in the same manner as bills.

Concurrent Resolutions
----------------------

Matters affecting the operations of both the House of Representatives and Senate
are usually initiated by means of concurrent resolutions.

A concurrent resolution originating in the House of Representatives is designated “H.Con.Res.”
followed by its individual number.

On approval by both the House of Representatives and Senate,
they are signed by the Clerk of the House and the Secretary of the Senate.

They are not presented to the President for action.

Simple Resolutions
------------------

A matter concerning the operation of either the House of Representatives or Senate
alone is initiated by a simple resolution.

A resolution affecting the House of Representatives is designated “H.Res.” followed by its number.

They are not presented to the President for action.

"""

```

## High-Level Overview

US Congress Constants.

base_url = "https://api.congress.gov/v3/"

BillTypes: list = ["hr", "s", "hjres", "sjres", "hconres", "sconres", "hres", "sres"]

bill_type_options: list[dict[str, str]] = [
{"label": "House Bill", "value": "hr"},
{"label": "Senate Bill", "value": "s"},
{"label": "House Joint Resolution", "value": "hjres"},
{"label": "Senate Joint Resolution", "value": "sjres"},
{"label": "House Concurrent Resolution", "value": "hconres"},
{"label": "Senate Concurrent Resolution", "value": "sconres"},
{"label": "House Simple Resolution", "value": "hres"},
{"label": "Senate Simple Resolution", "value": "sres"},
]

bill_type_docstring = """Bill type (e.g., "hr" for House bills).

Must be one of: hr, s, hjres, sjres, hconres, sconres, hres, sres.

## Detailed Structure

### Python File Structure

**Classes** (0):
None

**Functions** (0):
None

**Imports** (0):
None


## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

No direct file references found.

## Notes
- Generated: 2025-11-18T07:54:37.607783
- Generator: World's Best Repo Book Generator v1.0.0
