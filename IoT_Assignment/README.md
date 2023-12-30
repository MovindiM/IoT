# Node-RED IoT Project

This repository contains the code and documentation for a group project focusing on various aspects of Node-RED, including implementing a weather information service, manipulating the Node-RED message object, and building a Node-RED application for interacting with IoT systems.

## Problem 1: Weather Information Service

### Objective

To effectively use basic Node-RED functions and APIs, implementing a simple weather information service with email integration.

### Usage

1. Each group member can request weather information by sending an email to a common address in a specific format from their personal email account.
2. The requested information will be sent as an email from the common account to the respective personal account.
3. Requests and responses are independent of concurrent requests.
4. Error messages will be sent in case of incorrect email format or if the sender doesn't belong to the group.

## Problem 2: Node-RED Message Manipulation

### Objective

To manipulate the Node-RED message object effectively and create a timetable dashboard.

### Usage

1. Create a Node-RED message with a JSON object containing Semester 4 timetable for a chosen day.
2. Extract information by querying for a specific module or time slot and display it on the dashboard.
3. Generate audio-visual notifications 5 minutes before the start of each class/lab.

## Problem 3: Node-RED IoT Application

### Objective

To use Node-RED effectively as a user interface for interacting with IoT systems by building a weather dashboard.

### Features

- Enter location as coordinates or city in a text field.
- Dashboard title should be the entered location (city from OpenWeather).
- Weather updates in 30s intervals (adjustable by the user).
- Display temperature, humidity, pressure, wind speed, wind direction, sunrise time, and sunset time.
- Customized gauges for parameters and a speaker icon for weather description.
- Plots for temperature, humidity, and wind speed within the past hour (toggle feature).
- Set warning limits for parameters with customizable thresholds.
- Notifications for parameter values exceeding the set warning limits.

## Files and Directories

- `weather_service_flow.json`: Node-RED flow for the weather information service.
- `timetable_dashboard_flow.json`: Node-RED flow for the timetable dashboard.
- `weather_app_flow.json`: Node-RED flow for the IoT weather application.
