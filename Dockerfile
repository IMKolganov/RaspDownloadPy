# Stage 1: Build React App
FROM node:14 AS build-react

# Set working directory for React app
WORKDIR /app/react

# Copy package.json and package-lock.json to install dependencies
COPY react/package.json react/package-lock.json ./

# Install dependencies
RUN npm install

# Copy all files from react/build to working directory
COPY react/build ./build

COPY react/src ./build

# Copy public folder (ensure it contains index.html)
COPY react/public ./public

# Build React app
#RUN npm run build #ONLY LOCAL! https://github.com/facebook/create-react-app/issues/821

#for develop
RUN npm install react-devtools --save-dev

# Stage 2: Build Flask App
FROM python:3.9-slim

# Set working directory for Flask app
WORKDIR /app

# Copy requirements.txt to install Python dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from current directory to working directory
COPY . .

# Copy static files from React build output to Flask static/js folder
COPY --from=build-react /app/react/build/static/js /app/static/js

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run Flask application
CMD ["python", "app.py"]
