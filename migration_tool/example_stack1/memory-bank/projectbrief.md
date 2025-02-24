# Project Brief

## Overview
This project involves migrating an AWS CDK stack from VPCv1 to VPCv2. The migration is necessary to update the infrastructure code to use the latest VPC constructs provided by AWS CDK.

## Core Requirements
1. Identify existing VPC definitions in the CDK stack
2. Migrate from `new VPC()` to `new VPCv2()`
3. Update property mappings according to the new VPCv2 specification
4. Maintain existing CIDR range configurations

## Migration Rules
- Replace `new VPC()` with `new VPCv2()`
- Update CIDR configuration:
  ```typescript
  // Old format
  cidr: <current_value>
  
  // New format
  primaryAddressBlock: IpAddresses.ipv4(<current_value>)
  ```

## Success Criteria
- All VPC definitions successfully migrated to VPCv2
- Existing CIDR ranges preserved
- Infrastructure functionality maintained
- Code compiles successfully
