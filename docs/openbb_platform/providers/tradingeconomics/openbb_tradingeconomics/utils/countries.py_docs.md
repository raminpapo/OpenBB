# Documentation: openbb_platform/providers/tradingeconomics/openbb_tradingeconomics/utils/countries.py

## File Metadata
- **Path**: `openbb_platform/providers/tradingeconomics/openbb_tradingeconomics/utils/countries.py`
- **Size**: 4,616 characters, 236 lines
- **Words**: 308
- **Extension**: .py
- **Classification**: Text file

## Original Source

```python
"""Countries list for Trading Economics API."""

country_dict = {
    "G20": [
        "United States",
        "Euro Area",
        "China",
        "Japan",
        "Germany",
        "United Kingdom",
        "France",
        "India",
        "Italy",
        "Brazil",
        "Canada",
        "South Korea",
        "Russia",
        "Spain",
    ],
    "Australia": [
        "Australia",
        "Fiji",
        "Kiribati",
        "New Caledonia",
        "New Zealand",
        "Papua New Guinea",
        "Samoa",
        "Solomon Islands",
        "Tonga",
        "Vanuatu",
    ],
    "America": [
        "Antigua and Barbuda",
        "Argentina",
        "Aruba",
        "Bahamas",
        "Barbados",
        "Belize",
        "Bermuda",
        "Bolivia",
        "Brazil",
        "Canada",
        "Cayman Islands",
        "Chile",
        "Colombia",
        "Costa Rica",
        "Cuba",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "El Salvador",
        "Grenada",
        "Guatemala",
        "Guyana",
        "Haiti",
        "Honduras",
        "Jamaica",
        "Mexico",
        "Nicaragua",
        "Panama",
        "Paraguay",
        "Peru",
        "Puerto Rico",
        "Suriname",
        "Trinidad and Tobago",
        "United States",
        "Uruguay",
        "Venezuela",
    ],
    "Europe": [
        "Albania",
        "Andorra",
        "Austria",
        "Belarus",
        "Belgium",
        "Bosnia and Herzegovina",
        "Bulgaria",
        "Croatia",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Estonia",
        "Euro area",
        "Faroe Islands",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hungary",
        "Iceland",
        "Ireland",
        "Isle of Man",
        "Italy",
        "Kosovo",
        "Latvia",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Malta",
        "Moldova",
        "Monaco",
        "Montenegro",
        "Netherlands",
        "North Macedonia",
        "Norway",
        "Poland",
        "Portugal",
        "Romania",
        "Russia",
        "Serbia",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden",
        "Switzerland",
        "Turkey",
        "Ukraine",
        "United Kingdom",
    ],
    "Africa": [
        "Algeria",
        "Angola",
        "Benin",
        "Botswana",
        "Burkina Faso",
        "Burundi",
        "Cameroon",
        "Cape Verde",
        "Central African Republic",
        "Chad",
        "Comoros",
        "Congo",
        "Djibouti",
        "Egypt",
        "Equatorial Guinea",
        "Eritrea",
        "Ethiopia",
        "Gabon",
        "Gambia",
        "Ghana",
        "Guinea",
        "Guinea Bissau",
        "Ivory Coast",
        "Kenya",
        "Lesotho",
        "Liberia",
        "Libya",
        "Madagascar",
        "Malawi",
        "Mali",
        "Mauritania",
        "Mauritius",
        "Morocco",
        "Mozambique",
        "Namibia",
        "Niger",
        "Nigeria",
        "Republic of the Congo",
        "Rwanda",
        "Sao Tome and Principe",
        "Senegal",
        "Seychelles",
        "Sierra Leone",
        "Somalia",
        "South Africa",
        "South Sudan",
        "Sudan",
        "Swaziland",
        "Tanzania",
        "Togo",
        "Tunisia",
        "Uganda",
        "Zambia",
        "Zimbabwe",
    ],
    "Asia": [
        "Afghanistan",
        "Armenia",
        "Azerbaijan",
        "Bahrain",
        "Bangladesh",
        "Bhutan",
        "Brunei",
        "Cambodia",
        "China",
        "East Timor",
        "Georgia",
        "Hong Kong",
        "India",
        "Indonesia",
        "Iran",
        "Iraq",
        "Israel",
        "Japan",
        "Jordan",
        "Kazakhstan",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Lebanon",
        "Macao",
        "Malaysia",
        "Maldives",
        "Mongolia",
        "Myanmar",
        "Nepal",
        "North Korea",
        "Oman",
        "Palestine",
        "Pakistan",
        "Philippines",
        "Qatar",
        "Saudi Arabia",
        "Singapore",
        "South Korea",
        "Sri Lanka",
        "Syria",
        "Taiwan",
        "Tajikistan",
        "Thailand",
        "Turkmenistan",
        "United Arab Emirates",
        "Uzbekistan",
        "Vietnam",
        "Yemen",
    ],
}

COUNTRIES = list(
    {
        item.lower().replace(" ", "_")
        for sublist in country_dict.values()
        for item in sublist
    }
)

```

## High-Level Overview

Countries list for Trading Economics API.

country_dict = {
"G20": [
"United States",
"Euro Area",
"China",
"Japan",
"Germany",
"United Kingdom",
"France",
"India",
"Italy",
"Brazil",
"Canada",
"South Korea",
"Russia",
"Spain",
],
"Australia": [

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
- Generated: 2025-11-18T07:54:43.479821
- Generator: World's Best Repo Book Generator v1.0.0
