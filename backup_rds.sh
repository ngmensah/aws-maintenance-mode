#!/bin/bash
instances=$(aws rds describe-db-instances --query 'DBInstances[*].DBInstanceIdentifier' --output text)
for id in $instances; do
  aws rds create-db-snapshot --db-instance-identifier $id --db-snapshot-identifier ${id}-backup
  echo "Created snapshot for $id"
done