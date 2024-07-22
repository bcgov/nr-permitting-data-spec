## Scope 
To oversee the management of permitting schemas this governance guidelines are applicable to all the permitting schemas defined for natural resource sector permitting systems including but not limited to housing, core, metadata and permit registry.

## Governance Committee 
The governance committe for the schema management will include representative from all key stakehoders group in this case representative from each permitting system across sectors (data stewards, data owners). They will oversee the development, implementation and maintenance of the schemas and will ensure the alignment with organizational goal and compliance issues.Roles and responsibilities will be defined as follows:

## Key Roles
•	Schema Owners: Data team will be the schema owner and responsible for the overall schema, including updates and compliance.

•	Contributors: Developers and data owners from specific program areas will act for the contributor role and can contribute for modification or update of the schemas.

•	Reviewers: Experts who can review and approve schema changes.

•	Administrators: Data team will manage repository access and oversee the governance process as administrators.

## Standards and Policies
**Schema Standards:**

•	All schemas must follow a consistent structure (e.g., naming conventions, versioning).

•	Mandatory fields and formats should be defined in every schema.

•	Every schema should have a purpose and usage guidelines.

**Policies:**

•	Version Control: Use semantic versioning (e.g., 1.0.0) to track changes.

•	Approval Process: 

•	Documentation: Ensure all schemas are well-documented and provide examples.

## Schema Repository Structure

•	Root Directory: Contains general information and governance documents.

•	schemas Directory: Contain all the schema definition json. May include subdirectories for domain purpose in future.

•	autogen_docs Directory: Documentation for each schema.

•	Tools Directory: Tools for validation, deployment, and monitoring.

Example:

root/

|-- schemas/

|   |-- core-permit-schema

|   |-- housing/

|   |   |-- housing-permit-schema.json

|   |   |-- housing_permit_v1.1-schema.json

|-- autogen_docs/

|   |-- housing-permit-schema.md

|-- tools/

|   |-- validate_schema.py

|-- README.md

|-- GOVERNANCE.md

## Lifecycle Management Process

Creation and Updates:

•	Use feature branches for schema development.

•	Submit pull requests for new schemas or updates. Add reviewer to review and approve changes.

•	Conduct reviews and approvals via pull request reviews.

•	Merge upon approval.

## Feedback Mechanism
Half yearly review will be conducted to capture improvement feedback from users and govennance committe members. Periodic review will ensure the update with new requirements, technologies and best practices. 




