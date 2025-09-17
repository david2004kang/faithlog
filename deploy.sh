#!/bin/bash

# FaithLog Deployment Script
# This script deploys the FaithLog application using Docker

set -e  # Exit on any error

echo "🚀 Starting FaithLog deployment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    print_warning ".env file not found. Creating from .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        print_status ".env file created. Please edit it with your settings."
    else
        print_error ".env.example file not found. Please create .env file manually."
        exit 1
    fi
fi

# Build and start services
print_status "Building Docker images..."
docker-compose build

print_status "Starting services..."
docker-compose up -d

# Wait for database to be ready
print_status "Waiting for database to be ready..."
sleep 10

# Run migrations
print_status "Running database migrations..."
docker-compose exec web python manage.py migrate

# Collect static files
print_status "Collecting static files..."
docker-compose exec web python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
print_status "Creating superuser (if needed)..."
docker-compose exec web python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@faithlog.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

# Show status
print_status "Checking service status..."
docker-compose ps

print_status "🎉 Deployment completed successfully!"
print_status "Application is running at: http://localhost:8000"
print_status "Admin panel: http://localhost:8000/admin"
print_status "Default admin credentials: admin/admin123"

echo ""
print_warning "Remember to:"
print_warning "1. Change the default admin password"
print_warning "2. Update your .env file with production settings"
print_warning "3. Set up proper SSL/TLS certificates for production"
