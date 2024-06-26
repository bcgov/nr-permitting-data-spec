# Metadata Data Discovery Schema

*This reference data provides a standard list of metadata values for data collected from different source systems.*

## Properties

- **`source_system`** *(string)*: Acronym for the source system providing the data, as it is defined in IRS.
- **`agency`** *(string)*: Acronym for the agency or ministry that owns the dataset.
- **`business`** *(string)*: Business domain or area responsible for the data.
- **`data_custodian`**: Data custodian(s) of the dataset. Refer to *[#/$defs/users](#%24defs/users)*.
- **`data_owner`**: Data owner(s) of the dataset. Refer to *[#/$defs/users](#%24defs/users)*.
- **`data_specialist`**: Data specialist(s) of the dataset. Refer to *[#/$defs/users](#%24defs/users)*.
- **`data_quality_metrics`** *(object)*: Quantified information pertaining to the quality of the data observed in the dataset.
  - **`accuracy`** *(number)*: Percentage of correct values in the dataset compared to the total number of values.
  - **`completeness`** *(number)*: Percentage of missing values in the dataset.
  - **`timeliness`** *(integer)*: Frequency at which data is updated or refreshed to reflect the most recent information, expressed in minutes.
  - **`duplication`** *(number)*: Percentage of duplicated records in the dataset.
- **`description`** *(string)*: Description of the dataset.
- **`security_classification`**: Security classification of the dataset. Refer to *[#/$defs/security_classification](#%24defs/security_classification)*.
- **`technology`** *(object)*: Description of the underlying technology of the dataset.
  - **`name`** *(string, required)*: Name of the technology.
  - **`version`** *(string, required)*: Version of the technology.
- **`tags`** *(array)*: Tags of the dataset, defined as key-value pairs.
  - **Items** *(object)*
    - **`key`** *(string, required)*
    - **`value`** *(string, required)*
- **`categories`** *(array)*: Categories to define the dataset.
  - **Items** *(string)*
- **`storage_descriptor`** *(array)*: Relational data storage description at a table granularity.
  - **Items** *(object)*
    - **`table_name`** *(string, required)*: Name of the table as it is defined in the source database.
    - **`schema_name`** *(string, required)*: Name of the schema as it is defined in the source database.
    - **`columns`** *(array, required)*: Relational data storage description at a column granularity. Length must be at least 1.
      - **Items** *(object)*
        - **`name`** *(string, required)*: Column name.
        - **`type`** *(string, required)*: Column data type.
        - **`precision`** *(string)*: Precision of the column (optional).
        - **`description`** *(string, required)*: Description of the column.
        - **`security_classification`**: Security classification of the column. Refer to *[#/$defs/security_classification](#%24defs/security_classification)*.
        - **`nullable`** *(boolean, required)*: Flag to indicate if the column is nullable.
- **`column_mapping`** *(object)*: Object mapping source system columns as defined in the storage_descriptor to those of the MVD. Each key should have the form 'schema_name.table_name.column'.
- **`extraction_query`** *(string)*: Extraction query used to retrieve target data from the source system.
- **`flowchart`** *(object)*: Graph representation of the flowchart.
  - **`root`** *(integer, required)*: Zero indexed root node of the flowchart. Minimum: `0`.
  - **`nodes`** *(array, required)*: Nodes of the flowchart.
    - **Items** *(string)*: Textual information to display inside each node.
  - **`edges`** *(array, required)*: Representation of each edge in the flowchart, including direction and textual information to display.
    - **Items** *(object)*: Representation of a single edge in the flowchart.
      - **`origin_node`** *(number, required)*: Index of the origin node of the edge in the flowchart, zero-indexed.
      - **`destination_node`** *(number, required)*: Index of the destination node of the edge in the flowchart, zero-indexed.
      - **`text`** *(string, required)*: Textual information to display on the edge of the flowchart.
## Definitions

- <a id="%24defs/users"></a>**`users`** *(array)*
  - **Items** *(object)*
    - **`name`** *(string, required)*: Name of the user.
    - **`email`** *(string, format: email, required)*: Email of the user.
- <a id="%24defs/security_classification"></a>**`security_classification`** *(string)*: Must be one of: `["Protected A", "Protected B", "Protected C"]`.
