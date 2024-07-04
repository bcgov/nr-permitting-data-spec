# Natural Resource Common Permitting Data Specifications

[![lifecycle:maturing](https://img.shields.io/badge/Lifecycle-Maturing-007EC6)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)
[![Contributions:Welcome](https://img.shields.io/badge/Contributions-Welcome-green)](https://github.com/bcgov/nr-permitting-data-spec/issues)
![Data:Schema](https://img.shields.io/badge/Data-Schema-aqua)

## Description
This repository contains common schemas related to permitting in the Natural Resources Sector. 

The intent of these are to standardize the way permitting in the Natural Resource Sector is described as data to enable quality and interoperability.

Hosting these will enable and ensure version history will be maintained.

These will be reviewed as required with the related data managers and permitting teams.

## Purpose

The common specifications are to

* create cross sector data governance
* feed intelligence to the sector
* moving towards harmonized statuses 
* activity-based permit bundling
* and application process tracking
* enable consistent collection of data and metadata
* leverage for an integrated data schema for reporting and analytics
* identify opportunities on data quality, data visualizations, and gaps
* develops data patterns and guidelines
* develop common schema patterns for other areas like First Nations Consultation

## Overview

### Schemas

| Subject | Description |JSON| DOC| 
| --- | --- | --- | --- |
| Core Specification | The core permitting content, structure, data types, and expected enums that are consistent across all permitting datasets. | [json](core-permit-schema.json)| [doc](core-permit-schema.md) | 
| Housing Specification | The housing specific schema elements that extend the core schema. | [json](housing-permit-schema.json)| [doc](housing-permit-schema.md)|
| Metadata Specification |The metadata elements required and captured while discovering and onboarding into an integrated dataset. |[json](metadata-discovery-schema.json) |[doc](metadata-discovery-schema.md)  |
| Permit Name Registry Specification |This spec is to enable the registry of permit names from source systems/information to be used as enums in the core Core Specification. |[json](permit-name-registry-schema.json) |[doc](permit-name-registry-schema.md)  |

### Scripts

| Subject | Description |Readme|
| --- | --- | --- |
| Validation | This package takes a JSON document and validates it against an expected schema structure as defined in a JSON schema definition file. |[readme](https://github.com/bcgov/nr-permitting-data-spec/blob/630b56ce631adf02dc819ec54bd710cc1e57276e/tools/schemas/validation/README.md) |
| Auto-generation of docs | This package converts JSON schema definition files into markdown files. | [readme](https://github.com/bcgov/nr-permitting-data-spec/blob/630b56ce631adf02dc819ec54bd710cc1e57276e/tools/autogen/docs/README.md) |

## Future

* Complete data dictionaries
* Finalize status and states terms

### Schemas
* status and state registries 
    * To enable the mapping of source values to a standardized list
* activity bundling
    * To enable identifying what permits are applicable to an activity on the landbase, e.g., housing, mining, connectivity.
* client/proponent
* other permitting initiatives

### Design

Along with the data specification will be the design presentation to enable a common look and feel.

