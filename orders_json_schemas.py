order_schema_authenticated = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "name": {"type": "string"},
        "order": {
            "type": "object",
            "properties": {
                "number": {"type": "integer"},
                "price": {"type": "integer"},
                "status": {"type": "string"},
                "name": {"type": "string"},
                "owner": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string", "format": "email"},
                        "name": {"type": "string"},
                        "createdAt": {"type": "string", "format": "date-time"},
                        "updatedAt": {"type": "string", "format": "date-time"}
                    },
                    "required": ["email", "name"]
                },
                "ingredients": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "_id": {"type": "string"},
                            "name": {"type": "string"},
                            "type": {"type": "string"},
                            "price": {"type": "integer"}
                        },
                        "required": ["_id", "name", "type", "price"]
                    }
                }
            },
            "required": ["number", "price", "status", "name", "owner", "ingredients"]
        }
    },
    "required": ["success", "name", "order"]
}


order_schema_unauthenticated = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "name": {"type": "string"},
        "order": {
            "type": "object",
            "properties": {
                "number": {"type": "integer"}
            },
            "required": ["number"]
        }
    },
    "required": ["success", "name", "order"]
}
