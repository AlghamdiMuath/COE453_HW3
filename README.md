# COE453_HW3 — Arithmetic API on Google Cloud Functions

Homework 3 for **COE 453 – Distributed Systems and Cloud Computing** at KFUPM. Deploys four basic arithmetic operations (`add`, `sub`, `mul`, `div`) as **Google Cloud Functions**, fronted by an **API Gateway** described in `openapi.yaml` (Swagger 2.0).

## What's inside

- `add.py`, `sub.py`, `mul.py`, `div.py` — one Cloud Function per operation. Each uses `functions_framework` and reads `X` and `Y` from query parameters, validates them, and returns JSON.
- `openapi.yaml` — Swagger 2.0 spec defining the four `GET` endpoints behind API Gateway. Includes input validation and 400 responses for bad input.

## Deploy

```bash
# For each function:
gcloud functions deploy add --runtime python39 --trigger-http --allow-unauthenticated --entry-point add
# Then create the API Gateway with the OpenAPI spec:
gcloud api-gateway api-configs create my-config --api=arithmetic-api --openapi-spec=openapi.yaml --project=PROJ_ID
```

Replace `{PROJ_ID}` in `openapi.yaml` with your GCP project ID before deploying.

## Example

```
GET /add?X=2&Y=3
{"result": 5}
```

---

*Archived: course artifact, kept for reference. See `COE453_HW3_cloudRun` for the Cloud Run variant.*
