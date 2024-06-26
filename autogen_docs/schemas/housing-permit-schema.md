# Housing Permit Schema

*This reference data provides a standard set of housing attributes to supplement the core permit schema.*

## Properties

- **`housing_dwelling_type`** *(string)*: The type of dwelling units being developed, e.g, Single-family, Multi-family, Secondary Unit, Other (optional). Must be one of: `["Single-family", "Multi-family", "Secondary Unit", "Duplexes", "Apartments", "Condominiums", "Other"]`.
- **`housing_dwelling_type_code`** *(['string', 'null'])*: The code for the type of dwelling units being developed, e.g, SFD, MFD, SU, O. Must be one of: `["SFD", "MFD", "SU"]`.
- **`housing_dwelling_capacity_ranges`** *(['string', 'null'])*: The number of dwelling or units defined in ranges. Must be one of: `["1-9", "10-49", "50-500", ">500"]`.
- **`housing_dwelling_capacity`** *(integer)*: The number of dwellings or units to be developed.
- **`purpose_built_rental_ind`** *(string)*: Indicating whether the application corresponds to a  purpose built residential unit, property, or dwelling that is available for long term rent by tenants, i.e., Y, N, U. Must be one of: `["Y", "N", "U"]`.
- **`indigenous_led_ind`** *(string)*: A value indicating whether the application is led by Indigenous groups, i.e., Y, N, U. Must be one of: `["Y", "N", "U"]`.
- **`social_housing_ind`** *(string)*: A value indicating whether the application's purpose pertains to Social Housing, i.e., Y, N, U. Must be one of: `["Y", "N", "U"]`.
