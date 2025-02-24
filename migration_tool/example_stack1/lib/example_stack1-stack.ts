import * as cdk from 'aws-cdk-lib';
import { IVpc } from 'aws-cdk-lib/aws-ec2/lib/vpc';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class Vpcv1Stack extends cdk.Stack {
  public readonly routeTableId: string;
  public readonly vpc: IVpc;
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    this.vpc = new cdk.aws_ec2.Vpc(this, 'vpc', {
      cidr: '10.0.0.0/16',
      availabilityZones: ['us-east-2a', 'us-east-2b'],
      natGateways: 0,
      createInternetGateway: true,
      subnetConfiguration: [
        {
          name: 'isolatedSubnet',
          subnetType: cdk.aws_ec2.SubnetType.PRIVATE_ISOLATED,
          cidrMask: 24,
        },
        {
          name: 'isolatedSubnet2',
          subnetType: cdk.aws_ec2.SubnetType.PRIVATE_ISOLATED,
          cidrMask: 24,
        },
        {
          name: 'publicSubnet',
          subnetType: cdk.aws_ec2.SubnetType.PUBLIC,
          cidrMask: 24,
        }
      ],
      restrictDefaultSecurityGroup: false,
    });
  }
}
