import * as cdk from 'aws-cdk-lib';
import { VpcV2, IpAddresses } from '../../../shikha372_cdk_fork/aws-cdk/packages/@aws-cdk/aws-ec2-alpha';
import { Construct } from 'constructs';

export class Vpcv2Stack extends cdk.Stack {
  public readonly routeTableId: string;
  public readonly vpc: VpcV2;
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create VPC with primary CIDR block
    this.vpc = new VpcV2(this, 'vpc', {
      primaryAddressBlock: IpAddresses.ipv4('10.0.0.0/16'),
    });

    // Add isolated subnets
    this.vpc.addSubnets({
      availabilityZone: 'us-east-2a',
      ipv4CidrBlock: IpAddresses.ipv4('10.0.0.0/24'),
      name: 'isolatedSubnet1',
      type: 'isolated'
    });

    this.vpc.addSubnets({
      availabilityZone: 'us-east-2b',
      ipv4CidrBlock: IpAddresses.ipv4('10.0.1.0/24'),
      name: 'isolatedSubnet2',
      type: 'isolated'
    });

    // Add isolated subnet 2 group
    this.vpc.addSubnets({
      availabilityZone: 'us-east-2a',
      ipv4CidrBlock: IpAddresses.ipv4('10.0.2.0/24'),
      name: 'isolatedSubnet2-1',
      type: 'isolated'
    });

    this.vpc.addSubnets({
      availabilityZone: 'us-east-2b',
      ipv4CidrBlock: IpAddresses.ipv4('10.0.3.0/24'),
      name: 'isolatedSubnet2-2',
      type: 'isolated'
    });

    // Add public subnets
    this.vpc.addSubnets({
      availabilityZone: 'us-east-2a',
      ipv4CidrBlock: IpAddresses.ipv4('10.0.4.0/24'),
      name: 'publicSubnet1',
      type: 'public'
    });

    this.vpc.addSubnets({
      availabilityZone: 'us-east-2b',
      ipv4CidrBlock: IpAddresses.ipv4('10.0.5.0/24'),
      name: 'publicSubnet2',
      type: 'public'
    });
  }
}
