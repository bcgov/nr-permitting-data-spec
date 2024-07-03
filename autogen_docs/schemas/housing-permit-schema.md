# Housing Permitting Schema

*This data specification provides a standard list of values for Natural Resource Sector permitting data realted to housing attributes to supplementing the core permit schema.*

## Properties

- **`project_linking_id`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/project_linking_id](#schemas/defintions/core-permit-schema.json%23/properties/project_linking_id)*.
- **`project_name`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/project_name](#schemas/defintions/core-permit-schema.json%23/properties/project_name)*.
- **`project_description`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/project_description](#schemas/defintions/core-permit-schema.json%23/properties/project_description)*.
- **`project_location_description`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/project_location_description](#schemas/defintions/core-permit-schema.json%23/properties/project_location_description)*.
- **`physical_address`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/physical_address](#schemas/defintions/core-permit-schema.json%23/properties/physical_address)*.
- **`region_name`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/region_name](#schemas/defintions/core-permit-schema.json%23/properties/region_name)*.
- **`agency`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/agency](#schemas/defintions/core-permit-schema.json%23/properties/agency)*.
- **`business_domain`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/business_domain](#schemas/defintions/core-permit-schema.json%23/properties/business_domain)*.
- **`application_id`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/application_id](#schemas/defintions/core-permit-schema.json%23/properties/application_id)*.
- **`application_name`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/application_name](#schemas/defintions/core-permit-schema.json%23/properties/application_name)*.
- **`application_type`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/application_type](#schemas/defintions/core-permit-schema.json%23/properties/application_type)*.
- **`application_tracking_state`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/application_tracking_state](#schemas/defintions/core-permit-schema.json%23/properties/application_tracking_state)*.
- **`application_status`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/application_status](#schemas/defintions/core-permit-schema.json%23/properties/application_status)*.
- **`permit_id`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/permit_id](#schemas/defintions/core-permit-schema.json%23/properties/permit_id)*.
- **`permit_name`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/permit_name](#schemas/defintions/core-permit-schema.json%23/properties/permit_name)*.
- **`permit_application_type`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/permit_application_type](#schemas/defintions/core-permit-schema.json%23/properties/permit_application_type)*.
- **`received_date`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/received_date](#schemas/defintions/core-permit-schema.json%23/properties/received_date)*.
- **`tech_review_completion_date`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/tech_review_completion_date](#schemas/defintions/core-permit-schema.json%23/properties/tech_review_completion_date)*.
- **`rejected_date`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/rejected_date](#schemas/defintions/core-permit-schema.json%23/properties/rejected_date)*.
- **`adjudication_date`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/adjudication_date](#schemas/defintions/core-permit-schema.json%23/properties/adjudication_date)*.
- **`amendment_date`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/amendment_date](#schemas/defintions/core-permit-schema.json%23/properties/amendment_date)*.
- **`fn_consultn_start_date`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/fn_consultn_start_date](#schemas/defintions/core-permit-schema.json%23/properties/fn_consultn_start_date)*.
- **`fn_consultn_completion_date`**: Refer to *[./schemas/defintions/core-permit-schema.json#/properties/fn_consultn_completion_date](#schemas/defintions/core-permit-schema.json%23/properties/fn_consultn_completion_date)*.
- **`housing_dwelling_type`** *(string)*: The type of dwelling units being developed, e.g, Single-family, Multi-family, Secondary Unit, Other (optional). Must be one of: `["Single-family", "Multi-family", "Secondary Unit", "Duplexes", "Apartments", "Condominiums", "Other"]`.
- **`housing_dwelling_type_code`** *(['string', 'null'])*: The code for the type of dwelling units being developed.

  Examples:
  ```json
  "SFD"
  ```

  ```json
  "MFD"
  ```

  ```json
  "SU"
  ```

- **`housing_dwelling_capacity_ranges`** *(['string', 'null'])*: The number of dwelling or units defined in ranges. Must be one of: `["1-9", "10-49", "50-500", ">500"]`.
- **`housing_dwelling_capacity`** *(integer)*: The number of dwellings or units to be developed.
- **`purpose_built_rental_ind`** *(string)*: Indicating whether the application corresponds to a  purpose built residential unit, property, or dwelling that is available for long term rent by tenants, i.e., Y, N, U. Must be one of: `["Y", "N", "U"]`.
- **`indigenous_led_ind`** *(string)*: A value indicating whether the application is led by Indigenous groups, i.e., Y, N, U. Must be one of: `["Y", "N", "U"]`.
- **`social_housing_ind`** *(string)*: A value indicating whether the application's purpose pertains to Social Housing, i.e., Y, N, U. Must be one of: `["Y", "N", "U"]`.
- **`version`** *(integer)*: Defines the version of the schema being represented. Must be one of: `[0.1]`. Default: `1`.
