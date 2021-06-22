#!/bin/bash
docker-compose up -d
docker-compose logs -f

# Airflow startup finished when webserver logs health checks!
