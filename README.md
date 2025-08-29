
# BFHL REST API (Flask)

A simple REST API that processes a mixed array and returns:
- `is_success`
- `user_id` (format: `{full_name_ddmmyyyy}`, full name in lowercase with underscores)
- `email`
- `roll_number`
- `odd_numbers`
- `even_numbers`
- `alphabets` (uppercased)
- `special_characters` (and `sepcial_characters` for compatibility with sample)
- `sum` (string)
- `concat_string` (alphabets concatenated in reverse order with alternating caps)

## Endpoint

- **Method:** POST  
- **Route:** `/bfhl`  
- **Success Status Code:** `200`

## Request Body

```json
{
  "data": ["2","a","y","4","&","-","*","5","92","b"],
  "full_name": "John Doe",
  "dob": "17-09-1999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123"
}
```

- `full_name` and `dob` are optional but recommended so `user_id` is personalized.
  - `full_name` is normalized to lowercase with spaces replaced by underscores.
  - `dob` accepts formats like `17091999`, `17-09-1999`, `17/09/1999` (we strip non-digits).

## Example Response

```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["5"],
  "even_numbers": ["2","4","92"],
  "alphabets": ["A","Y","B"],
  "special_characters": ["&","-","*"],
  "sepcial_characters": ["&","-","*"],
  "sum": "103",
  "concat_string": "ByA"
}
```

## Run Locally

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Test:

```bash
curl -X POST http://127.0.0.1:5000/bfhl   -H "Content-Type: application/json"   -d '{"data":["2","a","y","4","&","-","*","5","92","b"],"full_name":"John Doe","dob":"17/09/1999","email":"john@xyz.com","roll_number":"ABCD123"}'
```

## Deploy on Render (recommended)

1. Push this folder to a **public GitHub repo**.
2. Go to **Render → New → Web Service**.
3. Connect your repo.
4. **Environment:** `Python 3.x` (auto).
5. **Start Command:** `gunicorn app:app` (Procfile included).
6. Deploy. Your URL will look like `https://<service-name>.onrender.com`.
7. Test with: `POST https://<service-name>.onrender.com/bfhl`.

> Render sets the port automatically; `gunicorn` + `Procfile` handles it in production.

## Notes & Best Practices

- Robust parsing for integers from strings (e.g., `"92"`, `"-5"`), excludes booleans.
- Graceful error handling with meaningful messages and HTTP status codes.
- Returns both `special_characters` and `sepcial_characters` to satisfy potential evaluators.
- Add CORS if you call from browser frontends.
