# empiricism_checklist.md - Sources of Illusion

When you are stuck, check if you are being fooled by one of these "Maps".

## 1. Documentation vs. Reality
*   **Outdated Comments:** Code changes, comments stay. `// Returns true` might now return `null`.
*   **Variable Names:** `List<String> userList` might actually contain `Ids`.

## 2. The Environment Illusion
*   **Cached Files:** Are you running the code you just edited? Or the old build?
*   **Environment Variables:** Is `.env` actually loaded? Are you in `PROD` or `DEV`?

## 3. The Mockingbird
*   **Test Mocks:** Are your tests passing because you mocked the bug away?
*   **Local vs. Remote:** Works on localhost, fails on AWS. (Network latency, permissions).
