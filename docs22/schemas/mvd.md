# permitting_mvd

*Standardisation of the attributes collected from all LOB source systems associated with the PMT*

## Properties

- **`id`** *(string, format: uuid)*: Unique ID of the permit.
- **`application_id`** *(string, format: uuid)*: Unique ID of the submitted application for a permit.
- **`source_system`** *(string)*: Acronym for the source system providing the permit tracking. Must be one of: `["APTS", "CATS", "EPUPS; PPA", "FTA", "MOTI", "RARN", "RRS", "TANTALIS", "WILD", "WMA"]`.
- **`source_system_id`** *(string, format: uuid)*: Unique ID of the permit in the source system.
- **`project_id`** *(string, format: uuid)*: ID of the project this permit relates to.
- **`agency`** *(string)*: Acronym for the agency or ministry issuing the permit. Must be one of: `["AF", "ENV", "FOR", "MOTI", "WLRS", "BCER"]`.
- **`business`** *(string)*: Business domain or area responsible for the permit. Must be one of: `["Archaeology", "Contaminated Sites", "Lands", "Riparian", "Transportation", "Water"]`.
- **`application_status`** *(string)*: Status of the application to obtain a permit. Must be one of: `["Issued", "Denied", "Pending", "In Review"]`.
- **`permit_application_name`** *(string)*: The business domain permit type. Must be one of: `["Commercial General", "Nominal Rent Tenure", "Residential", "Roadways - Public", "Utilities", "New Groundwater Licence", "Water Licence", "Change Approval for Works in and About a Stream"]`.
- **`permit_application_type`** *(['string', 'null'])*: The form type for a permit or licence application. Must be one of: `["New", "Amendment", "Cancel", "Change Ownership"]`.
- **`received_date`** *(string, format: date-time)*: Date in which the application for permit was submitted.
- **`accepted_date`** *(['string', 'null'], format: date-time)*: Date in which the review of the initial application's completeness concludes.
- **`tech_review_completion_date`** *(['string', 'null'], format: date-time)*: Date in which the technical team concludes their review of the application.
- **`rejected_date`** *(['string', 'null'], format: date-time)*: Date in which the permit is rejected.
- **`adjudication_date`** *(['string', 'null'], format: date-time)*: Date in which the permit is adjudicated, approved or issued.
- **`amendment_date`** *(['string', 'null'], format: date-time)*: Date in which the permit is amended.
- **`fn_consultn_start_date`** *(['string', 'null'], format: date-time)*: Date in which the consultation with First Nations starts.
- **`fn_consultn_completion_date`** *(['string', 'null'], format: date-time)*: Date in which the consultation with First Nations ends.
