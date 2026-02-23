variable "aws_region" {
  description = "AWS region to deploy to"
  type        = string
  default     = "eu-central-1"
}

variable "project_name" {
  description = "Name prefix for all resources"
  type        = string
  default     = "finance-tracker-api"
}
