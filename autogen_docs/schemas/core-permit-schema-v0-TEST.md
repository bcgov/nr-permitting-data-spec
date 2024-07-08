# Core Permitting Schema

*This data specification provides a standard list of values for Natural Resource Sector core permitting data.*

## Properties

- **`project`**: Refer to *[/v0/objects/project.json](#0/objects/project.json)*.
- **`application`**: Refer to *[/v0/objects/application.json](#0/objects/application.json)*.
- **`region_name`** *(string)*: Natural Resource administrative boundary associated with the physical project location. Must be one of: `["Cariboo", "Kootenay-Boundary", "Northeast", "Omineca", "Skeena", "South Coast", "Thompson-Okanagan", "West Coast"]`.
- **`agency`** *(string)*: Acronym for the agency or ministry issuing the permit. Must be one of: `["AGRI", "ENV", "EMLI", "FOR", "MIRR", "MOTI", "WLRS", "BCER"]`.
- **`business_domain`** *(string)*: Business domain, office or area responsible for the permit. Must be one of: `["Archaeology", "Contaminated Sites", "Lands", "Riparian", "Transportation", "Water"]`.
- **`source_system_acronym`** *(string)*: Acronym for the source system providing the permit tracking. Must be one of: `["APTS", "CATS", "EPUPS; PPA", "FTA", "MOTI", "RARN", "RRS", "TANTALIS", "WILD", "WMA"]`.
- **`permit_id`** *(string, format: uuid)*: A permit specific ID used to identify the issued permit id. A meaningful number/code used by the business area to identify the permit.
- **`permit_name`** *(string)*: The business domain permit name type. Must be one of: `["Change approval for work in and about a stream", "Commercial General", "Contaminated Sites Remediation", "Groundwater Licence", "Heritage Inspection Permit", "Highway Use Permit", "Investigation Permit", "Municipal subdivision", "Nominal Rent Tenure", "Notification of authorized changes in and about a stream", "Occupant Licence to Cut", "Other", "Private Timber Mark", "Residential", "Rezoning", "Riparian Area Development Permit", "Roadways - Public", "Rural subdivision", "Short-term use approval", "Site Alteration Permit", "Sponsored Crown Grant", "Surface Water Licence", "Utilities"]`.
- **`permit_application_type`** *(['string', 'null'])*: The form type for a permit or licence application. Must be one of: `["New", "Amendment", "Cancel", "Change Ownership"]`.
- **`received_date`** *(string, format: date-time)*: Date in which the application for permit was submitted.
- **`accepted_date`** *(['string', 'null'], format: date-time)*: Date in which the review of the initial application's completeness concludes.
- **`tech_review_completion_date`** *(['string', 'null'], format: date-time)*: Date in which the technical team concludes their review of the application.
- **`rejected_date`** *(['string', 'null'], format: date-time)*: Date in which the permit is rejected.
- **`adjudication_date`** *(['string', 'null'], format: date-time)*: Date in which the permit is adjudicated as either issued or not issued.
- **`amendment_date`** *(['string', 'null'], format: date-time)*: Date in which the permit is amended.
- **`fn_consultn_start_date`** *(['string', 'null'], format: date-time)*: Date in which the consultation with First Nations starts.
- **`fn_consultn_completion_date`** *(['string', 'null'], format: date-time)*: Date in which the consultation with First Nations ends.
