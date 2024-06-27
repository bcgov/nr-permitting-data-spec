# Permit Name Registry Schema

*This data specification enables the creation of a standard list of permit names for the Natural Resource Sector permitting systems.*

## Properties

- **`permit-name-registry-id`** *(string, format: uuid)*: A unique key of registered permit names.
- **`source_system_acronym`** *(string)*: Acronym for the source system providing the permit tracking.
- **`permit_name`** *(string)*: The business domain permit name type.
- **`permit_application_type`** *(['string', 'null'])*: The form types for a permit or licence application. Must be one of: `["Amendment", "Cancel", "Change Ownership", "New"]`.
- **`create_timestamp`** *(date-time)*: The date and time the record was created.
- **`create_user`** *(string)*: The user or proxy account that created the record.
- **`update_timestamp`** *(date-time)*: The date and time the record was created or last updated.
- **`update_user`** *(string)*: The user or proxy account that created or last updated the record.
