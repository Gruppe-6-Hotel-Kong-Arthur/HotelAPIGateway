# HotelAPIGateway


docker build -t api_gateway . && docker image prune -f

docker rm -f api_gateway && docker run -d -p 5010:5010 -e GUEST_SERVICE_URL=http://guest_service:5001 -e ROOM_INVENTORY_SERVICE_URL=http://room_inventory_service:5002 -e RESERVATION_SERVICE_URL=http://reservation_service:5003 -e DRINKS_SERVICE_URL=http://drinks_service:5004 -e CSV_EXPORT_SERVICE_URL=http://csv_export_service:5005 -e DRINKS_SALES_SERVICE_URL=http://drinks_sales_service:5006 --name api_gateway --network microservice-network api_gateway