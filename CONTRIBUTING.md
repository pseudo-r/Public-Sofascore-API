# Contributing to Public-Sofascore-API

We welcome contributions! If you have found a new endpoint, an undocumented query parameter, or notice any changes in Sofascore's response structures, feel free to open a Pull Request.

## How to Contribute

1. **Fork the repository**
2. **Create a branch** (`git checkout -b feature/new-endpoint`)
3. **Verify the endpoint**
   - Ensure you include details on how to bypass the WAF (e.g. valid User-Agent, Referer, or `curl_cffi` scripts).
   - Verify it functions currently on `api.sofascore.com`.
4. **Document it**
   - Use the existing Markdown format (Endpoint, Method, Required Params, Example Response).
   - Please trim large JSON blobs to only show the most relevant keys.
5. **Commit and Push**
   - Create a clean, descriptive pull request.

## Local Testing

If modifying the Django `espn_service/sofascore_client.py` implementation, run the local test suite using Docker:
```bash
cd espn_service
docker compose -f docker-compose.test.yml run --rm test
```
