variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  type    = string
  default = "pixelshare"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}
