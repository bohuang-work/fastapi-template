terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }
}

### Provider Configuration
provider "aws" {
  region = "eu-central-1"
  shared_credentials_files = ["~/.aws/credentials"]
  profile = "bohuang-admin"
}

### AWS EC2 Instance Docker Image
data "aws_ami" "parking_ami" {
  most_recent = true
  owners      = ["099720109477"] # Ubuntu official account ID

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }
}