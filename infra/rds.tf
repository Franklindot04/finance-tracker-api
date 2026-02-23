# -----------------------------------------
# RDS Subnet Group
# Ensures RDS is placed in private subnets
# -----------------------------------------
resource "aws_db_subnet_group" "rds_subnets" {
  name       = "${var.project_name}-rds-subnets"
  subnet_ids = [
    aws_subnet.private_a.id
  ]

  tags = {
    Name = "${var.project_name}-rds-subnets"
  }
}

# -----------------------------------------
# RDS PostgreSQL Instance
# -----------------------------------------
resource "aws_db_instance" "postgres" {
  identifier              = "${var.project_name}-db"
  engine                  = "postgres"
  engine_version          = "15.4"
  instance_class          = "db.t3.micro"
  allocated_storage       = 20

  username                = var.db_username
  password                = var.db_password
  db_name                 = var.db_name

  db_subnet_group_name    = aws_db_subnet_group.rds_subnets.name
  vpc_security_group_ids  = [aws_security_group.rds_sg.id]

  publicly_accessible     = false
  multi_az                = false
  skip_final_snapshot     = true

  tags = {
    Name = "${var.project_name}-db"
  }
}
