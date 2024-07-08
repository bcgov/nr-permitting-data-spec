# Application Object

*An address similar to http://microformats.org/wiki/h-card*

## Properties

- **`application_id`** *(string)*: Unique ID of the submitted application for a permit.
- **`application_name`** *(['string', 'null'])*: Name of the application for a permit.
- **`application_type`** *(string)*: The form type for a permit or licence application. Must be one of: `["Amendment", "Cancel", "Change Ownership", "New"]`.
- **`application_lifecycle_state`** *(string)*: Tracking state of an application in progress. Must be one of: `["Active", "Closed", "On hold"]`.
- **`application_status`** *(string)*: Status of the application during the process and final decision. Must be one of: `["Abandoned", "Approved", "Cancelled", "In Process", "In Referral", "Issued", "Offered", "Rejected", "Requested", "Suspended", "With client"]`.
