# from aws_cdk import (
#     aws_ec2 as ec2,
#     # Duration,
#     Stack,
#     # aws_sqs as sqs,
# )
# from constructs import Construct

# class CdkVpcRtSubnetStack(Stack):

#     def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
#         super().__init__(scope, construct_id, **kwargs)

#         vpc =ec2.Vpc(
#             self, "MukilVPC",
#             cidr="10.0.0.0/16",
#             enable_dns_hostnames=True,
#             enable_dns_support=True)
        
#         # Create an Internet Gateway
#         IG = ec2.CfnInternetGateway(self, "InternetGateway")

#         # Attach IG to VPC
#         ec2.CfnVPCGatewayAttachment(self, "VPCGatewayAttachmentMC",
#             vpc_id=vpc.vpc_id,
#             internet_gateway_id=IG.ref)
        
#         # Create a Public Route Table
#         public_rt = ec2.CfnRouteTable(self, "PublicRT",
#             vpc_id=vpc.vpc_id)
     

#         # Create a Public Subnet
#         public_subnet = ec2.CfnSubnet(self, "PublicSubnet",
#             vpc_id=vpc.vpc_id,
#             cidr_block= "10.0.252.0/24",
#             availability_zone=vpc.availability_zones[0],
#             map_public_ip_on_launch=True)
        
#         # Create a Public Route
#         ec2.CfnRoute(self, "PublicRoute",
#             route_table_id=public_rt.ref,
#             destination_cidr_block="0.0.0.0/0",
#             gateway_id=IG.ref)
        
#         ec2.CfnSubnetRouteTableAssociation(self, "PublicSubnetRouteTableAssociation",
#             subnet_id=public_subnet.ref,
#             route_table_id=public_rt.ref)
#         #private
        
#         elasticip = ec2.CfnEIP(self, "ElasticIP",
#             domain="vpc")
        
#         nat_gateway = ec2.CfnNatGateway(self, "NATGateway",
#             subnet_id=public_subnet.ref,
#             allocation_id= elasticip.attr_allocation_id)
        
#         privatesubnet = ec2.CfnSubnet(self, "PrivateSubnet",
#             vpc_id=vpc.vpc_id,
#             cidr_block="10.0.2.0/24",
#             availability_zone=vpc.availability_zones[1])
        
#         privateroutetable = ec2.CfnRouteTable(self, "PrivateRT",
#             vpc_id=vpc.vpc_id)

#         ec2.CfnSubnetRouteTableAssociation(self, "PrivateSubnetRouteTableAssociation",
#             subnet_id=privatesubnet.ref,
#             route_table_id=privateroutetable.ref)

#         #attach nat to private subnet  
#         ec2.CfnRoute(self, "PrivateRoute",
#             route_table_id=privateroutetable.ref,
#             destination_cidr_block="0.0.0.0/0",
#             nat_gateway_id=nat_gateway.ref)
                  

        
        




from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
)
from constructs import Construct

class CdkVpcRtSubnetStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC using CfnVPC
        vpc = ec2.CfnVPC(self, "MukilVPC",
            cidr_block="10.0.0.0/16",
            enable_dns_hostnames=True,
            enable_dns_support=True)
        
        # Create an Internet Gateway
        IG = ec2.CfnInternetGateway(self, "InternetGateway")

        # Attach IG to VPC
        ec2.CfnVPCGatewayAttachment(self, "VPCGatewayAttachmentMC",
            vpc_id=vpc.ref,
            internet_gateway_id=IG.ref)
        
        # Create a Public Route Table
        public_rt = ec2.CfnRouteTable(self, "PublicRT",
            vpc_id=vpc.ref)
     
        # Create a Public Subnet
        public_subnet = ec2.CfnSubnet(self, "PublicSubnet",
            vpc_id=vpc.ref,
            cidr_block= "10.0.252.0/24",
            availability_zone=self.availability_zones[0],
            map_public_ip_on_launch=True)
        
        # Create a Public Route
        ec2.CfnRoute(self, "PublicRoute",
            route_table_id=public_rt.ref,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=IG.ref)
        
        ec2.CfnSubnetRouteTableAssociation(self, "PublicSubnetRouteTableAssociation",
            subnet_id=public_subnet.ref,
            route_table_id=public_rt.ref)
        
        # Private resources
        elasticip = ec2.CfnEIP(self, "ElasticIP",
            domain="vpc")
        
        nat_gateway = ec2.CfnNatGateway(self, "NATGateway",
            subnet_id=public_subnet.ref,
            allocation_id=elasticip.attr_allocation_id)
        
        privatesubnet = ec2.CfnSubnet(self, "PrivateSubnet",
            vpc_id=vpc.ref,
            cidr_block="10.0.2.0/24",
            availability_zone=self.availability_zones[1])
        
        privateroutetable = ec2.CfnRouteTable(self, "PrivateRT",
            vpc_id=vpc.ref)

        ec2.CfnSubnetRouteTableAssociation(self, "PrivateSubnetRouteTableAssociation",
            subnet_id=privatesubnet.ref,
            route_table_id=privateroutetable.ref)

        # Attach NAT to private subnet  
        ec2.CfnRoute(self, "PrivateRoute",
            route_table_id=privateroutetable.ref,
            destination_cidr_block="0.0.0.0/0",
            nat_gateway_id=nat_gateway.ref)
        
        