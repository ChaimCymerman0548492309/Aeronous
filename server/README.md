# Real-Time Tracking System API

A simplified real-time tracking system with automatic target classification, built with FastAPI.

## Features

- **Target Management**:
  - Add multiple targets with POST
  - Retrieve all targets with GET
  - Delete specific targets by ID
- **Automatic Classification**:
  - Hostile (signal ≥ 80)
  - Friendly (signal < 30) 
  - Neutral (otherwise)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/targets` | POST | Add targets (accepts array of target objects) |
| `/targets` | GET | Retrieve all stored targets |
| `/targets/{id}` | DELETE | Delete specific target by ID |

## Target Object Structure

```json
{
  "id": "string (auto-generated UUID)",
  "name": "string",
  "heading": "float",
  "signal_strength": "int",
  "timestamp": "string (ISO format)",
  "classification": "string (auto-assigned)"
}