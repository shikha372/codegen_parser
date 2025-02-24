# Technical Context

## Technology Stack
- AWS CDK v2 (v2.178.1)
- TypeScript (v5.6.3)
- Node.js

## Key Dependencies
- `aws-cdk-lib`: ^2.179.0 (Core CDK library)
- `@aws-cdk/aws-ec2-alpha`: ^2.179.0-alpha.0 (EC2 constructs including VPC)
- `constructs`: ^10.0.0 (CDK construct library)

## Development Dependencies
- TypeScript tooling:
  - `typescript`: ~5.6.3
  - `ts-node`: ^10.9.2
  - `@types/node`: 22.7.9
- Testing framework:
  - `jest`: ^29.7.0
  - `ts-jest`: ^29.2.5
  - `@types/jest`: ^29.5.14

## Project Structure
```
example_stack1/
├── bin/              # CDK app entry point
├── lib/              # Stack definitions
│   ├── example_stack1-stack.ts    # Original stack
│   └── example_stack1-stack-v2.ts # Migration target
├── test/             # Test files
└── memory-bank/      # Project documentation
```

## Build & Test Commands
- `npm run build`: Compile TypeScript code
- `npm run watch`: Watch mode for TypeScript compilation
- `npm test`: Run Jest tests
- `npm run cdk`: Execute CDK commands

## Technical Constraints
- Must maintain compatibility with existing AWS infrastructure
- Need to preserve CIDR range configurations during VPC migration
- Must use VPCv2 constructs from aws-cdk-lib
