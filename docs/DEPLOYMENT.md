# Deployment Guide

## Docker

```bash
docker-compose up --build -d
```

## Kubernetes

```bash
kubectl apply -f kubernetes/configmap.yaml
kubectl apply -f kubernetes/secret.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ingress.yaml
```

## Production Checklist

- [ ] Set strong SECRET_KEY in environment
- [ ] Configure PostgreSQL with persistent volumes
- [ ] Set up Redis for caching
- [ ] Configure CORS for production domain
- [ ] Enable HTTPS with valid SSL certificate
- [ ] Set DEBUG=false
- [ ] Configure log rotation
- [ ] Set up database backups
- [ ] Configure monitoring with Prometheus/Grafana
- [ ] Set up CI/CD pipeline
- [ ] Run load tests before production deployment
