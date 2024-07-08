# Project Object

*Project contain context about the project.*

## Properties

- **`project_linking_id`** *(string, format: uuid)*: A unique key to track all permits related to a project or activity from all permitting systems.
- **`project_name`** *(['string', 'null'])*: Short name of the project, e.g., The Hudson, Capitol Hill.
- **`project_description`** *(['string', 'null'])*: Full description of the project. This field may contain information to better understand a project.
- **`project_location_description`** *(['string', 'null'])*: A short description for the geographical location or area of interest of the project.
- **`physical_address`**: This is the physical address if provided for a project. Refer to *[./address.json](#address.json)*.
