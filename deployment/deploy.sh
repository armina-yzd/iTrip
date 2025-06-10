docker compose -f docker-compose.yml \
               -f ../api_gateway/docker-compose.yml \
               -f ../services/IAM/docker-compose.yml \
               -f ../services/manage_services/docker-compose.yml \
               -f ../services/user_ticket/docker-compose.yml \
               -f ../front/docker-compose.yml \
               up -d --build