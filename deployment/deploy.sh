docker compose -f docker-compose.yml \
               -f ../api_gateway/docker-compose.yml \
               -f ../back/services/IAM/docker-compose.yml \
               -f ../back/services/manage_services/docker-compose.yml \
               -f ../back/services/user_ticket/docker-compose.yml \
               -f ../front/docker-compose.yml \
               up -d --build