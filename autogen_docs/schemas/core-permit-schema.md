# Core Permitting Schema

*This data specification provides a standard list of values for Natural Resource Sector core permitting data.*

## Properties

- **`project_linking_id`** *(string, format: uuid)*: A unique key to track all permits related to a project or activity from all permitting systems.
- **`project_name`** *(['string', 'null'])*: Short name of the project, e.g., The Hudson, Capitol Hill.
- **`project_description`** *(['string', 'null'])*: Full description of the project. This field may contain information to better understand a project.
- **`project_location_description`** *(['string', 'null'])*: A short description for the geographical location or area of interest of the project.
- **`physical_address`** *(['string', 'null'])*: This is the physical address if provided for a project.
- **`region_name`** *(string)*: Geographic administrative boundary associated with the physical project location.
- **`agency`** *(string)*: Acronym for the agency or ministry issuing the permit. Must be one of: `["AGRI", "ENV", "EMLI", "FOR", "MOTI", "WLRS", "BCER"]`.
- **`business_domain`** *(string)*: Business domain, office or area responsible for the permit. Must be one of: `["Archaeology", "Contaminated Sites", "Lands", "Riparian", "Transportation", "Water"]`.
- **`source_system_acronym`** *(string)*: Acronym for the source system providing the permit tracking. Must be one of: `["APTS", "CATS", "EPUPS; PPA", "FTA", "MOTI", "RARN", "RRS", "TANTALIS", "WILD", "WMA"]`.
- **`application_id`** *(string)*: Unique ID of the submitted application for a permit.
- **`application_name`** *(['string', 'null'])*: Name of the application for a permit.
- **`application_type`** *(string)*: The form type for a permit or licence application. Must be one of: `["Amendment", "Cancel", "Change Ownership", "New"]`.
- **`application_tracking_state`** *(string)*: Tracking state of an application in progress. Must be one of: `["Active", "Closed", "On hold", "Suspended"]`.
- **`application_status`** *(string)*: Status of the application to obtain a permit. Must be one of: `["Abandoned", "Approved", "Cancelled", "In Review", "Issued", "Offered", "Rejected", "Requested", "With client"]`.
- **`permit_id`** *(string, format: uuid)*: A permit specific ID used to identify the issued permit id. A meaningful number/code used by the business area to identify the permit.
- **`permit_name`** *(string)*: The business domain permit name type. Must be one of: `["Commercial General", "Nominal Rent Tenure", "Residential", "Roadways - Public", "Utilities", "Groundwater Licence", "Water Licence", "Change Approval for Works in and about a Stream"]`.
- **`permit_application_type`** *(['string', 'null'])*: The form type for a permit or licence application. Must be one of: `["New", "Amendment", "Cancel", "Change Ownership"]`.
- **`received_date`** *(string, format: date-time)*: Date in which the application for permit was submitted.
- **`accepted_date`** *(['string', 'null'], format: date-time)*: Date in which the review of the initial application's completeness concludes.
- **`tech_review_completion_date`** *(['string', 'null'], format: date-time)*: Date in which the technical team concludes their review of the application.
- **`rejected_date`** *(['string', 'null'], format: date-time)*: Date in which the permit is rejected.
- **`adjudication_date`** *(['string', 'null'], format: date-time)*: Date in which the permit is adjudicated, approved or issued.
- **`amendment_date`** *(['string', 'null'], format: date-time)*: Date in which the permit is amended.
- **`fn_consultn_start_date`** *(['string', 'null'], format: date-time)*: Date in which the consultation with First Nations starts.
- **`fn_consultn_completion_date`** *(['string', 'null'], format: date-time)*: Date in which the consultation with First Nations ends.
