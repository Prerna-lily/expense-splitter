# Expense Splitter API

A backend system for splitting expenses among groups of people.

## Features

- Expense tracking with flexible sharing options (percentage, exact amount, or equal)
- Automatic person creation when mentioned in expenses
- Settlement calculations to minimize transactions
- Balance tracking for each person
- RESTful API endpoints

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up PostgreSQL database:
```bash
# Create database
createdb expense_splitter

# Run migrations
alembic upgrade head
```

3. Run the application:
```bash
# Development mode
uvicorn app.main:app --reload

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

### Base URL
`http://localhost:8000/api/v1`

### Endpoints

#### People Management
- `GET /people` - List all people
- `GET /people/{name}` - Get specific person

#### Expense Management
- `GET /expenses` - List all expenses
- `POST /expenses` - Add new expense
- `PUT /expenses/{id}` - Update expense
- `DELETE /expenses/{id}` - Delete expense

#### Analytics
- `GET /analytics/settlements` - Get settlement summary
- `GET /analytics/balances` - Get balances for all people

### Request/Response Examples

#### Create Expense
```json
POST /expenses
{
    "amount": 1200.0,
    "description": "Dinner at Restaurant",
    "paid_by": "Shantanu",
    "shares": [
        {"person": "Shantanu", "type": "percentage", "value": 40},
        {"person": "Sanket", "type": "percentage", "value": 30},
        {"person": "Om", "type": "percentage", "value": 30}
    ]
}
```

#### Settlement Calculation
The system calculates settlements using the following logic:
1. Calculate net balance for each person (amount paid - amount owed)
2. Create transactions to minimize the number of transfers
3. Use exact amounts to avoid floating point precision issues

### Error Handling

- `400 Bad Request` - Invalid input data
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation errors
- `500 Internal Server Error` - Server errors

## Testing

1. Import the Postman collection from:
   - [Gist URL](https://gist.github.com/your-gist-id)
   - [Raw JSON URL](https://gist.githubusercontent.com/your-gist-id/raw/expense_splitter_api_collection.json)

2. The collection includes pre-populated test data with:
   - Sample people: Shantanu, Sanket, Om
   - Different expense scenarios
   - Settlement calculations
   - Balance tracking

## Deployment

1. Deploy to Railway.app:
   - Create a new project
   - Link your GitHub repository
   - Configure environment variables:
     - `DATABASE_URL`: PostgreSQL connection string
     - `PORT`: 8000
   - Deploy with Railway CLI:
   ```bash
   railway up
   ```

2. Deploy to Render.com:
   - Create a new web service
   - Link your GitHub repository
   - Configure environment variables:
     - `DATABASE_URL`: PostgreSQL connection string
     - `PORT`: 8000
   - Set up automatic deployments

## Known Limitations

1. Assumes all expenses are in the same currency
2. Does not handle currency conversion
3. Settlement calculations assume all people are willing to transact with each other
4. No user authentication (for simplicity)

## License

MIT
